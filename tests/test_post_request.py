"""Tests for POST request support in the client."""

import json
from typing import cast

import httpx
import pytest
import respx

from ahrefs import AhrefsClient, AsyncAhrefsClient
from ahrefs.types._generated import BatchAnalysisRequest, BatchAnalysisTarget

_BA_URL = "https://api.ahrefs.com/v3/batch-analysis/batch-analysis"
_BA_OK = {
    "targets": [
        {
            "index": 0,
            "url": "https://ahrefs.com",
            "mode": "domain",
            "protocol": "both",
            "ahrefs_rank": 641,
            "domain_rating": 91.0,
        }
    ]
}
_BA_REQ = BatchAnalysisRequest(
    select=["ahrefs_rank", "domain_rating"],
    targets=[
        BatchAnalysisTarget(url="https://ahrefs.com", mode="domain", protocol="both")
    ],
)


class TestPostRequestSendsJsonBody:
    @respx.mock
    def test_post_sends_json_body(self) -> None:
        route = respx.post(_BA_URL).mock(
            return_value=httpx.Response(200, json=_BA_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.batch_analysis(_BA_REQ)
        assert len(data) == 1
        assert data[0].ahrefs_rank == 641
        assert data[0].domain_rating == 91.0

        # Verify it was a POST with JSON body (not query params)
        sent_request = cast(httpx.Request, route.calls[0].request)
        assert sent_request.method == "POST"
        body = json.loads(sent_request.content)
        assert body["select"] == ["ahrefs_rank", "domain_rating"]
        assert len(body["targets"]) == 1
        assert body["targets"][0]["url"] == "https://ahrefs.com"
        # Query params should be empty for POST
        assert str(sent_request.url.params) == ""
        client.close()


class TestGetStillWorksNoRegression:
    @respx.mock
    def test_get_sends_query_params(self) -> None:
        from ahrefs.types._generated import SiteExplorerDomainRatingRequest

        dr_url = "https://api.ahrefs.com/v3/site-explorer/domain-rating"
        dr_ok = {"domain_rating": {"domain_rating": 85.5, "ahrefs_rank": 123}}
        route = respx.get(dr_url).mock(
            return_value=httpx.Response(200, json=dr_ok)
        )
        req = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.site_explorer_domain_rating(req)
        assert data is not None
        assert data.domain_rating == 85.5

        # Verify it was a GET with query params
        sent_request = cast(httpx.Request, route.calls[0].request)
        assert sent_request.method == "GET"
        sent_params: dict[str, str] = dict(sent_request.url.params)
        assert sent_params["target"] == "ahrefs.com"
        client.close()


class TestPostKwargs:
    @respx.mock
    def test_post_with_kwargs(self) -> None:
        route = respx.post(_BA_URL).mock(
            return_value=httpx.Response(200, json=_BA_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.batch_analysis(
            select=["ahrefs_rank"],
            targets=[
                BatchAnalysisTarget(
                    url="https://ahrefs.com", mode="domain", protocol="both"
                )
            ],
        )
        assert len(data) == 1
        assert data[0].ahrefs_rank == 641
        assert route.call_count == 1
        client.close()

    def test_missing_required_kwargs_raises(self) -> None:
        client = AhrefsClient(api_key="test-key", max_retries=0)
        with pytest.raises(ValueError, match="select"):
            client.batch_analysis(
                targets=[
                    BatchAnalysisTarget(
                        url="https://ahrefs.com", mode="domain", protocol="both"
                    )
                ],
            )
        client.close()


class TestPostRetries:
    @respx.mock
    def test_post_retries_on_429(self) -> None:
        route = respx.post(_BA_URL).mock(
            side_effect=[
                httpx.Response(429, text="Rate limited"),
                httpx.Response(200, json=_BA_OK),
            ]
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        data = client.batch_analysis(_BA_REQ)
        assert len(data) == 1
        assert route.call_count == 2
        client.close()

    @respx.mock
    def test_post_retries_on_500(self) -> None:
        route = respx.post(_BA_URL).mock(
            side_effect=[
                httpx.Response(500, text="Server Error"),
                httpx.Response(200, json=_BA_OK),
            ]
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        data = client.batch_analysis(_BA_REQ)
        assert len(data) == 1
        assert route.call_count == 2
        client.close()


class TestAsyncPostRequest:
    @respx.mock
    @pytest.mark.asyncio
    async def test_async_post_sends_json_body(self) -> None:
        route = respx.post(_BA_URL).mock(
            return_value=httpx.Response(200, json=_BA_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            data = await client.batch_analysis(_BA_REQ)
        assert len(data) == 1
        assert data[0].ahrefs_rank == 641

        sent_request = cast(httpx.Request, route.calls[0].request)
        assert sent_request.method == "POST"
        body = json.loads(sent_request.content)
        assert body["select"] == ["ahrefs_rank", "domain_rating"]

"""Tests for list-valued query parameter CSV serialization."""

import json
from typing import cast
from urllib.parse import parse_qs

import httpx
import pytest
import respx

from ahrefs import AhrefsClient, AsyncAhrefsClient
from ahrefs._base_client import flatten_list_params
from ahrefs.types import CountryEnum, DataSourceEnum

# --- Unit tests for flatten_list_params ---


class TestFlattenListParams:
    def test_non_empty_list_becomes_csv(self) -> None:
        result = flatten_list_params({"country": ["us", "gb"], "select": "url"})
        assert result == {"country": "us,gb", "select": "url"}

    def test_empty_list_omits_key(self) -> None:
        result = flatten_list_params({"country": [], "select": "url"})
        assert result == {"select": "url"}
        assert "country" not in result

    def test_none_items_filtered_out(self) -> None:
        result = flatten_list_params({"country": ["us", None, "gb"]})
        assert result == {"country": "us,gb"}

    def test_all_none_list_omits_key(self) -> None:
        result = flatten_list_params({"country": [None, None]})
        assert "country" not in result

    def test_scalar_values_unchanged(self) -> None:
        result = flatten_list_params({"target": "ahrefs.com", "limit": 10})
        assert result == {"target": "ahrefs.com", "limit": 10}

    def test_single_item_list(self) -> None:
        result = flatten_list_params({"country": ["us"]})
        assert result == {"country": "us"}


# --- Integration tests: GET with async client ---

_BR_URL = "https://api.ahrefs.com/v3/brand-radar/ai-responses"
_BR_OK: dict[str, list[dict[str, str]]] = {"ai_responses": []}


class TestAsyncGetCsvParams:
    @respx.mock
    @pytest.mark.asyncio
    async def test_country_list_serializes_as_csv(self) -> None:
        route = respx.get(_BR_URL).mock(
            return_value=httpx.Response(200, json=_BR_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            await client.brand_radar_ai_responses(
                select="url",
                data_source=DataSourceEnum.CHATGPT,
                country=[CountryEnum.US, CountryEnum.GB],
            )
        sent = cast(httpx.Request, route.calls[0].request)
        params = parse_qs(str(sent.url.params))
        assert params["country"] == ["us,gb"]
        assert len(params["country"]) == 1

    @respx.mock
    @pytest.mark.asyncio
    async def test_empty_country_list_omits_key(self) -> None:
        route = respx.get(_BR_URL).mock(
            return_value=httpx.Response(200, json=_BR_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            await client.brand_radar_ai_responses(
                select="url",
                data_source=DataSourceEnum.CHATGPT,
            )
        sent = cast(httpx.Request, route.calls[0].request)
        params = parse_qs(str(sent.url.params))
        assert "country" not in params


# --- Integration tests: GET with sync client ---


class TestSyncGetCsvParams:
    @respx.mock
    def test_country_list_serializes_as_csv(self) -> None:
        route = respx.get(_BR_URL).mock(
            return_value=httpx.Response(200, json=_BR_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        client.brand_radar_ai_responses(
            select="url",
            data_source=DataSourceEnum.CHATGPT,
            country=[CountryEnum.US, CountryEnum.GB],
        )
        sent = cast(httpx.Request, route.calls[0].request)
        params = parse_qs(str(sent.url.params))
        assert params["country"] == ["us,gb"]
        assert len(params["country"]) == 1
        client.close()

    @respx.mock
    def test_empty_country_list_omits_key(self) -> None:
        route = respx.get(_BR_URL).mock(
            return_value=httpx.Response(200, json=_BR_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        client.brand_radar_ai_responses(
            select="url",
            data_source=DataSourceEnum.CHATGPT,
        )
        sent = cast(httpx.Request, route.calls[0].request)
        params = parse_qs(str(sent.url.params))
        assert "country" not in params
        client.close()


# --- Integration tests: POST/PUT url_params flattened ---

_MGMT_CREATE_URL = "https://api.ahrefs.com/v3/management/brand-radar-prompts"
_MGMT_CREATE_OK: dict[str, list[dict[str, str]]] = {
    "prompts": [{"prompt": "test", "country": "us", "created_at": "2026-01-01"}]
}


class TestPostUrlParamsFlattened:
    @respx.mock
    def test_sync_post_body_preserves_lists(self) -> None:
        """POST JSON bodies preserve native list types (not CSV-flattened)."""
        route = respx.post(_MGMT_CREATE_URL).mock(
            return_value=httpx.Response(200, json=_MGMT_CREATE_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        client.management_create_brand_radar_prompts(
            report_id="abc123",
            countries=["us", "gb"],
            prompts=["my prompt"],
        )
        sent = cast(httpx.Request, route.calls[0].request)
        body = json.loads(sent.content)
        # Body should have native lists, not CSV strings
        assert isinstance(body["countries"], list)
        assert body["countries"] == ["us", "gb"]
        assert isinstance(body["prompts"], list)
        # report_id should be in query params, not body
        params = dict(sent.url.params)
        assert params["report_id"] == "abc123"
        client.close()

    @respx.mock
    @pytest.mark.asyncio
    async def test_async_post_body_preserves_lists(self) -> None:
        """POST JSON bodies preserve native list types (not CSV-flattened)."""
        route = respx.post(_MGMT_CREATE_URL).mock(
            return_value=httpx.Response(200, json=_MGMT_CREATE_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            await client.management_create_brand_radar_prompts(
                report_id="abc123",
                countries=["us", "gb"],
                prompts=["my prompt"],
            )
        sent = cast(httpx.Request, route.calls[0].request)
        body = json.loads(sent.content)
        assert isinstance(body["countries"], list)
        assert body["countries"] == ["us", "gb"]
        params = dict(sent.url.params)
        assert params["report_id"] == "abc123"


class TestPostUrlParamsListFlattened:
    """Directly test that list-valued query_params on POST are CSV-flattened."""

    _URL = "https://api.ahrefs.com/v3/test-section/test-endpoint"

    @respx.mock
    def test_sync_post_url_params_list_flattened(self) -> None:
        from pydantic import BaseModel, Field

        class _StubRequest(BaseModel):
            key: list[str] = Field(default_factory=list)
            val: str = ""

        class _StubResponse(BaseModel):
            ok: bool = True

        route = respx.post(self._URL).mock(
            return_value=httpx.Response(200, json={"ok": True})
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        client._request(  # pyright: ignore[reportPrivateUsage]
            "test-section",
            "test-endpoint",
            _StubRequest(key=["a", "b"], val="x"),
            _StubResponse,
            http_method="POST",
            query_params={"key": ["a", "b"]},
        )
        sent = cast(httpx.Request, route.calls[0].request)
        params = parse_qs(str(sent.url.params))
        assert params["key"] == ["a,b"]
        client.close()

    @respx.mock
    @pytest.mark.asyncio
    async def test_async_post_url_params_list_flattened(self) -> None:
        from pydantic import BaseModel, Field

        class _StubRequest(BaseModel):
            key: list[str] = Field(default_factory=list)
            val: str = ""

        class _StubResponse(BaseModel):
            ok: bool = True

        route = respx.post(self._URL).mock(
            return_value=httpx.Response(200, json={"ok": True})
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            await client._request(  # pyright: ignore[reportPrivateUsage]
                "test-section",
                "test-endpoint",
                _StubRequest(key=["a", "b"], val="x"),
                _StubResponse,
                http_method="POST",
                query_params={"key": ["a", "b"]},
            )
        sent = cast(httpx.Request, route.calls[0].request)
        params = parse_qs(str(sent.url.params))
        assert params["key"] == ["a,b"]

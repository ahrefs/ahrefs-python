"""Tests for keyword-argument convenience on generated client methods."""

from typing import cast

import httpx
import pytest
import respx

from ahrefs import AhrefsClient
from ahrefs.types._generated import SiteExplorerDomainRatingRequest

_DR_URL = "https://api.ahrefs.com/v3/site-explorer/domain-rating"
_DR_OK = {"domain_rating": {"domain_rating": 85.5, "ahrefs_rank": 123}}


class TestKwargsOnly:
    @respx.mock
    def test_call_with_kwargs(self) -> None:
        route = respx.get(_DR_URL).mock(return_value=httpx.Response(200, json=_DR_OK))
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.site_explorer_domain_rating(
            target="ahrefs.com", date="2025-01-15"
        )
        assert data is not None
        assert data.domain_rating == 85.5
        assert route.call_count == 1
        client.close()

    @respx.mock
    def test_optional_kwargs_default_when_omitted(self) -> None:
        route = respx.get(_DR_URL).mock(return_value=httpx.Response(200, json=_DR_OK))
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.site_explorer_domain_rating(
            target="ahrefs.com", date="2025-01-15"
        )
        # protocol is optional and omitted — model default ("both") should apply
        assert data is not None
        # respx doesn't ship type information for recorded calls; cast for pyright.
        sent_request = cast(httpx.Request, route.calls[0].request)
        sent_params: dict[str, str] = dict(sent_request.url.params)
        assert sent_params["protocol"] == "both"
        client.close()


class TestRequestObject:
    @respx.mock
    def test_call_with_request_object(self) -> None:
        route = respx.get(_DR_URL).mock(return_value=httpx.Response(200, json=_DR_OK))
        req = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.site_explorer_domain_rating(req)
        assert data is not None
        assert data.domain_rating == 85.5
        assert route.call_count == 1
        client.close()

    @respx.mock
    def test_request_object_takes_precedence_over_kwargs(self) -> None:
        route = respx.get(_DR_URL).mock(return_value=httpx.Response(200, json=_DR_OK))
        req = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
        client = AhrefsClient(api_key="test-key", max_retries=0)
        client.site_explorer_domain_rating(req, target="other.com")
        # Should use req's target, not the kwarg
        sent_request = cast(httpx.Request, route.calls[0].request)
        sent_params: dict[str, str] = dict(sent_request.url.params)
        assert sent_params["target"] == "ahrefs.com"
        client.close()


class TestRequiredKwargsValidation:
    def test_missing_required_kwarg_raises(self) -> None:
        client = AhrefsClient(api_key="test-key", max_retries=0)
        with pytest.raises(ValueError, match="target"):
            client.site_explorer_domain_rating(date="2025-01-15")
        client.close()

    def test_missing_all_required_kwargs_raises(self) -> None:
        client = AhrefsClient(api_key="test-key", max_retries=0)
        with pytest.raises(ValueError, match="target.*date"):
            client.site_explorer_domain_rating()
        client.close()

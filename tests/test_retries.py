"""Tests for retry behavior and backoff logic."""

import httpx
import pytest
import respx

from ahrefs import AhrefsClient, AsyncAhrefsClient
from ahrefs._base_client import calculate_backoff
from ahrefs._exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    raise_for_status,
)
from ahrefs.types._generated import SiteExplorerDomainRatingRequest


class TestCalculateBackoff:
    def test_first_attempt_base_delay(self) -> None:
        delay = calculate_backoff(0, base=0.5, max_delay=8.0)
        assert 0.5 <= delay < 1.0  # base + jitter [0, base)

    def test_delays_increase(self) -> None:
        # Attempt 0: min(0.5*1, 8) = 0.5, attempt 1: min(0.5*2, 8) = 1.0
        # With jitter, attempt 1 delay >= 1.0
        for _ in range(10):
            d0 = calculate_backoff(0, base=0.5, max_delay=8.0)
            assert 0.5 <= d0 < 1.0

    def test_max_delay_caps(self) -> None:
        delay = calculate_backoff(100, base=0.5, max_delay=8.0)
        assert delay < 8.0 + 0.5  # max_delay + max jitter


class TestRetryAfterParsing:
    def test_429_with_retry_after_header(self) -> None:
        response = httpx.Response(
            status_code=429,
            text="Too Many Requests",
            headers={"Retry-After": "5"},
            request=httpx.Request("GET", "https://api.ahrefs.com/v3/test"),
        )
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.retry_after == 5.0

    def test_429_without_retry_after_header(self) -> None:
        response = httpx.Response(
            status_code=429,
            text="Too Many Requests",
            request=httpx.Request("GET", "https://api.ahrefs.com/v3/test"),
        )
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.retry_after is None

    def test_429_with_non_numeric_retry_after(self) -> None:
        response = httpx.Response(
            status_code=429,
            text="Too Many Requests",
            headers={"Retry-After": "Thu, 01 Dec 2025 16:00:00 GMT"},
            request=httpx.Request("GET", "https://api.ahrefs.com/v3/test"),
        )
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.retry_after is None


_DR_URL = "https://api.ahrefs.com/v3/site-explorer/domain-rating"
_DR_OK = {"domain_rating": {"domain_rating": 85.5, "ahrefs_rank": 123}}
_DR_REQ = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")


class TestSyncRetries:
    @respx.mock
    def test_retries_on_429(self) -> None:
        route = respx.get(_DR_URL).mock(
            side_effect=[
                httpx.Response(429, text="Rate limited"),
                httpx.Response(200, json=_DR_OK),
            ]
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        response = client.site_explorer_domain_rating(_DR_REQ)
        assert response.domain_rating is not None
        assert response.domain_rating.domain_rating == 85.5
        assert route.call_count == 2
        client.close()

    @respx.mock
    def test_retries_on_500(self) -> None:
        route = respx.get(_DR_URL).mock(
            side_effect=[
                httpx.Response(500, text="Server Error"),
                httpx.Response(200, json=_DR_OK),
            ]
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        response = client.site_explorer_domain_rating(_DR_REQ)
        assert response.domain_rating is not None
        assert route.call_count == 2
        client.close()

    @respx.mock
    def test_no_retry_on_401(self) -> None:
        route = respx.get(_DR_URL).mock(
            return_value=httpx.Response(401, text="Unauthorized")
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        with pytest.raises(AuthenticationError):
            client.site_explorer_domain_rating(_DR_REQ)
        assert route.call_count == 1
        client.close()

    @respx.mock
    def test_no_retry_on_404(self) -> None:
        route = respx.get(_DR_URL).mock(
            return_value=httpx.Response(404, text="Not Found")
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        with pytest.raises(NotFoundError):
            client.site_explorer_domain_rating(_DR_REQ)
        assert route.call_count == 1
        client.close()

    @respx.mock
    def test_429_exhausts_retries(self) -> None:
        route = respx.get(_DR_URL).mock(
            return_value=httpx.Response(429, text="Rate limited")
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        with pytest.raises(RateLimitError):
            client.site_explorer_domain_rating(_DR_REQ)
        assert route.call_count == 3  # 1 + max_retries
        client.close()

    @respx.mock
    def test_5xx_exhausts_retries(self) -> None:
        route = respx.get(_DR_URL).mock(
            return_value=httpx.Response(503, text="Service Unavailable")
        )
        client = AhrefsClient(api_key="test-key", max_retries=2)
        with pytest.raises(APIError) as exc_info:
            client.site_explorer_domain_rating(_DR_REQ)
        assert exc_info.value.status_code == 503
        assert route.call_count == 3
        client.close()

    @respx.mock
    def test_retry_after_header_on_exhausted(self) -> None:
        respx.get(_DR_URL).mock(
            return_value=httpx.Response(
                429, text="Rate limited", headers={"Retry-After": "10"}
            )
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        with pytest.raises(RateLimitError) as exc_info:
            client.site_explorer_domain_rating(_DR_REQ)
        assert exc_info.value.retry_after == 10.0
        client.close()

    @respx.mock
    def test_max_retries_zero_disables(self) -> None:
        route = respx.get(_DR_URL).mock(
            return_value=httpx.Response(429, text="Rate limited")
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        with pytest.raises(RateLimitError):
            client.site_explorer_domain_rating(_DR_REQ)
        assert route.call_count == 1
        client.close()


class TestAsyncRetries:
    @respx.mock
    async def test_retries_on_429(self) -> None:
        route = respx.get(_DR_URL).mock(
            side_effect=[
                httpx.Response(429, text="Rate limited"),
                httpx.Response(200, json=_DR_OK),
            ]
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=2) as client:
            response = await client.site_explorer_domain_rating(_DR_REQ)
        assert response.domain_rating is not None
        assert route.call_count == 2

    @respx.mock
    async def test_retries_on_5xx(self) -> None:
        route = respx.get(_DR_URL).mock(
            side_effect=[
                httpx.Response(503, text="Service Unavailable"),
                httpx.Response(200, json=_DR_OK),
            ]
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=2) as client:
            response = await client.site_explorer_domain_rating(_DR_REQ)
        assert response.domain_rating is not None
        assert route.call_count == 2

    @respx.mock
    async def test_no_retry_on_401(self) -> None:
        route = respx.get(_DR_URL).mock(
            return_value=httpx.Response(401, text="Unauthorized")
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=2) as client:
            with pytest.raises(AuthenticationError):
                await client.site_explorer_domain_rating(_DR_REQ)
        assert route.call_count == 1

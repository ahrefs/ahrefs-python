"""Tests for Public API endpoints (crawler IPs and IP ranges)."""

from typing import cast

import httpx
import pytest
import respx

from ahrefs import AhrefsClient, AsyncAhrefsClient
from ahrefs._exceptions import AuthenticationError
from ahrefs.types._generated import (
    PublicCrawlerIpRangesData,
    PublicCrawlerIpsData,
)

_CRAWLER_IPS_URL = "https://api.ahrefs.com/v3/public/crawler-ips"
_CRAWLER_IP_RANGES_URL = "https://api.ahrefs.com/v3/public/crawler-ip-ranges"

_CRAWLER_IPS_OK = {
    "ips": [{"ip_address": "54.36.148.0"}, {"ip_address": "54.36.148.1"}]
}
_CRAWLER_IP_RANGES_OK = {
    "prefixes": [{"ipv4Prefix": "54.36.148.0/24"}, {"ipv4Prefix": "195.154.122.0/24"}]
}


class TestCrawlerIps:
    @respx.mock
    def test_returns_list_of_ips(self) -> None:
        respx.get(_CRAWLER_IPS_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IPS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.public_crawler_ips()
        assert isinstance(data, list)
        assert len(data) == 2
        assert isinstance(data[0], PublicCrawlerIpsData)
        assert data[0].ip_address == "54.36.148.0"
        assert data[1].ip_address == "54.36.148.1"
        client.close()

    @respx.mock
    def test_sends_authorization_header(self) -> None:
        route = respx.get(_CRAWLER_IPS_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IPS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        client.public_crawler_ips()
        sent_request = cast(httpx.Request, route.calls[0].request)
        assert "authorization" in sent_request.headers
        assert sent_request.headers["authorization"] == "Bearer test-key"
        client.close()

    @respx.mock
    @pytest.mark.asyncio
    async def test_async_returns_list_of_ips(self) -> None:
        respx.get(_CRAWLER_IPS_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IPS_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            data = await client.public_crawler_ips()
        assert isinstance(data, list)
        assert len(data) == 2
        assert isinstance(data[0], PublicCrawlerIpsData)
        assert data[0].ip_address == "54.36.148.0"


class TestCrawlerIpRanges:
    @respx.mock
    def test_returns_list_of_ranges(self) -> None:
        respx.get(_CRAWLER_IP_RANGES_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IP_RANGES_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.public_crawler_ip_ranges()
        assert isinstance(data, list)
        assert len(data) == 2
        assert isinstance(data[0], PublicCrawlerIpRangesData)
        assert data[0].ipv4_prefix == "54.36.148.0/24"
        assert data[1].ipv4_prefix == "195.154.122.0/24"
        client.close()

    @respx.mock
    def test_ipv4_prefix_alias_deserializes_camel_case(self) -> None:
        """Verify camelCase `ipv4Prefix` in JSON maps to snake_case `ipv4_prefix`."""
        respx.get(_CRAWLER_IP_RANGES_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IP_RANGES_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.public_crawler_ip_ranges()
        assert data[0].ipv4_prefix == "54.36.148.0/24"
        client.close()

    @respx.mock
    @pytest.mark.asyncio
    async def test_async_returns_list_of_ranges(self) -> None:
        respx.get(_CRAWLER_IP_RANGES_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IP_RANGES_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            data = await client.public_crawler_ip_ranges()
        assert isinstance(data, list)
        assert len(data) == 2
        assert isinstance(data[0], PublicCrawlerIpRangesData)
        assert data[0].ipv4_prefix == "54.36.148.0/24"


class TestNoApiKey:
    """Tests for public endpoints without an API key."""

    def test_sync_client_no_key(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        client = AhrefsClient()
        assert client._config.api_key is None
        client.close()

    @pytest.mark.asyncio
    async def test_async_client_no_key(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        async with AsyncAhrefsClient() as client:
            assert client._config.api_key is None

    @pytest.mark.parametrize("key", ["", "  ", "\t"])
    def test_sync_empty_key_treated_as_none(
        self, monkeypatch: pytest.MonkeyPatch, key: str
    ) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        client = AhrefsClient(api_key=key)
        assert client._config.api_key is None
        client.close()

    @pytest.mark.parametrize("key", ["", "  ", "\t"])
    @pytest.mark.asyncio
    async def test_async_empty_key_treated_as_none(
        self, monkeypatch: pytest.MonkeyPatch, key: str
    ) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        async with AsyncAhrefsClient(api_key=key) as client:
            assert client._config.api_key is None

    @pytest.mark.parametrize("key", ["", "  ", "\t"])
    def test_whitespace_key_falls_through_to_env(
        self, monkeypatch: pytest.MonkeyPatch, key: str
    ) -> None:
        monkeypatch.setenv("AHREFS_API_KEY", "env-key")
        client = AhrefsClient(api_key=key)
        assert client._config.api_key == "env-key"
        client.close()

    @respx.mock
    def test_no_auth_header_without_key(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        route = respx.get(_CRAWLER_IPS_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IPS_OK)
        )
        client = AhrefsClient(max_retries=0)
        client.public_crawler_ips()
        sent_request = cast(httpx.Request, route.calls[0].request)
        assert "authorization" not in sent_request.headers
        assert "user-agent" in sent_request.headers
        client.close()

    @respx.mock
    @pytest.mark.asyncio
    async def test_async_no_auth_header_without_key(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        route = respx.get(_CRAWLER_IPS_URL).mock(
            return_value=httpx.Response(200, json=_CRAWLER_IPS_OK)
        )
        async with AsyncAhrefsClient(max_retries=0) as client:
            await client.public_crawler_ips()
        sent_request = cast(httpx.Request, route.calls[0].request)
        assert "authorization" not in sent_request.headers
        assert "user-agent" in sent_request.headers

    @respx.mock
    def test_non_public_endpoint_without_key_raises(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        respx.get("https://api.ahrefs.com/v3/site-explorer/domain-rating").mock(
            return_value=httpx.Response(401, json={"error": "Unauthorized"})
        )
        client = AhrefsClient(max_retries=0)
        with pytest.raises(AuthenticationError):
            client.site_explorer_domain_rating(target="example.com", date="2025-01-15")
        client.close()

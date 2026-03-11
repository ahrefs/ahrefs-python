"""Tests for Public API endpoints (crawler IPs and IP ranges)."""

from typing import cast

import httpx
import pytest
import respx

from ahrefs import AhrefsClient, AsyncAhrefsClient
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

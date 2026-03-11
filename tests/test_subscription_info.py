"""Tests for Subscription Info API endpoint (limits and usage)."""

import httpx
import pytest
import respx

from ahrefs import AhrefsClient, AsyncAhrefsClient
from ahrefs.types._generated import SubscriptionInfoLimitsAndUsageData

_LIMITS_URL = "https://api.ahrefs.com/v3/subscription-info/limits-and-usage"

_LIMITS_OK = {
    "limits_and_usage": {
        "subscription": "Enterprise",
        "usage_reset_date": "2025-03-01",
        "units_limit_workspace": 1000000,
        "units_usage_workspace": 250000,
        "units_limit_api_key": 500000,
        "units_usage_api_key": 100000,
        "api_key_expiration_date": "2026-01-01T00:00:00Z",
    }
}

_LIMITS_NULLABLE = {
    "limits_and_usage": {
        "subscription": "Starter",
        "usage_reset_date": "2025-03-01",
        "units_limit_workspace": None,
        "units_usage_workspace": None,
        "units_limit_api_key": None,
        "units_usage_api_key": 50,
        "api_key_expiration_date": "2026-01-01T00:00:00Z",
    }
}


class TestLimitsAndUsage:
    @respx.mock
    def test_returns_data(self) -> None:
        respx.get(_LIMITS_URL).mock(
            return_value=httpx.Response(200, json=_LIMITS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.subscription_info_limits_and_usage()
        assert isinstance(data, SubscriptionInfoLimitsAndUsageData)
        assert data.subscription == "Enterprise"
        assert data.units_limit_workspace == 1000000
        assert data.units_usage_api_key == 100000
        client.close()

    @respx.mock
    def test_nullable_fields(self) -> None:
        respx.get(_LIMITS_URL).mock(
            return_value=httpx.Response(200, json=_LIMITS_NULLABLE)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.subscription_info_limits_and_usage()
        assert isinstance(data, SubscriptionInfoLimitsAndUsageData)
        assert data.subscription == "Starter"
        assert data.units_limit_workspace is None
        assert data.units_usage_workspace is None
        assert data.units_limit_api_key is None
        assert data.units_usage_api_key == 50
        client.close()

    @respx.mock
    @pytest.mark.asyncio
    async def test_async_returns_data(self) -> None:
        respx.get(_LIMITS_URL).mock(
            return_value=httpx.Response(200, json=_LIMITS_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            data = await client.subscription_info_limits_and_usage()
        assert isinstance(data, SubscriptionInfoLimitsAndUsageData)
        assert data.subscription == "Enterprise"
        assert data.units_usage_api_key == 100000

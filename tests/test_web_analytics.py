"""Tests for Web Analytics API support, focusing on reserved-word alias handling."""

from typing import cast

import httpx
import pytest
import respx
from pydantic import ValidationError

from ahrefs import AhrefsClient
from ahrefs.types._generated import (
    WebAnalyticsBrowsersData,
    WebAnalyticsChartData,
    WebAnalyticsStatsData,
    WebAnalyticsStatsRequest,
)

_STATS_URL = "https://api.ahrefs.com/v3/web-analytics/stats"
_BROWSERS_URL = "https://api.ahrefs.com/v3/web-analytics/browsers"
_CHART_URL = "https://api.ahrefs.com/v3/web-analytics/chart"

_STATS_OK = {
    "stats": {
        "pageviews": 1000,
        "visitors": 500,
        "visits": 600,
    }
}
_BROWSERS_OK = {
    "stats": [
        {
            "browser": "Chrome",
            "visitors": 300,
            "session_bounce_rate": 0.45,
            "avg_session_duration_sec": 120,
        },
    ]
}
_CHART_OK = {
    "points": [
        {
            "timestamp": "2025-01-01T00:00:00Z",
            "pageviews": 100,
            "visitors": 50,
            "visits": 60,
        },
    ]
}


class TestFromAliasRoundtrip:
    """Verify that `from_` Python field serializes as `from` for the API."""

    def test_request_model_accepts_from_underscore(self) -> None:
        req = WebAnalyticsStatsRequest(
            project_id=123,
            from_="2025-01-01T00:00:00Z",
            to="2025-01-31T23:59:59Z",
        )
        assert req.from_ == "2025-01-01T00:00:00Z"

    def test_model_dump_by_alias_produces_from(self) -> None:
        req = WebAnalyticsStatsRequest(
            project_id=123,
            from_="2025-01-01T00:00:00Z",
            to="2025-01-31T23:59:59Z",
        )
        dumped = req.model_dump(mode="json", by_alias=True, exclude_none=True)
        assert "from" in dumped
        assert "from_" not in dumped
        assert dumped["from"] == "2025-01-01T00:00:00Z"

    def test_model_dump_without_alias_uses_python_name(self) -> None:
        req = WebAnalyticsStatsRequest(
            project_id=123,
            from_="2025-01-01T00:00:00Z",
        )
        dumped = req.model_dump(mode="json", exclude_none=True)
        assert "from_" in dumped
        assert "from" not in dumped

    @respx.mock
    def test_client_sends_from_not_from_underscore(self) -> None:
        route = respx.get(_STATS_URL).mock(
            return_value=httpx.Response(200, json=_STATS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        client.web_analytics_stats(
            project_id=123,
            from_="2025-01-01T00:00:00Z",
            to="2025-01-31T23:59:59Z",
        )
        sent_request = cast(httpx.Request, route.calls[0].request)
        sent_params: dict[str, str] = dict(sent_request.url.params)
        assert "from" in sent_params
        assert "from_" not in sent_params
        assert sent_params["from"] == "2025-01-01T00:00:00Z"
        client.close()


class TestStatsEndpoint:
    @respx.mock
    def test_stats_returns_data(self) -> None:
        respx.get(_STATS_URL).mock(
            return_value=httpx.Response(200, json=_STATS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.web_analytics_stats(project_id=123)
        assert isinstance(data, WebAnalyticsStatsData)
        assert data.pageviews == 1000
        assert data.visitors == 500
        client.close()


class TestDimensionEndpoint:
    @respx.mock
    def test_browsers_returns_list(self) -> None:
        respx.get(_BROWSERS_URL).mock(
            return_value=httpx.Response(200, json=_BROWSERS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.web_analytics_browsers(project_id=123)
        assert isinstance(data, list)
        assert len(data) == 1
        assert isinstance(data[0], WebAnalyticsBrowsersData)
        assert data[0].browser == "Chrome"
        client.close()


class TestChartEndpoint:
    @respx.mock
    def test_chart_returns_list(self) -> None:
        respx.get(_CHART_URL).mock(
            return_value=httpx.Response(200, json=_CHART_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.web_analytics_chart(project_id=123, granularity="daily")
        assert isinstance(data, list)
        assert len(data) == 1
        assert isinstance(data[0], WebAnalyticsChartData)
        assert data[0].pageviews == 100
        client.close()


class TestKwargsVsRequestObject:
    @respx.mock
    def test_kwargs_equivalent_to_request_object(self) -> None:
        route = respx.get(_STATS_URL).mock(
            return_value=httpx.Response(200, json=_STATS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)

        # Call with kwargs
        client.web_analytics_stats(
            project_id=123,
            from_="2025-01-01T00:00:00Z",
        )
        kwargs_params = dict(cast(httpx.Request, route.calls[0].request).url.params)

        # Call with request object
        req = WebAnalyticsStatsRequest(
            project_id=123,
            from_="2025-01-01T00:00:00Z",
        )
        client.web_analytics_stats(req)
        obj_params = dict(cast(httpx.Request, route.calls[1].request).url.params)

        assert kwargs_params == obj_params
        client.close()


class TestRequiredProjectId:
    def test_missing_project_id_raises(self) -> None:
        client = AhrefsClient(api_key="test-key", max_retries=0)
        with pytest.raises(ValueError, match="project_id"):
            client.web_analytics_stats()
        client.close()

    def test_project_id_required_in_request_model(self) -> None:
        with pytest.raises(ValidationError):
            WebAnalyticsStatsRequest()  # type: ignore[call-arg]

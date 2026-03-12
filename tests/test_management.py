"""Tests for Management API endpoints (PUT, PATCH, query_params + body).

Test fixtures for live testing:
  - Project: id=9549866, name="gerwyn-test-agent-a"
  - Keyword list: id=1464605 (from Rank Tracker UI URL, not discoverable via API)
"""

import json
from typing import cast

import httpx
import pytest
import respx

from ahrefs import AhrefsClient, AsyncAhrefsClient
from ahrefs.types._generated import (
    AccessEnum,
    CountryEnum,
    ManagementCreateProjectCompetitorsCompetitor,
    ManagementLocationsData,
    ManagementProjectCompetitorsData,
    ManagementProjectKeywordsData,
    ManagementProjectKeywordsDeleteKeywordDelete,
    ManagementProjectKeywordsDeleteRequest,
    ManagementProjectsData,
    ManagementSetProjectKeywordsKeyword,
    ManagementSetProjectKeywordsLocation,
    ManagementUpdateProjectData,
    ModeEnum,
    ProtocolEnum,
)

_BASE = "https://api.ahrefs.com/v3/management"

# -- Mock responses -------------------------------------------------------

_PROJECTS_OK = {
    "projects": [
        {
            "project_id": "9549866",
            "project_name": "gerwyn-test-agent-a",
            "url": "example.com/",
            "mode": "domain",
            "protocol": "https",
            "access": "shared",
            "owned_by": "test@ahrefs.com",
            "keyword_count": 1,
            "web_analytics_data_key": "abc123",
        }
    ]
}

_UPDATE_PROJECT_OK = {
    "project": {
        "project_id": "9549866",
        "project_name": "gerwyn-test-agent-a",
        "url": "example.com/",
        "mode": "domain",
        "protocol": "https",
        "access": "shared",
    }
}

_PROJECT_KEYWORDS_OK = {
    "keywords": [
        {
            "keyword": "test keyword",
            "language_code": "en",
            "language": "English",
            "location_id": 2840,
            "location": "United States",
            "tags": [],
        }
    ]
}

_PROJECT_COMPETITORS_OK = {
    "competitors": [
        {"url": "moz.com/", "mode": "domain"},
        {"url": "semrush.com/", "mode": "domain"},
    ]
}

_LOCATIONS_OK = {
    "location": {
        "country_code": "gb",
        "languages": [["en", "English"]],
        "locations": [[1234, "London,United Kingdom"]],
    }
}

_KEYWORD_LIST_OK = {
    "keywords": [{"keyword": "test kw"}]
}


# -- GET endpoints ---------------------------------------------------------


class TestManagementGet:
    @respx.mock
    def test_projects_get(self) -> None:
        route = respx.get(f"{_BASE}/projects").mock(
            return_value=httpx.Response(200, json=_PROJECTS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.management_projects()
        assert len(data) == 1
        assert isinstance(data[0], ManagementProjectsData)
        assert data[0].project_name == "gerwyn-test-agent-a"

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "GET"
        client.close()

    @respx.mock
    def test_locations_get(self) -> None:
        route = respx.get(f"{_BASE}/locations").mock(
            return_value=httpx.Response(200, json=_LOCATIONS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.management_locations(country_code=CountryEnum.GB)
        assert isinstance(data, ManagementLocationsData)
        assert data.country_code == "gb"

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "GET"
        assert "country_code=gb" in str(sent.url)
        client.close()


# -- POST endpoints --------------------------------------------------------


class TestManagementPost:
    @respx.mock
    def test_create_projects_sends_post_with_json_body(self) -> None:
        route = respx.post(f"{_BASE}/projects").mock(
            return_value=httpx.Response(200, json=_PROJECTS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.management_create_projects(
            protocol=ProtocolEnum.HTTPS, url="example.com", mode=ModeEnum.DOMAIN,
            project_name="test-project",
        )
        assert len(data) == 1

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "POST"
        body = json.loads(sent.content)
        assert body["url"] == "example.com"
        assert body["project_name"] == "test-project"
        # No query params on this POST
        assert str(sent.url.params) == ""
        client.close()

    @respx.mock
    def test_create_competitors_sends_query_params_and_body(self) -> None:
        """POST /project-competitors has project_id as query param + body."""
        route = respx.post(f"{_BASE}/project-competitors").mock(
            return_value=httpx.Response(200, json=_PROJECT_COMPETITORS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.management_create_project_competitors(
            project_id=9549866,
            competitors=[
                ManagementCreateProjectCompetitorsCompetitor(
                    url="moz.com", mode="domain"
                ),
            ],
        )
        assert len(data) == 2
        assert isinstance(data[0], ManagementProjectCompetitorsData)

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "POST"
        # project_id should be in query params, NOT in body
        assert "project_id=9549866" in str(sent.url)
        body = json.loads(sent.content)
        assert "project_id" not in body
        assert len(body["competitors"]) == 1
        client.close()


# -- PUT endpoints ---------------------------------------------------------


class TestManagementPut:
    @respx.mock
    def test_set_project_keywords_sends_put(self) -> None:
        route = respx.put(f"{_BASE}/project-keywords").mock(
            return_value=httpx.Response(200, json=_PROJECT_KEYWORDS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.management_set_project_keywords(
            project_id=123,
            locations=[ManagementSetProjectKeywordsLocation(country="us")],
            keywords=[ManagementSetProjectKeywordsKeyword(keyword="test")],
        )
        assert len(data) == 1
        assert isinstance(data[0], ManagementProjectKeywordsData)

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "PUT"
        # project_id in query params, keywords/locations in body
        assert "project_id=123" in str(sent.url)
        body = json.loads(sent.content)
        assert "project_id" not in body
        assert body["keywords"][0]["keyword"] == "test"
        assert body["locations"][0]["country"] == "us"
        client.close()

    @respx.mock
    def test_keyword_list_keywords_sends_put(self) -> None:
        route = respx.put(f"{_BASE}/keyword-list-keywords").mock(
            return_value=httpx.Response(200, json=_KEYWORD_LIST_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.management_set_keyword_list_keywords(
            keyword_list_id=1464605,
            keywords=["alpha", "beta"],
        )
        assert len(data) == 1

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "PUT"
        assert "keyword_list_id=1464605" in str(sent.url)
        body = json.loads(sent.content)
        assert "keyword_list_id" not in body
        assert body["keywords"] == ["alpha", "beta"]
        client.close()


# -- PATCH endpoint --------------------------------------------------------


class TestManagementPatch:
    @respx.mock
    def test_update_project_sends_patch(self) -> None:
        route = respx.patch(f"{_BASE}/update-project").mock(
            return_value=httpx.Response(200, json=_UPDATE_PROJECT_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        data = client.management_update_project(
            access=AccessEnum.SHARED, project_id=9549866,
        )
        assert isinstance(data, ManagementUpdateProjectData)
        assert data.access == "shared"

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "PATCH"
        body = json.loads(sent.content)
        assert body["access"] == "shared"
        assert body["project_id"] == 9549866
        client.close()


# -- Async -----------------------------------------------------------------


class TestManagementAsync:
    @respx.mock
    @pytest.mark.asyncio
    async def test_async_put_with_query_params(self) -> None:
        route = respx.put(f"{_BASE}/project-keywords").mock(
            return_value=httpx.Response(200, json=_PROJECT_KEYWORDS_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            data = await client.management_set_project_keywords(
                project_id=123,
                locations=[ManagementSetProjectKeywordsLocation(country="us")],
                keywords=[ManagementSetProjectKeywordsKeyword(keyword="test")],
            )
        assert len(data) == 1

        sent = cast(httpx.Request, route.calls[0].request)
        assert sent.method == "PUT"
        assert "project_id=123" in str(sent.url)
        body = json.loads(sent.content)
        assert "project_id" not in body

    @respx.mock
    @pytest.mark.asyncio
    async def test_async_patch(self) -> None:
        respx.patch(f"{_BASE}/update-project").mock(
            return_value=httpx.Response(200, json=_UPDATE_PROJECT_OK)
        )
        async with AsyncAhrefsClient(api_key="test-key", max_retries=0) as client:
            data = await client.management_update_project(
                access=AccessEnum.SHARED, project_id=9549866,
            )
        assert isinstance(data, ManagementUpdateProjectData)
        assert data.access == "shared"


# -- Query params None filtering ------------------------------------------


class TestQueryParamsNoneFiltering:
    @respx.mock
    def test_none_query_param_excluded_from_url(self) -> None:
        """When a query param is None, it should not appear in the URL."""
        route = respx.put(f"{_BASE}/project-keywords-delete").mock(
            return_value=httpx.Response(200, json=_PROJECT_KEYWORDS_OK)
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        req = ManagementProjectKeywordsDeleteRequest(
            project_id=999,
            keywords=[ManagementProjectKeywordsDeleteKeywordDelete(keyword="x")],
        )
        client.management_project_keywords_delete(request=req)

        sent = cast(httpx.Request, route.calls[0].request)
        assert "project_id=999" in str(sent.url)
        client.close()

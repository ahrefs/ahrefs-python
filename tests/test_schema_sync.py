"""Smoke tests verifying the March 2026 schema sync landed correctly.

These tests verify structural expectations: types exist, fields exist,
methods exist, old names are gone. They don't test codegen patterns
(covered by test_codegen.py) or HTTP behavior (covered by other tests).
"""

import httpx
import pytest
import respx

from ahrefs import AhrefsClient


class TestRenamedMethodsExist:
    """Verify renamed site-explorer methods are callable and old names are gone."""

    @respx.mock
    def test_pages_by_backlinks_method_exists(self) -> None:
        url = "https://api.ahrefs.com/v3/site-explorer/pages-by-backlinks"
        respx.get(url).mock(
            return_value=httpx.Response(
                200, json={"pages": [{"url": "https://example.com"}]}
            )
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        result = client.site_explorer_pages_by_backlinks(
            target="ahrefs.com", select="url"
        )
        assert result is not None
        client.close()

    @respx.mock
    def test_pages_by_internal_links_method_exists(self) -> None:
        url = "https://api.ahrefs.com/v3/site-explorer/pages-by-internal-links"
        respx.get(url).mock(
            return_value=httpx.Response(
                200, json={"pages": [{"url": "https://example.com"}]}
            )
        )
        client = AhrefsClient(api_key="test-key", max_retries=0)
        result = client.site_explorer_pages_by_internal_links(
            target="ahrefs.com", select="url"
        )
        assert result is not None
        client.close()

    def test_old_backlinks_method_removed(self) -> None:
        client = AhrefsClient(api_key="test-key")
        assert not hasattr(client, "site_explorer_best_by_external_links")
        client.close()

    def test_old_internal_links_method_removed(self) -> None:
        client = AhrefsClient(api_key="test-key")
        assert not hasattr(client, "site_explorer_best_by_internal_links")
        client.close()


class TestRenamedTypesExist:
    """Verify renamed types are importable and old names are gone."""

    def test_new_backlinks_types_importable(self) -> None:
        from ahrefs.types import (
            SiteExplorerPagesByBacklinksData,
            SiteExplorerPagesByBacklinksRequest,
        )

        assert SiteExplorerPagesByBacklinksData is not None
        assert SiteExplorerPagesByBacklinksRequest is not None

    def test_new_internal_links_types_importable(self) -> None:
        from ahrefs.types import (
            SiteExplorerPagesByInternalLinksData,
            SiteExplorerPagesByInternalLinksRequest,
        )

        assert SiteExplorerPagesByInternalLinksData is not None
        assert SiteExplorerPagesByInternalLinksRequest is not None

    def test_old_backlinks_types_removed(self) -> None:
        with pytest.raises(ImportError):
            exec(  # noqa: S102
                "from ahrefs.types._generated"
                " import SiteExplorerBestByExternalLinksRequest"
            )

    def test_old_internal_links_types_removed(self) -> None:
        with pytest.raises(ImportError):
            exec(  # noqa: S102
                "from ahrefs.types._generated"
                " import SiteExplorerBestByInternalLinksRequest"
            )


class TestNewBrandRadarPromptsEndpoints:
    """Verify the 3 new management brand-radar-prompts methods exist."""

    _PROMPTS_OK: dict[str, list[dict[str, str]]] = {
        "prompts": [{"prompt": "test", "country": "us", "created_at": "2026-01-01"}]
    }
    _DELETE_OK: dict[str, list[dict[str, str]]] = {
        "prompts": [{"prompt": "test", "country": "us", "deleted_at": "2026-01-01"}]
    }

    @respx.mock
    def test_management_brand_radar_prompts_get(self) -> None:
        url = "https://api.ahrefs.com/v3/management/brand-radar-prompts"
        respx.get(url).mock(return_value=httpx.Response(200, json=self._PROMPTS_OK))
        client = AhrefsClient(api_key="test-key", max_retries=0)
        result = client.management_brand_radar_prompts(report_id="abc123")
        assert isinstance(result, list)
        client.close()

    @respx.mock
    def test_management_brand_radar_prompts_delete_put(self) -> None:
        url = "https://api.ahrefs.com/v3/management/brand-radar-prompts-delete"
        respx.put(url).mock(return_value=httpx.Response(200, json=self._DELETE_OK))
        client = AhrefsClient(api_key="test-key", max_retries=0)
        result = client.management_brand_radar_prompts_delete(
            report_id="abc123", countries=["us"], prompts=["test"]
        )
        assert isinstance(result, list)
        client.close()


class TestNewPagePositionsEnum:
    """Verify PagePositionsEnum exists with expected values."""

    def test_enum_values(self) -> None:
        from ahrefs.types import PagePositionsEnum

        assert PagePositionsEnum.TOP10.value == "top10"
        assert PagePositionsEnum.TOP100.value == "top100"

    def test_pages_history_request_accepts_page_positions(self) -> None:
        from ahrefs.types import PagePositionsEnum, SiteExplorerPagesHistoryRequest

        req = SiteExplorerPagesHistoryRequest(
            target="ahrefs.com",
            date_from="2025-01-01",
            page_positions=PagePositionsEnum.TOP10,
        )
        dumped = req.model_dump(mode="json")
        assert dumped["page_positions"] == "top10"


class TestNewFields:
    """Verify new fields exist on the correct data/request models."""

    def test_brand_radar_ai_responses_data_has_search_queries(self) -> None:
        from ahrefs.types._generated import BrandRadarAiResponsesData

        obj = BrandRadarAiResponsesData()
        assert hasattr(obj, "search_queries")

    def test_brand_radar_ai_responses_data_has_tags(self) -> None:
        from ahrefs.types._generated import BrandRadarAiResponsesData

        obj = BrandRadarAiResponsesData()
        assert hasattr(obj, "tags")

    def test_site_audit_page_explorer_data_has_size_uncompressed_fields(self) -> None:
        from ahrefs.types._generated import SiteAuditPageExplorerData

        obj = SiteAuditPageExplorerData()
        assert hasattr(obj, "size_uncompressed")
        assert hasattr(obj, "size_uncompressed_diff")
        assert hasattr(obj, "size_uncompressed_prev")

    def test_site_audit_projects_request_has_project_url(self) -> None:
        from ahrefs.types._generated import SiteAuditProjectsRequest

        obj = SiteAuditProjectsRequest(select="url")
        assert hasattr(obj, "project_url")

    def test_site_audit_projects_request_has_project_name(self) -> None:
        from ahrefs.types._generated import SiteAuditProjectsRequest

        obj = SiteAuditProjectsRequest(select="url")
        assert hasattr(obj, "project_name")

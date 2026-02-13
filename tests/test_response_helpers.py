"""Tests for the .data property on Response models."""

from ahrefs.types._generated import (
    SiteExplorerDomainRatingData,
    SiteExplorerDomainRatingResponse,
    SiteExplorerOrganicKeywordsData,
    SiteExplorerOrganicKeywordsResponse,
)


class TestSingleObjectDataProperty:
    def test_data_returns_inner_object(self) -> None:
        resp = SiteExplorerDomainRatingResponse.model_validate(
            {"domain_rating": {"domain_rating": 85.5, "ahrefs_rank": 123}}
        )
        assert resp.data is not None
        assert isinstance(resp.data, SiteExplorerDomainRatingData)
        assert resp.data.domain_rating == 85.5

    def test_data_returns_none_when_absent(self) -> None:
        resp = SiteExplorerDomainRatingResponse.model_validate({"domain_rating": None})
        assert resp.data is None

    def test_original_field_still_works(self) -> None:
        resp = SiteExplorerDomainRatingResponse.model_validate(
            {"domain_rating": {"domain_rating": 75.0, "ahrefs_rank": 456}}
        )
        assert resp.domain_rating is not None
        assert resp.domain_rating.domain_rating == 75.0


class TestListDataProperty:
    def test_data_returns_list(self) -> None:
        resp = SiteExplorerOrganicKeywordsResponse.model_validate(
            {
                "keywords": [
                    {"keyword": "test", "position": 1},
                    {"keyword": "test2", "position": 2},
                ]
            }
        )
        assert len(resp.data) == 2
        assert isinstance(resp.data[0], SiteExplorerOrganicKeywordsData)

    def test_data_returns_empty_list_when_none(self) -> None:
        resp = SiteExplorerOrganicKeywordsResponse.model_validate({"keywords": None})
        assert resp.data == []
        assert isinstance(resp.data, list)

    def test_original_field_still_works(self) -> None:
        resp = SiteExplorerOrganicKeywordsResponse.model_validate(
            {"keywords": [{"keyword": "test", "position": 1}]}
        )
        assert resp.keywords is not None
        assert len(resp.keywords) == 1

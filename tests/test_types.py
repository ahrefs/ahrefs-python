"""Tests for generated Pydantic type models."""

from ahrefs.types._generated import (
    SiteExplorerDomainRatingData,
    SiteExplorerDomainRatingRequest,
    SiteExplorerDomainRatingResponse,
    SiteExplorerOrganicKeywordsRequest,
)


class TestRequestModels:
    def test_domain_rating_request(self) -> None:
        req = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
        assert req.target == "ahrefs.com"
        assert req.date == "2025-01-15"

    def test_domain_rating_request_serialization(self) -> None:
        req = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
        data = req.model_dump(mode="json", exclude_none=True)
        assert data["target"] == "ahrefs.com"
        assert data["date"] == "2025-01-15"

    def test_optional_fields_excluded_when_none(self) -> None:
        req = SiteExplorerOrganicKeywordsRequest(
            target="ahrefs.com", date="2025-01-15", select="keyword,position"
        )
        data = req.model_dump(mode="json", exclude_none=True)
        assert "target" in data
        # Optional fields like where, limit should not appear when not set
        assert "where" not in data

    def test_organic_keywords_request(self) -> None:
        req = SiteExplorerOrganicKeywordsRequest(
            target="ahrefs.com",
            date="2025-01-15",
            select="keyword,position,volume",
            limit=10,
        )
        data = req.model_dump(mode="json", exclude_none=True)
        assert data["target"] == "ahrefs.com"
        assert data["limit"] == 10


class TestResponseModels:
    def test_domain_rating_response_from_dict(self) -> None:
        raw = {
            "domain_rating": {
                "domain_rating": 85.5,
                "ahrefs_rank": 123,
            }
        }
        resp = SiteExplorerDomainRatingResponse.model_validate(raw)
        assert resp.domain_rating is not None
        assert isinstance(resp.domain_rating, SiteExplorerDomainRatingData)
        assert resp.domain_rating.domain_rating == 85.5

    def test_response_round_trip(self) -> None:
        raw = {
            "domain_rating": {
                "domain_rating": 75.0,
                "ahrefs_rank": 456,
            }
        }
        resp = SiteExplorerDomainRatingResponse.model_validate(raw)
        dumped = resp.model_dump(mode="json")
        resp2 = SiteExplorerDomainRatingResponse.model_validate(dumped)
        assert resp2.domain_rating is not None
        assert resp2.domain_rating.domain_rating == 75.0

    def test_data_model_directly(self) -> None:
        data = SiteExplorerDomainRatingData(domain_rating=90.0, ahrefs_rank=50)
        assert data.domain_rating == 90.0
        assert data.ahrefs_rank == 50

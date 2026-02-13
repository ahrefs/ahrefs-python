"""Tests for DateStr and SelectStr coercion types."""

import datetime

from pydantic import BaseModel

from ahrefs.types._coercions import DateStr, SelectStr
from ahrefs.types._generated import (
    SiteExplorerDomainRatingRequest,
    SiteExplorerOrganicKeywordsRequest,
)


class _DateModel(BaseModel):
    date: DateStr


class _SelectModel(BaseModel):
    select: SelectStr


class TestDateStr:
    def test_string_passthrough(self) -> None:
        m = _DateModel(date="2025-01-15")
        assert m.date == "2025-01-15"

    def test_date_object_converted(self) -> None:
        m = _DateModel(date=datetime.date(2025, 1, 15))
        assert m.date == "2025-01-15"


class TestSelectStr:
    def test_string_passthrough(self) -> None:
        m = _SelectModel(select="keyword,position")
        assert m.select == "keyword,position"

    def test_list_joined(self) -> None:
        m = _SelectModel(select=["keyword", "position"])
        assert m.select == "keyword,position"


class TestRequestModelRoundTrip:
    def test_date_with_date_object(self) -> None:
        req = SiteExplorerDomainRatingRequest(
            target="ahrefs.com", date=datetime.date(2025, 1, 15)
        )
        data = req.model_dump(mode="json")
        assert data["date"] == "2025-01-15"

    def test_date_with_string(self) -> None:
        req = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
        data = req.model_dump(mode="json")
        assert data["date"] == "2025-01-15"

    def test_select_with_list(self) -> None:
        req = SiteExplorerOrganicKeywordsRequest(
            target="ahrefs.com",
            date="2025-01-15",
            select=["keyword", "position"],
        )
        data = req.model_dump(mode="json", exclude_none=True)
        assert data["select"] == "keyword,position"

    def test_select_with_string(self) -> None:
        req = SiteExplorerOrganicKeywordsRequest(
            target="ahrefs.com",
            date="2025-01-15",
            select="keyword,position",
        )
        data = req.model_dump(mode="json", exclude_none=True)
        assert data["select"] == "keyword,position"

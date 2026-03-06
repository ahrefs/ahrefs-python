"""Tests for DateStr, SelectStr, and HistoryStr coercion types."""

import datetime

import pytest
from pydantic import BaseModel, ValidationError

from ahrefs.types._coercions import DateStr, HistoryStr, SelectStr
from ahrefs.types._generated import (
    SiteExplorerBestByExternalLinksRequest,
    SiteExplorerDomainRatingRequest,
    SiteExplorerOrganicKeywordsRequest,
)


class _DateModel(BaseModel):
    date: DateStr


class _SelectModel(BaseModel):
    select: SelectStr


class _HistoryModel(BaseModel):
    history: HistoryStr


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


class TestHistoryStr:
    def test_live(self) -> None:
        m = _HistoryModel(history="live")
        assert m.history == "live"

    def test_all_time(self) -> None:
        m = _HistoryModel(history="all_time")
        assert m.history == "all_time"

    def test_since_date(self) -> None:
        m = _HistoryModel(history="since:2025-01-01")
        assert m.history == "since:2025-01-01"

    def test_invalid_value_rejected(self) -> None:
        with pytest.raises(ValidationError, match="recent"):
            _HistoryModel(history="recent")

    def test_invalid_since_format_rejected(self) -> None:
        with pytest.raises(ValidationError, match="Invalid history value"):
            _HistoryModel(history="since:01-2025")


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

    def test_history_valid(self) -> None:
        req = SiteExplorerBestByExternalLinksRequest(
            target="x", select="url_to", history="live"
        )
        assert req.history == "live"

    def test_history_invalid_rejected(self) -> None:
        with pytest.raises(ValidationError, match="recent"):
            SiteExplorerBestByExternalLinksRequest(
                target="x", select="url_to", history="recent"
            )

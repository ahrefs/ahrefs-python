"""Pydantic coercion types for request model fields."""

from __future__ import annotations

import datetime
from typing import Annotated, TypeAlias

from pydantic import BeforeValidator


def _coerce_date(value: str | datetime.date) -> str:
    """Accept str or datetime.date, return ISO date string."""
    if isinstance(value, datetime.date):
        return value.isoformat()
    return value


def _coerce_select(value: str | list[str]) -> str:
    """Accept str or list[str], return comma-separated string."""
    if isinstance(value, list):
        return ",".join(value)
    return value


DateStr: TypeAlias = Annotated[str | datetime.date, BeforeValidator(_coerce_date)]
"""String that also accepts datetime.date, converting to YYYY-MM-DD."""

SelectStr: TypeAlias = Annotated[str | list[str], BeforeValidator(_coerce_select)]
"""String that also accepts list[str], converting to comma-separated."""

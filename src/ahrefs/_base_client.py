"""Shared client configuration and utilities."""

from __future__ import annotations

import os
import random
from dataclasses import dataclass

from ahrefs._exceptions import AuthenticationError
from ahrefs._version import __version__

DEFAULT_BASE_URL = "https://api.ahrefs.com/v3"
DEFAULT_TIMEOUT = 60.0
DEFAULT_MAX_RETRIES = 2


@dataclass(frozen=True)
class ClientConfig:
    """Immutable configuration for the Ahrefs client."""

    api_key: str
    base_url: str = DEFAULT_BASE_URL
    timeout: float = DEFAULT_TIMEOUT
    max_retries: int = DEFAULT_MAX_RETRIES

    @classmethod
    def from_env_or_args(
        cls,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ClientConfig:
        resolved_key = api_key or os.environ.get("AHREFS_API_KEY")
        if not resolved_key:
            raise AuthenticationError(
                "No API key provided. Pass api_key= or set AHREFS_API_KEY env var."
            )
        return cls(
            api_key=resolved_key,
            base_url=base_url or DEFAULT_BASE_URL,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
            max_retries=max_retries if max_retries is not None else DEFAULT_MAX_RETRIES,
        )


def build_headers(api_key: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        "User-Agent": f"ahrefs-python/{__version__}",
    }


def build_url(base_url: str, api_section: str, endpoint: str) -> str:
    return f"{base_url}/{api_section}/{endpoint}"


def calculate_backoff(attempt: int, base: float = 0.5, max_delay: float = 8.0) -> float:
    """Calculate exponential backoff delay with jitter.

    delay = min(base * 2^attempt, max_delay) + random jitter [0, base)
    """
    delay: float = min(base * (2 ** attempt), max_delay)
    jitter: float = random.random() * base
    return delay + jitter

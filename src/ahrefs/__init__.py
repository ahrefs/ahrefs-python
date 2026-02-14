"""Python client for the Ahrefs API."""

from __future__ import annotations

from ahrefs._client import AsyncAhrefsClient
from ahrefs._exceptions import (
    AhrefsError,
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
)
from ahrefs._sync_client import AhrefsClient
from ahrefs._version import __version__

__all__ = [
    "__version__",
    "AhrefsClient",
    "AsyncAhrefsClient",
    "AhrefsError",
    "APIError",
    "AuthenticationError",
    "RateLimitError",
    "NotFoundError",
    "APIConnectionError",
    "APITimeoutError",
]

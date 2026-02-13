"""Python client for the Ahrefs API."""

from __future__ import annotations

import warnings

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


def __getattr__(name: str) -> object:
    """Lazy import types from ahrefs.types with deprecation warning."""
    from ahrefs.types import _generated

    try:
        value = getattr(_generated, name)
    except AttributeError:
        raise AttributeError(f"module 'ahrefs' has no attribute {name!r}") from None
    warnings.warn(
        f"Importing {name!r} from 'ahrefs' is deprecated. "
        f"Use 'from ahrefs.types import {name}' instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return value

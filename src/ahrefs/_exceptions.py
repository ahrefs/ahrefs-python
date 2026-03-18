"""Ahrefs API exception hierarchy."""

from __future__ import annotations

import json

import httpx


class AhrefsError(Exception):
    """Base exception for all Ahrefs client errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message: str = message


class APIError(AhrefsError):
    """Error response from the Ahrefs API (HTTP 4xx/5xx)."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        response_body: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class AuthenticationError(APIError):
    """401 Unauthorized - invalid or missing API key."""

    def __init__(
        self,
        message: str = "Invalid API key",
        *,
        response_body: str | None = None,
    ) -> None:
        super().__init__(message, status_code=401, response_body=response_body)


class RateLimitError(APIError):
    """429 Too Many Requests - rate limit exceeded."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        *,
        response_body: str | None = None,
        retry_after: float | None = None,
    ) -> None:
        super().__init__(message, status_code=429, response_body=response_body)
        self.retry_after: float | None = retry_after


class NotFoundError(APIError):
    """404 Not Found."""

    def __init__(
        self,
        message: str = "Resource not found",
        *,
        response_body: str | None = None,
    ) -> None:
        super().__init__(message, status_code=404, response_body=response_body)


class APIConnectionError(AhrefsError):
    """Failed to connect to the Ahrefs API (network error)."""


class APITimeoutError(APIConnectionError):
    """Request to the Ahrefs API timed out."""


def _parse_retry_after(response: httpx.Response) -> float | None:
    """Parse numeric Retry-After header. Ignores HTTP-date format."""
    value = response.headers.get("retry-after")
    if value is None:
        return None
    try:
        return min(float(value), 60.0)
    except ValueError:
        return None


def _extract_error_message(body: str) -> str:
    """Extract a human-readable message from an API error body.

    Parses JSON bodies for ``message`` or ``error`` fields.
    Falls back to the raw text truncated to 200 characters.
    """
    try:
        data = json.loads(body)
        if isinstance(data, dict):
            for key in ("message", "error"):
                value = data.get(key)
                if isinstance(value, str) and value:
                    return value
    except (json.JSONDecodeError, ValueError):
        pass
    return body[:200]


_404_HINT = (
    "Hint: This can mean the data is not available for the requested date, "
    "the target was not found in the index, or a parameter value is incorrect."
)


def _enrich_404_message(message: str) -> str:
    """Append a contextual hint to a 404 error message."""
    return f"{message}\n{_404_HINT}"


def raise_for_status(response: httpx.Response) -> None:
    """Translate HTTP error responses into typed exceptions."""
    if response.is_success:
        return

    body: str = response.text
    status: int = response.status_code
    message: str = _extract_error_message(body)

    if status == 401:
        raise AuthenticationError(message=message, response_body=body)
    elif status == 404:
        raise NotFoundError(message=_enrich_404_message(message), response_body=body)
    elif status == 429:
        retry_after = _parse_retry_after(response)
        raise RateLimitError(
            message=message, response_body=body, retry_after=retry_after
        )
    else:
        raise APIError(
            message=f"HTTP {status}: {message}",
            status_code=status,
            response_body=body,
        )

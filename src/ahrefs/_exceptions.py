"""Ahrefs API exception hierarchy."""

from __future__ import annotations

import httpx


class AhrefsError(Exception):
    """Base exception for all Ahrefs client errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


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
        self.retry_after = retry_after


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


def raise_for_status(response: httpx.Response) -> None:
    """Translate HTTP error responses into typed exceptions."""
    if response.is_success:
        return

    body = response.text
    status = response.status_code

    if status == 401:
        raise AuthenticationError(response_body=body)
    elif status == 404:
        raise NotFoundError(response_body=body)
    elif status == 429:
        retry_after = _parse_retry_after(response)
        raise RateLimitError(response_body=body, retry_after=retry_after)
    else:
        raise APIError(
            f"HTTP {status}: {body[:200]}",
            status_code=status,
            response_body=body,
        )

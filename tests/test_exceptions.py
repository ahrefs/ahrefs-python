"""Tests for the exception hierarchy and raise_for_status."""

import httpx
import pytest

from ahrefs._exceptions import (
    AhrefsError,
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    raise_for_status,
)


def _make_response(status_code: int, text: str = "") -> httpx.Response:
    """Create a mock httpx.Response."""
    return httpx.Response(
        status_code=status_code,
        text=text,
        request=httpx.Request("GET", "https://api.ahrefs.com/v3/test"),
    )


class TestExceptionHierarchy:
    def test_base_hierarchy(self) -> None:
        assert issubclass(APIError, AhrefsError)
        assert issubclass(AuthenticationError, APIError)
        assert issubclass(RateLimitError, APIError)
        assert issubclass(NotFoundError, APIError)
        assert issubclass(APIConnectionError, AhrefsError)
        assert issubclass(APITimeoutError, APIConnectionError)

    def test_api_error_has_status_code(self) -> None:
        err = APIError("test", status_code=500, response_body="error body")
        assert err.status_code == 500
        assert err.response_body == "error body"
        assert err.message == "test"

    def test_authentication_error_defaults(self) -> None:
        err = AuthenticationError()
        assert err.status_code == 401
        assert err.message == "Invalid API key"

    def test_rate_limit_error_defaults(self) -> None:
        err = RateLimitError()
        assert err.status_code == 429

    def test_not_found_error_defaults(self) -> None:
        err = NotFoundError()
        assert err.status_code == 404


class TestRaiseForStatus:
    def test_success_does_nothing(self) -> None:
        response = _make_response(200)
        raise_for_status(response)  # should not raise

    def test_401_raises_authentication_error(self) -> None:
        response = _make_response(401, "Unauthorized")
        with pytest.raises(AuthenticationError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.status_code == 401
        assert exc_info.value.response_body == "Unauthorized"

    def test_404_raises_not_found_error(self) -> None:
        response = _make_response(404, "Not Found")
        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.status_code == 404

    def test_429_raises_rate_limit_error(self) -> None:
        response = _make_response(429, "Too Many Requests")
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.status_code == 429

    def test_500_raises_api_error(self) -> None:
        response = _make_response(500, "Internal Server Error")
        with pytest.raises(APIError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.status_code == 500
        assert "500" in exc_info.value.message

    def test_catch_all_with_ahrefs_error(self) -> None:
        """All API exceptions can be caught with AhrefsError."""
        response = _make_response(401)
        with pytest.raises(AhrefsError):
            raise_for_status(response)

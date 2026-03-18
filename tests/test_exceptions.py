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
    _enrich_404_message,
    _extract_error_message,
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


class TestExtractErrorMessage:
    def test_json_with_message_field(self) -> None:
        body = '{"message": "Resource not found"}'
        assert _extract_error_message(body) == "Resource not found"

    def test_json_with_error_field(self) -> None:
        body = '{"error": "Invalid token"}'
        assert _extract_error_message(body) == "Invalid token"

    def test_message_takes_priority_over_error(self) -> None:
        body = '{"message": "msg", "error": "err"}'
        assert _extract_error_message(body) == "msg"

    def test_non_json_body(self) -> None:
        body = "Not JSON at all"
        assert _extract_error_message(body) == "Not JSON at all"

    def test_non_json_body_truncated(self) -> None:
        body = "x" * 500
        assert len(_extract_error_message(body)) == 200

    def test_json_without_message_or_error(self) -> None:
        body = '{"status": "fail"}'
        assert _extract_error_message(body) == body[:200]

    def test_empty_message_field_falls_back(self) -> None:
        body = '{"message": ""}'
        assert _extract_error_message(body) == body[:200]


class TestEnrich404Message:
    def test_hint_appended(self) -> None:
        result = _enrich_404_message("Resource not found")
        assert result.startswith("Resource not found")
        assert "\nHint:" in result
        assert "date" in result
        assert "target" in result.lower()
        assert "parameter" in result.lower()


class TestErrorEnrichmentIntegration:
    def test_404_json_body_enriched(self) -> None:
        response = _make_response(404, '{"message": "Resource not found"}')
        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(response)
        assert "Resource not found" in exc_info.value.message
        assert "Hint:" in exc_info.value.message
        assert exc_info.value.response_body == '{"message": "Resource not found"}'

    def test_404_non_json_body(self) -> None:
        response = _make_response(404, "Not Found")
        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(response)
        assert "Not Found" in exc_info.value.message
        assert "Hint:" in exc_info.value.message

    def test_401_json_body_parsed(self) -> None:
        response = _make_response(401, '{"error": "Invalid token"}')
        with pytest.raises(AuthenticationError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.message == "Invalid token"
        assert exc_info.value.response_body == '{"error": "Invalid token"}'

    def test_429_json_body_parsed(self) -> None:
        response = _make_response(429, '{"message": "Rate limit hit"}')
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.message == "Rate limit hit"

    def test_generic_error_json_parsed(self) -> None:
        response = _make_response(400, '{"message": "Validation failed"}')
        with pytest.raises(APIError) as exc_info:
            raise_for_status(response)
        assert "HTTP 400:" in exc_info.value.message
        assert "Validation failed" in exc_info.value.message

    def test_response_body_preserved(self) -> None:
        raw = '{"message": "Resource not found", "extra": "data"}'
        response = _make_response(404, raw)
        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(response)
        assert exc_info.value.response_body == raw

"""Async Ahrefs API client."""

from __future__ import annotations

import asyncio
from typing import TypeVar

import httpx
from pydantic import BaseModel

from ahrefs._base_client import (
    ClientConfig,
    build_headers,
    build_url,
    calculate_backoff,
)
from ahrefs._exceptions import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    RateLimitError,
    raise_for_status,
)
from ahrefs._generated_methods import GeneratedMethodsMixin

T = TypeVar("T", bound=BaseModel)


class AsyncAhrefsClient(GeneratedMethodsMixin):
    """Async client for the Ahrefs API.

    Args:
        api_key: API key. Defaults to AHREFS_API_KEY env var.
        base_url: Override the API base URL.
        timeout: Request timeout in seconds (default: 60).
        max_retries: Number of retries on transient errors (default: 2).
        http_client: Provide your own httpx.AsyncClient for full control.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._config = ClientConfig.from_env_or_args(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._owns_client = http_client is None
        self._client = http_client or httpx.AsyncClient(
            timeout=self._config.timeout,
        )

    async def _request(
        self,
        api_section: str,
        endpoint: str,
        request_model: BaseModel,
        response_model_class: type[T],
        *,
        exclude_none: bool = False,
        http_method: str = "GET",
    ) -> T:
        """Make a typed API request. Called by generated endpoint methods."""
        url = build_url(self._config.base_url, api_section, endpoint)
        params = request_model.model_dump(mode="json", exclude_none=exclude_none)

        last_exc: Exception | None = None
        for attempt in range(1 + self._config.max_retries):
            if attempt > 0 and last_exc is not None:
                if (
                    isinstance(last_exc, RateLimitError)
                    and last_exc.retry_after is not None
                ):
                    delay = last_exc.retry_after
                else:
                    delay = calculate_backoff(attempt - 1)
                await asyncio.sleep(delay)
            try:
                if http_method == "POST":
                    response = await self._client.post(
                        url,
                        json=params,
                        headers=build_headers(self._config.api_key),
                    )
                else:
                    response = await self._client.get(
                        url,
                        params=params,
                        headers=build_headers(self._config.api_key),
                    )
                raise_for_status(response)
                return response_model_class.model_validate(response.json())
            except RateLimitError as exc:
                last_exc = exc
            except APIError as exc:
                if exc.status_code >= 500:
                    last_exc = exc
                else:
                    raise
            except httpx.TimeoutException as exc:
                last_exc = APITimeoutError(str(exc))
                last_exc.__cause__ = exc
            except httpx.NetworkError as exc:
                last_exc = APIConnectionError(str(exc))
                last_exc.__cause__ = exc

        raise last_exc  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]

    async def close(self) -> None:
        """Close the underlying HTTP client if we own it."""
        if self._owns_client:
            await self._client.aclose()

    async def __aenter__(self) -> AsyncAhrefsClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()

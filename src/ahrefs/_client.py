"""Async Ahrefs API client."""

from __future__ import annotations

import asyncio
from typing import Any, TypeVar, cast

import httpx
from httpx import AsyncClient
from pydantic import BaseModel

from ahrefs._base_client import (
    ClientConfig,
    build_headers,
    build_url,
    calculate_backoff,
    flatten_list_params,
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
        self._config: ClientConfig = ClientConfig.from_env_or_args(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._owns_client: bool = http_client is None
        self._client: AsyncClient = http_client or httpx.AsyncClient(
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
        query_params: dict[str, Any] | None = None,
    ) -> T:
        """Make a typed API request. Called by generated endpoint methods."""
        url: str = build_url(self._config.base_url, api_section, endpoint)
        params: dict[str, Any] = request_model.model_dump(
            mode="json", by_alias=True, exclude_none=exclude_none
        )

        last_exc: Exception | None = None
        for attempt in range(1 + self._config.max_retries):
            if attempt > 0 and last_exc is not None:
                if (
                    isinstance(last_exc, RateLimitError)
                    and last_exc.retry_after is not None
                ):
                    delay: float = last_exc.retry_after
                else:
                    delay = calculate_backoff(attempt=attempt - 1)
                await asyncio.sleep(delay)
            try:
                if http_method in ("POST", "PUT", "PATCH"):
                    body: dict[str, Any] = params
                    url_params: dict[str, Any] | None = (
                        {k: v for k, v in query_params.items() if v is not None}
                        if query_params
                        else None
                    )
                    if url_params:
                        url_params = flatten_list_params(url_params)
                        body = {
                            k: v for k, v in params.items() if k not in url_params
                        }
                    response = await self._client.request(
                        http_method,
                        url,
                        json=body,
                        params=url_params or None,
                        headers=build_headers(self._config.api_key),
                    )
                else:
                    response = await self._client.get(
                        url,
                        params=flatten_list_params(params),
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
                last_exc = cast(Exception, APITimeoutError(message=str(exc)))
                last_exc.__cause__ = exc
            except httpx.NetworkError as exc:
                last_exc = cast(Exception, APIConnectionError(message=str(exc)))
                last_exc.__cause__ = exc

        if last_exc is None:
            raise RuntimeError("No exception to re-raise after retries")
        raise last_exc

    async def close(self) -> None:
        """Close the underlying HTTP client if we own it."""
        if self._owns_client:
            await self._client.aclose()

    async def __aenter__(self) -> AsyncAhrefsClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()

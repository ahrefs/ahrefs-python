"""Tests for client construction and configuration."""
# pyright: reportPrivateUsage=false

import pytest

from ahrefs import AhrefsClient, AsyncAhrefsClient
from ahrefs._base_client import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from ahrefs._exceptions import AuthenticationError


class TestClientConstruction:
    def test_explicit_api_key(self) -> None:
        client = AhrefsClient(api_key="test-key")
        assert client._config.api_key == "test-key"
        client.close()

    def test_api_key_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("AHREFS_API_KEY", "env-key")
        client = AhrefsClient()
        assert client._config.api_key == "env-key"
        client.close()

    def test_missing_api_key_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        with pytest.raises(AuthenticationError, match="No API key"):
            AhrefsClient()

    def test_default_config(self) -> None:
        client = AhrefsClient(api_key="test")
        assert client._config.base_url == DEFAULT_BASE_URL
        assert client._config.timeout == DEFAULT_TIMEOUT
        assert client._config.max_retries == DEFAULT_MAX_RETRIES
        client.close()

    def test_custom_config(self) -> None:
        client = AhrefsClient(
            api_key="test",
            base_url="https://custom.api.com",
            timeout=30.0,
            max_retries=5,
        )
        assert client._config.base_url == "https://custom.api.com"
        assert client._config.timeout == 30.0
        assert client._config.max_retries == 5
        client.close()

    def test_keyword_only_args(self) -> None:
        """Constructor requires keyword arguments."""
        with pytest.raises(TypeError):
            AhrefsClient("test-key")  # type: ignore[misc]  # pyright: ignore[reportCallIssue]


class TestAsyncClientConstruction:
    def test_explicit_api_key(self) -> None:
        client = AsyncAhrefsClient(api_key="test-key")
        assert client._config.api_key == "test-key"

    def test_missing_api_key_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("AHREFS_API_KEY", raising=False)
        with pytest.raises(AuthenticationError, match="No API key"):
            AsyncAhrefsClient()


class TestContextManager:
    def test_sync_context_manager(self) -> None:
        with AhrefsClient(api_key="test") as client:
            assert client._config.api_key == "test"
        # client should be closed after context exit

    @pytest.mark.asyncio
    async def test_async_context_manager(self) -> None:
        async with AsyncAhrefsClient(api_key="test") as client:
            assert client._config.api_key == "test"
        # client should be closed after context exit


class TestExternalHttpClient:
    def test_sync_external_client_not_closed(self) -> None:
        import httpx

        external = httpx.Client()
        client = AhrefsClient(api_key="test", http_client=external)
        assert not client._owns_client
        client.close()
        # external client should NOT be closed
        assert not external.is_closed
        external.close()

    @pytest.mark.asyncio
    async def test_async_external_client_not_closed(self) -> None:
        import httpx

        external = httpx.AsyncClient()
        client = AsyncAhrefsClient(api_key="test", http_client=external)
        assert not client._owns_client
        await client.close()
        assert not external.is_closed
        await external.aclose()

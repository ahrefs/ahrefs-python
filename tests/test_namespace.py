"""Tests for namespace exports and deprecation warnings."""

import warnings

import pytest


class TestTypesNamespace:
    def test_import_from_ahrefs_types(self) -> None:
        """Types should be importable from ahrefs.types without warning."""
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            from ahrefs.types import SiteExplorerDomainRatingRequest

            assert SiteExplorerDomainRatingRequest is not None

    def test_import_from_top_level_emits_deprecation(self) -> None:
        """Importing a type from top-level 'ahrefs' should emit DeprecationWarning."""
        with pytest.warns(DeprecationWarning, match="from ahrefs.types"):
            import ahrefs

            _ = ahrefs.SiteExplorerDomainRatingRequest

    def test_top_level_non_existent_raises(self) -> None:
        """Accessing a non-existent attribute on ahrefs should raise AttributeError."""
        import ahrefs

        with pytest.raises(AttributeError, match="has no attribute"):
            _ = ahrefs.TotallyFakeClassName

    def test_client_exports_no_warning(self) -> None:
        """Accessing client classes should not emit warnings."""
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            from ahrefs import AhrefsClient, AsyncAhrefsClient

            assert AhrefsClient is not None
            assert AsyncAhrefsClient is not None

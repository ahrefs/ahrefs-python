"""Tests for namespace exports."""

import warnings

import pytest


class TestTypesNamespace:
    def test_import_from_ahrefs_types(self) -> None:
        """Types should be importable from ahrefs.types without warning."""
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            from ahrefs.types import SiteExplorerDomainRatingRequest

            assert SiteExplorerDomainRatingRequest is not None

    def test_top_level_type_import_raises(self) -> None:
        """'from ahrefs import <GeneratedType>' should raise ImportError."""
        with pytest.raises(ImportError):
            exec("from ahrefs import SiteExplorerDomainRatingRequest")  # noqa: S102

    def test_top_level_type_attribute_raises(self) -> None:
        """'ahrefs.<GeneratedType>' should raise AttributeError."""
        import ahrefs

        with pytest.raises(AttributeError):
            ahrefs.SiteExplorerDomainRatingRequest  # noqa: B018

    def test_top_level_non_existent_raises(self) -> None:
        """Accessing a non-existent attribute on ahrefs should raise AttributeError."""
        import ahrefs

        with pytest.raises(AttributeError):
            ahrefs.TotallyFakeClassName  # noqa: B018

    def test_client_exports_no_warning(self) -> None:
        """Accessing client classes should not emit warnings."""
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            from ahrefs import AhrefsClient, AsyncAhrefsClient

            assert AhrefsClient is not None
            assert AsyncAhrefsClient is not None

"""Tests for namespace exports."""

import ast
import warnings
from pathlib import Path

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


_GENERATED_PY = (
    Path(__file__).resolve().parent.parent
    / "src" / "ahrefs" / "types" / "_generated.py"
)
_COERCION_TYPES = {"DateStr", "SelectStr", "HistoryStr"}


def _get_generated_classes() -> set[str]:
    """Extract all public class names from _generated.py using AST."""
    tree = ast.parse(_GENERATED_PY.read_text())
    return {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef) and not node.name.startswith("_")
    }


class TestAllCompleteness:
    def test_all_generated_non_response_types_in_all(self) -> None:
        """Every non-Response class in _generated.py must be in __all__."""
        import ahrefs.types

        all_set = set(ahrefs.types.__all__)
        generated = _get_generated_classes()
        exportable = {c for c in generated if not c.endswith("Response")}
        missing = exportable - all_set
        assert not missing, f"Missing from __all__: {sorted(missing)}"

    def test_no_stale_entries_in_all(self) -> None:
        """Every __all__ entry (except coercions) must exist in _generated.py."""
        import ahrefs.types

        generated = _get_generated_classes()
        stale = {
            name
            for name in ahrefs.types.__all__
            if name not in generated and name not in _COERCION_TYPES
        }
        assert not stale, f"Stale entries in __all__: {sorted(stale)}"

    def test_no_response_types_in_all(self) -> None:
        """No Response types should leak into __all__."""
        import ahrefs.types

        response_types = [n for n in ahrefs.types.__all__ if n.endswith("Response")]
        assert not response_types, f"Response types in __all__: {response_types}"

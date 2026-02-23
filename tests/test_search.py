"""Tests for BM25 method search module."""

import json
import subprocess
import sys
from pathlib import Path
from typing import cast

from ahrefs.search import MethodSearcher, MethodSearchResult, search_api_methods


class TestIndexLoading:
    def test_index_loads(self) -> None:
        searcher = MethodSearcher()
        # Must match the actual index count, not just > 0
        src = Path(__file__).parent.parent / "src" / "ahrefs"
        with open(src / "_search_index.json") as f:
            expected = len(json.load(f))
        assert len(searcher._entries) == expected

    def test_index_method_count_matches_generated(self) -> None:
        src = Path(__file__).parent.parent / "src" / "ahrefs"
        with open(src / "_search_index.json") as f:
            index = json.load(f)

        content = (src / "_generated_methods.py").read_text()
        # Count async methods excluding _request
        method_count = content.count("    async def ") - 1
        assert len(index) == method_count

    def test_index_entry_structure(self) -> None:
        searcher = MethodSearcher()
        entry = searcher._entries[0]
        assert "method" in entry
        assert "section" in entry
        assert "description" in entry
        assert "parameters" in entry
        assert "returns" in entry
        assert "type" in entry["returns"]
        assert "fields" in entry["returns"]


class TestSearchRelevance:
    def test_domain_rating_search(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating")
        methods = [r.method for r in results]
        assert "site_explorer_domain_rating" in methods

    def test_domain_rating_positive_score(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating")
        dr_results = [r for r in results if r.method == "site_explorer_domain_rating"]
        assert len(dr_results) == 1
        assert dr_results[0].score > 0

    def test_backlinks_search(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("backlinks", limit=10)
        methods = [r.method for r in results]
        assert "site_explorer_all_backlinks" in methods

    def test_no_matches(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("xyzzyplugh_nonexistent")
        assert results == []

    def test_empty_query(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("")
        assert results == []

    def test_underscore_query_normalized(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain_rating")
        methods = [r.method for r in results]
        assert "site_explorer_domain_rating" in methods


class TestSectionFiltering:
    def test_filter_by_section(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("backlinks", section="site-explorer")
        assert len(results) > 0
        for r in results:
            assert r.section == "site-explorer"

    def test_unknown_section(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("anything", section="nonexistent")
        assert results == []


class TestMethodSearchResult:
    def test_result_types(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating")
        assert len(results) > 0
        r = results[0]
        assert isinstance(r, MethodSearchResult)
        assert isinstance(r.method, str)
        assert isinstance(r.score, float)
        assert isinstance(r.parameters, list)
        assert isinstance(r.section, str)
        assert isinstance(r.description, str)
        assert isinstance(r.returns, dict)

    def test_frozen_dataclass(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating")
        r = results[0]
        try:
            r.method = "foo"  # type: ignore[misc]
            raise AssertionError("Should have raised FrozenInstanceError")
        except AttributeError:
            pass

    def test_domain_rating_entry(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating", limit=10)
        dr = [r for r in results if r.method == "site_explorer_domain_rating"][0]
        assert dr.section == "site-explorer"
        param_names = [p["name"] for p in dr.parameters]
        assert "target" in param_names
        assert "date" in param_names
        fields = cast(list[dict[str, str]], dr.returns["fields"])
        field_names = [f["name"] for f in fields]
        assert "domain_rating" in field_names


class TestFormatForContext:
    def test_format_structure(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating", limit=10)
        dr = [r for r in results if r.method == "site_explorer_domain_rating"][0]
        output = dr.format_for_context()
        assert output.startswith("### site_explorer_domain_rating()")
        assert "Section: site-explorer" in output
        assert "Parameters:" in output
        assert "Returns:" in output

    def test_empty_description_omitted(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating", limit=10)
        dr = [r for r in results if r.method == "site_explorer_domain_rating"][0]
        output = dr.format_for_context()
        # Parameters with descriptions should have ": desc"
        # Parameters without should not end with ": "
        for line in output.split("\n"):
            assert not line.endswith(": ")

    def test_no_double_period(self) -> None:
        result = MethodSearchResult(
            method="test",
            section="test",
            description="Already has period.",
            score=1.0,
            parameters=[],
            returns={"type": "str", "fields": []},
        )
        output = result.format_for_context()
        assert "Already has period." in output
        assert "Already has period.." not in output

    def test_results_are_independent_copies(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating", limit=2)
        assert len(results) >= 1
        results[0].parameters.append({"name": "injected"})
        fresh = searcher.search("domain rating", limit=2)
        param_names = [p["name"] for p in fresh[0].parameters]
        assert "injected" not in param_names

    def test_negative_limit(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating", limit=-1)
        assert results == []


class TestListSections:
    def test_all_sections(self) -> None:
        searcher = MethodSearcher()
        sections = searcher.list_sections()
        assert sections == [
            "batch-analysis",
            "brand-radar",
            "keywords-explorer",
            "rank-tracker",
            "serp-overview",
            "site-audit",
            "site-explorer",
        ]


class TestSearchApiMethods:
    def test_convenience_function(self) -> None:
        result = search_api_methods("domain rating", limit=2)
        assert isinstance(result, str)
        assert "site_explorer_domain_rating" in result

    def test_limit(self) -> None:
        result = search_api_methods("domain rating", limit=2)
        # "domain rating" matches multiple methods; verify exactly 2 returned
        blocks = [b for b in result.split("\n\n") if b.startswith("### ")]
        assert len(blocks) == 2

    def test_section_filter(self) -> None:
        result = search_api_methods("overview", section="brand-radar")
        assert "Section: brand-radar" in result


class TestNamespace:
    def test_not_in_top_level(self) -> None:
        """MethodSearcher should not be importable from the top-level ahrefs package."""
        import ahrefs
        assert not hasattr(ahrefs, "MethodSearcher")
        assert not hasattr(ahrefs, "search_api_methods")


class TestSearchEdgeCases:
    def test_limit_zero(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("domain rating", limit=0)
        assert results == []

    def test_whitespace_only_query(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("   ")
        assert results == []

    def test_hyphen_query_normalized(self) -> None:
        searcher = MethodSearcher()
        results = searcher.search("site-explorer")
        methods = [r.method for r in results]
        assert any("site_explorer" in m for m in methods)


class TestCLI:
    """Tests for python -m ahrefs.api_search CLI."""

    def _run(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-m", "ahrefs.api_search", *args],
            capture_output=True,
            text=True,
            timeout=30,
        )

    def test_sections_flag(self) -> None:
        result = self._run("--sections")
        assert result.returncode == 0
        assert "site-explorer" in result.stdout

    def test_search_query(self) -> None:
        result = self._run("domain rating")
        assert result.returncode == 0
        assert "site_explorer_domain_rating" in result.stdout

    def test_json_output(self) -> None:
        result = self._run("domain rating", "--json", "-n", "1")
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert isinstance(data, list)
        assert len(data) == 1
        assert "method" in data[0]
        assert "score" in data[0]

    def test_no_query_exits_with_help(self) -> None:
        result = self._run()
        assert result.returncode == 1

    def test_no_results(self) -> None:
        result = self._run("xyzzyplugh_nonexistent")
        assert result.returncode == 0
        assert "No results" in result.stderr


class TestNoDependencies:
    def test_stdlib_only(self) -> None:
        import ast

        import ahrefs.search as mod
        assert mod.__file__ is not None
        source = Path(mod.__file__).read_text()
        tree = ast.parse(source)
        allowed = {
            "json", "math", "dataclasses",
            "pathlib", "typing", "__future__",
        }
        # Walk the full AST to catch imports inside functions/conditionals
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    assert alias.name in allowed, (
                        f"Unexpected import: {alias.name}"
                    )
            elif isinstance(node, ast.ImportFrom):
                assert node.module is not None
                assert node.module in allowed, (
                    f"Unexpected import from: {node.module}"
                )

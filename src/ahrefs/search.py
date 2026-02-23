"""BM25 Okapi search over generated API methods.

Usage::

    from ahrefs.search import MethodSearcher

    searcher = MethodSearcher()
    results = searcher.search("domain rating")
    for r in results:
        print(r.format_for_context())
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

_INDEX_PATH = Path(__file__).parent / "_search_index.json"

# BM25 Okapi constants
_K1 = 1.5
_B = 0.75


def _tokenize(text: str) -> list[str]:
    """Normalize and split text into search tokens.

    Only underscores and hyphens are replaced with spaces (not all punctuation)
    because the corpus is structured API metadata — method names use underscores
    (site_explorer_domain_rating) and sections use hyphens (site-explorer).
    General punctuation in descriptions (periods, commas) is left intact since
    queries target field names, not prose.
    """
    return text.lower().replace("_", " ").replace("-", " ").split()


@dataclass(frozen=True)
class MethodSearchResult:
    """A single search result with method metadata and relevance score."""

    method: str
    section: str
    description: str
    score: float
    parameters: list[dict[str, str | bool]]
    returns: dict[str, str | list[dict[str, str]]]

    def format_for_context(self) -> str:
        """Format this result as compact text for LLM context injection."""
        lines: list[str] = []
        lines.append(f"### {self.method}()")
        if self.description:
            desc = self.description
            if not desc.endswith((".", "?", "!")):
                desc += "."
            lines.append(desc)
        lines.append(f"Section: {self.section}")
        lines.append("")

        lines.append("Parameters:")
        for p in self.parameters:
            req = "required" if p["required"] else "optional"
            desc_part = f": {p['description']}" if p.get("description") else ""
            lines.append(f"- {p['name']} ({p['type']}, {req}){desc_part}")
        lines.append("")

        ret = self.returns
        lines.append(f"Returns: {ret['type']}")
        fields = cast(list[dict[str, str]], ret.get("fields", []))
        for f in fields:
            desc_part = f": {f['description']}" if f.get("description") else ""
            lines.append(f"- {f['name']} ({f['type']}){desc_part}")

        return "\n".join(lines)


class MethodSearcher:
    """BM25 Okapi search over API method metadata.

    Loads the search index from ``_search_index.json`` at instantiation.
    """

    def __init__(self) -> None:
        with open(_INDEX_PATH, encoding="utf-8") as f:
            self._entries: list[dict[str, Any]] = json.load(f)

        # Build per-document token lists, TF maps, and BM25 stats
        self._doc_tf: list[dict[str, int]] = []
        self._doc_lengths: list[int] = []

        # Term -> document frequency
        df: dict[str, int] = {}

        for entry in self._entries:
            tokens = self._build_doc_tokens(entry)
            tf: dict[str, int] = {}
            for token in tokens:
                tf[token] = tf.get(token, 0) + 1
            self._doc_tf.append(tf)
            self._doc_lengths.append(len(tokens))
            for term in tf:
                df[term] = df.get(term, 0) + 1

        n = len(self._entries)
        self._avgdl = sum(self._doc_lengths) / n if n else 1.0

        # Precompute IDF: log((N - df + 0.5) / (df + 0.5) + 1)
        self._idf: dict[str, float] = {}
        for term, freq in df.items():
            self._idf[term] = math.log((n - freq + 0.5) / (freq + 0.5) + 1.0)

    @staticmethod
    def _build_doc_tokens(entry: dict[str, Any]) -> list[str]:
        """Build the tokenized document text for a single index entry.

        Concatenates all searchable fields into a single string, then
        tokenizes using _tokenize() to ensure the same normalization
        is applied to both documents and queries.
        """
        parts: list[str] = []

        # Method name and section are the primary identifiers
        parts.append(str(entry["method"]))
        parts.append(str(entry["section"]))
        # Description (OpenAPI summary)
        parts.append(str(entry.get("description", "")))
        # Parameter names and descriptions
        for p in entry.get("parameters", []):
            parts.append(str(p["name"]))
            parts.append(str(p.get("description", "")))
        # Return field names and descriptions
        returns = entry.get("returns", {})
        for f in returns.get("fields", []):
            parts.append(str(f["name"]))
            parts.append(str(f.get("description", "")))

        # Use _tokenize for consistent normalization with query tokenization
        return _tokenize(" ".join(parts))

    def search(
        self,
        query: str,
        *,
        section: str | None = None,
        limit: int = 5,
    ) -> list[MethodSearchResult]:
        """Search for API methods matching a natural-language query.

        Args:
            query: Search query (underscores/hyphens are normalized).
            section: Optional kebab-case section to restrict results.
            limit: Maximum number of results to return.

        Returns:
            List of MethodSearchResult sorted by descending BM25 score.
        """
        query_tokens = _tokenize(query)
        if not query_tokens:
            return []

        results: list[MethodSearchResult] = []

        for i, entry in enumerate(self._entries):
            if section is not None and entry["section"] != section:
                continue

            score = self._score(query_tokens, i)
            if score > 0:
                params = [dict(p) for p in entry.get("parameters", [])]
                ret = entry.get("returns", {})
                ret_copy = {
                    "type": ret.get("type", ""),
                    "fields": [dict(f) for f in ret.get("fields", [])],
                }
                results.append(MethodSearchResult(
                    method=str(entry["method"]),
                    section=str(entry["section"]),
                    description=str(entry.get("description", "")),
                    score=score,
                    parameters=params,
                    returns=ret_copy,
                ))

        results.sort(key=lambda r: r.score, reverse=True)
        return results[:max(0, limit)]

    def _score(self, query_tokens: list[str], doc_idx: int) -> float:
        """Compute BM25 Okapi score for a document against query tokens."""
        tf = self._doc_tf[doc_idx]
        dl = self._doc_lengths[doc_idx]

        score = 0.0
        for term in query_tokens:
            if term not in tf:
                continue
            term_freq = tf[term]
            idf = self._idf.get(term, 0.0)
            numerator = term_freq * (_K1 + 1)
            denominator = term_freq + _K1 * (1 - _B + _B * dl / self._avgdl)
            score += idf * numerator / denominator

        return score

    def list_sections(self) -> list[str]:
        """Return a sorted list of all section identifiers in the index."""
        sections = {str(e["section"]) for e in self._entries}
        return sorted(sections)


_searcher: MethodSearcher | None = None


def _get_searcher() -> MethodSearcher:
    """Return a module-level singleton MethodSearcher, created on first use."""
    global _searcher
    if _searcher is None:
        _searcher = MethodSearcher()
    return _searcher


def search_api_methods(
    query: str,
    *,
    section: str | None = None,
    limit: int = 5,
) -> str:
    """One-shot search returning formatted context text."""
    searcher = _get_searcher()
    results = searcher.search(query, section=section, limit=limit)
    return "\n\n".join(r.format_for_context() for r in results)

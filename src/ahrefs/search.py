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
_K1: float = 1.5
_B: float = 0.75
# Name field (method, section, description) is weighted higher than body
# (params, return fields) so exact method-name matches aren't buried by
# long parameter lists.
_NAME_WEIGHT = 2

# Per-result char cap for format_for_context(). P95 of method sizes is ~8K;
# only one outlier (site_audit_page_explorer, 86K, 605 fields) gets trimmed.
_MAX_RESULT_CHARS = 9000


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
    parameters: list[dict[str, str | bool | list[str]]]
    returns: dict[str, str | list[dict[str, str]]]

    def format_for_context(self) -> str:
        """Format this result as compact text for LLM context injection."""
        lines: list[str] = []
        lines.append(f"### {self.method}()")
        if self.description:
            desc: str = self.description
            if not desc.endswith((".", "?", "!")):
                desc += "."
            lines.append(desc)
        lines.append(f"Section: {self.section}")
        lines.append("")

        lines.append("Parameters:")
        for p in self.parameters:
            req = "required" if p["required"] else "optional"
            type_str = str(p["type"])
            enum_vals = p.get("enum_values")
            if isinstance(enum_vals, list) and enum_vals:
                if len(enum_vals) > 20:
                    shown = ", ".join(str(v) for v in enum_vals[:20])
                    remaining = len(enum_vals) - 20
                    type_str = f"{type_str} ({shown}, ... and {remaining} more)"
                else:
                    type_str = f"{type_str} ({', '.join(str(v) for v in enum_vals)})"
            desc_part = f": {p['description']}" if p.get("description") else ""
            lines.append(f"- {p['name']} ({type_str}, {req}){desc_part}")
        lines.append("")

        ret: dict[str, str | list[dict[str, str]]] = self.returns
        lines.append(f"Returns: {ret['type']}")
        fields: list[dict[str, str]] = cast(list[dict[str, str]], ret.get("fields", []))
        for f in fields:
            desc_part = f": {f['description']}" if f.get("description") else ""
            lines.append(f"- {f['name']} ({f['type']}){desc_part}")

        text = "\n".join(lines)
        if len(text) > _MAX_RESULT_CHARS:
            cut: int = text[:_MAX_RESULT_CHARS].rfind("\n")
            text = text[:cut] if cut > 0 else text[:_MAX_RESULT_CHARS]
            text += "\n... [truncated]"
        return text


class MethodSearcher:
    """BM25 Okapi search over API method metadata.

    Loads the search index from ``_search_index.json`` at instantiation.
    """

    def __init__(self) -> None:
        with open(_INDEX_PATH, encoding="utf-8") as f:
            self._entries: list[dict[str, Any]] = json.load(f)

        # Per-field TF maps and lengths
        self._name_tf: list[dict[str, int]] = []
        self._name_lengths: list[int] = []
        self._body_tf: list[dict[str, int]] = []
        self._body_lengths: list[int] = []

        # Shared document frequency (term present in either field)
        df: dict[str, int] = {}

        for entry in self._entries:
            name_tokens: list[str] = self._build_name_tokens(entry)
            body_tokens: list[str] = self._build_body_tokens(entry)

            ntf: dict[str, int] = {}
            for token in name_tokens:
                ntf[token] = ntf.get(token, 0) + 1
            self._name_tf.append(ntf)
            self._name_lengths.append(len(name_tokens))

            btf: dict[str, int] = {}
            for token in body_tokens:
                btf[token] = btf.get(token, 0) + 1
            self._body_tf.append(btf)
            self._body_lengths.append(len(body_tokens))

            # A term contributes to df if it appears in either field
            all_terms: set[str] = set(ntf) | set(btf)
            for term in all_terms:
                df[term] = df.get(term, 0) + 1

        n: int = len(self._entries)
        self._name_avgdl: float = sum(self._name_lengths) / n if n else 1.0
        self._body_avgdl: float = sum(self._body_lengths) / n if n else 1.0

        # Precompute IDF: log((N - df + 0.5) / (df + 0.5) + 1)
        self._idf: dict[str, float] = {}
        for term, freq in df.items():
            self._idf[term] = math.log((n - freq + 0.5) / (freq + 0.5) + 1.0)

    @staticmethod
    def _build_name_tokens(entry: dict[str, Any]) -> list[str]:
        """Tokenize the identity fields: method name, section, description."""
        parts: list[str] = [
            str(entry["method"]),
            str(entry["section"]),
            str(entry.get("description", "")),
        ]
        return _tokenize(" ".join(parts))

    @staticmethod
    def _build_body_tokens(entry: dict[str, Any]) -> list[str]:
        """Tokenize the detail fields: param and return-field names/descriptions."""
        parts: list[str] = []
        for p in entry.get("parameters", []):
            parts.append(str(p["name"]))
            parts.append(str(p.get("description", "")))
        returns = entry.get("returns", {})
        for f in returns.get("fields", []):
            parts.append(str(f["name"]))
            parts.append(str(f.get("description", "")))
        return _tokenize(text=" ".join(parts))

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

            score: float = self._score(query_tokens=query_tokens, doc_idx=i)
            if score > 0:
                params: list[dict[Any, Any]] = [
                    dict(p) for p in entry.get("parameters", [])
                ]
                ret = entry.get("returns", {})
                ret_copy: dict[str, Any | list[dict[Any, Any]]] = {
                    "type": ret.get("type", ""),
                    "fields": [dict(f) for f in ret.get("fields", [])],
                }
                results.append(
                    MethodSearchResult(
                        method=str(entry["method"]),
                        section=str(entry["section"]),
                        description=str(entry.get("description", "")),
                        score=score,
                        parameters=params,
                        returns=ret_copy,
                    )
                )

        results.sort(key=lambda r: r.score, reverse=True)
        return results[: max(0, limit)]

    @staticmethod
    def _field_score(
        query_tokens: list[str],
        tf: dict[str, int],
        dl: int,
        avgdl: float,
        idf: dict[str, float],
    ) -> float:
        """Compute BM25 Okapi score for one field."""
        score: float = 0.0
        for term in query_tokens:
            if term not in tf:
                continue
            term_freq: int = tf[term]
            term_idf: float = idf.get(term, 0.0)
            numerator: float = term_freq * (_K1 + 1)
            denominator: float = term_freq + _K1 * (1 - _B + _B * dl / avgdl)
            score += term_idf * numerator / denominator
        return score

    def _score(self, query_tokens: list[str], doc_idx: int) -> float:
        """Compute two-field BM25 score: name_bm25 + body_bm25."""
        name_score: float = self._field_score(
            query_tokens=query_tokens,
            tf=self._name_tf[doc_idx],
            dl=self._name_lengths[doc_idx],
            avgdl=self._name_avgdl,
            idf=self._idf,
        )
        body_score: float = self._field_score(
            query_tokens=query_tokens,
            tf=self._body_tf[doc_idx],
            dl=self._body_lengths[doc_idx],
            avgdl=self._body_avgdl,
            idf=self._idf,
        )
        return _NAME_WEIGHT * name_score + body_score

    def list_sections(self) -> list[str]:
        """Return a sorted list of all section identifiers in the index."""
        sections: set[str] = {str(e["section"]) for e in self._entries}
        return sorted(sections)


_searcher: MethodSearcher | None = None


def _get_searcher() -> MethodSearcher:
    """Return a module-level singleton MethodSearcher, created on first use."""
    global _searcher
    if _searcher is None:
        _searcher = MethodSearcher()
    assert _searcher is not None  # we just assigned it
    return _searcher


def search_api_methods(
    query: str,
    *,
    section: str | None = None,
    limit: int = 5,
) -> str:
    """One-shot search returning formatted context text."""
    searcher: MethodSearcher = _get_searcher()
    results: list[MethodSearchResult] = searcher.search(
        query, section=section, limit=limit
    )
    return "\n\n".join(r.format_for_context() for r in results)

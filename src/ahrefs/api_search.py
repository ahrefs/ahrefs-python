"""CLI for searching ahrefs-python API methods.

Usage::

    python -m ahrefs.api_search "domain rating"
    python -m ahrefs.api_search "backlinks" -s site-explorer -n 2
    python -m ahrefs.api_search "batch" --json
    python -m ahrefs.api_search --sections
"""

from __future__ import annotations

import argparse
import json
import sys

from ahrefs.search import MethodSearcher


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="python -m ahrefs.api_search",
        description="Search ahrefs-python API methods.",
    )
    parser.add_argument(
        "query", nargs="?", default="",
        help="search query (e.g. 'domain rating')",
    )
    parser.add_argument(
        "--section", "-s", default=None,
        help="restrict to a section (e.g. site-explorer)",
    )
    parser.add_argument(
        "--limit", "-n", type=int, default=5,
        help="max results (default: 5)",
    )
    parser.add_argument(
        "--sections", action="store_true",
        help="list available sections and exit",
    )
    parser.add_argument(
        "--json", action="store_true", dest="as_json",
        help="output results as JSON",
    )
    args = parser.parse_args()

    searcher = MethodSearcher()

    if args.sections:
        for s in searcher.list_sections():
            print(s)
        sys.exit(0)

    if not args.query:
        parser.print_help()
        sys.exit(1)

    results = searcher.search(
        args.query, section=args.section, limit=args.limit,
    )

    if not results:
        print("No results.", file=sys.stderr)
        sys.exit(0)

    if args.as_json:
        out = [
            {
                "method": r.method,
                "section": r.section,
                "description": r.description,
                "score": round(r.score, 4),
                "parameters": r.parameters,
                "returns": r.returns,
            }
            for r in results
        ]
        print(json.dumps(out, indent=2))
    else:
        print(
            "\n\n".join(r.format_for_context() for r in results)
        )


if __name__ == "__main__":
    main()

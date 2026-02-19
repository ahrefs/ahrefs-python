"""Standalone integration test for the ahrefs-python SDK.

Exercises a representative set of endpoints against the live Ahrefs API.
Requires AHREFS_API_KEY environment variable to be set.

Usage:
    python tests/integration_test.py
    # or via the shell wrapper:
    ./tests/integration_test.sh
"""

from __future__ import annotations

import os
import sys
import traceback
from collections.abc import Callable
from datetime import date, timedelta

from ahrefs import AhrefsClient, AuthenticationError
from ahrefs.types import CountryEnum, SiteExplorerDomainRatingRequest

TARGET = "ahrefs.com"
DATE = (date.today() - timedelta(days=30)).isoformat()
passed: list[str] = []
failed: list[str] = []


def run_test(name: str, fn: Callable[[], None]) -> None:
    """Run a test function, track pass/fail."""
    try:
        fn()
        passed.append(name)
        print(f"  PASS  {name}")
    except Exception:
        failed.append(name)
        print(f"  FAIL  {name}")
        traceback.print_exc()
        print()


def main() -> None:
    api_key = os.environ.get("AHREFS_API_KEY")
    if not api_key:
        print("ERROR: AHREFS_API_KEY environment variable is not set.")
        print("Set it directly or create a .env file with AHREFS_API_KEY=<key>")
        sys.exit(1)

    client = AhrefsClient(api_key=api_key)
    print(f"Testing against target={TARGET}, date={DATE}\n")

    # ── 1. Domain Rating (scalar, cheapest call) ─────────────────────
    def test_domain_rating() -> None:
        data = client.site_explorer_domain_rating(target=TARGET, date=DATE)
        assert data is not None, "data is None"
        assert isinstance(data.domain_rating, float), (
            f"expected float, got {type(data.domain_rating)}"
        )
        assert data.domain_rating > 0, f"expected positive DR, got {data.domain_rating}"

    run_test("site_explorer_domain_rating", test_domain_rating)

    # ── 2. Domain Rating via request object ──────────────────────────
    def test_domain_rating_request_object() -> None:
        req = SiteExplorerDomainRatingRequest(target=TARGET, date=DATE)
        data = client.site_explorer_domain_rating(req)
        assert data is not None, "data is None"
        assert isinstance(data.domain_rating, float)

    run_test(
        "site_explorer_domain_rating (request object)",
        test_domain_rating_request_object,
    )

    # ── 3. Backlinks Stats (scalar, different shape) ─────────────────
    def test_backlinks_stats() -> None:
        data = client.site_explorer_backlinks_stats(target=TARGET, date=DATE)
        assert data is not None, "data is None"
        assert isinstance(data.live, int), f"expected int, got {type(data.live)}"
        assert data.live > 0, f"expected positive live count, got {data.live}"
        assert isinstance(data.live_refdomains, int)
        assert data.live_refdomains > 0

    run_test("site_explorer_backlinks_stats", test_backlinks_stats)

    # ── 4. Metrics (rich scalar response) ────────────────────────────
    def test_metrics() -> None:
        data = client.site_explorer_metrics(target=TARGET, date=DATE)
        assert data is not None, "data is None"
        assert isinstance(data.org_keywords, int)
        assert data.org_keywords > 0
        assert isinstance(data.org_traffic, int)

    run_test("site_explorer_metrics", test_metrics)

    # ── 5. Organic Keywords (list endpoint) ──────────────────────────
    def test_organic_keywords() -> None:
        data = client.site_explorer_organic_keywords(
            target=TARGET,
            date=DATE,
            select="keyword,volume,best_position",
            limit=5,
        )
        assert isinstance(data, list), f"expected list, got {type(data)}"
        assert len(data) > 0, "expected non-empty list"
        item = data[0]
        assert item.keyword is not None, "keyword is None"
        assert isinstance(item.keyword, str)

    run_test("site_explorer_organic_keywords", test_organic_keywords)

    # ── 6. Refdomains (list endpoint, different shape) ───────────────
    def test_refdomains() -> None:
        data = client.site_explorer_refdomains(
            target=TARGET,
            select="domain,domain_rating,links_to_target",
            limit=5,
        )
        assert isinstance(data, list), f"expected list, got {type(data)}"
        assert len(data) > 0, "expected non-empty list"
        item = data[0]
        assert item.domain is not None

    run_test("site_explorer_refdomains", test_refdomains)

    # ── 7. Keywords Explorer Overview (different API section) ────────
    def test_keywords_explorer() -> None:
        data = client.keywords_explorer_overview(
            keywords="ahrefs",
            country=CountryEnum.US,
            select="keyword,volume,difficulty",
            limit=5,
        )
        assert isinstance(data, list), f"expected list, got {type(data)}"
        assert len(data) > 0, "expected non-empty list"
        item = data[0]
        assert item.keyword is not None

    run_test("keywords_explorer_overview", test_keywords_explorer)

    # ── 8. Context manager ───────────────────────────────────────────
    def test_context_manager() -> None:
        with AhrefsClient(api_key=api_key) as ctx_client:
            data = ctx_client.site_explorer_domain_rating(target=TARGET, date=DATE)
            assert data is not None

    run_test("context_manager", test_context_manager)

    # ── 9. AuthenticationError with bad key ──────────────────────────
    def test_auth_error() -> None:
        bad_client = AhrefsClient(api_key="invalid-key-12345", max_retries=0)
        try:
            bad_client.site_explorer_domain_rating(target=TARGET, date=DATE)
            raise AssertionError("Expected AuthenticationError")
        except AuthenticationError:
            pass  # expected
        finally:
            bad_client.close()

    run_test("authentication_error", test_auth_error)

    # ── Summary ──────────────────────────────────────────────────────
    client.close()
    print(f"\n{'=' * 50}")
    print(f"Results: {len(passed)} passed, {len(failed)} failed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
    print(f"{'=' * 50}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

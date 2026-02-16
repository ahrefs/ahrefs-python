# Ahrefs Python SDK

[![CI](https://github.com/ahrefs/ahrefs-python/actions/workflows/ci.yml/badge.svg)](https://github.com/ahrefs/ahrefs-python/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Python client for the [Ahrefs API](https://ahrefs.com/api). Typed request and response models for all endpoints, auto-generated from the official OpenAPI specifications.

[API Documentation](https://docs.ahrefs.com/docs/api/v3/)

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Request Styles](#request-styles)
  - [Working with Responses](#working-with-responses)
  - [Common Examples](#common-examples)
  - [Error Handling](#error-handling)
  - [Configuration](#configuration)
  - [Automatic Retries](#automatic-retries)
  - [Async Support](#async-support)
  - [Custom HTTP Client](#custom-http-client)
  - [Resource Cleanup](#resource-cleanup)
- [API Sections](#api-sections)
- [AI Coding Assistant](#ai-coding-assistant)
- [License](#license)

## Installation

```sh
# Via SSH
pip install git+ssh://git@github.com/ahrefs/ahrefs-python.git

# Via HTTPS
pip install git+https://github.com/ahrefs/ahrefs-python.git
```

Requires Python 3.11+.

## Quick Start

```python
from ahrefs import AhrefsClient

client = AhrefsClient(api_key="your-api-key")  # or set AHREFS_API_KEY env var

response = client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")
print(response.data.domain_rating)  # 91.0
print(response.data.ahrefs_rank)    # 3
```

## Usage

### Request Styles

Every method supports two calling styles:

**Keyword arguments** (recommended for most use):

```python
response = client.site_explorer_domain_rating(
    target="ahrefs.com",
    date="2025-01-15",
)
```

**Request objects** (full type safety, IDE autocomplete):

```python
from ahrefs.types import SiteExplorerDomainRatingRequest

request = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
response = client.site_explorer_domain_rating(request)
```

Both styles are equivalent. Method names follow the pattern `{api_section}_{endpoint}`, e.g. `site_explorer_organic_keywords`, `keywords_explorer_overview`.

### Working with Responses

Every response has a `.data` property for convenient access.

**Scalar endpoints** return a single data object:

```python
response = client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")
print(response.data.domain_rating)  # 91.0
print(response.data.ahrefs_rank)    # 3
```

**List endpoints** return a list of data objects. Use `select` to choose columns and `limit` to control result count:

```python
response = client.site_explorer_organic_keywords(
    target="ahrefs.com",
    date="2025-01-15",
    select="keyword,volume,best_position",
    limit=10,
)

for item in response.data:
    print(item.keyword, item.volume, item.best_position)
```

### Common Examples

**Domain metrics with country filter:**

```python
response = client.site_explorer_metrics(
    target="ahrefs.com",
    date="2025-01-15",
    country="us",
)
print(response.data.org_traffic, response.data.paid_traffic)
```

**Time-series history:**

```python
response = client.site_explorer_metrics_history(
    target="ahrefs.com",
    date_from="2024-01-01",
    date_to="2025-01-01",
)
for point in response.data:
    print(point.date, point.org_traffic)
```

**Referring domains with filtering and sorting:**

```python
response = client.site_explorer_refdomains(
    target="ahrefs.com",
    select="domain,domain_rating,traffic_domain",
    limit=20,
    order_by="domain_rating:desc",
)
for rd in response.data:
    print(rd.domain, rd.domain_rating, rd.traffic_domain)
```

**Keywords Explorer:**

```python
response = client.keywords_explorer_overview(
    select="keyword,volume,difficulty",
    country="us",
    keywords="python sdk,ahrefs api",
)
for kw in response.data:
    print(kw.keyword, kw.volume, kw.difficulty)
```

### Error Handling

Unsuccessful requests raise typed exceptions:

```python
import ahrefs

client = ahrefs.AhrefsClient(api_key="...")

try:
    response = client.site_explorer_domain_rating(target="example.com", date="2025-01-15")
except ahrefs.AuthenticationError:
    # Invalid or missing API key (HTTP 401)
    ...
except ahrefs.RateLimitError as e:
    # Rate limit exceeded (HTTP 429)
    print(f"Retry after {e.retry_after}s")
except ahrefs.NotFoundError:
    # Resource not found (HTTP 404)
    ...
except ahrefs.APIError as e:
    # Other API errors (HTTP 4xx/5xx)
    print(e.status_code, e.response_body)
except ahrefs.APIConnectionError:
    # Network error (connection failure, timeout)
    ...
```

All exceptions inherit from `ahrefs.AhrefsError`.

### Configuration

```python
client = ahrefs.AhrefsClient(
    api_key="...",           # or set AHREFS_API_KEY env var
    base_url="...",          # override API base URL (default: https://api.ahrefs.com/v3)
    timeout=30.0,            # request timeout in seconds (default: 60)
    max_retries=3,           # retries on transient errors (default: 2)
)
```

### Automatic Retries

The client automatically retries on transient errors:

- **HTTP 429** (rate limit) -- respects `Retry-After` headers
- **HTTP 5xx** (server errors)
- Connection failures and timeouts

Retries use exponential backoff with jitter. Set `max_retries=0` to disable:

```python
client = ahrefs.AhrefsClient(api_key="...", max_retries=0)
```

### Async Support

An asynchronous client is available with the same interface:

```python
from ahrefs import AsyncAhrefsClient

async with AsyncAhrefsClient(api_key="...") as client:
    response = await client.site_explorer_domain_rating(
        target="ahrefs.com",
        date="2025-01-15",
    )
    print(response.data.domain_rating)
```

The async client uses `httpx.AsyncClient` under the hood and supports all the same methods and configuration options.

### Custom HTTP Client

Provide your own `httpx.Client` for full control over HTTP behavior (proxies, custom transport, mocking):

```python
import httpx

my_client = httpx.Client(proxy="http://localhost:8080")
client = ahrefs.AhrefsClient(api_key="...", http_client=my_client)
```

When you provide your own HTTP client, the library will not close it on `client.close()` -- you manage its lifecycle.

### Resource Cleanup

Both clients support context managers for automatic cleanup:

```python
# Sync
with ahrefs.AhrefsClient(api_key="...") as client:
    response = client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")

# Async
async with ahrefs.AsyncAhrefsClient(api_key="...") as client:
    response = await client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")
```

Or call `.close()` manually when done.

## API Sections

See the [full API reference](docs/api-reference.md) for parameters, types, and response fields.

<!-- METHOD_INDEX_START -->
**Brand Radar** (6 methods)

- `brand_radar_ai_responses()`
- `brand_radar_impressions_history()`
- `brand_radar_impressions_overview()`
- `brand_radar_mentions_history()`
- `brand_radar_mentions_overview()`
- `brand_radar_sov_overview()`

**Keywords Explorer** (6 methods)

- `keywords_explorer_matching_terms()`
- `keywords_explorer_overview()`
- `keywords_explorer_related_terms()`
- `keywords_explorer_search_suggestions()`
- `keywords_explorer_volume_by_country()`
- `keywords_explorer_volume_history()`

**Rank Tracker** (5 methods)

- `rank_tracker_competitors_overview()`
- `rank_tracker_competitors_pages()`
- `rank_tracker_competitors_stats()`
- `rank_tracker_overview()`
- `rank_tracker_serp_overview()`

**Serp Overview** (1 method)

- `serp_overview_serp_overview()`

**Site Audit** (4 methods)

- `site_audit_issues()`
- `site_audit_page_content()`
- `site_audit_page_explorer()`
- `site_audit_projects()`

**Site Explorer** (26 methods)

- `site_explorer_all_backlinks()`
- `site_explorer_anchors()`
- `site_explorer_backlinks_stats()`
- `site_explorer_best_by_external_links()`
- `site_explorer_best_by_internal_links()`
- `site_explorer_broken_backlinks()`
- `site_explorer_domain_rating()`
- `site_explorer_domain_rating_history()`
- `site_explorer_keywords_history()`
- `site_explorer_linked_anchors_external()`
- `site_explorer_linked_anchors_internal()`
- `site_explorer_linkeddomains()`
- `site_explorer_metrics()`
- `site_explorer_metrics_by_country()`
- `site_explorer_metrics_history()`
- `site_explorer_organic_competitors()`
- `site_explorer_organic_keywords()`
- `site_explorer_outlinks_stats()`
- `site_explorer_pages_by_traffic()`
- `site_explorer_pages_history()`
- `site_explorer_paid_pages()`
- `site_explorer_refdomains()`
- `site_explorer_refdomains_history()`
- `site_explorer_top_pages()`
- `site_explorer_total_search_volume_history()`
- `site_explorer_url_rating_history()`

<!-- METHOD_INDEX_END -->

## AI Coding Assistant

If you use [Claude Code](https://docs.anthropic.com/en/docs/claude-code), install the companion skill to teach it the SDK patterns and all available methods:

```sh
npx skills add ahrefs/ahrefs-api-skills --skill ahrefs-python --global
```

See [ahrefs/ahrefs-api-skills](https://github.com/ahrefs/ahrefs-api-skills) for details.

## License

MIT -- see [LICENSE](LICENSE) for details.

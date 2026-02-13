# Ahrefs Python SDK

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
  - [Error Handling](#error-handling)
  - [Configuration](#configuration)
  - [Automatic Retries](#automatic-retries)
  - [Async Support](#async-support)
  - [Custom HTTP Client](#custom-http-client)
  - [Resource Cleanup](#resource-cleanup)
- [API Sections](#api-sections)
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

| Section | Example method | Description |
|---------|---------------|-------------|
| Site Explorer | `site_explorer_domain_rating()` | Domain metrics, backlinks, organic keywords, competitors |
| Keywords Explorer | `keywords_explorer_overview()` | Keyword metrics, search volume, related terms |
| Brand Radar | `brand_radar_ai_responses()` | Brand monitoring, mentions, share of voice |
| Rank Tracker | `rank_tracker_overview()` | SERP tracking, competitor rankings |
| Site Audit | `site_audit_issues()` | Technical SEO issues, page analysis |
| SERP Overview | `serp_overview_serp_overview()` | SERP analysis for keywords |

See the [full API reference](https://docs.ahrefs.com/docs/api/v3/) for all available endpoints and parameters.

## License

MIT -- see [LICENSE](LICENSE) for details.

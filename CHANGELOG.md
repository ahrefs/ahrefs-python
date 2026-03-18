# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.8.0-alpha]

### Breaking

- `site_explorer_best_by_external_links()` renamed to `site_explorer_pages_by_backlinks()`
- `site_explorer_best_by_internal_links()` renamed to `site_explorer_pages_by_internal_links()`
- Corresponding type renames: `SiteExplorerBestByExternalLinks{Data,Request}` → `SiteExplorerPagesByBacklinks{Data,Request}`, same for internal links
- Brand Radar `country` parameter changed from `CountryEnum | None` to `list[CountryEnum | None]` across all 9 brand-radar endpoints — wrap single values in a list

### Added

- `management_brand_radar_prompts()`, `management_create_brand_radar_prompts()`, `management_brand_radar_prompts_delete()` — manage Brand Radar custom prompts
- `PagePositionsEnum` for filtering `site_explorer_pages_history()` by ranking position (`top10`, `top100`)
- `search_queries` filter and response field on Brand Radar endpoints
- `tags` response field on `brand_radar_ai_responses()`
- `size_uncompressed`, `size_uncompressed_diff`, `size_uncompressed_prev` fields on `site_audit_page_explorer()`
- `project_url`, `project_name` filter parameters on `site_audit_projects()`

### Fixed

- List-valued query parameters (e.g. `country`) now serialize as CSV instead of repeated keys, matching the API's expected format

## [0.7.1-alpha]

### Changed

- Error messages now extract structured content from API responses instead of showing raw JSON
- `NotFoundError` includes a contextual hint about common 404 causes (date availability, target not found, incorrect parameters)
- Method search results now show valid enum values inline (e.g. `ModeEnum (exact, prefix, domain, subdomains)`)
- History endpoints clearly labeled as "Time-series." and point-in-time siblings as "Point-in-time snapshot." in search results

## [0.7.0-alpha]

### Added

- Management API support (13 endpoints) — manage Rank Tracker projects, keywords, keyword lists, and competitors
- PUT and PATCH HTTP method support
- HTTP method tags (`[POST]`, `[PUT]`, `[PATCH]`) in docstrings and API reference for write endpoints

## [0.6.0-alpha]

### Added

- Public API support: `public_crawler_ips()` and `public_crawler_ip_ranges()` for retrieving Ahrefs crawler IP addresses
- Subscription Info API support: `subscription_info_limits_and_usage()` for checking API usage, limits, and key expiration

## [0.5.0-alpha]

### Added

- Web Analytics API support (34 endpoints) — 17 dimension endpoints and 17 chart variants
- Python reserved word handling: `from` parameter available as `from_` with automatic API serialization

## [0.4.3-alpha]

### Added

- New `report_id` and `prompts` parameters on all Brand Radar endpoints
- `PromptsEnum` type (`"ahrefs"` | `"custom"`) for prompt source filtering

### Changed

- Minor description improvements on Brand Radar endpoints
- Cap per-result search output at 9K chars to prevent outlier methods from bloating search results

## [0.3.1]

### Added

- `brand_radar_sov_history()`, `brand_radar_cited_domains()`, `brand_radar_cited_pages()` methods
- Updated API schemas (52 endpoints total)

## [0.3.0]

### Added

- `batch_analysis()` method for the Batch Analysis POST endpoint
- `BatchAnalysisRequest`, `BatchAnalysisTarget`, `BatchAnalysisData` types
- POST request support in both sync and async clients (`http_method` parameter on `_request()`)
- POST endpoint support with typed request bodies and nested models

## [0.2.0]

### Changed

- **BREAKING**: Client methods now return Data objects directly instead of Response wrappers
  - Scalar endpoints return `Data | None` (e.g. `SiteExplorerDomainRatingData | None`)
  - List endpoints return `list[Data]` (e.g. `list[SiteExplorerOrganicKeywordsData]`)
  - Before: `response = client.method(...)` then `response.data.field`
  - After: `data = client.method(...)` then `data.field`
- Response classes removed from `ahrefs.types` public exports (still available internally for JSON parsing)

## [0.1.0]

### Added

- Initial release of the Ahrefs Python SDK
- Sync and async clients (`AhrefsClient`, `AsyncAhrefsClient`)
- Typed request/response models for all Ahrefs API v3 endpoints
- Automatic retries with exponential backoff and jitter
- `DateStr` and `SelectStr` type coercions for convenience
- Comprehensive error hierarchy (`AhrefsError`, `APIError`, `AuthenticationError`, etc.)

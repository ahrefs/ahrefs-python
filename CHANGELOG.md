# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.0]

### Added

- `batch_analysis()` method for the Batch Analysis POST endpoint
- `BatchAnalysisRequest`, `BatchAnalysisTarget`, `BatchAnalysisData` types
- POST request support in both sync and async clients (`http_method` parameter on `_request()`)
- Codegen support for POST endpoints with JSON request bodies and `$ref` resolution

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

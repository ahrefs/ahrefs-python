# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Initial release of the Ahrefs Python SDK
- Sync and async clients (`AhrefsClient`, `AsyncAhrefsClient`)
- Typed request/response models for all Ahrefs API v3 endpoints
- Automatic retries with exponential backoff and jitter
- `DateStr` and `SelectStr` type coercions for convenience
- Comprehensive error hierarchy (`AhrefsError`, `APIError`, `AuthenticationError`, etc.)

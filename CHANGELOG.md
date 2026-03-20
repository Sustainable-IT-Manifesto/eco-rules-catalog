# Changelog

All notable changes to the Eco Rules Catalog will be documented in this file.

The format is based on Keep a Changelog and follows semantic versioning (pre-1.0).

---

## [v0.3.0] — Infrastructure and Scanner Model Update

### Added

- New category:
  - `INF` (Infrastructure)

- New families:
  - `DOCKER`
  - `COMPOSE`
  - `K8S`

- Starter infrastructure rules covering:
  - container image inefficiencies
  - manifest configuration issues
  - scaling and resource allocation

- Category index pages (optional, if implemented)

### Changed

- Introduced **family-level `scanner_profile`**
- Introduced **optional rule-level `scanner_override`**
- Refactored applicability model to reduce duplication
- Improved documentation structure and browsing

### Why it matters

The catalog now captures inefficiency not only in code, but in:

- containers
- orchestration
- deployment defaults
- runtime behavior

This aligns the catalog with modern distributed systems.

Because waste is a bug.

---

## [v0.2.1]

### Added

- Rule examples
- Improved documentation and browsing

---

## [v0.2.0]

### Added

- Initial structured catalog
- Registry and schema definitions
- Rule normalization and generation pipeline

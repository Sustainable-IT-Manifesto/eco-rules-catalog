# Changelog

All notable changes to the Eco Rules Catalog will be documented in this file.

The format is based on Keep a Changelog and follows semantic versioning (pre-1.0).

---

## v0.4.0 - 2026-05-21

### Added

- Formal schema definitions for `cost_dimensions`, `amplification`, `temporal_behavior`, `runtime_evidence`, and `sustainability_priority`.
- Documentation for the new systems-level metadata fields.
- Migration entry documenting the 0.4.0 schema formalization.

### Changed

- Updated catalog registry version from `0.3.0` to `0.4.0`.
- Updated rule metadata catalog versions to `0.4.0`.
- Promoted the 0.3.0 expansion into a more explicit systems intelligence release.

### Compatibility

- Existing 0.3.x rules remain structurally compatible.
- Additional rule properties are still allowed so experimental metadata can continue to evolve.

## v0.3.1 - 2026-05-21

### Added

- Sustainability, resilience, and observability categories.
- New families for carbon, energy, water, hardware lifecycle, caching, serialization, frontend/UI, RAG, prompts, agents, security efficiency, logging, tracing, metrics, failure handling, disaster recovery, and graceful degradation.
- Initial optional systems-level metadata fields.

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

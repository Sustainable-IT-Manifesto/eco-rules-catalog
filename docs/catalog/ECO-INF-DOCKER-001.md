# ECO-INF-DOCKER-001

**Name:** Missing multi-stage builds

**Category:** Infrastructure

**Family:** Docker

**Primary layer:** `process`

**System layers:** `process`, `code`

## Description

Dockerfiles that combine build and runtime concerns into a single final image increase storage, network transfer, cache churn, and deployment overhead.

## Impact

- **cost:** Larger images cost more to store and move.
- **performance:** Slower pulls and startup in constrained environments.
- **carbon:** More bytes transferred and stored than necessary.

## Detection

- **method:** dockerfile-lint
- **selector:** multi_stage_build_missing

## Remediation

- **guidance:** Separate build and runtime stages so only runtime assets ship in the final image.
- **examples:**
  - Use multi-stage builds with a builder stage and a minimal runtime stage.

## Pattern examples

### Single-stage image with compiler toolchain

A runtime image includes package managers, compilers, and build caches that are only needed during build.

## Remediation examples

### Split build and runtime stages

Build assets in one stage, then copy only the required runtime artifacts into a smaller final image.

## Metadata

- **status:** draft
- **severity:** medium
- **version:** 0.3.0-draft

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

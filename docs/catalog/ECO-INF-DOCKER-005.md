# ECO-INF-DOCKER-005

**Name:** Build tooling shipped in runtime image

**Category:** Infrastructure

**Family:** Docker

**Primary layer:** `process`

**System layers:** `process`, `code`

## Description

Shipping build-only tools in the final image increases image size and operational complexity while providing no runtime efficiency benefit.

## Impact

- **cost:** Bigger runtime images cost more to move and store.
- **performance:** Extra image weight slows distribution and cold starts.
- **carbon:** Unnecessary runtime bytes increase repeated resource use.

## Detection

- **method:** dockerfile-lint
- **selector:** build_tooling_in_runtime_image

## Remediation

- **guidance:** Keep build tooling in dedicated builder stages and ship only runtime dependencies.
- **examples:**
  - Copy built binaries or packaged assets into a clean runtime stage.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **status:** draft
- **severity:** medium
- **version:** 0.3.0-draft

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

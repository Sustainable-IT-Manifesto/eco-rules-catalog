# ECO-INF-DOCKER-003

**Name:** Missing or too-permissive .dockerignore

**Category:** Infrastructure

**Family:** Docker

**Primary layer:** `process`

**System layers:** `process`, `code`

## Description

Without a properly scoped .dockerignore, source trees, artifacts, caches, and documentation may be copied into the build context even when they are not required for the image.

## Impact

- **cost:** Larger contexts waste build and CI resources.
- **performance:** Builds become slower and less cache-friendly.
- **carbon:** Repeated transfer of unnecessary files increases waste.

## Detection

- **method:** dockerfile-lint
- **selector:** dockerignore_missing_or_broad

## Remediation

- **guidance:** Add and maintain a .dockerignore tuned to the actual files required for the build.
- **examples:**
  - Exclude node_modules, .git, test outputs, local caches, and generated artifacts unless explicitly needed.

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

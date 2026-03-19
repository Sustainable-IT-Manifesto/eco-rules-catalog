# ECO-INF-DOCKER-004

**Name:** Package manager caches left in image layers

**Category:** Infrastructure

**Family:** Docker

**Primary layer:** `process`

**System layers:** `process`, `code`

## Description

Docker image layers that retain apt, apk, pip, npm, or similar caches increase storage and transfer overhead while adding little or no runtime value.

## Impact

- **cost:** Larger images increase storage and transfer cost.
- **performance:** Pulling and scanning images takes longer.
- **carbon:** Extra bytes are stored and transmitted repeatedly.

## Detection

- **method:** dockerfile-lint
- **selector:** package_manager_caches_retained

## Remediation

- **guidance:** Clear package manager caches in the same layer where packages are installed, or use build-stage-only installs where possible.
- **examples:**
  - Combine install and cleanup in a single RUN instruction so caches do not persist into a committed layer.

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

# ECO-INF-DOCKER-002

**Name:** Oversized base image

**Category:** Infrastructure

**Family:** Docker

**Primary layer:** `architecture`

**System layers:** `architecture`, `process`

## Description

Using a large general-purpose base image when a smaller runtime image would suffice adds waste to build, deployment, and vulnerability management workflows.

## Impact

- **cost:** Larger images cost more to store and distribute.
- **performance:** Longer image pull times delay startup.
- **carbon:** Unnecessary transfer and storage increase resource use.

## Detection

- **method:** dockerfile-lint
- **selector:** oversized_base_image

## Remediation

- **guidance:** Prefer minimal runtime images that still meet operational needs.
- **examples:**
  - Use slim or distroless images when practical and compatible with debugging and support needs.

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

# ECO-NET-NET-001

**Name:** Missing HTTP caching headers

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Missing cache headers causes repeated downloads and wasted work.

## Impact

- **confidence:** 0.75
- **notes:** Large impact for static and semi-static responses.
- **type:** network

## Detection

- **languages:** `infra`, `org`
- **method:** trace

## Remediation

- **guidance:** Add Cache-Control/ETag; use immutable asset hashing where possible.
- **tradeoffs:** Requires cache invalidation discipline.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

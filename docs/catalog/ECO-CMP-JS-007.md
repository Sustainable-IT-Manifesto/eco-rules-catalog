# ECO-CMP-JS-007

**Name:** Missing HTTP caching headers (client-side)

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `network`

**System layers:** `network`

## Description

Missing cache headers causes repeated downloads and wasted bandwidth.

## Impact

- **confidence:** 0.7
- **notes:** High on static assets.
- **type:** network

## Detection

- **languages:** `javascript`
- **method:** trace

## Remediation

- **guidance:** Set Cache-Control/ETag; use immutable assets with hashes.
- **tradeoffs:** Requires proper build pipeline.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to JavaScript family](categories/cmp/families/js/index.md)
- [Back to Rule Browser](../rule-browser.md)

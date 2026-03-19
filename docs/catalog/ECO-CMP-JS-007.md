# ECO-CMP-JS-007

**Name:** Missing HTTP caching headers (client-side)

**Category:** CMP

**Family:** JS

**Primary layer:** `network`

**System layers:** `network`

## Description

Missing cache headers causes repeated downloads and wasted bandwidth.

## Impact

- **confidence:** 0.7
- **notes:** High on static assets.
- **type:** network

## Detection

- **languages:**
  - javascript
- **method:** trace

## Remediation

- **guidance:** Set Cache-Control/ETag; use immutable assets with hashes.
- **tradeoffs:** Requires proper build pipeline.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

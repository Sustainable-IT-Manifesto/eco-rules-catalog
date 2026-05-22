# ECO-CMP-JS-013

**Name:** Uncompressed static assets

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `network`

**System layers:** `network`

## Description

Serving assets without compression increases bandwidth and energy use.

## Impact

- **confidence:** 0.8
- **notes:** Big win for text assets.
- **type:** network

## Detection

- **languages:** `javascript`
- **method:** trace

## Remediation

- **guidance:** Enable gzip/brotli; ensure proper caching.
- **tradeoffs:** Server/CDN config changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

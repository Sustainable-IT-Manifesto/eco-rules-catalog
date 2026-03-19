# ECO-CMP-JS-013

**Name:** Uncompressed static assets

**Category:** CMP

**Family:** JS

**Primary layer:** `network`

**System layers:** `network`

## Description

Serving assets without compression increases bandwidth and energy use.

## Impact

- **confidence:** 0.8
- **notes:** Big win for text assets.
- **type:** network

## Detection

- **languages:**
  - javascript
- **method:** trace

## Remediation

- **guidance:** Enable gzip/brotli; ensure proper caching.
- **tradeoffs:** Server/CDN config changes.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

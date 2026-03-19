# ECO-NET-NET-002

**Name:** No gzip/brotli compression

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Serving text assets without compression increases bandwidth and energy use.

## Impact

- **confidence:** 0.8
- **notes:** High win for JSON/HTML/CSS/JS.
- **type:** network

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Enable gzip/brotli at CDN/load balancer/origin.
- **tradeoffs:** Minimal; watch CPU on origin if no CDN.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

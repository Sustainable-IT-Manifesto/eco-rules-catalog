# ECO-NET-NET-002

**Name:** No gzip/brotli compression

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Serving text assets without compression increases bandwidth and energy use.

## Impact

- **confidence:** 0.8
- **notes:** High win for JSON/HTML/CSS/JS.
- **type:** network

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Enable gzip/brotli at CDN/load balancer/origin.
- **tradeoffs:** Minimal; watch CPU on origin if no CDN.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Networking category](categories/net/index.md)
- [Back to Network family](categories/net/families/net/index.md)
- [Back to Rule Browser](../rule-browser.md)

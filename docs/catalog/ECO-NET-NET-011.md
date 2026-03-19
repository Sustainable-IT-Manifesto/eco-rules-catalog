# ECO-NET-NET-011

**Name:** No CDN usage for static content

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Serving static content from origin increases latency and origin load.

## Impact

- **confidence:** 0.7
- **notes:** High for global audiences.
- **type:** network

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Use a CDN for static assets and cacheable endpoints.
- **tradeoffs:** Operational overhead and caching discipline.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

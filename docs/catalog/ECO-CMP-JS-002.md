# ECO-CMP-JS-002

**Name:** Polling instead of events

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `network`

**System layers:** `network`

## Description

Polling increases unnecessary network traffic and compute.

## Impact

- **confidence:** 0.7
- **notes:** Often significant at scale.
- **type:** network

## Detection

- **languages:** `javascript`
- **method:** regex

## Remediation

- **guidance:** Use webhooks, SSE, websockets, or event-driven patterns.
- **tradeoffs:** More moving parts.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

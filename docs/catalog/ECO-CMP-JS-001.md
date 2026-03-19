# ECO-CMP-JS-001

**Name:** Synchronous filesystem calls in request path

**Category:** CMP

**Family:** JS

**Primary layer:** `code`

**System layers:** `code`

## Description

Sync FS calls block the event loop and reduce concurrency.

## Impact

- **confidence:** 0.9
- **notes:** High propagation in Node services.
- **type:** latency

## Detection

- **languages:**
  - javascript
- **method:** ast

## Remediation

- **guidance:** Use async fs APIs (promises/callbacks).
- **tradeoffs:** Refactor required.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

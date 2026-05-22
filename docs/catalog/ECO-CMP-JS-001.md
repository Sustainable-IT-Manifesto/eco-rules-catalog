# ECO-CMP-JS-001

**Name:** Synchronous filesystem calls in request path

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `code`

**System layers:** `code`

## Description

Sync FS calls block the event loop and reduce concurrency.

## Impact

- **confidence:** 0.9
- **notes:** High propagation in Node services.
- **type:** latency

## Detection

- **languages:** `javascript`
- **method:** ast

## Remediation

- **guidance:** Use async fs APIs (promises/callbacks).
- **tradeoffs:** Refactor required.

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

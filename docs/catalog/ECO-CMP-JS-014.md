# ECO-CMP-JS-014

**Name:** Client-side heavy computation without workers

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `code`

**System layers:** `code`

## Description

Heavy CPU work on main thread harms responsiveness and drains battery.

## Impact

- **confidence:** 0.7
- **notes:** Visible as long tasks.
- **type:** cpu

## Detection

- **languages:** `javascript`
- **method:** trace

## Remediation

- **guidance:** Move heavy compute to web workers; optimize algorithms.
- **tradeoffs:** More complexity.

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

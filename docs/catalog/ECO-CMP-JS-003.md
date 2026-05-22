# ECO-CMP-JS-003

**Name:** Large unoptimized bundles

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `code`

**System layers:** `code`

## Description

Large bundles increase transfer size, parse time, and energy use.

## Impact

- **confidence:** 0.75
- **notes:** Affects every page view.
- **type:** network

## Detection

- **languages:** `javascript`
- **method:** trace

## Remediation

- **guidance:** Enable tree-shaking, code splitting, and remove dead deps.
- **tradeoffs:** Build config changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

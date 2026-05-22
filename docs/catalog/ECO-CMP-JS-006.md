# ECO-CMP-JS-006

**Name:** Over-fetching API responses

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `network`

**System layers:** `network`

## Description

Returning unused fields increases payload size and wasted processing.

## Impact

- **confidence:** 0.6
- **notes:** Often easy win.
- **type:** network

## Detection

- **languages:** `javascript`
- **method:** trace

## Remediation

- **guidance:** Return only needed fields; use pagination and sparse responses.
- **tradeoffs:** API contract changes.

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

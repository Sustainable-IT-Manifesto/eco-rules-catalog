# ECO-CMP-JS-004

**Name:** Memory leaks via event listeners

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `code`

**System layers:** `code`

## Description

Unremoved listeners retain objects and increase memory over time.

## Impact

- **confidence:** 0.7
- **notes:** Often progressive and hard to notice.
- **type:** memory

## Detection

- **languages:** `javascript`
- **method:** hybrid

## Remediation

- **guidance:** Remove listeners on cleanup; use weak refs where appropriate.
- **tradeoffs:** Requires lifecycle discipline.

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

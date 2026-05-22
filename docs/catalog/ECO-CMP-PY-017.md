# ECO-CMP-PY-017

**Name:** Large object retained in global scope

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Long-lived globals can cause persistent memory bloat.

## Impact

- **confidence:** 0.65
- **notes:** Often invisible until scale.
- **type:** memory

## Detection

- **languages:** `python`
- **method:** hybrid

## Remediation

- **guidance:** Avoid storing large payloads globally; use caching with eviction.
- **tradeoffs:** May require new cache strategy.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Python family](categories/cmp/families/py/index.md)
- [Back to Rule Browser](../rule-browser.md)

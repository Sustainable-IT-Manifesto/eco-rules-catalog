# ECO-CMP-PY-010

**Name:** Inefficient data structure choice

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Using lists for membership tests instead of sets/dicts increases CPU time.

## Impact

- **confidence:** 0.7
- **notes:** High impact when lookups are frequent.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Use set/dict for membership-heavy operations.
- **tradeoffs:** Memory tradeoff for speed.

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

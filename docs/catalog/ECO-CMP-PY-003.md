# ECO-CMP-PY-003

**Name:** Repeated invariant computation inside loop

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Recomputing values that do not change inside a loop wastes CPU cycles.

## Impact

- **confidence:** 0.6
- **notes:** Best targeted when loop counts are high.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Move invariant work outside the loop.
- **tradeoffs:** Minimal.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

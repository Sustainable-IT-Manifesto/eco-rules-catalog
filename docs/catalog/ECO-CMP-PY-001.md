# ECO-CMP-PY-001

**Name:** String concatenation in loops

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Repeated string concatenation in a loop increases allocations and CPU.

## Impact

- **confidence:** 0.7
- **notes:** Most visible in tight loops / hot paths.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Use list accumulation + join(), or StringIO.
- **tradeoffs:** Slightly more verbose.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

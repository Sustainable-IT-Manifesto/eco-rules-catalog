# ECO-CMP-PY-018

**Name:** Recursive algorithm without safeguards

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Recursion without depth safeguards risks overhead and runtime errors.

## Impact

- **confidence:** 0.55
- **notes:** Depends on input size.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Consider iterative approaches or enforce depth limits.
- **tradeoffs:** Code rewrite.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

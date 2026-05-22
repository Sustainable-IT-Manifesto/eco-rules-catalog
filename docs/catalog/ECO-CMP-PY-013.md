# ECO-CMP-PY-013

**Name:** Inefficient pandas row iteration

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Row-wise pandas iteration is slow compared to vectorized operations.

## Impact

- **confidence:** 0.8
- **notes:** High in analytics/ETL.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Use vectorized ops or apply carefully; avoid iterrows in hot paths.
- **tradeoffs:** Learning curve / refactor time.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

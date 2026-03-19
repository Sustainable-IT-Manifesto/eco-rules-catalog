# ECO-CMP-PY-013

**Name:** Inefficient pandas row iteration

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Row-wise pandas iteration is slow compared to vectorized operations.

## Impact

- **confidence:** 0.8
- **notes:** High in analytics/ETL.
- **type:** cpu

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Use vectorized ops or apply carefully; avoid iterrows in hot paths.
- **tradeoffs:** Learning curve / refactor time.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-PY-002

**Name:** Unbounded list growth

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Collections that grow without bounds increase memory pressure and GC churn.

## Impact

- **confidence:** 0.8
- **notes:** Often shows up in ETL, batch jobs, API aggregation.
- **type:** memory

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Use generators, pagination, batching, or streaming APIs.
- **tradeoffs:** May require refactoring call sites.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

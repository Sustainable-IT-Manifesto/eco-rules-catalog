# ECO-DAT-DATA-012

**Name:** Unbounded analytics queries

**Category:** Data

**Family:** Data

**Primary layer:** `data`

**System layers:** `data`

## Description

Unbounded queries cause runaway compute and unpredictable cost.

## Impact

- **confidence:** 0.75
- **notes:** Common in BI and ad-hoc SQL.
- **type:** cost

## Detection

- **languages:** `infra`, `database`
- **method:** trace

## Remediation

- **guidance:** Add quotas, limits, and guardrails; require partition filters.
- **tradeoffs:** May restrict ad-hoc exploration.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Data category](categories/dat/index.md)
- [Back to Data family](categories/dat/families/data/index.md)
- [Back to Rule Browser](../rule-browser.md)

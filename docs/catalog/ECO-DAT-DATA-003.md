# ECO-DAT-DATA-003

**Name:** Large unused indexes

**Category:** Data

**Family:** Data

**Primary layer:** `data`

**System layers:** `data`

## Description

Unused indexes waste storage and slow writes.

## Impact

- **confidence:** 0.6
- **notes:** Validate via usage stats.
- **type:** storage

## Detection

- **languages:** `database`
- **method:** query

## Remediation

- **guidance:** Drop truly unused indexes; reassess queries.
- **tradeoffs:** Risk if usage stats incomplete.

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

# ECO-DAT-DATA-003

**Name:** Large unused indexes

**Category:** DAT

**Family:** DATA

**Primary layer:** `data`

**System layers:** `data`

## Description

Unused indexes waste storage and slow writes.

## Impact

- **confidence:** 0.6
- **notes:** Validate via usage stats.
- **type:** storage

## Detection

- **languages:**
  - database
- **method:** query

## Remediation

- **guidance:** Drop truly unused indexes; reassess queries.
- **tradeoffs:** Risk if usage stats incomplete.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

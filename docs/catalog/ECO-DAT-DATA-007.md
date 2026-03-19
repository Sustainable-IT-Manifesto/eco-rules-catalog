# ECO-DAT-DATA-007

**Name:** No partitioning for large tables

**Category:** DAT

**Family:** DATA

**Primary layer:** `data`

**System layers:** `data`

## Description

Large tables without partitioning lead to expensive queries and maintenance.

## Impact

- **confidence:** 0.65
- **notes:** Strong when datasets grow.
- **type:** io

## Detection

- **languages:**
  - database
- **method:** query

## Remediation

- **guidance:** Partition by time/key; enforce pruning; archive older partitions.
- **tradeoffs:** Migration complexity.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-DAT-DATA-005

**Name:** Full table scans without index

**Category:** Data

**Family:** Data

**Primary layer:** `data`

**System layers:** `data`

## Description

Full scans increase CPU, IO, and latency for queries.

## Impact

- **confidence:** 0.75
- **notes:** Often visible in query plans.
- **type:** io

## Detection

- **languages:** `database`
- **method:** query

## Remediation

- **guidance:** Add appropriate indexes; rewrite queries; partition large tables.
- **tradeoffs:** Index/storage tradeoffs.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

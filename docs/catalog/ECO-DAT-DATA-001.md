# ECO-DAT-DATA-001

**Name:** Duplicate stored data

**Category:** DAT

**Family:** DATA

**Primary layer:** `data`

**System layers:** `data`

## Description

Redundant data increases storage footprint and cost.

## Impact

- **confidence:** 0.6
- **notes:** Often found in pipelines and analytics copies.
- **type:** storage

## Detection

- **languages:**
  - database
  - infra
- **method:** query

## Remediation

- **guidance:** Deduplicate; normalize; define canonical sources.
- **tradeoffs:** Migration effort.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-NET-NET-008

**Name:** Over-fetching API fields

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Returning unnecessary fields increases payload size and processing.

## Impact

- **confidence:** 0.6
- **notes:** Often easy wins.
- **type:** network

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Use sparse fieldsets; avoid sending unused data.
- **tradeoffs:** API contract changes.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

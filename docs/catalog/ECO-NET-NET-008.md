# ECO-NET-NET-008

**Name:** Over-fetching API fields

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Returning unnecessary fields increases payload size and processing.

## Impact

- **confidence:** 0.6
- **notes:** Often easy wins.
- **type:** network

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Use sparse fieldsets; avoid sending unused data.
- **tradeoffs:** API contract changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

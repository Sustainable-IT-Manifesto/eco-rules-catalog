# ECO-NET-NET-010

**Name:** Large payloads without pagination

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Large unpaginated responses increase memory and bandwidth waste.

## Impact

- **confidence:** 0.75
- **notes:** Often hurts tail latency.
- **type:** network

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Introduce pagination, streaming, or filtering.
- **tradeoffs:** API redesign effort.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-NET-NET-010

**Name:** Large payloads without pagination

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Large unpaginated responses increase memory and bandwidth waste.

## Impact

- **confidence:** 0.75
- **notes:** Often hurts tail latency.
- **type:** network

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Introduce pagination, streaming, or filtering.
- **tradeoffs:** API redesign effort.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

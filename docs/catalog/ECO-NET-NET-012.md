# ECO-NET-NET-012

**Name:** No HTTP/2 or HTTP/3 where applicable

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Older HTTP versions may reduce efficiency for multiplexed workloads.

## Impact

- **confidence:** 0.5
- **notes:** Depends on traffic patterns and client support.
- **type:** latency

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Enable HTTP/2+ on TLS endpoints; evaluate HTTP/3 at edge.
- **tradeoffs:** Operational complexity.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

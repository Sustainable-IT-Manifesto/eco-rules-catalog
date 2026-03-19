# ECO-NET-NET-003

**Name:** Chatty microservice communication

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Many small calls increase latency and cross-service overhead.

## Impact

- **confidence:** 0.7
- **notes:** Common with naive service decomposition.
- **type:** latency

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Aggregate requests, introduce caching, or redesign boundaries.
- **tradeoffs:** May reduce separation or increase payload size.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

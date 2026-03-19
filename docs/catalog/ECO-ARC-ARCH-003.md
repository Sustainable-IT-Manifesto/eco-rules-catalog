# ECO-ARC-ARCH-003

**Name:** Long synchronous dependency chain

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Synchronous call chains amplify latency and failure propagation.

## Impact

- **confidence:** 0.8
- **notes:** Common microservice anti-pattern.
- **type:** latency

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Introduce async boundaries, caching, or collapse hops.
- **tradeoffs:** Consistency and design tradeoffs.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

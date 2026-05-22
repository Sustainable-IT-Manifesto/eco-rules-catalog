# ECO-ARC-ARCH-003

**Name:** Long synchronous dependency chain

**Category:** Architecture

**Family:** Architecture

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Synchronous call chains amplify latency and failure propagation.

## Impact

- **confidence:** 0.8
- **notes:** Common microservice anti-pattern.
- **type:** latency

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Introduce async boundaries, caching, or collapse hops.
- **tradeoffs:** Consistency and design tradeoffs.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Architecture category](categories/arc/index.md)
- [Back to Architecture family](categories/arc/families/arch/index.md)
- [Back to Rule Browser](../rule-browser.md)

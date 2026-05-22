# ECO-NET-NET-014

**Name:** Synchronous cross-region calls

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Cross-region synchronous calls increase latency and cost.

## Impact

- **confidence:** 0.7
- **notes:** Often a structural design issue.
- **type:** latency

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Co-locate dependencies; async replicate; cache at edges.
- **tradeoffs:** Consistency tradeoffs.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Networking category](categories/net/index.md)
- [Back to Network family](categories/net/families/net/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-ARC-ARCH-018

**Name:** No cold-start optimization

**Category:** Architecture

**Family:** Architecture

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Cold starts inflate latency and may force overprovisioning.

## Impact

- **confidence:** 0.5
- **notes:** Depends on platform.
- **type:** latency

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Reduce init work; warm pools selectively; cache dependencies.
- **tradeoffs:** More tuning.

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

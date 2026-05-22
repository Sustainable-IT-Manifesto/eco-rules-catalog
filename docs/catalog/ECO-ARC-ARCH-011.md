# ECO-ARC-ARCH-011

**Name:** Excessive replica counts

**Category:** Architecture

**Family:** Architecture

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Too many replicas increase baseline waste.

## Impact

- **confidence:** 0.6
- **notes:** Validate against SLOs.
- **type:** cost

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Reduce replicas and add autoscaling with guardrails.
- **tradeoffs:** Risk if SLOs not defined.

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

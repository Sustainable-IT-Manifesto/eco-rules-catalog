# ECO-ARC-ARCH-011

**Name:** Excessive replica counts

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Too many replicas increase baseline waste.

## Impact

- **confidence:** 0.6
- **notes:** Validate against SLOs.
- **type:** cost

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Reduce replicas and add autoscaling with guardrails.
- **tradeoffs:** Risk if SLOs not defined.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

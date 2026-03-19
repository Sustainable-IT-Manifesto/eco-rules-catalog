# ECO-ARC-ARCH-001

**Name:** Over-provisioned compute

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Sustained low utilization suggests oversized instances or replicas.

## Impact

- **confidence:** 0.65
- **notes:** Best detected via utilization trends.
- **type:** cost

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Right-size; reduce replicas; add autoscaling with guardrails.
- **tradeoffs:** Must validate against SLOs.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

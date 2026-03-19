# ECO-ARC-ARCH-006

**Name:** Unbounded message queues

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Queues without bounds hide backpressure and create runaway cost.

## Impact

- **confidence:** 0.8
- **notes:** High propagation under partial failures.
- **type:** reliability

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Add backpressure, caps, DLQs, and shedding strategies.
- **tradeoffs:** Must define loss/priority behavior.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

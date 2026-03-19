# ECO-CMP-PY-012

**Name:** CPU-bound work in request thread

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

CPU-heavy work in request handlers reduces throughput and increases latency.

## Impact

- **confidence:** 0.75
- **notes:** Often visible as p95/p99 regression.
- **type:** latency

## Detection

- **languages:**
  - python
- **method:** trace

## Remediation

- **guidance:** Offload CPU work to background jobs or optimize/compile hotspots.
- **tradeoffs:** Added system complexity.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

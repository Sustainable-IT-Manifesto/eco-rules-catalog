# ECO-CMP-PY-012

**Name:** CPU-bound work in request thread

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

CPU-heavy work in request handlers reduces throughput and increases latency.

## Impact

- **confidence:** 0.75
- **notes:** Often visible as p95/p99 regression.
- **type:** latency

## Detection

- **languages:** `python`
- **method:** trace

## Remediation

- **guidance:** Offload CPU work to background jobs or optimize/compile hotspots.
- **tradeoffs:** Added system complexity.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Python family](categories/cmp/families/py/index.md)
- [Back to Rule Browser](../rule-browser.md)

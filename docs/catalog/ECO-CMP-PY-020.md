# ECO-CMP-PY-020

**Name:** Synchronous subprocess invocation in hot path

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Blocking subprocess calls increase latency and consume resources.

## Impact

- **confidence:** 0.7
- **notes:** High variance; often spikes p99.
- **type:** latency

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Avoid subprocess in request paths; cache results or move to background jobs.
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

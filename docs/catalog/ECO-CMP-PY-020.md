# ECO-CMP-PY-020

**Name:** Synchronous subprocess invocation in hot path

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Blocking subprocess calls increase latency and consume resources.

## Impact

- **confidence:** 0.7
- **notes:** High variance; often spikes p99.
- **type:** latency

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Avoid subprocess in request paths; cache results or move to background jobs.
- **tradeoffs:** Added system complexity.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-JAVA-001

**Name:** Excessive object creation in hot path

**Category:** CMP

**Family:** JAVA

**Primary layer:** `code`

**System layers:** `code`

## Description

High allocation rates increase GC pressure and CPU cost.

## Impact

- **confidence:** 0.75
- **notes:** Often shows up as p99 spikes.
- **type:** cpu

## Detection

- **languages:**
  - java
- **method:** trace

## Remediation

- **guidance:** Reduce allocations; reuse objects; optimize parsing.
- **tradeoffs:** May reduce readability.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

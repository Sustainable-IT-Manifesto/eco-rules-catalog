# ECO-CMP-JAVA-009

**Name:** Large heap allocation spikes

**Category:** CMP

**Family:** JAVA

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Heap spikes increase GC pauses and tail latency.

## Impact

- **confidence:** 0.7
- **notes:** Common in parsing/serialization bursts.
- **type:** latency

## Detection

- **languages:**
  - java
- **method:** trace

## Remediation

- **guidance:** Reduce allocations; stream processing; tune GC when needed.
- **tradeoffs:** Measurement required.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

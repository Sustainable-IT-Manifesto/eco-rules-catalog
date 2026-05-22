# ECO-CMP-JAVA-009

**Name:** Large heap allocation spikes

**Category:** Computation

**Family:** Java

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Heap spikes increase GC pauses and tail latency.

## Impact

- **confidence:** 0.7
- **notes:** Common in parsing/serialization bursts.
- **type:** latency

## Detection

- **languages:** `java`
- **method:** trace

## Remediation

- **guidance:** Reduce allocations; stream processing; tune GC when needed.
- **tradeoffs:** Measurement required.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

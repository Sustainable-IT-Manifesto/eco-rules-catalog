# ECO-CMP-JAVA-003

**Name:** Thread pool misconfiguration

**Category:** Computation

**Family:** Java

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Incorrect thread pool sizing can waste CPU or cause latency collapse.

## Impact

- **confidence:** 0.7
- **notes:** Tune to workload and downstream limits.
- **type:** latency

## Detection

- **languages:** `java`
- **method:** trace

## Remediation

- **guidance:** Tune pools; add backpressure; align with DB/HTTP limits.
- **tradeoffs:** Requires measurement.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Java family](categories/cmp/families/java/index.md)
- [Back to Rule Browser](../rule-browser.md)

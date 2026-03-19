# ECO-CMP-JAVA-003

**Name:** Thread pool misconfiguration

**Category:** CMP

**Family:** JAVA

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Incorrect thread pool sizing can waste CPU or cause latency collapse.

## Impact

- **confidence:** 0.7
- **notes:** Tune to workload and downstream limits.
- **type:** latency

## Detection

- **languages:**
  - java
- **method:** trace

## Remediation

- **guidance:** Tune pools; add backpressure; align with DB/HTTP limits.
- **tradeoffs:** Requires measurement.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

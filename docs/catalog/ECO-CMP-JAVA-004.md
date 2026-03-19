# ECO-CMP-JAVA-004

**Name:** Reflection in hot path

**Category:** CMP

**Family:** JAVA

**Primary layer:** `code`

**System layers:** `code`

## Description

Reflection adds overhead and can inflate latency and CPU usage.

## Impact

- **confidence:** 0.6
- **notes:** Context-dependent.
- **type:** cpu

## Detection

- **languages:**
  - java
- **method:** ast

## Remediation

- **guidance:** Avoid reflection in hot paths; precompute accessors.
- **tradeoffs:** Reduced dynamism.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

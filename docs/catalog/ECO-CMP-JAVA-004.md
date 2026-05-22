# ECO-CMP-JAVA-004

**Name:** Reflection in hot path

**Category:** Computation

**Family:** Java

**Primary layer:** `code`

**System layers:** `code`

## Description

Reflection adds overhead and can inflate latency and CPU usage.

## Impact

- **confidence:** 0.6
- **notes:** Context-dependent.
- **type:** cpu

## Detection

- **languages:** `java`
- **method:** ast

## Remediation

- **guidance:** Avoid reflection in hot paths; precompute accessors.
- **tradeoffs:** Reduced dynamism.

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

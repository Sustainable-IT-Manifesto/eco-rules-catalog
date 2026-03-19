# ECO-CMP-JAVA-007

**Name:** Blocking calls in reactive pipeline

**Category:** CMP

**Family:** JAVA

**Primary layer:** `code`

**System layers:** `code`

## Description

Blocking in reactive code collapses concurrency and throughput.

## Impact

- **confidence:** 0.9
- **notes:** High propagation risk.
- **type:** latency

## Detection

- **languages:**
  - java
- **method:** hybrid

## Remediation

- **guidance:** Use non-blocking APIs; isolate blocking work in bounded schedulers.
- **tradeoffs:** Complexity / tuning.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

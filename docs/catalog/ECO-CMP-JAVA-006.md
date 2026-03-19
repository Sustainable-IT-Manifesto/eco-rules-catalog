# ECO-CMP-JAVA-006

**Name:** Missing connection pooling

**Category:** CMP

**Family:** JAVA

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

No pooling increases connection churn and DB overhead.

## Impact

- **confidence:** 0.85
- **notes:** High propagation under load.
- **type:** latency

## Detection

- **languages:**
  - java
- **method:** config

## Remediation

- **guidance:** Use and tune a pool (e.g., HikariCP).
- **tradeoffs:** Must manage max connections.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

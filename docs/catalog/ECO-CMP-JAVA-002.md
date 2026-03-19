# ECO-CMP-JAVA-002

**Name:** Unbounded cache growth

**Category:** CMP

**Family:** JAVA

**Primary layer:** `code`

**System layers:** `code`

## Description

Caches without limits grow until they become the problem.

## Impact

- **confidence:** 0.85
- **notes:** High outage risk.
- **type:** memory

## Detection

- **languages:**
  - java
- **method:** config

## Remediation

- **guidance:** Use bounded caches with eviction policies and TTL.
- **tradeoffs:** Possible cache misses; tune properly.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

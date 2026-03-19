# ECO-CMP-JAVA-008

**Name:** Excessive synchronization contention

**Category:** CMP

**Family:** JAVA

**Primary layer:** `code`

**System layers:** `code`

## Description

Over-synchronization creates contention and wastes CPU.

## Impact

- **confidence:** 0.7
- **notes:** Often visible as lock wait.
- **type:** cpu

## Detection

- **languages:**
  - java
- **method:** trace

## Remediation

- **guidance:** Reduce lock scope; use concurrent structures; redesign hotspots.
- **tradeoffs:** Harder correctness work.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

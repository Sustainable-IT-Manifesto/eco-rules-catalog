# ECO-CMP-JAVA-010

**Name:** Debug logging in production hot path

**Category:** CMP

**Family:** JAVA

**Primary layer:** `code`

**System layers:** `code`

## Description

Verbose logs in hot paths waste CPU and I/O.

## Impact

- **confidence:** 0.6
- **notes:** Worse with sync appenders.
- **type:** io

## Detection

- **languages:**
  - java
- **method:** config

## Remediation

- **guidance:** Lower verbosity; sample; avoid heavy string formatting unless enabled.
- **tradeoffs:** Less detail unless sampled.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

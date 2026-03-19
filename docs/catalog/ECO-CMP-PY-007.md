# ECO-CMP-PY-007

**Name:** Loading entire file into memory

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Reading large files fully into memory increases peak RAM and risk of OOM.

## Impact

- **confidence:** 0.75
- **notes:** Common in file processing / ETL.
- **type:** memory

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Stream/chunk reads; process iteratively.
- **tradeoffs:** May change downstream logic.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

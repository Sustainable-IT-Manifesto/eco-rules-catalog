# ECO-AIM-AI-011

**Name:** Storing all embeddings indefinitely

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Embedding stores without retention grow unbounded and expensive.

## Impact

- **confidence:** 0.7
- **notes:** Often overlooked.
- **type:** storage

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Apply retention and tiering; delete stale embeddings.
- **tradeoffs:** Must re-embed when needed.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

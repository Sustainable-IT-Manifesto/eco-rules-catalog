# ECO-AIM-AI-015

**Name:** No batching of vector search queries

**Category:** AI/ML

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Unbatched vector queries increase overhead and reduce throughput.

## Impact

- **confidence:** 0.55
- **notes:** Depends on query load.
- **type:** cpu

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Batch retrieval queries where possible.
- **tradeoffs:** May add slight latency.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

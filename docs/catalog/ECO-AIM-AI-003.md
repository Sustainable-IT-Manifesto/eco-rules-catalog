# ECO-AIM-AI-003

**Name:** Re-embedding unchanged data

**Category:** AI/ML

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Recomputing embeddings for unchanged inputs wastes compute.

## Impact

- **confidence:** 0.75
- **notes:** Common in RAG pipelines.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** hybrid

## Remediation

- **guidance:** Cache embeddings; invalidate on content change only.
- **tradeoffs:** Cache management.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to AI/ML category](categories/aim/index.md)
- [Back to AI family](categories/aim/families/ai/index.md)
- [Back to Rule Browser](../rule-browser.md)

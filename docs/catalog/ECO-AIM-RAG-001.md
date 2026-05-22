# ECO-AIM-RAG-001

**Name:** Embedding regeneration without change detection

**Category:** AI/ML

**Family:** Retrieval-Augmented Generation

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Embeddings are regenerated for unchanged content, wasting compute and increasing pipeline latency.

## Impact

- **type:** ai-compute
- **confidence:** 0.75
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Use content hashing, incremental indexing, and idempotent embedding pipelines.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** medium
- **storage:** medium
- **human_time:** low
- **carbon:** high
- **water:** medium

## Amplification

- **scales_with_users:** No
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- embedding job logs
- content hashes
- vector DB writes

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0
- **status:** draft
- **source:** catalog expansion recommendations applied 2026-05-21

## Navigation

- [Back to Human Catalog](index.md)
- [Back to AI/ML category](categories/aim/index.md)
- [Back to Retrieval-Augmented Generation family](categories/aim/families/rag/index.md)
- [Back to Rule Browser](../rule-browser.md)

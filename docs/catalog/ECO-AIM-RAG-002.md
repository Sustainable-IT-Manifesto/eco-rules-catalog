# ECO-AIM-RAG-002

**Name:** Excessive retrieval fan-out

**Category:** AI/ML

**Family:** Retrieval-Augmented Generation

**Primary layer:** `ai`

**System layers:** `ai`

## Description

RAG retrieval queries too many sources, chunks, or indexes before ranking, increasing latency and inference context.

## Impact

- **type:** ai-compute
- **confidence:** 0.65
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Tune top-k, prefiltering, reranking, chunking, and index design against answer quality and cost.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** high
- **storage:** medium
- **human_time:** medium
- **carbon:** high
- **water:** medium

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** Yes

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- retrieval traces
- vector DB metrics
- prompt token counts

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

# ECO-AIM-PROMPT-001

**Name:** Repeated static prompt context

**Category:** AI/ML

**Family:** Prompt Construction

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Large static instructions or reference material are injected into every prompt instead of being cached, retrieved, or shortened.

## Impact

- **type:** ai-compute
- **confidence:** 0.8
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Shorten stable instructions, use prompt caching where available, and retrieve only context needed for the task.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** medium
- **storage:** low
- **human_time:** low
- **carbon:** high
- **water:** medium

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** No
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- prompt logs
- token usage
- LLM billing

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
- [Back to Prompt Construction family](categories/aim/families/prompt/index.md)
- [Back to Rule Browser](../rule-browser.md)

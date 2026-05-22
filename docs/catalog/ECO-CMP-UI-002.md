# ECO-CMP-UI-002

**Name:** Excessive polling from client UI

**Category:** Computation

**Family:** Frontend/UI

**Primary layer:** `network`

**System layers:** `network`

## Description

Frontend code polls APIs frequently when event-driven, cached, or user-triggered updates would be sufficient.

## Impact

- **type:** network
- **confidence:** 0.8
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Replace tight polling with backoff, conditional requests, webhooks, push, or user-triggered refresh.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** low
- **network:** high
- **storage:** low
- **human_time:** low
- **carbon:** medium
- **water:** low

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

- browser network traces
- API logs
- RUM

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
- [Back to Computation category](categories/cmp/index.md)
- [Back to Frontend/UI family](categories/cmp/families/ui/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-DAT-CACHE-002

**Name:** Cache stampede risk

**Category:** Data

**Family:** Caching

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Many workers may recompute the same expired value simultaneously, amplifying load during bursts.

## Impact

- **type:** resilience
- **confidence:** 0.7
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Use request coalescing, jittered expiration, stale-while-revalidate, or locks where appropriate.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** medium
- **storage:** low
- **human_time:** medium
- **carbon:** high
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** No
- **scales_non_linearly:** Yes

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- cache metrics
- request bursts
- backend saturation

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
- [Back to Rule Browser](../rule-browser.md)

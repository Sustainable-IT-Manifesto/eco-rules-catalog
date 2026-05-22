# ECO-DAT-CACHE-001

**Name:** Missing cache for repeated expensive lookup

**Category:** Data

**Family:** Caching

**Primary layer:** `data`

**System layers:** `data`

## Description

The same expensive query, API call, or computation is performed repeatedly when results could be safely cached.

## Impact

- **type:** compute
- **confidence:** 0.75
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Introduce bounded caching with explicit invalidation, freshness requirements, and observability.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** medium
- **storage:** low
- **human_time:** low
- **carbon:** high
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- query traces
- APM spans
- flamegraphs

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
- [Back to Data category](categories/dat/index.md)
- [Back to Caching family](categories/dat/families/cache/index.md)
- [Back to Rule Browser](../rule-browser.md)

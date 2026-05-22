# ECO-RES-FAIL-001

**Name:** Retry storm without backoff

**Category:** Resilience & Reliability

**Family:** Failure Handling

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Clients retry failures aggressively without exponential backoff, jitter, or circuit breaking.

## Impact

- **type:** resilience
- **confidence:** 0.85
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Use exponential backoff, jitter, retry budgets, circuit breakers, and idempotency checks.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** high
- **storage:** low
- **human_time:** high
- **carbon:** high
- **water:** medium

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

- incident logs
- request rates
- dependency saturation

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
- [Back to Resilience & Reliability category](categories/res/index.md)
- [Back to Failure Handling family](categories/res/families/fail/index.md)
- [Back to Rule Browser](../rule-browser.md)

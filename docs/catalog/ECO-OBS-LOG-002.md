# ECO-OBS-LOG-002

**Name:** Large payload logging

**Category:** Observability & Telemetry

**Family:** Logging

**Primary layer:** `data`

**System layers:** `data`

## Description

Application logs capture full request, response, or message bodies where summaries or identifiers would be sufficient.

## Impact

- **type:** storage
- **confidence:** 0.75
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Log identifiers, sizes, hashes, or sampled payloads rather than full bodies, especially for large or sensitive data.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** medium
- **storage:** high
- **human_time:** medium
- **carbon:** medium
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

- log samples
- storage billing
- privacy review

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
- [Back to Observability & Telemetry category](categories/obs/index.md)
- [Back to Logging family](categories/obs/families/log/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-GO-009

**Name:** Excessive JSON marshal/unmarshal churn

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Repeatedly marshaling and unmarshaling the same data or using JSON as an internal handoff format.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect json.Marshal followed by json.Unmarshal, map[string]any conversions, or internal JSON round-trips.

## Remediation

- **guidance:** Pass typed structures, stream encode/decode, avoid unnecessary round-trips, or use more efficient internal formats.
- **tradeoffs:** JSON remains useful at boundaries; focus on internal repeated transformations.

## Cost Dimensions

- **compute:** medium
- **memory:** high
- **network:** low
- **storage:** low
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

- CPU profiles
- allocation profiles
- request traces
- benchmark results

## Pattern examples

### Excessive JSON marshal/unmarshal churn

Repeatedly marshaling and unmarshaling the same data or using JSON as an internal handoff format.

## Remediation examples

### Reduce avoidable work

Pass typed structures, stream encode/decode, avoid unnecessary round-trips, or use more efficient internal formats.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

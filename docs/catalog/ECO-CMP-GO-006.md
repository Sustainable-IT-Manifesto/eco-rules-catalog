# ECO-CMP-GO-006

**Name:** Inefficient slice growth

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Appending many items without preallocating capacity when size is known or bounded.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect make([]T, 0) followed by append loops where length is known.

## Remediation

- **guidance:** Use make([]T, 0, n) or make([]T, n) and assign by index when appropriate.
- **tradeoffs:** Overestimating capacity can retain memory longer than needed.

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

### Inefficient slice growth

Appending many items without preallocating capacity when size is known or bounded.

## Remediation examples

### Reduce avoidable work

Use make([]T, 0, n) or make([]T, n) and assign by index when appropriate.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

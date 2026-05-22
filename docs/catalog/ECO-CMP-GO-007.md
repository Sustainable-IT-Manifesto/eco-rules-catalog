# ECO-CMP-GO-007

**Name:** Defers inside hot loops

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Using defer inside high-iteration loops where immediate cleanup is possible.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect defer inside loops, especially file, lock, or response-body cleanup.

## Remediation

- **guidance:** Move loop body into a helper function or close/unlock explicitly at the end of each iteration.
- **tradeoffs:** Explicit cleanup is easier to get wrong; keep helper functions small.

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

### Defers inside hot loops

Using defer inside high-iteration loops where immediate cleanup is possible.

## Remediation examples

### Reduce avoidable work

Move loop body into a helper function or close/unlock explicitly at the end of each iteration.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-GO-008

**Name:** Per-item database or network calls

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Calling database, RPC, or HTTP clients inside loops over collections.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect Query, Exec, Do, or RPC calls inside loops over records or IDs.

## Remediation

- **guidance:** Batch, join, prefetch, pipeline, or use bounded parallelism with backpressure.
- **tradeoffs:** Batching needs careful partial failure handling.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** medium
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

### Per-item database or network calls

Calling database, RPC, or HTTP clients inside loops over collections.

## Remediation examples

### Reduce avoidable work

Batch, join, prefetch, pipeline, or use bounded parallelism with backpressure.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

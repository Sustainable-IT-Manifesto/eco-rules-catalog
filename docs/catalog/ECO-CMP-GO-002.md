# ECO-CMP-GO-002

**Name:** Unbounded goroutine fan-out

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Launching one goroutine per item without concurrency limits.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect go statements inside loops over unbounded or externally sized collections.

## Remediation

- **guidance:** Use worker pools, semaphores, errgroup with limits, rate limits, and bounded queues.
- **tradeoffs:** Concurrency limits must be tuned to workload and downstream capacity.

## Cost Dimensions

- **compute:** high
- **memory:** high
- **network:** low
- **storage:** low
- **human_time:** medium
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** Yes

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

### Unbounded goroutine fan-out

Launching one goroutine per item without concurrency limits.

## Remediation examples

### Reduce avoidable work

Use worker pools, semaphores, errgroup with limits, rate limits, and bounded queues.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

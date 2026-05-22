# ECO-CMP-GO-001

**Name:** Goroutine leak from missing cancellation

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Starting goroutines without a clear cancellation, timeout, or lifecycle owner.

## Impact

- **type:** memory
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect go statements lacking context propagation, done channel handling, or bounded lifecycle.

## Remediation

- **guidance:** Pass context.Context, select on cancellation, close channels deliberately, and make owners responsible for shutdown.
- **tradeoffs:** Cancellation plumbing adds ceremony but prevents long-running operational decay.

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
- **time_degradation:** Yes

## Runtime Evidence

- goroutine dumps
- pprof goroutine profiles
- memory profiles
- request traces

## Pattern examples

### Goroutine leak from missing cancellation

Starting goroutines without a clear cancellation, timeout, or lifecycle owner.

## Remediation examples

### Reduce avoidable work

Pass context.Context, select on cancellation, close channels deliberately, and make owners responsible for shutdown.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

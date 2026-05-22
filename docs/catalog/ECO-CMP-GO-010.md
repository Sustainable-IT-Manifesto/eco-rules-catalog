# ECO-CMP-GO-010

**Name:** Ticker or timer leak

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Creating time.Ticker or timers without stopping them when lifecycle ends.

## Impact

- **type:** memory
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect time.NewTicker or NewTimer without Stop in cancellable code paths.

## Remediation

- **guidance:** Stop tickers/timers with defer or lifecycle cleanup, and drain channels where needed.
- **tradeoffs:** Timer cleanup can be subtle; write small helper patterns and tests.

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
- **burst_sensitive:** No
- **time_degradation:** Yes

## Runtime Evidence

- pprof heap profiles
- goroutine dumps
- long-running process metrics

## Pattern examples

### Ticker or timer leak

Creating time.Ticker or timers without stopping them when lifecycle ends.

## Remediation examples

### Reduce avoidable work

Stop tickers/timers with defer or lifecycle cleanup, and drain channels where needed.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

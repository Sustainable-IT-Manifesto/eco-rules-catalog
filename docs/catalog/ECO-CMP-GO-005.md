# ECO-CMP-GO-005

**Name:** String concatenation in loops

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Building large strings with repeated + or fmt.Sprintf in loops.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect +=, +, or fmt.Sprintf in loops that grow output.

## Remediation

- **guidance:** Use strings.Builder, bytes.Buffer, preallocation, or streaming encoders.
- **tradeoffs:** For tiny strings, readability may outweigh optimization.

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

### String concatenation in loops

Building large strings with repeated + or fmt.Sprintf in loops.

## Remediation examples

### Reduce avoidable work

Use strings.Builder, bytes.Buffer, preallocation, or streaming encoders.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

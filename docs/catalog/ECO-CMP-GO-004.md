# ECO-CMP-GO-004

**Name:** Repeated regexp compilation

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Compiling regular expressions repeatedly instead of reusing compiled patterns.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Find regexp.Compile or MustCompile inside loops or handlers.

## Remediation

- **guidance:** Hoist compiled regex values to package-level vars, init-time construction, or bounded caches.
- **tradeoffs:** Dynamic patterns may require validation and cache eviction.

## Cost Dimensions

- **compute:** high
- **memory:** medium
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

### Repeated regexp compilation

Compiling regular expressions repeatedly instead of reusing compiled patterns.

## Remediation examples

### Reduce avoidable work

Hoist compiled regex values to package-level vars, init-time construction, or bounded caches.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

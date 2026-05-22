# ECO-CMP-GO-003

**Name:** Missing HTTP client timeout

**Category:** Computation

**Family:** Go

**Primary layer:** `code`

**System layers:** `code`

## Description

Using http.Client or default clients without explicit timeouts.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `go`
- **parser:** go_ast
- **notes:** Detect http.DefaultClient, http.Get, or clients with zero Timeout in service paths.

## Remediation

- **guidance:** Set client, request, dial, TLS, and response-header timeouts appropriate to the dependency.
- **tradeoffs:** Timeouts need service-level objectives and retry policy alignment.

## Cost Dimensions

- **compute:** medium
- **memory:** high
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

### Missing HTTP client timeout

Using http.Client or default clients without explicit timeouts.

## Remediation examples

### Reduce avoidable work

Set client, request, dial, TLS, and response-header timeouts appropriate to the dependency.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Go family](categories/cmp/families/go/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-CPP-004

**Name:** Synchronous blocking on futures or async results

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Blocking threads while waiting for asynchronous work in request or event-loop paths.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Detect get(), wait(), join(), blocking waits, or condition variables in latency-sensitive paths.

## Remediation

- **guidance:** Propagate async composition, use continuations/coroutines, or isolate blocking work in bounded executors.
- **tradeoffs:** Async refactors can be invasive; prioritize high-traffic boundaries.

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

### Synchronous blocking on futures or async results

Blocking threads while waiting for asynchronous work in request or event-loop paths.

## Remediation examples

### Reduce avoidable work

Propagate async composition, use continuations/coroutines, or isolate blocking work in bounded executors.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)

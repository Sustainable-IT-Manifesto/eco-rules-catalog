# ECO-CMP-CPP-007

**Name:** Shared pointer overuse

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Using std::shared_ptr where unique ownership, references, or values would be sufficient.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Detect shared_ptr in tight data structures, hot loops, or single-owner lifecycles.

## Remediation

- **guidance:** Prefer unique_ptr, references, values, observer_ptr-like patterns, or explicit lifetime ownership.
- **tradeoffs:** Shared ownership is appropriate for genuinely shared lifetimes.

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

### Shared pointer overuse

Using std::shared_ptr where unique ownership, references, or values would be sufficient.

## Remediation examples

### Reduce avoidable work

Prefer unique_ptr, references, values, observer_ptr-like patterns, or explicit lifetime ownership.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-RS-005

**Name:** Mutex held across await

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Holding a Mutex, RwLock, or guard across an await point.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Detect lock guard lifetimes crossing .await in async functions.

## Remediation

- **guidance:** Limit lock scope before await, clone small values, restructure state ownership, or use async-aware concurrency primitives carefully.
- **tradeoffs:** Reducing lock scope may require rethinking shared mutable state.

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

### Mutex held across await

Holding a Mutex, RwLock, or guard across an await point.

## Remediation examples

### Reduce avoidable work

Limit lock scope before await, clone small values, restructure state ownership, or use async-aware concurrency primitives carefully.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-CPP-008

**Name:** Lock contention in hot paths

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Holding mutexes around expensive work or high-frequency shared state updates.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Detect broad lock scopes, nested locks, or locks around I/O/formatting.

## Remediation

- **guidance:** Narrow lock scope, shard state, use lock-free or wait-free structures carefully, or redesign ownership.
- **tradeoffs:** Lock-free code can be harder to reason about; measure before and after.

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

### Lock contention in hot paths

Holding mutexes around expensive work or high-frequency shared state updates.

## Remediation examples

### Reduce avoidable work

Narrow lock scope, shard state, use lock-free or wait-free structures carefully, or redesign ownership.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)

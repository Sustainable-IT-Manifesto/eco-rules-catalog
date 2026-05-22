# ECO-CMP-CPP-002

**Name:** Heap allocation in tight loops

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Allocating with new, make_unique, vector growth, or temporary containers repeatedly in hot loops.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Find allocations inside loops, callbacks, render paths, or packet/message processing.

## Remediation

- **guidance:** Reserve capacity, reuse buffers, use stack allocation, arenas, object pools, or move allocation outside the loop.
- **tradeoffs:** Pools and arenas require lifecycle discipline and can increase retained memory.

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

### Heap allocation in tight loops

Allocating with new, make_unique, vector growth, or temporary containers repeatedly in hot loops.

## Remediation examples

### Reduce avoidable work

Reserve capacity, reuse buffers, use stack allocation, arenas, object pools, or move allocation outside the loop.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)

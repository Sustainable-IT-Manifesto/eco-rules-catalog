# ECO-CMP-CPP-010

**Name:** Template or dependency bloat in build-critical paths

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Heavy template instantiation or broad dependencies causing excessive compile time and binary growth.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Look for large header-only dependencies, repeated template instantiations, or broad includes in common headers.

## Remediation

- **guidance:** Use forward declarations, precompiled headers judiciously, explicit instantiation, smaller includes, and dependency hygiene.
- **tradeoffs:** Compile-time optimization must not undermine type safety or maintainability.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** low
- **storage:** medium
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

### Template or dependency bloat in build-critical paths

Heavy template instantiation or broad dependencies causing excessive compile time and binary growth.

## Remediation examples

### Reduce avoidable work

Use forward declarations, precompiled headers judiciously, explicit instantiation, smaller includes, and dependency hygiene.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-CPP-001

**Name:** Avoidable copies of large objects

**Category:** Computation

**Family:** C++

**Primary layer:** `code`

**System layers:** `code`

## Description

Passing, returning, or assigning large containers and objects by value when moves or references would avoid copying.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `cpp`
- **parser:** cpp_ast_or_tree_sitter
- **notes:** Detect large parameter-by-value, missing std::move, or range-for copies.

## Remediation

- **guidance:** Use const references, moves, views, emplacement, or explicit ownership transfer where appropriate.
- **tradeoffs:** References and moves can obscure ownership; prefer simple value semantics for small types.

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

### Avoidable copies of large objects

Passing, returning, or assigning large containers and objects by value when moves or references would avoid copying.

## Remediation examples

### Reduce avoidable work

Use const references, moves, views, emplacement, or explicit ownership transfer where appropriate.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to C++ family](categories/cmp/families/cpp/index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-CMP-RS-010

**Name:** Oversized dependency feature sets

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Enabling broad crate features or default features that pull unnecessary code, build work, or runtime behavior.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Inspect Cargo.toml for default-features=true where narrow features would suffice.

## Remediation

- **guidance:** Disable default features and enable only required feature flags; review dependency trees periodically.
- **tradeoffs:** Feature minimization can increase maintenance when crates change feature boundaries.

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

### Oversized dependency feature sets

Enabling broad crate features or default features that pull unnecessary code, build work, or runtime behavior.

## Remediation examples

### Reduce avoidable work

Disable default features and enable only required feature flags; review dependency trees periodically.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)

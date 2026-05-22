# ECO-AIM-AGENT-001

**Name:** Unbounded agent tool-call loop

**Category:** AI/ML

**Family:** AI Agents

**Primary layer:** `ai`

**System layers:** `ai`

## Description

An agent can repeatedly call tools without a bounded budget, convergence check, or escalation path.

## Impact

- **type:** ai-compute
- **confidence:** 0.8
- **notes:** Added as part of the 0.3.0 expansion to capture cross-system sustainability and operational waste.

## Detection

- **method:** static-or-runtime
- **confidence:** 0.55
- **runtime_validation_required:** Yes

## Remediation

- **guidance:** Add explicit budgets, loop detection, tool-call limits, and human escalation for non-converging tasks.
- **tradeoffs:** May require architecture, product, or operations review rather than a local code change.

## Cost Dimensions

- **compute:** high
- **memory:** medium
- **network:** high
- **storage:** low
- **human_time:** medium
- **carbon:** high
- **water:** medium

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** No
- **scales_non_linearly:** Yes

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- agent traces
- tool-call logs
- LLM billing

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0
- **status:** draft
- **source:** catalog expansion recommendations applied 2026-05-21

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

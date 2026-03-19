# ECO-INF-K8S-001

**Name:** Missing or mis-sized CPU and memory requests and limits

**Category:** Infrastructure

**Family:** Kubernetes

**Primary layer:** `process`

**System layers:** `process`, `architecture`

## Description

Kubernetes workloads that omit or poorly size CPU and memory requests and limits make scheduling and capacity planning less efficient, increasing cluster waste and instability.

## Impact

- **cost:** Poor sizing can lead to overprovisioning or noisy-neighbor contention.
- **performance:** Bad sizing increases throttling or eviction risk.
- **carbon:** Inefficient capacity use drives unnecessary cluster footprint.

## Detection

- **method:** yaml-k8s
- **selector:** missing_requests_limits

## Remediation

- **guidance:** Set realistic requests and limits based on actual workload behavior and revise them as measurements improve.
- **examples:**
  - Use observed workload baselines instead of copy-pasted defaults.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **status:** draft
- **severity:** medium
- **version:** 0.3.0-draft

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)

# ECO-INF-K8S-004

**Name:** Heavy or redundant sidecars

**Category:** Infrastructure

**Family:** Kubernetes

**Primary layer:** `architecture`

**System layers:** `architecture`, `network`, `process`

## Description

Workloads that carry heavy or redundant sidecars for logging, metrics, proxies, or helpers can create duplicated per-pod overhead that scales poorly across clusters.

## Impact

- **cost:** Per-pod overhead multiplies across replica counts.
- **performance:** Sidecars compete for pod resources and may add latency.
- **carbon:** Repeated duplicated overhead increases cluster resource use.

## Detection

- **method:** yaml-k8s
- **selector:** heavy_or_redundant_sidecars

## Remediation

- **guidance:** Use sidecars intentionally, consolidate where possible, and prefer shared platform capabilities when they reduce duplicated per-pod cost.
- **examples:**
  - Review whether the same capability can be provided once per node or per cluster instead of once per pod.

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

# ECO-INF-K8S-002

**Name:** Missing HPA for horizontally scalable workloads

**Category:** Infrastructure

**Family:** Kubernetes

**Primary layer:** `process`

**System layers:** `process`, `architecture`

## Description

When a workload is horizontally scalable, the absence of an HPA or equivalent scaling policy can lead to static overprovisioning or inefficient manual scaling.

## Impact

- **cost:** Static replicas often overrun actual need.
- **performance:** Manual scaling lags real demand.
- **carbon:** Idle replicas consume resources without corresponding value.

## Detection

- **method:** yaml-k8s
- **selector:** missing_hpa_for_scalable_workload

## Remediation

- **guidance:** Use autoscaling where workloads and metrics support it, and tune target thresholds carefully.
- **examples:**
  - Deploy HPA for stateless services with clear CPU or custom metric signals.

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

# ECO-INF-K8S-003

**Name:** Overly aggressive health probes

**Category:** Infrastructure

**Family:** Kubernetes

**Primary layer:** `process`

**System layers:** `process`, `network`

## Description

Health probes that run more often than necessary or do expensive work can create avoidable load on applications and the cluster control path.

## Impact

- **cost:** Probe overhead adds up across many pods.
- **performance:** Expensive probes can compete with application work.
- **carbon:** Repeated low-value probe traffic and execution waste resources.

## Detection

- **method:** yaml-k8s
- **selector:** aggressive_health_probes

## Remediation

- **guidance:** Tune probe frequency and probe implementation so checks are lightweight and proportional to real operational need.
- **examples:**
  - Avoid high-frequency probes that trigger full dependency checks on every interval.

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

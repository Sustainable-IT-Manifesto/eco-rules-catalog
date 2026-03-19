# ECO-INF-K8S-005

**Name:** Unpinned images using latest or floating tags

**Category:** Infrastructure

**Family:** Kubernetes

**Primary layer:** `process`

**System layers:** `process`, `architecture`

## Description

Using latest or other floating tags reduces reproducibility and can increase unnecessary redeployments, image pull churn, and debugging effort.

## Impact

- **cost:** Unexpected image changes increase operational churn.
- **performance:** Repeated pulls and redeploys waste time and resources.
- **carbon:** Unnecessary image movement and deployment churn increase resource use.

## Detection

- **method:** yaml-k8s
- **selector:** floating_image_tag

## Remediation

- **guidance:** Pin images to explicit versions or digests and update them deliberately.
- **examples:**
  - Use immutable digests in production manifests when practical.

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

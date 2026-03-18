# ECO-ARC-ARCH-001 — Over-provisioned compute

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** rightsizing, utilization, cost, carbon
- **Legacy ID:** ECO-ARCH-001

## Summary

Sustained low utilization suggests oversized instances or replicas.

## Rationale

Over-provisioning is continuous waste: cost and emissions without benefit.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Best detected via utilization trends.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Right-size; reduce replicas; add autoscaling with guardrails.",
  "tradeoffs": "Must validate against SLOs."
}
```

## Ontology

```json
{
  "system_layers": [
    "architecture"
  ]
}
```

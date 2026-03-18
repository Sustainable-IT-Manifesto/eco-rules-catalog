# ECO-ARC-ARCH-004 — No autoscaling policy

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** autoscaling
- **Legacy ID:** ECO-ARCH-004

## Summary

Without scaling policies, systems drift into waste or fragility.

## Rationale

Static sizing is rarely correct across demand variability.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Both over- and under-provisioning risk.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Add autoscaling with SLO guardrails and max limits.",
  "tradeoffs": "Tuning required."
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

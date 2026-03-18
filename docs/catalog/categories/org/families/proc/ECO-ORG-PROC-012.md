# ECO-ORG-PROC-012 — No SLO-based scaling validation

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** note
- **Tags:** slo, autoscaling
- **Legacy ID:** ECO-PROC-012

## Summary

Scaling without SLO validation often leads to overprovisioning or fragility.

## Rationale

SLOs turn scaling from guesswork into evidence.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Systemic practice.",
  "type": "reliability"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Define SLOs and validate scaling changes against them.",
  "tradeoffs": "Requires observability maturity."
}
```

## Ontology

```json
{
  "system_layers": [
    "process"
  ]
}
```

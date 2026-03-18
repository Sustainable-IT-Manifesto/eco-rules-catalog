# ECO-AIM-AI-013 — No GPU utilization monitoring

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** Ai
- **Tier:** 4
- **Severity:** warning
- **Tags:** gpu, observability
- **Legacy ID:** ECO-AI-013

## Summary

Without GPU utilization metrics, accelerator waste stays invisible.

## Rationale

You can’t right-size accelerators without seeing utilization.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Systemic maturity.",
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
  "guidance": "Add GPU metrics, dashboards, and alerts.",
  "tradeoffs": "Telemetry overhead."
}
```

## Ontology

```json
{
  "system_layers": [
    "ai"
  ]
}
```

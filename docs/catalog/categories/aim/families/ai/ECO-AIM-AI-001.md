# ECO-AIM-AI-001 — Oversized model selection

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** Ai
- **Tier:** 3
- **Severity:** warning
- **Tags:** ai, model-selection
- **Legacy ID:** ECO-AI-001

## Summary

Using larger models than needed increases inference cost and emissions.

## Rationale

Model size is a direct multiplier for compute and energy.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Workload-dependent.",
  "type": "carbon"
}
```

## Detection

```json
{
  "languages": [
    "python",
    "infra"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Benchmark smaller models and quantify tradeoffs before scaling.",
  "tradeoffs": "May reduce marginal quality."
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

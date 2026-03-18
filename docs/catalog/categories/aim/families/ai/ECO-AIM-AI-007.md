# ECO-AIM-AI-007 — No model quantization

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** Ai
- **Tier:** 3
- **Severity:** note
- **Tags:** ai, quantization
- **Legacy ID:** ECO-AI-007

## Summary

Failure to quantize when appropriate wastes inference compute.

## Rationale

Quantization can reduce compute cost with acceptable quality tradeoffs.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Model-dependent.",
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
  "guidance": "Evaluate quantization for inference workloads.",
  "tradeoffs": "Potential quality/compatibility changes."
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

# ECO-AIM-AI-009 — No evaluation before scaling model

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 3
- **Severity:** warning
- **Tags:** ai, evaluation
- **Legacy ID:** ECO-AI-009

## Summary

Scaling without evaluation wastes resources and can degrade outcomes.

## Rationale

Scale should follow evidence, not excitement.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Common governance gap.",
  "type": "cost"
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
  "guidance": "Require eval gates before scaling model size/traffic.",
  "tradeoffs": "Slower rollout."
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

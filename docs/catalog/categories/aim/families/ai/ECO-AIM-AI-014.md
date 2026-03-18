# ECO-AIM-AI-014 — Inefficient feature preprocessing pipelines

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** Ai
- **Tier:** 2
- **Severity:** note
- **Tags:** ai, pipelines
- **Legacy ID:** ECO-AI-014

## Summary

Preprocessing waste increases training and inference cost.

## Rationale

Preprocessing is often a hidden cost multiplier.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Measure and optimize hotspots.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Cache features; vectorize; batch transforms.",
  "tradeoffs": "Complexity."
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

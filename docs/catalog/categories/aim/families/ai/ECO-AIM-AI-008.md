# ECO-AIM-AI-008 — Re-training without drift detection

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 3
- **Severity:** warning
- **Tags:** ai, training
- **Legacy ID:** ECO-AI-008

## Summary

Training without drift checks wastes compute and introduces risk.

## Rationale

Training should be triggered by need, not habit.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "High compute waste risk.",
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
  "guidance": "Add drift detection and training triggers.",
  "tradeoffs": "Monitoring complexity."
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

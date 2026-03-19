# ECO-AIM-AI-010 — Overly frequent fine-tuning cycles

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 3
- **Severity:** note
- **Tags:** ai, finetuning
- **Legacy ID:** ECO-AI-010

## Summary

Frequent tuning without clear value wastes compute.

## Rationale

Tuning cycles should be justified by measurable benefit.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Depends on pipeline.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Set tuning cadence based on outcomes and drift.",
  "tradeoffs": "May delay improvements."
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

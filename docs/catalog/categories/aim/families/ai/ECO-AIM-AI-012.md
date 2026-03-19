# ECO-AIM-AI-012 — Large model in low-SLA workload

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 3
- **Severity:** warning
- **Tags:** ai, rightsizing
- **Legacy ID:** ECO-AI-012

## Summary

Using high-cost models where latency/quality needs are modest wastes resources.

## Rationale

Model choice should match workload needs, not default to maximum.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Usually a quick win.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Tier models by use case; route requests by need.",
  "tradeoffs": "Routing complexity."
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

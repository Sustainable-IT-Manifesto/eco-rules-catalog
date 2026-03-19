# ECO-AIM-AI-006 — Unbounded context window usage

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 2
- **Severity:** warning
- **Tags:** ai, context-window
- **Legacy ID:** ECO-AI-006

## Summary

Excessive context increases token cost and latency.

## Rationale

Token usage is a direct multiplier for cost and energy.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Often the biggest controllable factor.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org",
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Summarize, retrieve selectively, and cap context intentionally.",
  "tradeoffs": "Requires prompt/pipeline design."
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

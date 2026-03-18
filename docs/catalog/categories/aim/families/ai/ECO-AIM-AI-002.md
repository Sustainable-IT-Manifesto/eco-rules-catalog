# ECO-AIM-AI-002 — No inference batching

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** Ai
- **Tier:** 2
- **Severity:** warning
- **Tags:** ai, batching
- **Legacy ID:** ECO-AI-002

## Summary

No batching increases per-request overhead and lowers throughput.

## Rationale

Batching improves throughput and reduces overhead per token/request.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often significant for GPU inference.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "python",
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Introduce batching at gateway/inference server.",
  "tradeoffs": "Added latency for low volume; needs tuning."
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

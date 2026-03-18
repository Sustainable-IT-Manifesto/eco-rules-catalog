# ECO-AIM-AI-011 — Storing all embeddings indefinitely

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** Ai
- **Tier:** 4
- **Severity:** warning
- **Tags:** ai, embeddings, retention
- **Legacy ID:** ECO-AI-011

## Summary

Embedding stores without retention grow unbounded and expensive.

## Rationale

Embeddings are data; they need lifecycle rules too.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often overlooked.",
  "type": "storage"
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
  "guidance": "Apply retention and tiering; delete stale embeddings.",
  "tradeoffs": "Must re-embed when needed."
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

# ECO-AIM-AI-003 — Re-embedding unchanged data

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 2
- **Severity:** warning
- **Tags:** ai, embeddings
- **Legacy ID:** ECO-AI-003

## Summary

Recomputing embeddings for unchanged inputs wastes compute.

## Rationale

Embeddings should be cached based on content hash/version.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Common in RAG pipelines.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Cache embeddings; invalidate on content change only.",
  "tradeoffs": "Cache management."
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

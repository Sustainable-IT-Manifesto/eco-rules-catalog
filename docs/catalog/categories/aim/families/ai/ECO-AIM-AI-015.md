# ECO-AIM-AI-015 — No batching of vector search queries

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 2
- **Severity:** note
- **Tags:** ai, vector-search
- **Legacy ID:** ECO-AI-015

## Summary

Unbatched vector queries increase overhead and reduce throughput.

## Rationale

Batching reduces per-request overhead for retrieval.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Depends on query load.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Batch retrieval queries where possible.",
  "tradeoffs": "May add slight latency."
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

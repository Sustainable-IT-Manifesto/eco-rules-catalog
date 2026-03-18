# ECO-AIM-AI-004 — No prompt caching

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** Ai
- **Tier:** 2
- **Severity:** note
- **Tags:** ai, caching
- **Legacy ID:** ECO-AI-004

## Summary

Repeated prompts without caching waste tokens and compute.

## Rationale

Many prompts are repetitive; caching reduces repeated work.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Strong for templated workflows.",
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
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Cache deterministic responses with TTL and safe scoping.",
  "tradeoffs": "Risk of staleness; privacy considerations."
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

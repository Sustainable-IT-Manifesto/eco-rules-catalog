# ECO-DAT-DATA-014 — Stale feature flags accumulating

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 2
- **Severity:** note
- **Tags:** feature-flags
- **Legacy ID:** ECO-DATA-014

## Summary

Feature flags left indefinitely add complexity and runtime overhead.

## Rationale

Stale flags increase cognitive load and sometimes runtime branching costs.

## Impact

```json
{
  "confidence": 0.5,
  "notes": "Mostly complexity-driven waste.",
  "type": "cpu"
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
  "guidance": "Set expiration dates and cleanup workflows.",
  "tradeoffs": "Requires discipline."
}
```

## Ontology

```json
{
  "system_layers": [
    "data"
  ]
}
```

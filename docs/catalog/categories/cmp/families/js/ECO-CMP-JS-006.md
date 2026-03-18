# ECO-CMP-JS-006 — Over-fetching API responses

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Network
- **Tier:** 1
- **Severity:** note
- **Tags:** javascript, api, payload
- **Legacy ID:** ECO-JS-006

## Summary

Returning unused fields increases payload size and wasted processing.

## Rationale

Extra bytes multiply across users and calls.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Often easy win.",
  "type": "network"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Return only needed fields; use pagination and sparse responses.",
  "tradeoffs": "API contract changes."
}
```

## Ontology

```json
{
  "system_layers": [
    "network"
  ]
}
```

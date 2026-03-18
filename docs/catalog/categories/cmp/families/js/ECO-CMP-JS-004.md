# ECO-CMP-JS-004 — Memory leaks via event listeners

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** javascript, memory, leak
- **Legacy ID:** ECO-JS-004

## Summary

Unremoved listeners retain objects and increase memory over time.

## Rationale

Leaks increase baseline memory and trigger more GC work.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often progressive and hard to notice.",
  "type": "memory"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Remove listeners on cleanup; use weak refs where appropriate.",
  "tradeoffs": "Requires lifecycle discipline."
}
```

## Ontology

```json
{
  "system_layers": [
    "code"
  ]
}
```

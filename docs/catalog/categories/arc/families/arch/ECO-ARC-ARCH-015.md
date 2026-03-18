# ECO-ARC-ARCH-015 — Tight coupling across bounded contexts

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** note
- **Tags:** coupling
- **Legacy ID:** ECO-ARCH-015

## Summary

Coupling increases coordination cost and failure propagation.

## Rationale

Coupling drives accidental complexity and multiplies work.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Architecture review item.",
  "type": "reliability"
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
  "guidance": "Clarify boundaries; reduce synchronous dependencies.",
  "tradeoffs": "Refactoring effort."
}
```

## Ontology

```json
{
  "system_layers": [
    "architecture"
  ]
}
```

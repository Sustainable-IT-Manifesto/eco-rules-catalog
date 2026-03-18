# ECO-CMP-JS-008 — Excessive DOM reflow

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 1
- **Severity:** warning
- **Tags:** javascript, dom, performance
- **Legacy ID:** ECO-JS-008

## Summary

Layout thrashing increases CPU and drains battery.

## Rationale

Repeated measure/mutate cycles trigger expensive layout work.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Common in complex UI interactions.",
  "type": "cpu"
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
  "guidance": "Batch DOM reads/writes; use requestAnimationFrame patterns.",
  "tradeoffs": "Refactor UI code."
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

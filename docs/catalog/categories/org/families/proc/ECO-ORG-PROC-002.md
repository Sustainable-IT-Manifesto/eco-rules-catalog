# ECO-ORG-PROC-002 — No baseline measurement

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** warning
- **Tags:** measurement, baseline
- **Legacy ID:** ECO-PROC-002

## Summary

Without baseline data, improvements can’t be validated.

## Rationale

Baseline-first prevents wasted optimization cycles and false wins.

## Impact

```json
{
  "confidence": 0.9,
  "notes": "Foundational.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Establish baselines before optimization; track before/after.",
  "tradeoffs": "Instrumentation effort."
}
```

## Ontology

```json
{
  "system_layers": [
    "process"
  ]
}
```

# ECO-CMP-JS-010 — Missing request timeout

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Network
- **Tier:** 2
- **Severity:** error
- **Tags:** javascript, timeouts
- **Legacy ID:** ECO-JS-010

## Summary

Requests without timeouts hang and create cascading latency.

## Rationale

Timeouts are a reliability boundary; missing them removes the boundary.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "High propagation risk.",
  "type": "reliability"
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
  "guidance": "Use AbortController / client timeouts; set defaults.",
  "tradeoffs": "Endpoint tuning."
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

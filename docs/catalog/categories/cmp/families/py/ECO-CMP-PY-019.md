# ECO-CMP-PY-019 — Excessive thread spawning

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, concurrency
- **Legacy ID:** ECO-PY-019

## Summary

Creating many threads increases overhead and contention.

## Rationale

Thread creation and contention can reduce throughput and increase CPU waste.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Often misused for I/O that could be async.",
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
  "guidance": "Use thread pools, async I/O, or bounded concurrency.",
  "tradeoffs": "Requires concurrency redesign."
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

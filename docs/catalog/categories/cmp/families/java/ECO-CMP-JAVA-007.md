# ECO-CMP-JAVA-007 — Blocking calls in reactive pipeline

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Code
- **Tier:** 2
- **Severity:** error
- **Tags:** java, reactive, blocking
- **Legacy ID:** ECO-JAVA-007

## Summary

Blocking in reactive code collapses concurrency and throughput.

## Rationale

Reactive systems rely on non-blocking work to scale efficiently.

## Impact

```json
{
  "confidence": 0.9,
  "notes": "High propagation risk.",
  "type": "latency"
}
```

## Detection

```json
{
  "languages": [
    "java"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Use non-blocking APIs; isolate blocking work in bounded schedulers.",
  "tradeoffs": "Complexity / tuning."
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

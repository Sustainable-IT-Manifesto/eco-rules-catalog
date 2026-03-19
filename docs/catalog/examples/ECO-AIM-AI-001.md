# ECO-AIM-AI-001 Examples

## Pattern

A service sends large repeated prompt boilerplate and unnecessary context on every inference request.

### Why this is inefficient

- more tokens than needed
- higher latency
- higher cost
- unnecessary compute

## Better

Cache or template stable prompt sections and send only the variable content where possible.

## Tradeoffs

- caching adds some implementation complexity
- prompt trimming should not remove important context

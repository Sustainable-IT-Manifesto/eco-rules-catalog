# From Waste to Design

## An Executive Brief on the Eco Rules and Sustainable IT Maturity

**Author:** Matt “Kelly” Williams
Making Software Greener | Sustainable IT Manifesto

---

## Executive Summary

Most inefficiency in software systems is not dramatic.
It does not break production.
It does not raise alarms.

It accumulates.

Retries without boundaries.
Compute provisioned “just in case.”
Logs stored indefinitely.
Oversized AI models used by default.

Individually, these decisions are reasonable.
Collectively, they create structural waste — increasing cost, carbon, latency, and operational risk.

The Eco Rules Catalog makes this waste visible.
The Sustainable IT Manifesto (SITM) provides the maturity path to address it.

This brief outlines:

* The structural nature of software waste
* The four propagation tiers of inefficiency
* The SITM maturity progression
* A practical adoption model for organizations

---

## Waste Is Structural

Waste in software systems rarely comes from incompetence.

It emerges from:

* Missing boundaries
* Unexamined defaults
* Lack of measurement
* Overprovisioned infrastructure
* Undefined lifecycle policies

Performance, cost, and carbon are not separate problems.
They are the same problem observed at different layers.

Without intentional design, inefficiency compounds.

---

## The Eco Rules Catalog

The Eco Rules Catalog is a structured registry of repeatable inefficiency patterns across:

* Code
* Network
* Architecture
* Data
* AI/ML
* Governance

Version 1.0.0 includes 125 foundational rules.

Each rule identifies:

* The inefficiency pattern
* The propagation tier
* The impact surface (CPU, memory, latency, storage, cost, carbon)
* The smallest safe intervention

The goal is not optimization for its own sake.
It is architectural clarity.

---

## Propagation Tiers

Not all inefficiencies are equal.

### Tier 1 — Local

Code-level inefficiencies. Easy to fix. Individually small.

### Tier 2 — Amplified

Service-level behaviors that multiply under load (timeouts, retries, chatty services).

### Tier 3 — Structural

Architectural design decisions that scale waste (overprovisioning, no autoscaling, no lifecycle tiers).

### Tier 4 — Organizational

Governance-level gaps (no performance budgets, no cost visibility, no ownership).

Higher tiers create exponential impact.

---

## The SITM Maturity Pathway

The Sustainable IT Manifesto defines a four-stage maturity model:

### Aware

Waste becomes visible.

### Conscious

Propagation and system impact are understood.

### Enabled

Teams can intervene safely with measurement and guardrails.

### Empowered

Efficiency is embedded in design, budgeting, and governance.

The rules do not change across stages.
The relationship to them does.

---

## Why This Matters Now

Three forces are accelerating structural waste:

1. Cloud abstraction (infrastructure feels infinite)
2. Microservice amplification (propagation multiplies)
3. AI workloads (compute intensity increases rapidly)

Without boundaries, costs and carbon scale faster than value.

Organizations that treat efficiency as reactive optimization will fall behind.

Organizations that design constraints into systems will be more resilient.

---

## Adoption Model

A practical rollout follows four phases:

**Phase 1 — Visibility**
Identify common inefficiencies. Introduce vocabulary.

**Phase 2 — Propagation Review**
Analyze retries, utilization, storage growth, AI workloads.

**Phase 3 — Guardrails**
Implement autoscaling policies, retention rules, observability, SLO validation.

**Phase 4 — Governance Integration**
Define performance budgets, cost visibility, lifecycle ownership.

This progression aligns directly with SITM maturity.

---

## Strategic Outcomes

Organizations that adopt this model achieve:

* Lower operational cost
* Reduced incident amplification
* Smaller carbon footprint
* Improved system resilience
* Clearer architectural decision-making

Efficiency becomes a design principle, not a late-stage correction.

---

## Closing Perspective

Sustainable IT is not about doing more with less.

It is about building systems with boundaries.

When boundaries are explicit:

* Waste decreases
* Resilience increases
* Scale becomes intentional

Performance, cost, and carbon are signals of the same underlying design quality.

The Eco Rules make inefficiency visible.
SITM provides the pathway to maturity.

The opportunity is not to optimize everything.

It is to design better systems from the start.


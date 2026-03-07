---

# From Waste to Design

## The Eco Rules Catalog and the Sustainable IT Maturity Pathway

**Author:** Matt “Kelly” Williams
Founder, Making Software Greener (http://MakingSoftwareGreener.com)
Creator, Sustainable IT Manifesto (http://SustainableITManifesto.org)

---

## Executive Summary

Most inefficiency in software systems is not dramatic.

It does not crash systems.
It does not trigger alarms.
It does not show up as a headline.

It accumulates.

A retry here.
An oversized model there.
Logs stored forever.
Compute provisioned “just in case.”

Individually, these decisions are reasonable.
Collectively, they form structural waste.

The Eco Rules Catalog was created to make that waste visible.
The Sustainable IT Manifesto (SITM) provides the maturity path to address it.

This paper describes:

* The Eco Rules as a discipline-level catalog of software inefficiencies
* The four propagation tiers of waste
* The SITM maturity pathway: Aware → Conscious → Enabled → Empowered
* How organizations move from reactive optimization to structural prevention

This is not about austerity.
It is about architectural clarity.

---

# 1. Waste Is Structural, Not Accidental

Most teams believe inefficiency is caused by:

* Sloppy code
* Inexperienced developers
* Lack of performance tuning

In practice, most waste emerges from:

* Missing boundaries
* Lack of measurement
* Unexamined defaults
* Overly cautious provisioning
* Absent lifecycle policies

Waste persists not because engineers are careless, but because systems are not designed with explicit constraints.

Performance, cost, and carbon are not separate concerns.
They are the same concern measured at different layers.

---

# 2. The Eco Rules Catalog

The Eco Rules Catalog is a structured registry of repeatable inefficiency patterns across:

* Code
* Network
* Architecture
* Data
* AI/ML
* Governance

Each rule identifies:

* The pattern
* The propagation tier
* The likely impact surface (CPU, memory, latency, storage, cost, carbon)
* The smallest safe intervention

The catalog does not assign blame.
It identifies signals.

Examples:

* String concatenation inside loops
* Missing timeouts on network calls
* Retry storms without backoff
* Over-provisioned compute
* Logs retained indefinitely
* Oversized model selection
* No performance budget defined

The catalog spans 125 foundational rules in Version 1.0.0.

---

# 3. Propagation Tiers

Not all inefficiencies are equal.

The catalog organizes waste into four propagation tiers.

## Tier 1 — Local Inefficiency

Small inefficiencies at the code level.

Examples:

* Repeated invariant computation
* Unoptimized data structures
* Excessive logging in hot paths

These are inexpensive to fix but numerous.

---

## Tier 2 — Service-Level Amplification

Patterns that amplify under load.

Examples:

* Missing timeouts
* Retry storms
* N+1 database queries
* Polling instead of push

These issues convert small disruptions into system strain.

---

## Tier 3 — Architectural Waste

Structural inefficiencies that scale waste.

Examples:

* Over-provisioned compute
* Always-on low-traffic services
* Long synchronous dependency chains
* Hot storage used for cold data

These are not code mistakes.
They are design decisions.

---

## Tier 4 — Organizational Propagation

Systemic inefficiencies embedded in process.

Examples:

* No performance budget
* No cost observability
* No baseline measurement
* No lifecycle governance
* No sustainability accountability owner

At this tier, waste is cultural.

---

# 4. The SITM Maturity Pathway

The Sustainable IT Manifesto frames maturity as:

Aware → Conscious → Enabled → Empowered

This pathway describes how individuals and organizations relate to waste.

The Eco Rules remain constant.
The interpretation evolves.

---

## Aware — Recognition

“I can see inefficiency.”

At this stage:

* Engineers recognize waste patterns.
* Code-level inefficiencies become visible.
* Simple fixes are applied.

Primary focus:
Tier 1 and obvious Tier 2 rules.

Milestone:
Waste becomes observable.

---

## Conscious — Propagation

“I understand consequences.”

At this stage:

* Teams recognize amplification.
* Retry behavior is examined.
* Latency percentiles are tracked.
* Structural bottlenecks become visible.

Primary focus:
Tier 2 and Tier 3 rules.

Milestone:
Waste is understood as systemic, not isolated.

---

## Enabled — Intervention

“I can change it safely.”

At this stage:

* Baseline → Change → After discipline exists.
* Autoscaling is validated against SLOs.
* Retention policies are implemented.
* Observability informs architectural changes.

Primary focus:
Tier 3 structural rules and measurement anchors.

Milestone:
Intervention is deliberate, not reactive.

---

## Empowered — Prevention

“We design boundaries.”

At this stage:

* Performance budgets exist before scaling.
* Cost and carbon are observable at service level.
* Decommissioning workflows are routine.
* Architectural review includes efficiency gates.
* AI workloads are routed intentionally.

Primary focus:
Tier 4 governance and structural design.

Milestone:
Waste prevention is embedded in architecture and culture.

---

# 5. The Shift from Optimization to Design

Most organizations optimize after pain.

Empowered organizations design constraints before scale.

This requires:

* Explicit budgets
* Explicit lifecycle policies
* Explicit accountability
* Explicit observability

Without these, efficiency becomes accidental.

With them, it becomes structural.

---

# 6. AI and the Acceleration of Waste

AI introduces new amplification vectors:

* Token growth
* Oversized model selection
* Always-on inference endpoints
* Repeated embedding of unchanged data
* GPU underutilization

Without discipline, AI multiplies inefficiency faster than traditional systems.

The Eco Rules extend naturally to AI systems because the underlying principle remains:

Boundaries define sustainability.

---

# 7. A Practical Adoption Model

Organizations can adopt the Eco Rules in phases:

### Phase 1 — Awareness Workshops

Introduce common Tier 1 and Tier 2 patterns.

### Phase 2 — Propagation Review

Analyze retry patterns, dependency chains, and utilization metrics.

### Phase 3 — Structural Guardrails

Implement retention policies, autoscaling, and observability standards.

### Phase 4 — Governance Integration

Define performance budgets and accountability ownership.

This progression mirrors SITM maturity.

---

# 8. Certification and Institutionalization

The Eco Rules can support:

* Sustainable IT Foundation (Aware)
* Sustainable IT Practitioner (Conscious)
* Sustainable IT Specialist (Enabled)
* Sustainable IT Expert / Master (Empowered)

Certification is not about memorizing rules.

It is about demonstrating:

* Recognition
* Propagation awareness
* Safe intervention
* Structural design integration

---

# 9. Conclusion

Waste is rarely visible at first.

It accumulates quietly in defaults, retries, oversized resources, and infinite retention.

The Eco Rules Catalog makes waste visible.

The SITM pathway provides the maturity arc to address it.

This is not about doing more with less.

It is about building systems that respect boundaries.

Performance, cost, and carbon are not competing priorities.

They are the same signal seen from different vantage points.

When boundaries are clear, resilience improves.

When propagation is understood, incidents shrink.

When governance is explicit, waste declines.

Sustainable IT is not a feature.

It is a design discipline.

---


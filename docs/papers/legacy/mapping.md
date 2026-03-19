# Mapping the Eco Rules Catalog to SITM

The Eco Rules describe what waste looks like.

The SITM pathway describes how people and organizations mature in relation to waste.

The rules themselves do not change across stages.
What changes is:

* The depth of understanding
* The scope of responsibility
* The level of intervention
* Whether action is reactive or structural

---

# AWARE

“I can see it.”

## Focus

Recognition. Vocabulary. Pattern identification.

At this stage, individuals recognize inefficiency patterns in isolation. Waste becomes visible.

## Typical Audience

Developers, early-career engineers, students, teams new to sustainability discussions.

## Rule Categories Most Relevant

Primarily Tier 1 and clear Tier 2 signals.

### Code-Level Visibility

* ECO-PY-001 — String concatenation in loops
* ECO-PY-003 — Repeated invariant computation
* ECO-JS-003 — Large unoptimized bundles
* ECO-JAVA-001 — Excessive object creation
* ECO-PY-009 — Repeated regex compilation
* ECO-JS-011 — Multi-pass array transformations

### Obvious Network Signals

* ECO-NET-002 — No compression
* ECO-NET-005 — Missing timeouts
* ECO-NET-010 — No pagination

### AI Efficiency Signals

* ECO-AI-006 — Unbounded context window usage
* ECO-AI-002 — No inference batching

## What Aware Looks Like

* “That’s inefficient.”
* “That’s avoidable.”
* “I didn’t realize that mattered.”

Measurement is not yet systematic. Recognition is the milestone.

---

# CONSCIOUS

“I understand the consequences.”

## Focus

Propagation. Tradeoffs. System-level impact.

At this stage, inefficiency is no longer isolated. Teams understand how local waste amplifies across services and infrastructure.

## Typical Audience

Senior engineers, SREs, platform engineers, architects.

## Rule Categories Most Relevant

Tier 2 and Tier 3 propagation rules.

### Reliability and Amplification

* ECO-NET-007 — Retry storms
* ECO-NET-015 — No circuit breaker
* ECO-NET-003 — Chatty microservices
* ECO-PY-005 — N+1 database queries
* ECO-JAVA-005 — N+1 ORM queries

### Architectural Propagation

* ECO-ARCH-003 — Long synchronous dependency chains
* ECO-ARCH-006 — Unbounded message queues
* ECO-ARCH-004 — No autoscaling policy
* ECO-ARCH-005 — No container resource limits

### Data Growth and Drift

* ECO-DATA-004 — Logs stored indefinitely
* ECO-DATA-005 — Full table scans without index

### AI Propagation

* ECO-AI-001 — Oversized model selection
* ECO-AI-005 — Always-on inference endpoints

## What Conscious Looks Like

* Monitoring p95 and p99 latency
* Observing retry behavior during incidents
* Recognizing structural bottlenecks
* Seeing cost and carbon as system outcomes

Conscious teams understand propagation, not just inefficiency.

---

# ENABLED

“I can change it safely.”

## Focus

Guardrails. Baselines. Safe intervention.

At this stage, teams can intervene deliberately and measure the outcome.

## Typical Audience

Staff engineers, lead architects, platform teams, technical leadership.

## Rule Categories Most Relevant

Tier 3 structural changes and measurement anchors.

### Architecture Controls

* ECO-ARCH-001 — Over-provisioned compute
* ECO-ARCH-002 — Always-on low-traffic service
* ECO-ARCH-010 — No observability on utilization
* ECO-ARCH-012 — Lack of graceful degradation strategy

### Data Governance

* ECO-DATA-002 — Missing retention policy
* ECO-DATA-013 — No data lifecycle governance
* ECO-DATA-009 — No archival tier strategy

### AI Efficiency Controls

* ECO-AI-013 — No GPU utilization monitoring
* ECO-AI-009 — No evaluation before scaling model
* ECO-AI-007 — No model quantization

### Process Anchors

* ECO-PROC-002 — No baseline measurement
* ECO-PROC-005 — Feature shipped without load testing

## What Enabled Looks Like

* Baseline → Change → After measurement discipline
* Right-sizing with SLO validation
* Autoscaling guardrails in place
* Explicit retention policies

Enabled teams can reduce waste without destabilizing the system.

---

# EMPOWERED

“We design systems that prevent waste.”

## Focus

Structural prevention. Cultural integration. Governance.

At this stage, efficiency is not reactive. It is designed into architecture and process.

## Typical Audience

Engineering leadership, CTOs, governance bodies, sustainability leads.

## Rule Categories Most Relevant

Tier 4 governance and systemic architecture rules.

### Governance and Budgeting

* ECO-PROC-001 — No performance budget defined
* ECO-PROC-003 — No cost observability
* ECO-PROC-004 — No carbon awareness
* ECO-PROC-011 — No decommission workflow
* ECO-PROC-015 — No sustainability accountability owner

### Structural Architecture

* ECO-ARCH-015 — Tight coupling across domains
* ECO-ARCH-016 — No tenant isolation
* ECO-ARCH-020 — Underutilized GPU resources

### Lifecycle and Data Stewardship

* ECO-DATA-013 — No lifecycle governance
* ECO-DATA-015 — Shadow data stores outside governance

## What Empowered Looks Like

* Efficiency is embedded in design review
* Budgets exist before scaling
* Waste prevention is policy, not suggestion
* Systems degrade gracefully by design
* Decommissioning is routine, not exceptional

Empowered organizations do not chase inefficiency.
They design boundaries that prevent it.

---

# Structural Insight

The Eco Rules are the objective layer.
The SITM progression is the adoption layer.

The same rule may appear at multiple stages, but its meaning changes:

* At Aware, it is a code smell.
* At Conscious, it is a propagation risk.
* At Enabled, it is an intervention opportunity.
* At Empowered, it becomes a design constraint.

---

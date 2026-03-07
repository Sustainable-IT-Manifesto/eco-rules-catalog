# Rule completeness checklist


## Minimal completeness (for acceptance)

* [ ] `id` present and unique
* [ ] `title` is short and concrete (≤ 80 chars)
* [ ] `summary` explains the inefficiency in plain language
* [ ] `family`, `layer`, `tier`, `severity` set
* [ ] at least **one** of: `impact`, `detection`, `remediation` present

## Strong completeness (recommended)

* [ ] `rationale` explains “why this matters”
* [ ] `impact` lists impacted resources (CPU/memory/network/storage/latency/cost/energy/dev-time)
* [ ] `detection` includes method + what triggers it
* [ ] `remediation` includes smallest safe fix + tradeoffs
* [ ] `tags` for searchability (mechanism + resource + layer)
* [ ] example exists: `examples/<RULE_ID>.md` with **Bad** + **Better**
* [ ] false-positive notes (what not to flag)
* [ ] safe autofix guidance (if applicable)
* [ ] references (optional but strong)

## “Release readiness” (for stable versions)

* [ ] detection criteria is testable (unit tests or fixture patterns)
* [ ] severity is consistent with rubric
* [ ] rule maps cleanly into ontology (resource/mechanism/layer/detection/remediation)
* [ ] backwards compatibility plan if rule semantics changed



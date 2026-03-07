### Neo4j property graph schema

**Node labels**

* `Rule`
* `ResourceImpact`
* `Mechanism`
* `SystemLayer`
* `DetectionMethod`
* `RemediationPattern`
* optional: `Family`, `Tag`

**Relationships**

* `(Rule)-[:AFFECTS]->(ResourceImpact)`
* `(Rule)-[:CAUSED_BY]->(Mechanism)`
* `(Rule)-[:OCCURS_IN]->(SystemLayer)`
* `(Rule)-[:DETECTED_BY]->(DetectionMethod)`
* `(Rule)-[:CORRECTED_BY]->(RemediationPattern)`
* `(Rule)-[:IN_FAMILY]->(Family)` (optional)
* `(Rule)-[:TAGGED]->(Tag)` (optional)

**Rule node properties**

* `id` (string, unique)
* `title` (string)
* `summary` (string)
* `tier` (int)
* `severity` (string)
* `family` (string) — or relationship to `Family`
* `layer` (string) — or relationship to `SystemLayer`

### Import shape (JSON → Neo4j)

Best practice: generate “dimension nodes” once and connect rules to them. This enables queries like:

* “show all rules affecting Network + Latency”
* “which mechanisms dominate Tier 2?”
* “what remediations address most CPU-heavy patterns?”

Example Cypher query patterns:

```cypher
// Find rules that affect Network and are detected via Static Analysis
MATCH (r:Rule)-[:AFFECTS]->(ri:ResourceImpact {name:"Network"}),
      (r)-[:DETECTED_BY]->(d:DetectionMethod {name:"Static Analysis"})
RETURN r.id, r.title, r.tier, r.severity
ORDER BY r.tier ASC, r.id ASC;
```



# Code rules

**Total rules:** 116

- [Back to catalog index](../index.md)

## Rules

### [ECO-CMP-CPP-001 — Avoidable copies of large objects](../ECO-CMP-CPP-001.md)

Passing, returning, or assigning large containers and objects by value when moves or references would avoid copying.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-002 — Heap allocation in tight loops](../ECO-CMP-CPP-002.md)

Allocating with new, make_unique, vector growth, or temporary containers repeatedly in hot loops.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-003 — Missing vector reserve before bulk insertion](../ECO-CMP-CPP-003.md)

Growing std::vector or similar containers without reserving when size is known or bounded.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-004 — Synchronous blocking on futures or async results](../ECO-CMP-CPP-004.md)

Blocking threads while waiting for asynchronous work in request or event-loop paths.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-005 — Expensive logging or stream formatting](../ECO-CMP-CPP-005.md)

Using iostream formatting, stringstream construction, or full object logging in hot paths.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-006 — Inefficient string concatenation](../ECO-CMP-CPP-006.md)

Repeated std::string concatenation without capacity planning for large outputs.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-007 — Shared pointer overuse](../ECO-CMP-CPP-007.md)

Using std::shared_ptr where unique ownership, references, or values would be sufficient.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-008 — Lock contention in hot paths](../ECO-CMP-CPP-008.md)

Holding mutexes around expensive work or high-frequency shared state updates.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-009 — Per-item remote calls](../ECO-CMP-CPP-009.md)

Making database, RPC, or HTTP calls inside loops over collections.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-CPP-010 — Template or dependency bloat in build-critical paths](../ECO-CMP-CPP-010.md)

Heavy template instantiation or broad dependencies causing excessive compile time and binary growth.

- Category: **Computation**
- Family: **C++**

### [ECO-CMP-FLASK-001 — Database query in request loop](../ECO-CMP-FLASK-001.md)

A Flask route performs repeated database queries while iterating over records.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-002 — Expensive work during app startup](../ECO-CMP-FLASK-002.md)

Flask application startup performs network calls, migrations, model loading, or large filesystem scans.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-003 — Uncached template fragment rendering](../ECO-CMP-FLASK-003.md)

Frequently rendered Flask templates recompute stable fragments on every request.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-004 — Session payload bloat](../ECO-CMP-FLASK-004.md)

Flask session data stores large objects or repeated state in client-side cookies or backing stores.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-005 — Repeated configuration lookup per request](../ECO-CMP-FLASK-005.md)

Request handlers repeatedly load configuration, secrets, or environment-dependent metadata.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-006 — Unbounded background task submission](../ECO-CMP-FLASK-006.md)

Flask endpoints enqueue background work without idempotency, rate limits, or queue bounds.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-007 — Debug logging in production request paths](../ECO-CMP-FLASK-007.md)

Flask handlers emit verbose logs or full payloads for every request.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-008 — Synchronous external calls in hot routes](../ECO-CMP-FLASK-008.md)

Flask routes synchronously call external APIs for data that could be cached or pre-fetched.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-009 — Large response serialization without pagination](../ECO-CMP-FLASK-009.md)

Flask routes serialize large result sets into JSON without pagination or field selection.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-FLASK-010 — Per-request object allocation in middleware](../ECO-CMP-FLASK-010.md)

Flask before/after request hooks allocate expensive objects or clients on every request.

- Category: **Computation**
- Family: **Flask**

### [ECO-CMP-GO-001 — Goroutine leak from missing cancellation](../ECO-CMP-GO-001.md)

Starting goroutines without a clear cancellation, timeout, or lifecycle owner.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-002 — Unbounded goroutine fan-out](../ECO-CMP-GO-002.md)

Launching one goroutine per item without concurrency limits.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-003 — Missing HTTP client timeout](../ECO-CMP-GO-003.md)

Using http.Client or default clients without explicit timeouts.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-004 — Repeated regexp compilation](../ECO-CMP-GO-004.md)

Compiling regular expressions repeatedly instead of reusing compiled patterns.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-005 — String concatenation in loops](../ECO-CMP-GO-005.md)

Building large strings with repeated + or fmt.Sprintf in loops.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-006 — Inefficient slice growth](../ECO-CMP-GO-006.md)

Appending many items without preallocating capacity when size is known or bounded.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-007 — Defers inside hot loops](../ECO-CMP-GO-007.md)

Using defer inside high-iteration loops where immediate cleanup is possible.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-008 — Per-item database or network calls](../ECO-CMP-GO-008.md)

Calling database, RPC, or HTTP clients inside loops over collections.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-009 — Excessive JSON marshal/unmarshal churn](../ECO-CMP-GO-009.md)

Repeatedly marshaling and unmarshaling the same data or using JSON as an internal handoff format.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-GO-010 — Ticker or timer leak](../ECO-CMP-GO-010.md)

Creating time.Ticker or timers without stopping them when lifecycle ends.

- Category: **Computation**
- Family: **Go**

### [ECO-CMP-JAVA-001 — Excessive object creation in hot path](../ECO-CMP-JAVA-001.md)

High allocation rates increase GC pressure and CPU cost.

- Category: **Computation**
- Family: **Java**

### [ECO-CMP-JAVA-002 — Unbounded cache growth](../ECO-CMP-JAVA-002.md)

Caches without limits grow until they become the problem.

- Category: **Computation**
- Family: **Java**

### [ECO-CMP-JAVA-004 — Reflection in hot path](../ECO-CMP-JAVA-004.md)

Reflection adds overhead and can inflate latency and CPU usage.

- Category: **Computation**
- Family: **Java**

### [ECO-CMP-JAVA-005 — N+1 ORM query pattern](../ECO-CMP-JAVA-005.md)

ORM queries inside loops multiply DB calls.

- Category: **Computation**
- Family: **Java**

### [ECO-CMP-JAVA-007 — Blocking calls in reactive pipeline](../ECO-CMP-JAVA-007.md)

Blocking in reactive code collapses concurrency and throughput.

- Category: **Computation**
- Family: **Java**

### [ECO-CMP-JAVA-008 — Excessive synchronization contention](../ECO-CMP-JAVA-008.md)

Over-synchronization creates contention and wastes CPU.

- Category: **Computation**
- Family: **Java**

### [ECO-CMP-JAVA-010 — Debug logging in production hot path](../ECO-CMP-JAVA-010.md)

Verbose logs in hot paths waste CPU and I/O.

- Category: **Computation**
- Family: **Java**

### [ECO-CMP-JOOMLA-001 — Extension query inside item loop](../ECO-CMP-JOOMLA-001.md)

A Joomla component, module, or plugin queries the database inside a loop over content items.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-002 — Plugin runs heavy logic on broad events](../ECO-CMP-JOOMLA-002.md)

A Joomla plugin performs expensive work on global events that fire across many page requests.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-003 — Template loads unbundled duplicate assets](../ECO-CMP-JOOMLA-003.md)

A Joomla template or extension loads duplicate JavaScript/CSS assets across modules.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-004 — Disabled or bypassed Joomla cache](../ECO-CMP-JOOMLA-004.md)

Extension or template code bypasses cacheable Joomla content paths for stable output.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-005 — Large media served without optimization](../ECO-CMP-JOOMLA-005.md)

Joomla templates or content fields serve oversized images or unoptimized media variants.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-006 — Manifest or update checks in request path](../ECO-CMP-JOOMLA-006.md)

Extension code performs remote update checks or manifest reads during normal page rendering.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-007 — Unbounded module rendering on every page](../ECO-CMP-JOOMLA-007.md)

Modules render expensive queries or transformations site-wide regardless of page context.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-008 — Verbose payload logging in extensions](../ECO-CMP-JOOMLA-008.md)

Joomla extensions log request bodies, query results, or debug details in production.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-009 — Inefficient ACL checks repeated per item](../ECO-CMP-JOOMLA-009.md)

Extension code repeats authorization checks individually across large item lists.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JOOMLA-010 — Synchronous third-party widgets on render](../ECO-CMP-JOOMLA-010.md)

Templates or extensions block page rendering on third-party scripts or API calls.

- Category: **Computation**
- Family: **Joomla**

### [ECO-CMP-JS-001 — Synchronous filesystem calls in request path](../ECO-CMP-JS-001.md)

Sync FS calls block the event loop and reduce concurrency.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-003 — Large unoptimized bundles](../ECO-CMP-JS-003.md)

Large bundles increase transfer size, parse time, and energy use.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-004 — Memory leaks via event listeners](../ECO-CMP-JS-004.md)

Unremoved listeners retain objects and increase memory over time.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-005 — Blocking crypto in event loop](../ECO-CMP-JS-005.md)

CPU-heavy crypto blocks the event loop and inflates latency.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-008 — Excessive DOM reflow](../ECO-CMP-JS-008.md)

Layout thrashing increases CPU and drains battery.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-009 — Unbounded promise chains](../ECO-CMP-JS-009.md)

Long or recursive promise chains can leak work and increase memory usage.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-011 — Inefficient array transformations (multi-pass)](../ECO-CMP-JS-011.md)

Multiple passes over arrays increases CPU and GC overhead.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-014 — Client-side heavy computation without workers](../ECO-CMP-JS-014.md)

Heavy CPU work on main thread harms responsiveness and drains battery.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JS-015 — Recreating large objects per render](../ECO-CMP-JS-015.md)

Allocating large objects repeatedly increases GC churn and CPU.

- Category: **Computation**
- Family: **JavaScript**

### [ECO-CMP-JSFW-001 — Component re-renders caused by unstable props](../ECO-CMP-JSFW-001.md)

React, Vue, or similar components re-render frequently because props, callbacks, or objects are recreated on every render.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-002 — Large client bundle from unused dependencies](../ECO-CMP-JSFW-002.md)

A JavaScript framework app ships large dependencies or unused code to most users.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-003 — Excessive hydration for mostly static pages](../ECO-CMP-JSFW-003.md)

Framework pages hydrate large component trees even when most content is static.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-004 — Polling loop without visibility or lifecycle controls](../ECO-CMP-JSFW-004.md)

Frontend framework code polls APIs continuously even when the tab is hidden or data is unchanged.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-005 — State store retains unbounded data](../ECO-CMP-JSFW-005.md)

Client state stores accumulate records, histories, or cache entries without eviction.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-006 — Rendering large lists without virtualization](../ECO-CMP-JSFW-006.md)

A framework app renders large lists or tables fully in the DOM.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-007 — Duplicate data fetching across components](../ECO-CMP-JSFW-007.md)

Multiple components independently fetch the same data during a single page lifecycle.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-008 — Image assets lack responsive delivery](../ECO-CMP-JSFW-008.md)

Framework pages serve large images without responsive sizes, modern formats, or lazy loading.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-009 — Route-level code split missing](../ECO-CMP-JSFW-009.md)

Single-page apps load admin, dashboard, or rarely used route code in the initial bundle.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-JSFW-010 — Expensive computed selectors run every render](../ECO-CMP-JSFW-010.md)

Framework selectors, computed values, or pipes recompute expensive transformations unnecessarily.

- Category: **Computation**
- Family: **JavaScript Frameworks**

### [ECO-CMP-PY-001 — String concatenation in loops](../ECO-CMP-PY-001.md)

Repeated string concatenation in a loop increases allocations and CPU.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-002 — Unbounded list growth](../ECO-CMP-PY-002.md)

Collections that grow without bounds increase memory pressure and GC churn.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-003 — Repeated invariant computation inside loop](../ECO-CMP-PY-003.md)

Recomputing values that do not change inside a loop wastes CPU cycles.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-004 — Blocking I/O inside async context](../ECO-CMP-PY-004.md)

Blocking calls inside async functions reduce concurrency and inflate latency.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-005 — N+1 database query pattern](../ECO-CMP-PY-005.md)

Queries executed inside iteration multiply round trips and load.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-007 — Loading entire file into memory](../ECO-CMP-PY-007.md)

Reading large files fully into memory increases peak RAM and risk of OOM.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-008 — Excessive logging in hot path](../ECO-CMP-PY-008.md)

Logging in tight loops or request hot paths adds CPU and I/O overhead.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-009 — Repeated regex compilation](../ECO-CMP-PY-009.md)

Compiling regex repeatedly wastes CPU; compile once and reuse.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-010 — Inefficient data structure choice](../ECO-CMP-PY-010.md)

Using lists for membership tests instead of sets/dicts increases CPU time.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-011 — Repeated JSON serialization cycles](../ECO-CMP-PY-011.md)

Serializing/deserializing repeatedly wastes CPU and increases latency.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-012 — CPU-bound work in request thread](../ECO-CMP-PY-012.md)

CPU-heavy work in request handlers reduces throughput and increases latency.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-013 — Inefficient pandas row iteration](../ECO-CMP-PY-013.md)

Row-wise pandas iteration is slow compared to vectorized operations.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-014 — Redundant environment variable lookups](../ECO-CMP-PY-014.md)

Repeated env lookups in hot code paths add overhead and noise.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-015 — Recreating database connections per request](../ECO-CMP-PY-015.md)

Creating DB connections per request increases latency and resource churn.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-017 — Large object retained in global scope](../ECO-CMP-PY-017.md)

Long-lived globals can cause persistent memory bloat.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-018 — Recursive algorithm without safeguards](../ECO-CMP-PY-018.md)

Recursion without depth safeguards risks overhead and runtime errors.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-019 — Excessive thread spawning](../ECO-CMP-PY-019.md)

Creating many threads increases overhead and contention.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-PY-020 — Synchronous subprocess invocation in hot path](../ECO-CMP-PY-020.md)

Blocking subprocess calls increase latency and consume resources.

- Category: **Computation**
- Family: **Python**

### [ECO-CMP-RAILS-001 — ActiveRecord N+1 query in controller or view](../ECO-CMP-RAILS-001.md)

Rails code loads associated records lazily while rendering a collection.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-002 — Callback performs heavy side effects](../ECO-CMP-RAILS-002.md)

ActiveRecord callbacks perform network calls, file work, or expensive computation during save/update flows.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-003 — View partial renders expensive helpers repeatedly](../ECO-CMP-RAILS-003.md)

Rails views call expensive helpers or render partials repeatedly across large collections.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-004 — Missing fragment cache for stable Rails content](../ECO-CMP-RAILS-004.md)

Stable page sections are recomputed for every Rails request.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-005 — Unbounded ActiveJob enqueue from request](../ECO-CMP-RAILS-005.md)

Rails requests enqueue many jobs without bounds, deduplication, or idempotency.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-006 — Inefficient count queries in hot paths](../ECO-CMP-RAILS-006.md)

Rails code uses repeated count queries or collection counting patterns in request paths.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-007 — Large serialized JSON responses](../ECO-CMP-RAILS-007.md)

Rails endpoints serialize full ActiveRecord objects or large associations without field selection.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-008 — Per-request service/client construction](../ECO-CMP-RAILS-008.md)

Rails controllers or middleware construct expensive clients or configuration objects on every request.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-009 — Verbose Rails logging in production](../ECO-CMP-RAILS-009.md)

Rails logs SQL binds, payloads, or debug details at high volume in production.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RAILS-010 — Asset pipeline ships unused JavaScript or CSS](../ECO-CMP-RAILS-010.md)

Rails asset configuration ships unused bundles or duplicate dependencies to many pages.

- Category: **Computation**
- Family: **Ruby on Rails**

### [ECO-CMP-RB-001 — String concatenation in loops](../ECO-CMP-RB-001.md)

Repeated string concatenation in a loop can create avoidable object churn and CPU overhead.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-002 — Eager materialization of large collections](../ECO-CMP-RB-002.md)

Creating large arrays with map/select before consuming results increases memory pressure and GC work.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-003 — Repeated regular expression compilation](../ECO-CMP-RB-003.md)

Compiling equivalent regular expressions repeatedly in hot paths wastes CPU and allocations.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-004 — N+1 ActiveRecord queries](../ECO-CMP-RB-004.md)

Loading associated records one row at a time amplifies database traffic and latency.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-005 — Inefficient ActiveRecord count usage](../ECO-CMP-RB-005.md)

Using count, length, or size without understanding query/materialization behavior can create unnecessary database work or memory usage.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-006 — Unbounded memoization or class-level caches](../ECO-CMP-RB-006.md)

Memoization and class-level caches without bounds can leak memory over time.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-007 — Blocking external calls inside request loops](../ECO-CMP-RB-007.md)

Making sequential HTTP/API calls inside loops increases latency, ties up workers, and amplifies downstream load.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-008 — Excessive object allocation in hot paths](../ECO-CMP-RB-008.md)

Allocating short-lived hashes, arrays, strings, or objects in tight loops increases GC pressure.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-009 — Loading full ActiveRecord objects for scalar data](../ECO-CMP-RB-009.md)

Fetching complete model objects when only IDs or scalar fields are needed wastes memory, CPU, and database bandwidth.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RB-010 — Per-record writes instead of batched operations](../ECO-CMP-RB-010.md)

Saving or updating records one at a time can create excessive database round trips and transaction overhead.

- Category: **Computation**
- Family: **Ruby**

### [ECO-CMP-RS-001 — Unnecessary clone in hot paths](../ECO-CMP-RS-001.md)

Calling clone() where borrowing, moving, or Copy semantics would avoid allocation and memory traffic.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-002 — Collecting iterators before immediate iteration](../ECO-CMP-RS-002.md)

Using collect() to materialize an intermediate Vec when the iterator could be consumed lazily.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-003 — Blocking work inside async tasks](../ECO-CMP-RS-003.md)

Running blocking file, network, CPU, or sleep operations inside async executors without isolation.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-004 — Unbounded channel growth](../ECO-CMP-RS-004.md)

Using unbounded channels where producer speed can exceed consumer capacity.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-005 — Mutex held across await](../ECO-CMP-RS-005.md)

Holding a Mutex, RwLock, or guard across an await point.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-006 — Repeated regex compilation](../ECO-CMP-RS-006.md)

Compiling regular expressions repeatedly instead of reusing compiled patterns.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-007 — Large debug formatting in production paths](../ECO-CMP-RS-007.md)

Using debug formatting or broad tracing of large structures in hot paths.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-008 — Inefficient string construction](../ECO-CMP-RS-008.md)

Repeated format! or push_str patterns that allocate avoidably while building large strings.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-009 — Per-item database or network calls](../ECO-CMP-RS-009.md)

Issuing database or HTTP calls inside collection loops instead of batching or joining.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-RS-010 — Oversized dependency feature sets](../ECO-CMP-RS-010.md)

Enabling broad crate features or default features that pull unnecessary code, build work, or runtime behavior.

- Category: **Computation**
- Family: **Rust**

### [ECO-CMP-UI-001 — Oversized frontend bundle](../ECO-CMP-UI-001.md)

A frontend ships excessive JavaScript or unused dependencies that increase transfer, parsing, and device energy cost.

- Category: **Computation**
- Family: **Frontend/UI**

### [ECO-OPS-SEC-002 — Secrets retrieval on every request](../ECO-OPS-SEC-002.md)

Application code fetches secrets from a remote secret store on each request instead of caching with rotation-aware controls.

- Category: **Operations**
- Family: **Identity & Security Efficiency**

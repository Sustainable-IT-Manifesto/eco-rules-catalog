# Networking rules

**Category code:** `NET`

**Total rules:** 15

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-NET-NET-001 — Missing HTTP caching headers](../ECO-NET-NET-001.md)

Missing cache headers causes repeated downloads and wasted work.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-002 — No gzip/brotli compression](../ECO-NET-NET-002.md)

Serving text assets without compression increases bandwidth and energy use.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-003 — Chatty microservice communication](../ECO-NET-NET-003.md)

Many small calls increase latency and cross-service overhead.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-004 — Redundant authentication calls](../ECO-NET-NET-004.md)

Repeated auth calls waste CPU and network and add latency.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-005 — Missing timeouts](../ECO-NET-NET-005.md)

Missing timeouts remove a critical reliability boundary for network calls.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-006 — No connection reuse (keep-alive disabled)](../ECO-NET-NET-006.md)

Disabling keep-alive increases handshake overhead and latency.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-007 — Excessive retry storms](../ECO-NET-NET-007.md)

Aggressive retries amplify failures and increase waste.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-008 — Over-fetching API fields](../ECO-NET-NET-008.md)

Returning unnecessary fields increases payload size and processing.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-009 — Under-fetching causing follow-up calls](../ECO-NET-NET-009.md)

Responses missing needed data cause extra round trips.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-010 — Large payloads without pagination](../ECO-NET-NET-010.md)

Large unpaginated responses increase memory and bandwidth waste.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-011 — No CDN usage for static content](../ECO-NET-NET-011.md)

Serving static content from origin increases latency and origin load.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-012 — No HTTP/2 or HTTP/3 where applicable](../ECO-NET-NET-012.md)

Older HTTP versions may reduce efficiency for multiplexed workloads.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-013 — Excessive polling intervals](../ECO-NET-NET-013.md)

Frequent polling increases load even when nothing changes.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-014 — Synchronous cross-region calls](../ECO-NET-NET-014.md)

Cross-region synchronous calls increase latency and cost.

- Family: **NET**
- Layer: **network**

### [ECO-NET-NET-015 — Missing circuit breaker patterns](../ECO-NET-NET-015.md)

Without circuit breakers, failures propagate and waste resources.

- Family: **NET**
- Layer: **network**

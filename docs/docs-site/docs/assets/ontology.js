(async function () {
  const root = document.getElementById("eco-ontology-root");
  if (!root) return;
  const res = await fetch("../catalog/_data/catalog_index.json");
  const data = await res.json();
  const facets = data.facets || {};
  function el(tag, attrs = {}, children = []) {
    const node = document.createElement(tag);
    Object.entries(attrs).forEach(([k, v]) => {
      if (k === "class") node.className = v;
      else if (k === "html") node.innerHTML = v;
      else node.setAttribute(k, v);
    });
    children.forEach(c => node.appendChild(c));
    return node;
  }
  function section(title, facetKey, paramKey) {
    const items = facets[facetKey] || {};
    const keys = Object.keys(items).sort((a,b)=>a.localeCompare(b));
    const h = el("h2", { html: title });
    const ul = el("ul");
    keys.forEach(k => {
      const count = items[k];
      const href = `../catalog/search/?${encodeURIComponent(paramKey)}=${encodeURIComponent(k)}`;
      const a = el("a", { href });
      a.textContent = `${k} (${count})`;
      ul.appendChild(el("li", {}, [a]));
    });
    return el("div", {}, [h, ul]);
  }
  root.appendChild(el("p", { html: `<strong>Catalog version:</strong> ${data.catalog_version || "unknown"} &nbsp; | &nbsp; <strong>Total rules:</strong> ${data.rule_count || 0}` }));
  root.appendChild(section("Categories", "category", "category"));
  root.appendChild(section("Families", "family", "family"));
  root.appendChild(section("Resource Impacts", "resource_impacts", "resource"));
  root.appendChild(section("Mechanisms", "mechanisms", "mechanism"));
  root.appendChild(section("System Layers", "system_layers", "system_layer"));
  root.appendChild(section("Detection Methods", "detection_methods", "detection"));
  root.appendChild(section("Remediation Patterns", "remediation_patterns", "remediation"));
})();

(async function () {
  const root = document.getElementById("eco-search-root");
  if (!root) return;

  const dataUrl = "./_data/catalog_index.json";
  const res = await fetch(dataUrl);
  const data = await res.json();

  const rules = data.rules || [];
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

  function option(value, label) {
    const o = document.createElement("option");
    o.value = value;
    o.textContent = label;
    return o;
  }

  function mkSelect(labelText, values) {
    const select = document.createElement("select");
    select.appendChild(option("", `All ${labelText}`));
    values.forEach(v => select.appendChild(option(v, v)));
    return select;
  }

  function valuesFromFacet(name) {
    return Object.keys(facets[name] || {}).sort((a,b)=>a.localeCompare(b));
  }

  const q = el("input", { type: "search", placeholder: "Search ID, title, summary…" });
  const categorySel = mkSelect("categories", valuesFromFacet("category"));
  const familySel = mkSelect("families", valuesFromFacet("family"));
  const layerSel = mkSelect("layers", valuesFromFacet("layer"));
  const tierSel = mkSelect("tiers", valuesFromFacet("tier"));
  const sevSel = mkSelect("severities", valuesFromFacet("severity"));
  const resSel = mkSelect("resource impacts", valuesFromFacet("resource_impacts"));
  const mechSel = mkSelect("mechanisms", valuesFromFacet("mechanisms"));
  const sysSel = mkSelect("system layers", valuesFromFacet("system_layers"));
  const detSel = mkSelect("detection methods", valuesFromFacet("detection_methods"));
  const remSel = mkSelect("remediation patterns", valuesFromFacet("remediation_patterns"));
  const results = el("div", {});

  const params = new URLSearchParams(window.location.search);
  function applyParam(sel, key) {
    const v = params.get(key);
    if (v) sel.value = v;
  }
  applyParam(categorySel, "category");
  applyParam(familySel, "family");
  applyParam(layerSel, "layer");
  applyParam(tierSel, "tier");
  applyParam(sevSel, "severity");
  applyParam(resSel, "resource");
  applyParam(mechSel, "mechanism");
  applyParam(sysSel, "system_layer");
  applyParam(detSel, "detection");
  applyParam(remSel, "remediation");
  const qParam = params.get("q");
  if (qParam) q.value = qParam;

  function matchesFacet(rule, sel, field, inOntologyKey) {
    if (!sel.value) return true;
    if (inOntologyKey) {
      const arr = (rule.ontology && rule.ontology[inOntologyKey]) || [];
      return arr.includes(sel.value);
    }
    return String(rule[field] ?? "") === sel.value;
  }

  function slugify(s) {
    return (s || "uncategorized").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }

  function getRuleHref(rule) {
    const cat = slugify(rule.category);
    const fam = slugify(rule.family);
    const rid = (rule.id || "UNKNOWN").replace(/[^A-Za-z0-9._-]+/g, "_");
    return `../catalog/categories/${cat}/families/${fam}/${rid}/`;
  }

  function render() {
    const text = q.value.trim().toLowerCase();
    const filtered = rules.filter(r => {
      if (text) {
        const hay = `${r.id} ${r.canonical_id || ""} ${r.title} ${r.summary}`.toLowerCase();
        if (!hay.includes(text)) return false;
      }
      if (!matchesFacet(r, categorySel, "category")) return false;
      if (!matchesFacet(r, familySel, "family")) return false;
      if (!matchesFacet(r, layerSel, "layer")) return false;
      if (tierSel.value && String(r.tier ?? "") !== tierSel.value) return false;
      if (sevSel.value && String(r.severity ?? "") !== sevSel.value) return false;
      if (!matchesFacet(r, resSel, null, "resource_impacts")) return false;
      if (!matchesFacet(r, mechSel, null, "mechanisms")) return false;
      if (!matchesFacet(r, sysSel, null, "system_layers")) return false;
      if (!matchesFacet(r, detSel, null, "detection_methods")) return false;
      if (!matchesFacet(r, remSel, null, "remediation_patterns")) return false;
      return true;
    });

    results.innerHTML = "";
    results.appendChild(el("div", { html: `<p><strong>${filtered.length}</strong> of <strong>${rules.length}</strong> rules</p>` }));
    const ul = el("ul");
    filtered.slice(0, 500).forEach(r => {
      const li = el("li");
      const a = el("a", { href: getRuleHref(r) });
      a.textContent = `${r.id} — ${r.title}`;
      li.appendChild(a);
      ul.appendChild(li);
    });
    if (filtered.length > 500) {
      results.appendChild(el("p", { html: "Showing first 500 results. Narrow your filters to see more." }));
    }
    results.appendChild(ul);
  }

  const controls = el("div", {}, [
    el("p", { html: `<strong>Catalog version:</strong> ${data.catalog_version || "unknown"} &nbsp; | &nbsp; <strong>Total rules:</strong> ${data.rule_count || rules.length}` }),
    q,
    el("div", { html: "<br/>" }),
    categorySel, familySel, layerSel, tierSel, sevSel,
    el("div", { html: "<br/>" }),
    resSel, mechSel, sysSel, detSel, remSel
  ]);
  [q, categorySel, familySel, layerSel, tierSel, sevSel, resSel, mechSel, sysSel, detSel, remSel].forEach(x => {
    x.style.marginRight = "8px";
    x.style.marginBottom = "8px";
  });
  q.style.minWidth = "320px";
  root.appendChild(controls);
  root.appendChild(results);
  [q, categorySel, familySel, layerSel, tierSel, sevSel, resSel, mechSel, sysSel, detSel, remSel].forEach(x => {
    x.addEventListener("input", render);
    x.addEventListener("change", render);
  });
  render();
})();

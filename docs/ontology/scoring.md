**Score components**

1. **Resource breadth**: how many resources affected
2. **Propagation / Tier**: how likely it amplifies at scale
3. **Severity**: operational seriousness
4. **Confidence**: confidence of detection or impact claim
5. **Fix effort**: how hard it is to remediate safely (optional)

### Suggested score formula

Let:

* `R` = number of impacted resource categories (1–8)
* `T` = tier (1–4)
* `S` = severity weight: `{note:0.5, low:1, medium:2, high:3, critical:4}` (tune as you like)
* `C` = confidence (0.0–1.0), default 0.6 if unknown
* `E` = effort weight (1–3), default 2 if unknown (1 easy, 2 moderate, 3 hard)

Then:

**ImpactScore (0–100)**

```
base = (10 * R) + (12 * (T - 1)) + (8 * S)
adjusted = base * (0.6 + 0.4*C)
final = adjusted * (1.1 - 0.1*E)
clamp to 0..100
```

Why this works:

* Tier matters a lot (amplification)
* Breadth matters (multi-resource waste is more systemic)
* Confidence prevents low-quality signals from dominating
* Effort gently penalizes “hard fixes” so roadmaps balance wins vs rewrites

### Example interpretation buckets

* 0–25: opportunistic cleanup
* 26–50: backlog priority
* 51–75: plan and track
* 76–100: needs architectural attention



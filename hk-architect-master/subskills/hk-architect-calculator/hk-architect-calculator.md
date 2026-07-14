---
name: hk-architect-calculator
description: HK architect calculators — GFA/PR (BO + PNAP APP-2), OTTV/RTTV, MOE exit width/travel distance (FS Code 2011), occupant load (BO/FS Code), all metric, HK codes only.
disable-model-invocation: true
---

# HK Architect Calculator

All calculations use metric units and HK codes. No imperial equivalents.

For **run_hk_calculator egress or GFA roll-up**, use `hk-architect-calculator`. For other topics, see the routing table below.

## When to Use This Skill

Quantitative checks: GFA/PR, OTTV/RTTV formulas, MOE widths, occupant load, dispatcher JSON.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| run_hk_calculator egress or GFA roll-up | `hk-architect-calculator` | `—` |
| PNAP exemption interpretation | `—` | `hk-building-codes` |
| Full fire strategy narrative | `—` | `hk-fire-life-safety` |

## Halt criteria

- Calculator output is preliminary — not statutory sign-off.
---

## 1. GFA & Plot Ratio Calculator

```
Permissible GFA = Site Area (m²) × Plot Ratio (from OZP)

Domestic GFA used = Σ floor areas (domestic use) — GFA exemptions
Non-domestic GFA used = Σ floor areas (non-domestic use) — GFA exemptions

Check: Domestic GFA used ≤ Site Area × Domestic PR
       Non-domestic GFA used ≤ Site Area × Non-domestic PR
```

### PNAP APP-2 Exemption Deductions

| Item | Deduct from GFA | Cap |
|---|---|---|
| Balcony | Actual area | ≤ 2 m depth; aggregate ≤ 1/2 unit facade width |
| Bay window | Actual area | ≤ 0.5 m projection; ≤ 50% facade width per floor |
| Utility platform | Actual area | ≤ 1.5 m × 2.0 m per unit |
| Plant room / lift overrun | Full area | Must not breach BHR |

---

## 2. OTTV Calculator

```
OTTV (W/m²) = [Uw × (1-WWR) × TDeq] + [Uf × WWR × ΔT] + [SC × WWR × SF]

Where (typical HK CZ 1A values):
  TDeq = 14°C (equivalent temperature difference, opaque wall)
  ΔT   = 6°C (indoor–outdoor mean temperature difference)
  SF   = 150–180 W/m² (E/W); 80–110 W/m² (N/S)

Target: OTTV ≤ 20 W/m² (BEAM Plus); ≤ 35 W/m² (BEC baseline)
```

---

## 3. RTTV Calculator

```
RTTV (W/m²) = [Ur × (1-RWR) × TDeq_roof] + [SC_skylight × RWR × SF_roof]

Where:
  TDeq_roof = 25°C (flat roof, CZ 1A)
  SF_roof   = 200 W/m² (horizontal surface, HK)

Target: RTTV ≤ 25 W/m² (BEAM Plus); ≤ 35 W/m² (BEC baseline)
```

---

## 4. Occupant Load (BO / FS Code 2011)

| Use | Occupant Load Factor |
|---|---|
| Office | 1 person per 10 m² GFA |
| Retail (ground floor) | 1 person per 3 m² GFA |
| Retail (upper floors) | 1 person per 5 m² GFA |
| Restaurant / dining | 1 person per 1.5 m² GFA |
| Assembly (fixed seats) | 1 person per seat |
| Assembly (no fixed seats) | 1 person per 0.65 m² GFA |
| Residential | 1 person per bedroom (min 2 per unit) |
| Car park | 1 person per 30 m² GFA |

---

## 5. Means of Escape Calculator (BO Reg. 41 + FS Code)

```
Required exit width (mm) = 
  ≤ 50 persons:   750 mm
  51–200 persons: 1050 mm
  > 200 persons:  1050 + (persons − 200) / 50 × 150 mm

Max travel distance:
  Residential (sprinklered):     45 m
  Residential (unsprinklered):   30 m
  Non-domestic (sprinklered):    60 m
  Non-domestic (unsprinklered):  45 m
```

---

## 6. Daylight Factor (Quick Estimate)

```
DF (%) ≈ (Window area × Tf × θ) / (Floor area × (1 − R²))

Where:
  Tf = glass transmittance (typically 0.6–0.75)
  θ  = angle of visible sky (degrees) / 180
  R  = average room surface reflectance (typically 0.4–0.5)

Note: Use simulation (Radiance/Dialux) for HK urban canyon sites.
```

---

## 7. Dispatcher calculators (`run_hk_calculator`)

Markdown formulas above are for reasoning; numeric checks use `main.py`:

| `calc_type` | Input `data` | Output |
|---|---|---|
| `egress_1004_7` | `{"length": m, "width": m, "sprinklered": bool}` | Diagonal vs FS Code travel-distance limit (simplified room only) |
| `gfa_aggregator` | `{"floors": [{"area": float, "is_exempt": bool}, ...]}` or a list of floor dicts | `total_gfa`, `exempt_gfa`, `accountable_gfa` |
| `layout_sort` | `{"items": [{"x": n, "y": n}, ...]}` or a list of items | Items sorted top-to-bottom, left-to-right |

OTTV, RTTV, occupant load, and daylight factor are **not** implemented in `core/calculators.py` — apply the formulas in this skill manually or via external tools.

---

*Sources: Buildings Ordinance Cap. 123, PNAP APP-2, FS Code 2011, BEAM Plus NB v2.0, EMSD BEC 2021, ASHRAE 90.1-2022 (CZ 1A).*
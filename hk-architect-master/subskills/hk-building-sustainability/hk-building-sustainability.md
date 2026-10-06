---
name: hk-building-sustainability
description: BEAM Plus (NB, EB, Interiors, Neighbourhood), OTTV/RTTV, HK energy codes, green building credits, and subtropical climate performance strategies for Hong Kong.
disable-model-invocation: true
---

# HK Building Sustainability

Covers BEAM Plus rating system, OTTV/RTTV compliance, energy codes, and climate-responsive design for Hong Kong (ASHRAE CZ 1A — hot-humid subtropical).

For **BEAM Plus / energy performance strategy**, use `hk-building-sustainability`. For other topics, see the routing table below.

## When to Use This Skill

BEAM Plus, OTTV/RTTV, greenery, EIA interfaces, green building credits. Sustainable Building Design quantitative rules (building separation, setback, site coverage of greenery) are PNAP APP-152.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| BEAM Plus / energy performance strategy | `hk-building-sustainability` | `—` |
| Daylight factor / Reg. 30 | `—` | `hk-daylighting-design` |
| Facade U-value detail only | `—` | `hk-building-envelope` |
---

## 1. BEAM Plus Overview

| Scheme | Scope | Certifier |
|---|---|---|
| NB (New Buildings) v2.0 | New construction; Provisional → Final | HKGBC |
| EB (Existing Buildings) v2.0 | In-use buildings | HKGBC |
| Interiors (older v1.0 label) | Use the non-residential v2.0 or residential tool in the rows below for a current fit-out | HKGBC |
| Neighbourhood | Master plan / district scale. A Neighbourhood certificate is not a New Buildings certificate; reassess under NB when the project moves from planning to building design | HKGBC |
| Data Centres (NDC / EDC) | Data-centre area at least 500 m², and data halls plus related plant a significant majority of floor area. New construction or major alteration uses NDC; operations use EDC | HKGBC |
| Existing Schools | Existing primary and secondary schools only, after at least one school calendar year of operational data. Not a generic existing-buildings scorecard | HKGBC |
| Interiors, non-residential v2.0 | Completed fit-out of offices, retail, restaurants, clubhouses, and other non-residential premises. Not whole-building NB or EB | HKGBC |
| Interiors, residential | Completed home fit-out. Item-count tool (Green at 30 items, Green+ at 45). Do not import the non-residential Platinum point table | HKGBC |
| Existing Buildings, global v1.0 | Existing buildings **outside Hong Kong**. Do not apply local EB v2.0 energy, water, or indoor-air baselines. The brochure has no rating table | HKGBC |

### 1.1 BEAM Plus NB Credit Categories

| Category | Max Points | Key Credits |
|---|---|---|
| Site Aspects (SA) | 30 | AVA, greenery, permeable paving, heritage |
| Materials Aspects (MA) | 20 | Recycled content, FSC timber, low-VOC |
| Energy Use (EU) | 35 | OTTV, RTTV, lighting power density, renewables |
| Water Use (WU) | 20 | Low-flow fixtures, rainwater harvesting, greywater |
| Indoor Environmental Quality (IEQ) | 30 | Natural ventilation, daylighting, acoustic, IAQ |
| Innovations & Additions (IA) | 10 | Pilot credits, exemplary performance |

### 1.2 Rating Levels

| Level | Points Required |
|---|---|
| Bronze | 40 |
| Silver | 55 |
| Gold | 65 |
| Platinum | 75 |

---

## 2. OTTV & RTTV

### 2.1 Overall Thermal Transfer Value (OTTV)

```
OTTV = Σ [Uw × (1 - WWR) × TDeq] + Σ [Uf × WWR × ΔT] + Σ [SC × WWR × SF]
```

| Parameter | Typical HK Value |
|---|---|
| Target OTTV (non-domestic) | ≤ 20 W/m² (BEAM Plus EU credit) |
| Baseline OTTV (code minimum) | ≤ 35 W/m² (EMSD BEC) |
| Solar factor (SF), E/W facade | ~150–180 W/m² |
| Shading coefficient (SC) target | ≤ 0.25 (high-performance glass) |

### 2.2 Roof Thermal Transfer Value (RTTV)

- Target: ≤ 25 W/m² (BEAM Plus); ≤ 35 W/m² (BEC baseline)
- Strategies: reflective coating (SRI ≥ 78), green roof, insulation (R ≥ 2.0 m²K/W)

---

## 3. Climate-Responsive Strategies (CZ 1A)

| Strategy | Application | Priority |
|---|---|---|
| External shading (E/W) | Horizontal fins, deep reveals, brise-soleil | High |
| High-performance glazing | Low-e, SHGC ≤ 0.25 for E/W; ≤ 0.35 for N/S | High |
| Natural cross-ventilation | Dual-aspect units; operable windows; stack effect | High |
| Green/reflective roof | Reduce RTTV; mitigate urban heat island | Medium |
| Rainwater harvesting | Irrigation, toilet flushing; HK annual rainfall ~2400 mm | Medium |
| PV panels | Roof + south facade; limited by typhoon wind loads | Medium |
| Thermal mass | Less critical in CZ 1A; focus on shading over mass | Low |

---

## 4. Energy Code (EMSD BEC) and Cap. 610

- **Building Energy Code (BEC)** administered by EMSD. Numerical standards sit in the code issued under the Buildings Energy Efficiency Ordinance, not in the Ordinance text.
- **Cap. 610** applies to prescribed buildings. Residential flats themselves are not a prescribed building; their common areas are. Classify every portion (commercial, residential common area, industrial, hotel, data centre) and confirm the main-switch approved loading and the Schedule 2 carve-outs before treating the project as fully inside the Ordinance.
- Stage-one declaration is due **two months after superstructure consent**. Freeze building-services design to the Gazette code in force for that consent, and name that edition in the declaration.
- The stage-one declaration, stage-two declaration, Form of Compliance, and energy audit must be certified by a **registered energy assessor** who is registered on the day of the act (Cap. 610B). Stage two carries the fee in Cap. 610A; stage one is not a fee item in that Schedule.
- The first Certificate of Compliance Registration is the maintenance baseline for central plant and for unit installations the developer provides.
- A later Form of Compliance clock (two months) starts for a fit-out of **500 m²** or more, a new **400 A** circuit, a chiller or unitary air-conditioner at or above **350 kW**, or a lift or escalator drive replacement.
- An Energy Audit Form is displayed at a conspicuous main-entrance position. Central plant of a Schedule 4 building above **7,000 m²**, and every data centre regardless of that floor-area relief, is on a **5-year** audit cycle once the relevant date has passed.
- BEAM Plus energy credits require performance above the BEC baseline. They do not replace Cap. 610.

### 4.1 Statutory OTTV under Cap. 123M

Cap. 123M requires a suitable overall thermal transfer value for the external walls and roofs of commercial buildings and hotels. The regulation does not print the W/m² caps. APP-67 (as amended September 2025) sets them, for new building plans or major revisions submitted **on or after 31 December 2025**:

| Envelope zone | Cap |
|---|---|
| Building tower | ≤ 20 W/m² (previous 21 W/m²) |
| Podium | ≤ 40 W/m² (previous 50 W/m²) |

Basement perimeter walls are not external walls for Cap. 123M. Where site coverage steps under PNAP APP-132, the notional podium for the calculation may be taken as 20 m above mean street level, or at a lower demarcation. Consent needs an OTTV summary sheet; occupation permit needs the full OTTV report and glass shading coefficients on the record plans. A residential recreational facility is controlled like commercial or hotel under APP-156 (same 20 / 40 caps); that path is not Cap. 123M.

### 4.2 Environmental Impact Assessment Ordinance (Cap. 499)

Screen the brief against Schedules 2 and 3 before massing. Splitting one scheme into contiguous pieces that each sit under a threshold can still be specified as one designated project. Do not start construction, operation, or decommissioning of a Schedule 2 designated project without an environmental permit, and do not depart from permit conditions on layout, method, or mitigation. A material change of layout, alignment, throughput, or mitigation after the permit is a fresh assessment problem. The Technical Memorandum on the Environmental Impact Assessment Process is the content specification the Director must follow.

Design locks that most often catch a building or site brief include the road class in Schedule 2 item A.1, the 100 m depot and cavern setbacks, the 5 ha and 1 ha reclamation tests and the dredging distances, sewage capacity and the 200 m sewage setback, a 400 kV substation, industrial-estate and batching-plant thresholds, a 20 ha theme park, a 10,000-person outdoor venue, and Deep Bay Buffer Zone residential or recreational development.

---

## 5. BEAM Plus Design Integration by Stage

| Stage | Action |
|---|---|
| Feasibility | Appoint BEAM Pro; select target level; map SA credits (site, AVA) |
| Concept | Fix orientation, shading strategy, OTTV target; confirm NV feasibility |
| Scheme | Specify glazing SC/U-values; size PV/rainwater systems; confirm IEQ strategy |
| Detail | Low-VOC specs, FSC timber, recycled content schedules |
| Construction | Commissioning plan; IAQ testing protocol |
| Occupation | Final BEAM Plus submission; post-occupancy monitoring |

---

*Sources: BEAM Plus NB v2.0, EB v2.0, EB Global v1.0, Data Centres, Existing Schools, Interiors (non-residential v2.0 and residential), and Neighbourhood brochures (HKGBC); Cap. 123M; PNAP APP-67 (September 2025 amendment); Buildings Energy Efficiency Ordinance Cap. 610 (20 September 2026) and Cap. 610A / 610B; Environmental Impact Assessment Ordinance Cap. 499 (11 April 2025) and its Technical Memorandum; EMSD Building Energy Code; ASHRAE 90.1-2022 (CZ 1A).*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-building-sustainability.md`. The master router links these files directly.

# Code of Practice for Foundations 2017
**Architect critical summary for schematic design**  
First issue April 2017 | Buildings Department  
Consolidated **2024 Edition** (October 2024) | Further amendments: **September 2025** (PNAP APP-18 Appendix A)

> Scope note: Deemed-to-satisfy guidance for **foundation design, site investigation, construction and testing** under the Buildings Ordinance / Building (Construction) Regulations. Departure from this Code (or use of other codes) requires demonstration of B(C)R compliance. **Seismic design is not included** — but if the superstructure is designed for seismic, foundations must be too. RSE / RGE own calculations; AP must lock **foundation typology, basement vs suspended G/F, reclaim / NSF, Scheduled / Designated Area constraints, and neighbour risk** at SD. Cross-check Dead & Imposed Loads Code, Wind Code, SUC / SUOS, GEO Guides 1–3 / TGN 12 & 26, Port Works Design Manual, PNAP (Scheduled Areas, Designated Area, APP-18 / APP-24 / APP-72 / APP-134), CoP Site Supervision + Technical Memorandum for Supervision Plans.

---

## Regulatory Overview

This Code covers **design and construction of foundations for buildings and structures in Hong Kong** using currently accepted local methods: shallow footings / strips / rafts, driven and bored piles (including socketed H, mini-piles, barrettes, CFA), basements / hollow boxes, diaphragm walls, retaining walls used as foundations, ground anchors, and **re-use of existing foundations** — plus site investigation, settlement, buoyancy, corrosion, neighbour effects, and testing.

At schematic design, lock **geology flags (reclaim / marble / Scheduled / Designated / slope / railway / nullah)**, **shallow vs piled vs basement box**, **G/F suspended vs on-grade**, and **vibration method vs neighbours** — these drive massing, pile-cap / transfer thickness, ELS programme, cost contingency and neighbour liability before GBP is frozen.

---

## Critical main topics and subtopics

### 1. Scope boundaries & roles (§1.1–1.2)

| Point | SD implication |
|---|---|
| Deemed-to-satisfy B(C)R foundations | Still need RSE/RGE calculations + BA approval |
| Methods based on local practice / experience are accepted when proven | Novel systems → trial piles + justification early |
| Seismic **not** in this Code | If tower is seismic-designed → foundation must follow |
| **Dry** GW (shallow): highest anticipated GW ≥ **1 m or footing width** (greater) below base | Affects dry vs submerged presumed values |
| **Submerged**: design GW at or above foundation base | Halves many granular presumed bearings |
| **Designated Area** | Northshore Lantau — GEO TGN 12 / PNAP APP-134 |
| **NSF** | Downdrag from consolidating strata — design load, not capacity |
| **Permanent vs transient tension** | Soil / GW uplift = permanent; wind = transient (different bond values) |
| **Minor / temporary structures** | MWCS items, walkways, disabled ramps, hoardings, pavilions, pergolas, kiosks — relaxed presumed bearing allowed |
| **Proof test** | B(C)R reg. 30 — representative units under load |
| **RSC (Foundation Works)** | Required if penetration **> 3 m** |
| **RSC (GI Field Works)** | All GI field works (except field density) |

---

### 2. Design aims that constrain SD (§2.1)

| Aim | SD implication |
|---|---|
| Safely carry dead + imposed + wind without impairing stability of the building **or** adjacent buildings, streets, land, slopes, services | Commission **≥50 m** neighbour survey early |
| Allowable capacity = lesser of (a) ultimate ÷ FoS, or (b) capacity limited by **tolerable movement** | Settlement often governs over “presumed rock” |
| Allowable capacity may increase **25%** when increase is **solely due to wind** | Do not bank this for gravity cases |
| Typical FoS on ultimate bearing ≈ **3** (may vary with reliability / geology) | Dissolution features, jointing, rock slip → higher caution |
| Design method, GI, parameters, construction and acceptance must be **mutually compatible** | Do not claim Cat. 1(a) without 5 m TCR proof |
| Inclined rock profile | Check joints — presumed values assume **no slip** |

**SD takeaway:** Foundation choice is a **site + neighbour + geology** problem first; structural calculation second.

---

### 3. Presumed bearing — early sizing tables (§2.2.2, Tables 2.1–2.2)

Use only if GI follows Ch.3 **and** structure is **not unduly settlement-sensitive**. Values are for **horizontal ground** with **negligible lateral load** at bearing level. Lateral rock bearing ≈ **1/3** vertical if no adverse joints. Self-weight of pile embedded in soil/rock **need not** be included in bearing stress. Intermediate dry/submerged → linear interpolation.

#### 3.1 Rock / intermediate (granite & volcanic unless noted)

| Category | Stratum (short) | Presumed qa (kPa) | Min. rock socket (piles) |
|---|---|---|---|
| **1(a)** | Fresh–slightly decomp. strong–very strong, grade II+, **100% TCR**, UCS ≥75 MPa (PLI₅₀ ≥3) | **10 000** | **500 mm** |
| **1(b)** | Fresh–slightly, grade II+, ≥**95% TCR**, UCS ≥50 MPa (PLI₅₀ ≥2) | **7 500** | **500 mm** |
| **1(c)** | Slightly–moderately, grade III+, ≥**85% TCR**, UCS ≥25 MPa (PLI₅₀ ≥1) | **5 000** | **300 mm** |
| **1(d)** | Moderately decomp., grade III+, ≥**50% TCR** | **3 000** | **300 mm** |
| **2** | Meta-sedimentary (grade III+, ≥85% TCR) — **excludes marble** | **3 000** | **300 mm** |
| **3** | CDG/CDV intermediate, SPT N ≥**200** | **1 000** | — |

**TCR rules that kill optimistic rock claims (Notes to Table 2.1 + Fig. 2.1):**

- Prove designated-grade TCR for **≥5 m** below founding (consecutive 1 m segments each meeting TCR %).
- No rock core within **600 mm** of pile base logged “non-intact” (GEOGUIDE 3).
- Max continuous inferior / washed length in TCR definition **≤300 mm**.
- Min. socket contribution itself is **ignored** when calculating bond resistance on non-driven piles.
- Presumed values **do not waive** settlement consideration.

#### 3.2 Soil — non-cohesive (dry / submerged)

| Density | SPT N | Dry (kPa) | Submerged (kPa) |
|---|---|---|---|
| Very dense | >50 | **500** | **250** |
| Dense | 30–50 | **300** | **150** |
| Medium dense | 10–30 | **100** | **50** |
| Loose | 4–10 | **<100** | **<50** |

#### 3.3 Soil — cohesive

| Consistency | Undrained strength | qa (kPa) |
|---|---|---|
| Very stiff / hard | >150 kPa | **300** |
| Stiff | 75–150 kPa | **150** |
| Firm | 40–75 kPa | **80** |

Minor/temporary footings on flat granular: **100 kPa dry / 50 kPa submerged**.

#### 3.4 Rock–concrete/grout bond (piles, Table 2.2) — concrete/grout ≥**30 MPa**

| Rock | Compression / transient tension | Permanent tension |
|---|---|---|
| 1(c) or better | **700** kPa | **350** kPa |
| 1(d) or 2 | **300** kPa | **150** kPa |

#### 3.5 Other capacity methods (§2.2.1, 2.2.3–2.2.5)

| Method | Architect note |
|---|---|
| Rational design | FoS usually **3**; may vary with variability / reliability |
| In-situ load testing | Scale effect, duration vs working life, founding variation |
| Bearing-capacity equation (shallow on soil) | FoS ≥**3**; qu capped (see §4 / 2025 amend for basements) |
| Other methods | Allowed if suitability demonstrated |

**Slope near crest (§2.2.4 Note 4):** interpolate ultimate capacity between edge of slope and **4 × footing width** from crest; also check overall slope stability.

**Irregular footing:** design on **largest inscribed rectangle**.

---

### 4. Settlement & rotation — criteria that freeze the structural system (§2.3)

#### 4.1 What must be predicted

Immediate + primary consolidation + secondary consolidation, from proper GI, Hong Kong–applicable methods, and case-history conformity. Fine-grained soils: oedometer CR / RR / Cα; secondary starts at **~95%** primary consolidation.

#### 4.2 Young’s modulus & Poisson (§2.3.1 + 2025 amend.)

| Case | Es (MPa) shortcut (absent better data) |
|---|---|
| Shallow foundations, granular | **1 × SPT N** |
| **Raft** on saprolite / residual from in-situ weathering with **N > 30** (2025) | **1.5 × SPT N** |
| Poisson non-cohesive | N 4–10 → 0.30–0.40; N 11–30 → 0.20–0.35; N >30 → 0.15–0.30 |
| Poisson cohesive | 0.1–0.3 |

Plate load tests may be required to verify Es (see §4 / §8.2).

#### 4.3 Reference movement criteria (§2.3.2) — non-sensitive buildings

Evaluate at base of shallow foundation / pile-cap base / **equivalent raft** for driven piles:

| Criterion | Limit (working loads) |
|---|---|
| Max **total settlement** | **≤ 30 mm** |
| **Differential** between columns / verticals | **≤ 1:500** |
| Max **angular rotation** under wind / transient | **≤ 1:500** |

For (a)+(b): dead may be taken at **50%**; imposed reductions per Dead & Imposed Loads Code.

**Deemed to satisfy total-settlement criterion:** foundation on Cat. **1(a)–1(d) or 2** rock, **or** driven to sound bearing with SPT N **≥ 200**.

**Must check differential settlement when:** mixed foundation systems; piles with large length differences; substantial variation in compressible strata.

**Exceeding reference criteria:** only with assessment that building, neighbours, services and connections remain OK for strength + serviceability.

**SD:** Mixed pad + pile, short + long piles, old + new → budget joints / stronger transfer from concept — do not “average” into one system late.

---

### 5. Reclaimed land — G/F typology rules (§2.4) — lock at SD

Reclamation ⇒ long-term consolidation of compressible material. Affects slabs, partitions, fence walls, ancillary structures, utilities and drainage.

| Element | Rule |
|---|---|
| Lowest floor slabs | **Not on-grade** unless exception |
| Slabs above **raft-type pile cap** | May be on-grade |
| Fence walls, landscaping, lightweight covered walkway | On-grade OK **if readily repairable/replaceable** |
| Carpark / L&U / vehicular ramp / pedestrian pavement slabs | Same — on-grade if repairable |
| Transformer rooms, pump houses | Foundations through reclaim to firm stratum; slabs **suspended** |
| Underground utilities under building | Support on **suspended slabs or pile caps**; flexible joint at on-grade interface |
| Pile caps | Detail against soil migration into void under cap if consolidation continues |
| Piles | Assess **NSF** |

#### 5.1 Alternative approach (§2.4.2)

If not following default rules: full time–settlement curves from site-specific GI + continuous instrumentation through construction; historical reclaim data only as reference unless accuracy guaranteed (CEDD).

#### 5.2 Long-term monitoring (§2.4.3)

If design needs long-term monitoring/maintenance, **AP must alert the developer** (and advise informing prospective buyers who may bear cost).

#### 5.3 “Old reclaim” exemption (§2.4.4)

May ignore consolidation if ≥**95% primary consolidation** complete — indicative years **without** detailed assessment (and **not** where new site formation / extensive high-pressure shallow foundations will re-consolidate):

| Aggregate clay thickness H (no sand/silt interbeds) | Years after reclaim |
|---|---|
| H ≤ 5 m | **10** |
| 5 < H ≤ 10 m | **20** |
| 10 < H ≤ 15 m | **30** |

**SD decision tree:**

```
Site on reclaim / marine clay?
  → Default: piled + suspended G/F + NSF
  → On-grade only for replaceable light uses or raft pile-cap decks
  → Plant rooms / transformers: never on-grade on consolidating fill
  → Old reclaim: only if 95% consolidation proven / age table applies
```

---

### 6. Loads, groundwater, sliding / uplift / overturning (§2.5)

#### 6.1 Design loads (§2.5.2)

Dead / imposed / wind per Dead & Imposed Loads Code + Wind Code. Imposed includes **buoyancy** and **earth pressure**. If foundations designed on **assumed loads**, prepare a schedule and **before superstructure construction** prove calculated loads ≤ assumed.

#### 6.2 Groundwater definitions (§2.5.3)

| Level | Meaning |
|---|---|
| **Highest anticipated** | Reliable data covering ≥ **one wet season**; tides, storm surge, rainfall, runoff, dewatering, long-term sea-level rise, permeability, tidal damping |
| **Highest possible** | Extreme events (flood, main burst); absent data → generally **ground surface** (reclamation may rise **above** G.L.) |

#### 6.3 Resistance factors (§2.5.4)

| Basis | Sliding | Uplift | Overturning |
|---|---|---|---|
| Highest **anticipated** GW | ≥ **1.5 ×** all | ≥ **1.5 ×** all | Wind **1.5×**; GW **1.5×**; other **2×** |
| Highest **possible** GW | **1.1×** GW + **1.5×** other | **1.1×** GW + **1.5×** other | Wind **1.5×**; GW **1.1×**; other **2×** |

Resistance uses **minimum dead load** only: structure + permanent finishes + permanent backfill (**ignore removable** finishes/fill). Accidental / landslide debris → GEO TGN 42. Marine → also Port Works Design Manual.

**SD:** Deep basement + high water → early hold-down piles / thicker raft / **temporary construction buoyancy** check before tower weight exists.

#### 6.4 Materials & stresses (§2.5.5)

| Item | Rule |
|---|---|
| Permissible stress method | Working stress **+25%** for wind-only increase |
| Cast-in-place with GW / underwater | Design strength **−20%** |
| Driven precast concrete axial | ≤ **0.2 fcu** |
| Marine concrete (general guide §2.6.4) | ≥ **C45**, w/c ≤0.38, silica fume 5–10%, cementitious 380–450 kg/m³, cover **75 mm**, crack ≤0.1 mm tidal/splash (×1.25 for flexural control design) |
| Underwater marine concrete for design | Treat as **C25** |
| Driven steel piles (FoS 2 on driving) | Axial ≤ **30% fy** |
| Pre-bored / jacked steel piles | Axial ≤ **50% fy** |
| Steel–grout bond (≥30 MPa grout) | **400** kPa (320 underwater); with shear studs ≤ **600** / 480 kPa |
| Steel surface for bond | Clean — no loose mill scale / rust / bond-reducing substances |

---

### 7. Corrosion protection (§2.6)

Provide protection **or** design for corrosion over working life. Need corrosive-agent info + GW fluctuation range.

| Condition | Action |
|---|---|
| Sulphate / chloride / aggressive chemicals | Protect concrete / steel |
| Alkali + high moisture | Reactive alkali ≤ **3.0 kg/m³** Na₂Oeq |
| Landfill site | Corrosion provisions on plans |
| Abrasion | Protect |
| Steel in splash / tidal / contact with other metals / stray current | Protect |
| Marine steel above seabed | Full protection for design life |
| Marine steel below seabed (no protection) | Allow **0.05 mm/year** loss on outside face |
| Stainless in marine | Must be **chloride-free** grade — common chloride-bearing grades **not** for marine |
| Steel in concrete + steel in seawater | **Isolate** (galvanic couple) |

---

### 8. What must appear on foundation plans (§2.7)

**Plan content (selection AP should expect):** block plan; site features + GI holes + neighbours + utilities + slopes + nullahs; layout, IDs, expected depths / founding levels, materials; for piles — size, cut-off, shoe, head, splices, pile–cap connection; pile-cap layout; bearing capacity + site verification method; characteristic D/L/W and critical combinations (**per pile or group**); installation / founding criteria; verticality / inclination control; **max concurrent piling rigs** on vibration-sensitive sites; obstruction method; dynamic formula parameters if used; precautionary / monitoring / contingency proposals.

**Supporting docs:** GI report (photos of samples/cores); calculations; neighbour effects assessment; **PR Plan** if vibration or ground movement expected.

---

### 9. Scheduled Areas & Designated Area (§2.8–2.9, §3.5–3.6, §7.8)

#### 9.1 Five Scheduled Areas (Fifth Schedule BO)

| No. | Area | SD flag |
|---|---|---|
| 1 | Mid-levels | Slope / GI control — PNAP |
| 2 | NW New Territories | **Marble / karst** |
| 3 | Railway Protection | MTR / railway PNAP |
| 4 | Ma On Shan | **Marble / karst** |
| 5 | Sewage Tunnel Protection | Tunnel clearance |

GI in Scheduled Areas: **approve GI plan** (B(A)R 8(1)(l)) + BA consent before site works. Foundation works often have extra settlement / vibration / performance-review conditions.

#### 9.2 Marble / karst (Areas 2 & 4) — layout can make or break the site

**Problem:** karstic marble upper surface — overhangs, channels, cavities (infilled or open). Stability depends on karst geometry + rock mass.

**Marble class (MQD):**

| Class | MQD | Quality | Foundation use |
|---|---|---|---|
| I | 75–100% | Very good | Good bearing |
| II | 50–75% | Good | Good bearing |
| III | 25–50% | Fair | Marginal |
| IV | 10–25% | Poor | Generally unsuitable |
| V | ≤10% | Very poor | Generally unsuitable (large continuous cavities) |

**Soil-bearing / friction foundations:** limit **increase of vertical effective stress at marble surface**:

| Site class | % area with drillhole rating ≥5 | Stress increase at marble |
|---|---|---|
| A Easy | 0–10% | Settlement in soil controls |
| B Fair | 10–25% | **5–10%** |
| C Very difficult | 25–50% | **3–5%** |
| D Extremely difficult | 50–100% | **<3%** |

**Preferred strategy:** piles bearing on marble + **suspended G/F** (reduce sinkhole risk). Installation must not create sinkholes.

**Driven piles on marble:** Class I/II; final set usually ≤**10 mm / 10 blows**; pre-bore through overhangs/roofs; **redundancy** A: 10–20%, B: 20–30%, C/D: specialist. End-bearing bored piles: rock mass in zone of influence = Class I or II.

**Marble presumed (Table 2.10, Class I/II):** **7 500** or **5 000** kPa bearing; bond 700 / 350 kPa (compression-transient / permanent). Zone of influence ≥ **3× pile base diameter**.

**After construction (Areas 2 & 4):** settlement monitoring by **qualified land surveyor** from soon after foundation completion **until OP**, ≥ monthly.

#### 9.3 Designated Area (complex geology)

May force layout change or abandonment. **Stage GI before finalising GBP**; deep holes for deep weathering. Geological input essential. Cost/programme risk is architectural as much as geotechnical.

#### 9.4 Sloping ground (§2.10, §3.3)

Flag if average gradient across site / 50 m strip **>15°**, or slope **>15°** within site or within **50 m** of boundary. Foundations imposing load on slopes/RWs, or changing GW regime → stability check as part of foundation design. **No building over main arterial stormwater nullah.** Disused tunnels may restrict foundation design (CEDD GIU records).

---

### 10. Site investigation — commission before SD freezes (§3)

| Item | Critical practice |
|---|---|
| Documentary study | CEDD GIU first; **verify** old project GI before use |
| Topographical | Slopes >15° on site / within 50 m |
| Geological / ground model | Weathering profiles, GW, lateral slope loads, uncertainty zones; update during construction |
| Structures survey | Pre-war buildings, party walls, appendages; photo defect survey; trial pit / drill existing foundations if records missing |
| Disused tunnels / culverts / nullahs / anchors / soil nails | Identify within & nearby |
| Utilities | Water, sewage tunnels, electricity, gas, drainage, telecom — verify on site; ETWB water-carrying services CoP for slopes |
| Rockhead | Prove rock by coring **≥5 m** (avoid boulder misread) |
| Spread footings depth | Explore **5 m into rock** or to negligible strain |
| Compressible clays | Explore to depth of insignificant strain under stress increase |
| Groundwater | Standpipes/piezometers over extended period; chemistry if aggressive |
| Lab / field | RSC (GI Field Works) + HOKLAS; old unsupervised GI → ascertain reliability |
| Designated Area | Staged GI **before** GBP finalisation |

**SD:** In HK, rockhead can jump within metres — do not set pile-cap / basement formation from one borehole.

---

### 11. Shallow foundations (§4)

#### 11.1 General

Structurally adequate RC footing/raft on adequate rock/soil at shallow depth. Must not overload neighbours, destabilise slopes, or clash with drains/nullahs/sewers/services.

#### 11.2 Plate load tests — when mandatory (§4.2.2)

Required when any of:

| Trigger | Note |
|---|---|
| Presumed qa **> 300 kPa** | Unless net increase (qa − qo) **< 50 kPa**; except Cat. 3 intermediate soil |
| qa from bearing-capacity equation / other methods | Except minor/temporary footings §2.2.2(5) |
| Es used in settlement **> 1 × N** (or **> 1.5 × N** for weathered-rock soils N>30 per 2025) | Must verify by plate test |

**Min. number:** 1 per soil type for each of first two **500 m²** of building site coverage + 1 per further **1 000 m²** (any fraction = one test).

#### 11.3 2025 basement amendments (APP-18)

For foundations supporting building(s) **with basement(s)** on granular soil:

| Item | Was | Now (2025) |
|---|---|---|
| qu limit in bearing equation | 3 000 kPa | **4 500 kPa** |
| Effective overburden depth for q | ≤ 3 m or Bf | Min. overburden around basement perimeter ≤ **10 m or Bf** |

#### 11.4 Types

| Type | SD hooks |
|---|---|
| Pad | Estimate total + differential settlement; enlarge pads to equalise pressures; design superstructure for residual differentials |
| Strip | Consistent founding along length; or design strip for differential |
| Raft | Design for 2-way differential settlement if needed |

---

### 12. Pile foundations — general rules (§5.1–5.3)

#### 12.1 Group effect & spacing (§5.1.2–5.1.3)

| Topic | Rule |
|---|---|
| Group reduction (friction piles, ≥5 piles) | Typically **0.85** (unless justified) |
| No group reduction if | Spacing >**3×** perimeter; **or** end-bearing; **or** rock-socketed; **or** driven to refusal on bedrock; **or** SPT N ≥**200** at toe |
| Friction / driven min. spacing | ≥ **perimeter** or **1 m** (greater); ≥ half perimeter or **500 mm** from boundary (H-pile perimeter = 2(b+d)) |
| Rock-socketed (mini / socketed H) | ≥ **750 mm** or **2×** casing OD |
| End-bearing bored | Nominal clear **≥500 mm** between shafts / bell-outs |

#### 12.2 Horizontal restraint, sliding, uplift (§5.1.4–5.1.6)

- Driven / small-diameter piles: adequate horizontal restraint in **≥2 directions** to piles or caps.
- Lateral sliding resistance: piles + ground must meet §2.5.4 sliding FoS.
- Uplift / overturning / buoyancy — each pile should satisfy:

\[
D_{min} + 0.9 R_u - 2.0 I_a - 1.5 U_a\text{(or }1.1 U_p\text{)} - 1.5 W_k \ge 0
\]
\[
D_{min} + R_a - I_a - U_a - W_k \ge 0
\]

Global analysis allowed if stiffnesses of piles, caps, ties, subgrade (and superstructure if used) are modelled.

#### 12.3 Pile group settlement (§5.1.7)

Equivalent raft method: friction-dominated groups → raft at **2/3 pile depth** below soft layer; end-bearing / hard rock sockets → raft at **toe level**.

#### 12.4 Negative skin friction (§5.2)

Consolidating + overlying soils: **no frictional capacity credit**; add NSF as load.

| Approach | What must be shown |
|---|---|
| **Conventional** | Capacity ≥ Gk+Qk+NSF (and with wind); β ≈ **0.25** if no better data; same group factor may apply to NSF |
| **Alternative** | Ground capacity ignores NSF; **structural** capacity includes NSF; settlement OK with NSF; test load ≥ **2Pc + NSF** |

Mitigation: proprietary bitumen/asphalt coating (site trials against damage) or double-skin liner with inert fill.

#### 12.5 Compression capacity (§5.3.2)

| Driven | Non-driven |
|---|---|
| Dynamic formula / static formula / load test; FoS generally ≥**3**, never <**2** | Founding + presumed / rational bearing & bond |
| Final set typically **25–50 mm/10 blows** (H-piles up to 100, then take 50); bedrock **10 mm/10 blows** | Min. socket depth **ignored** in bond calc; ignore bond on bell-out inclined faces |
| Drop hammer efficiency ≤**0.7** unless tested | Do **not** combine shaft + end bearing unless settlements mobilise both; may need instrumented trial piles |

#### 12.6 Uplift capacity (§5.3.3) — cone geometry matters for lot layout

| Topic | Rule |
|---|---|
| FoS on ultimate shaft uplift | Generally **≥3**, never <**2** (unless tested) |
| Tension proof test | Normally required; waived if tension ≤ **½** compression from shaft friction/bond **and** pile already in compression proof selection |
| Ru limited by | Effective rock/soil cone + soil column − pile self-weight |
| **Rock socket cone** | Half-angle ≤**30°** from vertical; ignore friction on soil-column face; **ignore anything outside lot boundary**; overlapping cones for groups |
| **Soil friction group cone** | SPT ≥30 → dilation ≤**1:4 (~15°)**; SPT <30 → **0°**; ignore cone face friction; ignore outside lot |
| Driven H transient tension | Uniform ≤**10 kPa** (N≥10); or β-method τs=βσ'v ≤120 kPa; or τs=1.5N ≤120 (or 0.75N ≤60 without trial); permanent = **50%** of transient (β / SPT methods) |

#### 12.7 Lateral load (§5.3.4)

| Topic | Rule |
|---|---|
| Check | Soil/rock resistance (incl. group), pile structural capacity, **P-Δ if deflection >25 mm** |
| nh (granular) | Dry/moist: N4–10 → 2200; N11–30 → 6600; N31–50 → 17600 kN/m²/m (submerged lower — Table 5.1) |
| Group nh reduction | Spacing/dia 3→0.25; 4→0.40; 6→0.70; 8→1.00 (Table 5.2); <3 → continuum method |
| Pile + pile cap together | Only with soil–structure interaction proving simultaneous mobilisation |
| Cap / wall / drag-wall friction | Do **not** count for lateral resistance unless compatible mobilisation proven |
| Rock socket lateral | Rock mass stability; allowable lateral ≈ **1/3** vertical if no adverse joints |
| Piles on slopes | Include slope effect + §2.10 |

---

### 13. Common pile types — architect’s choice matrix (§5.4–5.5)

| Type | Key SD / construction constraints |
|---|---|
| **Steel H / tubular** | Driven or pre-bored; plan needs chemistry, splice, tip protection, **H orientation** if lateral; weld NDT ≥**10%** of splices before driving spliced length |
| **Socketed steel H** | Rock per Table 2.1; rock–grout & steel–grout bond limits; non-shrink grout ≥30 MPa; min. **40 mm** grout cover to H; temp casing full depth in soil; test boring for overbreak control |
| **Precast RC** | Low/medium-rise; avoid boulder-rich ground; avoid hard driving; design for lift/transport/drive stresses |
| **Prestressed spun** | Drive to stiff residual/CD rock stratum; neighbour soil-movement assessment; stringent QC; thick stiff soil → conical shoe with cross stiffener |
| **Driven cast-in-place** | Dia ≤**750 mm**; no driving / vibration / chiselling within **5× dia** of unfilled hole or pile cast <**24 h** |
| **Small bored** | Dia ≤**750 mm**; ignore fill/marine friction unless no future consolidation; NSF applies |
| **CFA** | Rbc = µ Nav p L + 5 Nb Ab (Nav≤40, Nb≤200); µ=1.0 without trial, ≤1.6 with trial; incremental grout factor ≥**1.15**, total ≥**1.4**; refusal <300 mm/min deep → relocate if <**6 dia** from completed pile |
| **Large dia bored** | Shaft OD of casing **>750 mm**; **no dewatering** of hole; temp casing full depth in soil (or bentonite head in firm CD/HD rock); capacity from end bearing ± bell-out and/or rock-socket bond with length caps: with bell (b)+(c) socket ≤**1× dia or 3 m** (ignore 750 mm above bell); without bell (a)+(c) socket ≤**2× dia or 6 m**; bell-out ≤**1.65×** shaft, slope ≤**30°**; adjacent founding levels ≤ clear spacing on steep rockhead unless rock stability checked |
| **Mini-pile** | ≤5 bars ≤50 mm; casing OD ≤**450 mm**; working capacity ≤**2 350 kN**; capacity from **steel bars only** (≤**47.5% fy**); rock–grout bond; bar–grout **0.8 MPa**; clear bar spacing ≥20 mm; grout cover ≥**30 mm**; **no bending** for lateral — use rakers (hinged ends) or restrict cap displacement; check buckling; weak strata = lack of ≥5 m with avg N≥10 and no N<5; **no rakers in consolidating ground**; permanent casing ≥5 mm + grout cover ≥ max(20 mm, bar dia) typical |
| **Barrettes** | Rectilinear end-bearing on rock typical; slurry head incl. surcharge; RC guide walls |
| **Hand-dug caisson** | **Generally banned**; only if depth ≤**3 m** & inscribed dia ≥**1.5 m**, **or** only practical / no safe alternative |
| **H driven to bedrock** | Prefer bedrock slope ≤**25°**; refusal ≤**10 mm/10 blows** on ≥ grade III / 50% TCR rock; tip damage, deflection on sloping rock, buckling in weak overburden — often better as **socketed**; fixed-head detailing recommended |
| **Steel H shear piles** | Lateral / shear role — see RSE (clause 5.4.12) |

#### 13.1 Pile caps (§5.5)

- Mini-piles: design as **no bending** at cap and rock-socket connections → ensure pile + cap system stability.
- Cap ≥**800 mm** thick with H-piles into cap: bar-pair spacing may increase to **400 mm** with rules (adjacent ≤250 mm; trim bar with 90° hooks into H webs/flanges; trim ≥50% of larger adjacent bar, **not** counted in strength).

---

### 14. Basements, D-walls, retaining, anchors, re-use (§6)

| Element | SD hooks |
|---|---|
| **Basement / hollow box** | Vertical: wall-base bearing + slab bearing + wall friction (combine only if simultaneous mobilisation OK for neighbours); horizontal: passive + wall/base friction (same rule); walls/base ≥**C35** watertight; buoyancy per §2.5.4 **including during construction** before tower weight; include construction-stage stresses in permanent design |
| **Diaphragm wall** | Temp and/or permanent; thickness ≥**600 mm**; panels ~**3–7 m**; analyse seepage, toe stability, BM/shear/deflection for sequence, vertical bearing, slurry-trench stability, neighbour settlement; strutting / shear pins / toe grouting as needed |
| **Retaining walls** | B(C)R + GEOGUIDE 1 (or 6 for reinforced fill); if used as foundation or resisting foundation surcharge → also Ch.2 |
| **Permanent prestressed ground anchors** | Treated as **short-lived temporary** — **do not** incorporate into permanent building (monitoring commitment fails in practice); exceptional use only per GEOSPEC 1 with maintainer agreement + as-built pack |
| **Re-use existing foundations** | Need BD as-built / certified records (§2.7 info); full integrity / durability / load testing; old+new → differential settlement + preloading; protect during demolition |

**Re-use testing minima (guidance):**

| Existing type | Typical scheme |
|---|---|
| Large concrete (bored / caisson) | Dimensions; proof core each pile (clause 8.5) + ≥3 compression samples; visual → sulphate/chloride/carbonation if needed |
| Small concrete | Dimensions; head inspection; re-drive if driven; dynamic ≥**20%** driven steel; static load ≥**5%** |
| Steel / mini | Head inspection; re-drive driven; dynamic ≥**20%**; static ≥**5%** |
| Footings | Dimensions; proof core each; ≥3 compression samples; chemistry if needed |

---

### 15. Construction effects on neighbours & site practice (§7)

#### 15.1 Who can build

| Works | Contractor |
|---|---|
| Foundation penetration **> 3 m** | **RSC (Foundation Works)** |
| All foundation works | Site safety supervision (CoP Site Supervision + TM) + quality supervision (PNAP) |

#### 15.2 Neighbour assessment (§7.2.1–7.2.5)

| Topic | Architect-critical number / action |
|---|---|
| Assessment radius | Nearby buildings / land / services within **≥50 m** of boundary |
| Include | Vibration, dewatering, ELS; mitigation + monitoring + contingency |
| Settlement triggers (typical, non-sensitive — Table 7.2) | Alert **12** / Alarm **18** / Action **25** mm; services 12 mm or 1:600 → 25 mm or 1:300; tilt Alert **1:1000** → Action **1:500** |
| AAA response | Alert = more monitoring; Alarm = review method; Action = **suspend works** |
| Dewatering | Assessment + recharge option; stop if GW below design limits |
| Sensitive shallow foundations on loose sand/silt | High densification risk under vibration |

#### 15.3 Vibration (§7.2.6)

| Building | Transient / intermittent ppv | Continuous ppv |
|---|---|---|
| Robust / stable | **15** mm/s | **7.5** mm/s |
| Vibration-sensitive / dilapidated | **7.5** mm/s | **3** mm/s |

Heritage → AMO; railway → PNAP. Hospitals, old masonry, delicate utilities → **test drive** + pre-bore / limit concurrent hammers / control drop. Empirical prediction: kp ≈ **1.5** (or **3.0** to bedrock), verify by back-analysis.

#### 15.4 PR Plan (§7.2.7) — bilingual Chinese + English

Required for piling (incl. temp pile walls for ELS). Must include: programme & vibration activities; AP/RSE/RGE/RSC contacts; PR officer; OCs/MACs/DC; sensitive receptors; briefing/notice schedule; hotlines; complaint pledges; monitoring thresholds; action flow chart; complaint register.

#### 15.5 Blasting (§7.2.8)

B(C)R reg.23; DG(General) reg.46; PNAP APP-24 & APP-72; GS for Civil Engineering Works. Control vibration + flyrock.

#### 15.6 Pile construction QA that affects programme (§7.4)

| Item | Rule |
|---|---|
| Driven piles | Test driving before other piles; trial piles + §8.4 load test for special ground / new pile types |
| Test boring | Required when bit advances ahead of casing and hole **>450 mm** — overbreak / GW drawdown risk |
| Pre-drilling (rock / socket) | ≥**5 m** into specified rock or designed socket (deeper of the two) |
| Large bored / barrettes | Pre-drill **each** pile |
| Mini / socketed H / H to rock / small rock-socketed | Every pile tip within **5 m** of a pre-drill hole |
| Interface proof drill (large bored / barrettes) | **Each** pile — ≥1 m above & below interface |
| Post-install rock proof (small rock piles) | ≥2 holes if ≤100 piles; else **1%** of piles; rockhead contour plan with records |
| Proof tests | B(C)R mandatory for vertical or lateral piles — Ch.8 |

#### 15.7 Construction tolerances (Table 7.4)

| Foundation | Position | Verticality | Dimensions |
|---|---|---|---|
| Mini-piles | ±**15 mm** (may justify up to ±75) | **1 in 100** | ±3% |
| Marine piles | ±**150 mm** | **1 in 25** | ±3% |
| Other piles | ±**75 mm** | **1 in 75** | ±3% |
| Rafts / beams / caps / footings | ±**50 mm** | N/A | ±3% |

No part may extend **outside lot boundary**.

#### 15.8 Nuisance (§7.7)

| Issue | Control |
|---|---|
| Percussive piling | **EPD permit** (Noise Control Ordinance) |
| Diesel hammer smoke | Air Pollution Control Ordinance |
| Muddy / chemical waste | Not into drains — PHMSO / DSD indemnity risk |
| Vibration comfort | Beyond structural ppv — occupant discomfort |

#### 15.9 Ground treatment (§7.6)

Prove method + materials; test treated ground; protect neighbours.

---

### 16. Testing — what AP should expect on programme & cost (§8)

Except SPT and proof core-drilling, Ch.8 tests by **HOKLAS** labs.

| Test | Purpose / key acceptance (architect view) |
|---|---|
| **Plate load** | Verify qa & back-calculate Es; plate ≥300 mm; load to **3Wt**, hold 3Wt ≥**72 h**; Smax ≤**0.15B** for qa OK |
| **SPT** | Uncorrected N before works; caution for cohesive / marine deposits |
| **Compression load test** | Common for driven, small bored, socketed, mini; to **2×** working capacity, hold ≥**72 h**; fail if settlement > 2WL/(AE) + D/120 + 4 mm, or residual recovery rules fail |
| **Proof core** | Large bored / barrettes — full depth + ≥ max(½ dia, **600 mm**) into founding; no honeycomb/segregation; rock meets design; interface OK; if on soil, SPT every ≤1.5 m for ≥ max(3× dia, **5 m**) |
| **Sonic logging** | Cast-in-place / D-wall / barrette integrity — cannot identify defect nature; tubes can harm concrete |
| **Sonic echo** | Continuity; L/D ≤**30**; not for jointed piles; ≥7 days after cast |
| **Vibration / impedance** | Head stiffness / defects; damped at L/D ~20–30 |
| **Dynamic load (driven)** | **Not** generally accepted as proof test in HK; OK for defect screening / hammer efficiency / relative capacity |
| **Tension load test** | Similar 2× / 72 h protocol; reaction piles ≥ max(**3 dia**, **2 m**) clear; fail if extension > elastic + **4 mm** or residual rules / structural failure; if design tension uses ≤50% of compression bond/friction values, test load may be **1.5×** design uplift (2025 wording refined) |

---

### 17. SD checklist — freeze these before schematic is “done”

1. **Geology flags:** Scheduled Area / Designated Area / reclaim / marble / slope >15° / nullah / tunnel / railway / sewage tunnel?
2. **Foundation typology:** shallow vs pile vs basement box; avoid mixed systems unless differential settlement is designed in.
3. **G/F strategy on reclaim:** suspended vs limited on-grade exceptions; plant rooms never on consolidating fill.
4. **Basement depth vs GW:** permanent + **temporary** buoyancy FoS; C35 watertight walls/slab.
5. **Tower vs podium load path:** pile-cap thickness, transfer, NSF, wind 25% uplift on capacity only.
6. **Pile type vs neighbours:** driven (vibration + EPD permit + PR Plan) vs bored/socketed; concurrent rigs limit.
7. **Layout vs rockhead / marble:** steep rockhead founding steps; karst site class A–D may kill friction foundations.
8. **GI programme:** staged holes proving rock ≥5 m; piezometers through wet season; Designated Area GI before GBP freeze.
9. **Re-use / existing piles:** only with BD records + testing budget — do not assume free capacity.
10. **No permanent prestressed anchors** as a “cheap” uplift fix in the permanent building.
11. **Hand-dug caissons:** assume unavailable except rare justified cases.
12. **Programme allowances:** test piles, plate tests, pre-/post-drilling, interface cores, 72 h maintained load tests, marble settlement monitoring to OP.

---

### 18. Cross-references the RSE/RGE will expect opened

| Document | Use |
|---|---|
| GEOGUIDE 2 / 3 | GI & rock/soil description |
| GEOGUIDE 1 / 6 | Retaining / reinforced fill |
| GEO TGN 12 / PNAP APP-134 | Designated Area (Northshore Lantau) |
| GEO TGN 26 | Marble / karst |
| GEO TGN 42 | Landslide debris impact |
| GEO Publication 1/2006 | Settlement Fo coefficients |
| GEOSPEC 1 | Prestressed ground anchors (exceptional) |
| Dead & Imposed Loads / Wind Code | Foundation loads |
| CoP Structural Use of Concrete / Steel | Member / weld design |
| CoP Site Supervision + TM for Supervision Plans | RSC / quality supervision |
| Port Works Design Manual | Marine foundations |
| PNAP (Scheduled Areas, APP-18, APP-24, APP-72) | BA practice / blasting / railway |
| Noise / Air / PHMS Ordinances | Percussive piling permit, smoke, wastewater |

---

*Summary for AP schematic use only. Does not replace RSE/RGE design, BD approval, or the full Code text.*

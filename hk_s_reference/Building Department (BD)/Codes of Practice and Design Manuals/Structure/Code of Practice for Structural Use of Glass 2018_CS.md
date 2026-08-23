# Code of Practice for Structural Use of Glass 2018
**Architect critical summary for schematic design**  
First issue February 2018 | Buildings Department  
Amendments: **2020** (SSG retaining devices; gasket wording) · **2024** (balustrade weep holes deleted; CW mock-up p₂ = net wind on mullion per Wind Code 2019)

> Scope note: Deemed-to-satisfy guidance for **structural glass** — panes, laminated / IGU assemblies, glass walls, fins / beams / columns, curtain wall / window / window wall, tension-rod façades, and glass balustrades / protective barriers. Not a statute; compliance is deemed to satisfy the Buildings Ordinance and related regulations. Cross-check **Wind Code 2019**, **Dead & Imposed Loads Code**, B(C)R protective barriers (ss. 36–38), FS Code (fire-rated glass), OTTV/RTTV, PNAP APP-37 / APP-2 / APP-110, Access for External Maintenance CoP, and steel/aluminium structural CoPs for frames. RSE owns calculations; AP must lock **glass type, pane size, height above accessible FFL, redundancy, retention strategy, fin depth, clamp zone, and mock-up / heat-soak programme** at SD.

---

## Regulatory Overview

This Code covers **design, construction, testing and quality assurance of glass structures and glass elements in buildings** using soda-lime silicate glass under limit-state design (ULS + SLS). It applies wherever glass resists dead, imposed, wind, temperature or movement loads — façades, glass walls, roofs / canopies / skylights, floors / stairs, structural fins / beams / columns, and protective barriers.

At schematic design, lock **glass type by location** (annealed / heat-strengthened / tempered / laminated / IGU), **pane area vs height above accessible FFL**, **protective-barrier vs cladding role**, **structural sealant redundancy**, and **maintenance / replacement access** — these rules drive mullion grids, fin depths, balustrade typology, slab-edge clamp zones, and heat-soak / mock-up programme before GBP.

---

## Critical main topics and subtopics

### 1. Design aims — what “compliance” means (§1.2)

Limit-state design must achieve all of the following. Treat each as an SD brief item, not a late engineering detail.

| Aim (§1.2.1) | What to freeze at SD |
|---|---|
| **a)** Overall stability & buckling resistance | Fin / column / cable restraint strategy; corner side-wind |
| **b)** Strength under design loads **and** imposed deformations of supports | Interstorey drift joints; relative floor deflection; creep / settlement allowance |
| **c)** Integrity & robustness against progressive collapse | Multi-pane redundancy; alternate load paths; 70 m² collapse cap (§2.2.3) |
| **d)** Serviceability | Deflection / vibration often govern thickness before stress |
| **e)** Water & air tightness | CW / WW system type + mock-up (§8.3) |
| **f)** Durability | Interlayer UV/heat loss; sealant life; edge protection of laminates |
| **g)** Quality | ISO 9001 factory; heat soak; GASP; boil / impact / bending tests |
| **h)** Maintainability during design working life | Access for External Maintenance CoP + Annex D handover manual |

**Alternative / performance-based path (§1.2.2):** Allowed only if adequate information **including compliance testing** proves the same aims. Do not invent ad-hoc waivers on GBP day — budget specialist design + testing early for free-form, cable nets, glass structures, or non-standard interlayers.

---

### 2. Terms that change the brief (§1.3)

| Term | Meaning for SD |
|---|---|
| **Annealed (float)** | Ordinary float; breaks into large sharp shards; weak for impact / thermal / bending; flaws grow under sustained load |
| **Heat strengthened** | Surface compression **> 24 MPa and < 52 MPa**; breaks like annealed (still sharp shards) — **not** “safety glass” by itself |
| **Tempered (fully toughened)** | Surface compression **≥ 69 MPa**; breaks into small rough cubes; high bending strength; **NiS spontaneous breakage** → mandatory heat soak |
| **Laminated** | ≥2 panes bonded by interlayer; debris held on interlayer after breakage — required for many long-term / overhead / balustrade uses |
| **IGU** | Hermetic multi-pane unit with cavity + spacer / primary / secondary seals; load sharing + climate pressure effects |
| **Safety glass** | Laminated **or** tempered (“break-safe”) |
| **Wired glass** | Wire mesh in glass — not a substitute for laminated safety strategy in this Code’s structural uses |
| **Glass wall** | Wall mainly of structural glass spanning floor-to-floor |
| **Glass fin** | Vertical / sloping glass beam supporting façade / glass wall (mainly wind / lateral) |
| **Glass beam / column** | Horizontal bending member / vertical axial member — primary structure if supporting floors or beams |
| **Mullion / transom** | Vertical / horizontal CW or glass-wall members directly supporting glass |
| **Curtain wall** | Non-loadbearing enclosure; D+L+W to structure via fixings |
| **Window** | Framed glazing in external wall opening for light / ventilation |
| **Window wall** | Windows spanning between floor slabs |
| **Bite** | Width of structural sealant bonding glass to support |
| **Setting block** | Resilient block transferring glass dead load to frame at defined points |
| **Gasket** | Separates glass from hard contact with frames / plates |
| **Heat soak** | QC process heating tempered glass to precipitate NiS failures in oven, not in service |
| **Interlayer** | Adhesive layer(s) between panes — composite action, impact, solar, acoustic |
| **Nonlinear analysis** | Large-deflection / membrane action; needed when pane deflection is not “small” |

**SD takeaway:** “Tempered” ≠ safe for overhead. Overhead / long-term locations need **laminated** (often multi-layer). Large elevated façade tempered panes must be **laminated** under §5.2.1(3). Heat-strengthened alone still fails dangerously — do not specify HS for balustrades or overhead without lamination.

---

### 3. Why glass fails differently from steel / concrete (§4.1) — brief the team

| Behaviour | Design consequence |
|---|---|
| Brittle; fails suddenly at ultimate tensile strength | No plastic redistribution; local failure → global failure |
| Strength is statistical | Larger stressed area → higher failure probability; ultimate design strength defined so ≤ **8/1000** panes fail |
| No metallurgical fatigue; micro-cracks grow under sustained / cyclic load | Long-term load duration factors are severe (especially annealed) |
| Weak in tension; flaws at edges / holes / surface treatment dominate | Edge quality, hole placement, frit / etch matter as much as thickness |
| Tempered: locked-in surface compression | High bending strength; holes OK if diameter ≥ thickness for cooling; cutting **only before** tempering |
| Tempered NiS risk | α→β NiS volume growth in tensile core → spontaneous break; heat soak mandatory |

**Physical properties (Table 4.2) — for coordination:**

| Property | Value |
|---|---|
| E | **70,000 N/mm²** |
| Poisson ν | **0.22** |
| Thermal expansion α | **9 × 10⁻⁶ /°C** |
| Density ρ | **2,650 kg/m³** |
| G (shear) | E / [2(1+ν)] ≈ **28,700 N/mm²** (also used for fin buckling Annex C) |

Code applies to **soda-lime silicate** glass only (Table 4.1 composition).

---

### 4. Progressive collapse — 70 m² cap (§2.2.3)

Glass structures must not be unreasonably susceptible to disproportionate collapse from failure of a single element or small area (e.g. glass column → glass beam → glass floor).

| Rule | Detail |
|---|---|
| Collapse area limit | Portion at risk from **one single element** failure ≤ **70 m²** (floor, frontal **or** total area) |
| Extra measures | Enhance integrity / robustness to prevent local damage cascading |

**SD:** Atria, glass floors, glass columns supporting glass beams, and long fin-supported walls need **alternate load paths / multi-pane residual capacity** from concept. Do not hang a large glass floor on a single column line or a single fin without redundancy study.

---

### 5. Vibration (§2.3.3)

Natural frequencies of glass structures should be checked to mitigate human-induced and wind-induced oscillation. Glass floors and glass staircases may need human-comfort vibration assessment — specialist literature / guidelines. Flag early if you propose glass walk-on floors or monumental glass stairs.

---

### 6. Loads the AP must brief (§3)

#### 6.1 Characteristic loads (§3.2)

Dead, imposed, wind → B(C)R, Dead & Imposed Loads Code, Wind Code. Construction loads and support settlement also considered.

#### 6.2 Building movements the façade / glass wall must absorb (§3.3)

| Movement | SD implication |
|---|---|
| Concrete creep, settlement, shrinkage | Soft joints; do not hard-fix glass across movement |
| Horizontal **interstorey drift** | Stack joints / sliding anchors sized for drift |
| Relative vertical deflection between consecutive floors | Window wall / stick CW especially — avoid prying on glass |

#### 6.3 Temperature ranges (§3.4)

| Exposure | Design range |
|---|---|
| Surface not under direct sunlight | **0–40°C** |
| Exterior, direct sun — **clear** glass | **0–50°C** |
| Exterior, direct sun — **tinted** glass | **0–90°C** |

Include temperature at **installation**. Annex D notes ~**33°C** differential ≈ **20.7 N/mm²** thermal stress — annealed and edge-damaged panes are vulnerable; deep tint / frit / shadow bands amplify risk.

#### 6.4 Load duration — drives allowable strength (§3.5)

| Duration | Definition | Examples |
|---|---|---|
| **Short-term** | ≤ **3 seconds** | Wind; horizontal imposed load on protective barrier |
| **Medium-term** | > 3 s to ≤ **1 day** | Maintenance load; temperature load |
| **Long-term** | > **1 day** | Self-weight; sustained occupancy / storage |

---

### 7. Glass types, strength tables, surface treatment (§4.2–4.3)

#### 7.1 Type comparison (SD selection)

| Type | Break pattern | Surface stress | Use notes |
|---|---|---|---|
| Annealed | Large jagged shards — extremely dangerous | None (relieved) | Avoid where impact / thermal / fall hazard; never sole overhead glass |
| Heat strengthened | Smaller but still annealed-like shards | 24–52 MPa | Better thermal / crack resistance than annealed; still needs laminate for safety roles |
| Tempered | Small cubic fragments | ≥ 69 MPa | High strength; heat soak all panes; deflection often governs before strength is used |

#### 7.2 Ultimate design strength 𝑝𝑦 — short-term (Table 4.3)

| Type | 𝑝𝑦 (MPa) |
|---|---|
| Annealed | **20** |
| Heat strengthened | **40** |
| Tempered | **80** |

(= strength at which ≤ 8/1000 panes fail)

#### 7.3 Duration reduction 𝛾𝑑 (Table 4.4) — long-term kills annealed

| Type | Short | Medium | Long |
|---|---|---|---|
| Annealed | 1.00 | 0.53 | **0.29** |
| Heat strengthened | 1.00 | 0.73 | 0.53 |
| Tempered | 1.00 | 0.81 | 0.66 |

#### 7.4 Surface treatment reduction 𝛾𝑠 (Table 4.5)

| Surface | 𝛾𝑠 | SD note |
|---|---|---|
| Flat clear / tinted / coated | **1.0** | Baseline |
| Ceramic frit / enamel paint | **0.625** | Pattern / coverage can force thicker glass |
| Patterned / sandblasted / acid-etched | **0.5** | Privacy / decorative glass — half strength |

Surface-treated design strength must be verified by bending test (BS EN 1288-3). Characteristic bending strength of ≥5 specimens ≥ reduced design strength with FoS **2.0** (§8.1.8).

**Effective strength sketch:**  
𝑅 ∝ (𝛾𝑑 × 𝛾𝑠 × 𝑝𝑦) / 𝛾𝑚 with 𝛾𝑚 = **1.0** for glass (§5.4.3)

Example: fritted annealed under long-term → 20 × 0.29 × 0.625 ≈ **3.6 MPa** usable — often impractical; change type or drop frit on structural face.

---

### 8. Glass assemblies (§4.4)

#### 8.1 Laminated glass (§4.4.1)

| Topic | Rule |
|---|---|
| Build-up | ≥2 panes + interlayer (typically **0.38–6.0 mm**) |
| Default analysis | **No composite action** — each pane shares load by stiffness (𝑡³) unless Annex B1 tests justify composite |
| Composite cap | ≤ **70%** of monolithic stiffness (sum of thicknesses); **short-term loads only** |
| Glass matching | Prefer same type; thickness difference ≤ **one grade** |
| HS / tempered laminate risk | Roller-wave mismatch → delamination risk — provide **sufficient interlayer thickness** |
| Inner surface treatment | Durability tests may be required |
| Safety role | Debris adhered to interlayer — suitable for balustrades |
| After breakage | Replace ASAP — entire pane may still fall from height |
| Edge practice | Protect laminated edges from direct weather exposure |
| QC | Clause 9.2.1 + boil test |

Process (for awareness): oven ~70°C + rollers → autoclave ~140°C at ~0.8 N/mm² in vacuum bag.

#### 8.2 Insulating glass unit — IGU (§4.4.2)

| Topic | Rule |
|---|---|
| Build-up | ≥2 panes + spacer (desiccant) + primary seal + secondary seal |
| Secondary seal | **Two-part structural** sealant; continuous, no gaps/voids, fully bonded |
| Low-E edge | Coating **removed** at edge for secondary seal adhesion |
| Tin side | Outermost surfaces of IGU for future GASP stress measurement |
| Durability | Spacer/seal compatible; ASTM **E2190** |
| Sound fill | e.g. hexafluoride in cavity (performance, not structural) |

#### 8.3 Low-E (§4.4.3)

Mainly energy — structural effect usually insignificant for tempered; surface temperature / thermal stress more relevant for annealed.

#### 8.4 Fire-rated glass (§4.4.4)

Normal glass shatters under fire heat (low tensile + high thermal expansion). Fire glass typically clear intumescent interlayer gel in multi-laminate — thicker / more interlayers for higher FRP. Durability: high-temperature, humidity, radiation tests. Coordinate FS Code FRP separately.

#### 8.5 Decorative / fritted (§4.4.5)

Coating, etch, sandblast, frit, print, emboss, abrade, decorative interlayers — aesthetic but can reduce strength / durability. Effect on ultimate strength per §5.4; verify by BS EN 1288-3 bending tests.

#### 8.6 Interlayer materials (§7.4)

| Material | Notes |
|---|---|
| **PVB** (most common) | Typical UTS 28.1 MPa; elongation 275%; E ≈ 11 MPa (Table 7.1). Boil test required. Avoid sealant contact with interlayer |
| **Resins** (cast-in-place) | Performance-based — Annex B1 + B2 tests |
| **Ionoplast** | Higher modulus; less strength loss at elevated temperature than PVB — better for structural laminates / residual capacity; still Annex B1/B2 |
| **Intumescent** | Fire-rated assemblies |

Delamination is a major concern — QC + boil test + edge protection.

---

### 9. Safety rules that freeze glass specification (§5.2) — lock at SD

#### 9.1 Against glass breakage (§5.2.1)

| # | Condition | Required glass |
|---|---|---|
| (1) | Elements resisting **long-term** load: roof, canopy, skylight, **sloped glazing**, staircase, floor, beam, column, **and glass balustrade** | **Laminated** |
| (2) | Parts of building **exterior façade also serving as protective barrier** | **Tempered or laminated** |
| (3) | Tempered glass in exterior façade where **pane area > 2.5 m²** **and** any point of pane is **≥ 5 m** above finished floor level of accessible area on **either side** | Must be in **laminated** form |
| (4) | IGU in exterior façade | Rule (3) applies to **outermost pane only** |

**SD decision tree:**

```
Overhead / floor / stair / canopy / skylight / sloped / balustrade / long-term load?
  → Laminated always (often multi-layer for residual capacity)

Façade also a protective barrier?
  → Tempered or laminated (+ impact Class 1 if critical zone)

Façade tempered pane > 2.5 m² AND any point ≥ 5 m above accessible FFL either side?
  → Laminated (tempered alone forbidden)
  → IGU: laminate the outer pane

Four-sided SSG with any point ≥ 5 m above accessible FFL?
  → Retaining devices on two opposing edges (2020 Amend) — see §14.2
```

**Height measurement tip:** “Accessible area on either side” includes podium roofs, terraces, internal atria floors, and street level — measure to the nearest accessible FFL that people can occupy, not only the floor the glass sits on.

#### 9.2 Against element failure — redundancy (§5.2.2)

Glass roofs, **accessible** canopies and skylights, staircases, and floors subject to medium or long-term loads:

1. Construct with **multi-layered** glass panes designed for **ultimate** design loads; **and**
2. Provide structural redundancy so that if **any single glass pane fails**, remaining pane(s) support **unfactored characteristic loads** without failure.

**SD:** Overhead glass is never single-ply. Brief RSE for residual capacity after one ply break. Plan replacement access (gondola / BMU / roof walkway) from day one — damaged laminated panes can still fall as a unit.

---

### 10. Analysis assumptions that affect module size (§5.1, §5.3)

#### 10.1 Design thickness — use minimum, not nominal (Table 5.1)

| Nominal (mm) | 6 | 8 | 10 | 12 | 15 | 19 | 22 | 25 |
|---|---|---|---|---|---|---|---|---|
| **Min t for design (mm)** | 5.56 | 7.42 | 9.02 | **11.91** | **14.2** | 18.26 | 21.44 | 24.61 |

Specifying “12 mm” in drawings ≠ designing with 12 mm — RSE must use 11.91 mm.

#### 10.2 Linear vs nonlinear (§5.3.1–5.3.2)

| Condition | Method |
|---|---|
| Deflection < **¾ × thickness** | Linear OK (“small” deflection) |
| Deflection > thickness (typical 4-side SS under wind) | Membrane action significant → **nonlinear** / Code eqns 5.9–5.11 |
| Irregular shape / curved / complex edges | FE analysis; edge **free-to-pull-in** unless justified |

#### 10.3 Laminated load sharing (no composite) — eqn 5.1

Each pane takes share 𝑘_pane ∝ 𝑡³ / Σ𝑡ᵢ³ (all panes deflect together).

#### 10.4 Laminated with proven composite — eqn 5.2

𝜆 ≤ min(𝜆_test, **0.7**); use equivalent thickness for stress/deflection; **short-term only**.

#### 10.5 IGU load sharing — eqn 5.3

Same 𝑡³ sharing **but** loads on each pane increased by **+25%** for temperature / atmospheric pressure. Invalid if “deep cavity” — air gap **> sum of pane thicknesses**.

---

### 11. Ultimate limit state — factors & combinations (§5.4)

#### 11.1 Partial load factors 𝛾𝑓 (Table 5.2) — normal conditions

| Combination | Dead adverse | Dead beneficial | Imposed adverse | Imposed beneficial | Earth/water | Wind | Temp |
|---|---|---|---|---|---|---|---|
| **1** D + L + earth/water + temp | 1.4 | 1.0 | 1.6 | 0 | 1.4 | — | 1.2 |
| **2** D + W + earth/water + temp | 1.4 | 1.0 | — | — | 1.4 | 1.4 | 1.2 |
| **3** D + L + W + earth/water + temp | 1.2 | 1.0 | 1.2 | 0 | 1.2 | 1.2 | 1.2 |

Notes: beneficial earth/water 𝛾𝑓 ≤ 1.0 so factored = actual. For **SLS**, all adverse 𝛾𝑓 = **1.0**.

#### 11.2 Combined duration check — eqn 5.8

Σ (𝑆_ult / 𝑅_ult) for short + medium + long ≤ **1.0** — panes under mixed wind + self-weight + thermal must satisfy interaction.

#### 11.3 Four-side SS thickness equations (§5.4.5) — for awareness

For aspect ratio 𝑏/𝑎 < 5: 𝑡 ≥ min(𝑡₁, 𝑡₂) from eqns 5.9–5.10; for 𝑏/𝑎 ≥ 5: 𝑡 ≥ 𝑡₃ from 5.11. Strength coefficient 𝑐 = 𝑐₁ × 𝛾𝑑 × 𝛾𝑠 with 𝑐₁ = **1 / 2 / 4** for annealed / HS / tempered. **Only** for four-side simply supported rectangular panes — other supports need FE / recognised formulae.

---

### 12. Serviceability — deflection limits often govern (§5.5)

#### 12.1 Glass pane (§5.5.3)

| Support | Limit 𝛿_limit |
|---|---|
| Four-side simply supported | **L/60** of shorter span |
| Three-side simply supported | min(**𝑏/60**, **𝑎/30**) — free-edge geometry Fig. 5.1 |
| Two-side simply supported | **L/60** of loaded span |
| Cantilever | **L/30** of span |
| Point-supported | **L/60** of longer span between supports |

#### 12.2 Supporting structural members (§5.5.4) — also CW mock-up acceptance

| Member | Limit |
|---|---|
| Span ≤ **7.2 m** | Smaller of **L/180** or **20 mm** |
| Span > **7.2 m** | **L/360** |
| Cantilever | Smaller of **L/90** or **20 mm** |

Glass fin / beam: same as supporting members (§6.1.2).

**SD:** Tall stick CW / slender aluminium → **20 mm** cap often controls before glass stress. Large point-fixed glass → deflection between bolts controls. Do not promise ultra-thin tempered glass for big modules without deflection check.

#### 12.3 Durability of composite interlayers & sealants (§5.5.5)

Interlayers used for composite action and structural sealants under long-term sunlight can lose capacity — consider in design life. Durability tests (boil / weathering) per ANSI Z97.1 or BS EN ISO 12543; local HK conditions may require extra justification.

---

### 13. Glass element design by typology (§6)

#### 13.1 Glass wall — fin / spider / cable (§6.1)

| Topic | Rule |
|---|---|
| Systems | Glass fins, tension rods, cables — vertical, sloped, horizontal |
| Fin analysis | Buckling under combined in-plane + out-of-plane; **corner side-wind** simultaneously |
| Corner column / fin | Design for induced moments and forces |
| Connections | Structural sealant or point bolts — local stress concentration + stability |
| Point supports | Simple bolt, patch, countersunk; clearance, edge distance, movement, stress at holes; **no hard contact** |
| Spider fixings | Proof load test; publish mechanical props, dimensions, capacities, proprietary model; resilient gasket at glass interface (less stiff than glass) |
| Cable / rod support | Geometric nonlinearity, differential temperature, creep under long-term load, support movement |
| Verification | Full-scale mock-up; complex systems may need performance-based design + advanced nonlinear analysis |

#### 13.2 Glass fin / glass beam (§6.1.1–6.1.2)

| Check | Rule |
|---|---|
| Stability | Restrain from rotation; hold in position |
| Major-axis bending strength | Reduce ultimate design strength by **40%** (tempered 80 → **48 MPa**; HS 40 → **24 MPa**; annealed 20 → **12 MPa**) |
| Local buckling of free edge | Eqn 6.1: 𝐸𝑡³ / [6(1+ν)] > 𝑀𝑤 (working in-plane moment, 𝛾𝑓 = 1.0) |
| Lateral-torsional buckling | 𝑀𝑐𝑟 ≥ **1.7 𝑀𝑑** (Annex C) |
| Elastic moment capacity | 𝑀𝑒 = 𝛾𝑑 × 𝛾𝑠 × 𝑝𝑦𝑦 × 𝑍 > 𝑀𝑑 |
| Nonlinear FE option | Shell FE with imperfection **0.5% of fin length**; 𝑀𝑢 > 𝑀𝑑; or max principal stress < 𝑝𝑦𝑦 |
| Deflection | Same as §5.5.4 (L/180 or 20 mm ≤7.2 m; L/360 >7.2 m) |

**Annex C (architect-relevant):** End supports must be effectively restrained against twisting (torsional stiffness > **20GJ/L**). Intermediate buckling restraints prevent rotation about z-axis. Continuously restrained and unrestrained cases use different formulae. For critical non-load-sharing engineered fins with unusually light restraints, check restraint force capacity (C5). Coordinate **restraint locations** with façade module lines early — restraints are architecture as much as structure.

**2020 Amend (Annex C):** Torsional constant uses depth **𝑑** and thickness **𝑡** of fin (symbol clarification).

#### 13.3 Glass column (§6.1.3)

Primary support to glass beams / floors → adequately restrained; typically slender (buckling + out-of-plane tension from buckling); **sufficient structural redundancy** mandatory. Performance-based design from first principles + component and system testing.

#### 13.4 Curtain wall, window, window wall (§6.2)

| Requirement | Detail |
|---|---|
| Performance | Safely sustain & transmit combined D+L+W without excessive deflection / deformation damaging system or stability |
| Frames | Design to relevant steel / aluminium / stainless steel CoPs |
| Mock-up | Full-scale per §8.3 — complexity of interaction requires it |
| Attention items | Horizontal imposed loads; protection of openings; glass balustrade function; corrosion protection; material QC; **fire/smoke spread between floors** |
| System types | Stick and unitised — both need building movements, lateral displacement, thermal expansion, water/air, durability, corrosion, structural safety |

#### 13.5 Tensioning structural system (§6.3)

Stainless rods / cables: strong in tension, buckle in compression. Pre-tension so members stay in tension under **all** load combinations (pre-tension > induced compression). Design for geometric nonlinearity, differential temperature, creep, support movement, wind — full load-case matrix required.

---

### 14. Glass balustrades & protective barriers (§6.4) — high AP / PI risk

#### 14.1 Classification

- **Infill** panes (frame / handrail takes load; glass fills), or
- **Free-standing** glass panes (glass is the structure)

If also protective barrier: resist horizontal imposed load **or** wind; impact test required. Side wind at corners simultaneously.

#### 14.2 Structural rules

| Rule | Detail |
|---|---|
| Infill philosophy | Main frame (handrail + balusters) takes all handrail loads; glass **must not** be assumed to support main frame / handrail |
| Free-standing | Glass designed for all design loads; top-rail displacement ≤ §5.5.3 under worst of wind or horizontal imposed |
| Panic / congregation | Free-standing run of **≥ 2** continuous panels in areas where people may congregate / overcrowding: top rail attached so it **bridges** a failed pane, remains stable, and resists working load across the gap **without** structural failure of the barrier system |
| Panic alternative | Top rail may be omitted only if remaining intact layer(s) of **laminated** glass can resist working load when **one layer is broken** |
| Free-standing clamps | Continuous bottom clamps **each side**: min width **100 mm**; metal min thickness **12 mm**; continuous full length of pane; max bolt spacing **500 mm** |
| Non-bolted clamps | Clamping force depth ≥ **90 mm** unless specific tests prove system |
| Material | Laminated per §5.2.1(1); protective barrier glass must not break under appropriate impact test |
| Critical impact zone | Portions of glass measured up to **1100 mm** from FFL of surface adjoining the barrier → human collision zone |
| Impact standard | BS EN 12600 **Class 1** with **no glass breakage** |

**2024 Amend:** Fig. 6.1 — **8 mm dia. weep holes for external application deleted** from typical balustrade detail. Do not copy old weep-hole detail from pre-2024 figures.

**SD geometry:** Free-standing structural glass balustrade needs a **deep continuous clamp pocket** in slab edge / upstand / beam from GA stage (100 mm wide clamps + embedment + waterproofing). Panic locations (atriums, stadia, retail voids, school corridors) need continuous handrail continuity **or** proven residual laminated capacity. Coordinate Loading Code horizontal barrier loads and B(C)R barrier height separately.

---

### 15. Connections & sealants (§7)

#### 15.1 Structural sealant — base rules (§7.1)

| Parameter | Value |
|---|---|
| Permissible design strength (short / medium) | **138 kPa** |
| Movement capability (structural + weather) | ≥ **±25%** strain |
| Minimum bite | **6 mm** |
| Bite : thickness ratio | **1:1 to 3:1**; if > 3:1 → manufacturer review thickness |
| Long-term loads | **Do not use** structural sealant for long-term load resistance |
| Dead load of glass | Always on **setting blocks** (mechanical) |
| Water / vapour | Prevent long-term exposure of structural sealant to water or vapour |
| Manufacturer reports | Strength, elongation, shear (incl. elevated temp), bonding, adhesion/compatibility, durability |
| Standards | BS EN 13022-2; BS EN 15434; ASTM C1184 (or equivalent) |

Four-sided SSG bite (ASD wind):  
$$b_b = 0.5 \times p \times L_s / p_b$$  
(𝐿𝑠 = shorter span; 𝑝 = design wind for ASD; 𝑝𝑏 = permissible bond strength)

Two-/three-sided or irregular panes: evaluate bite from actual load distribution. Glass designed as simply supported (“floated”) — avoid metal contact and prying.

IGU secondary seal width for lateral load (eqn 7.2): same form using outer-pane design pressure 𝑝ₒ.

#### 15.2 Retaining devices for SSG — **2020 Amendment (critical)**

Applies to façade system or glass element **fixed by structural sealant on four sides**, where any point of the glass pane is at a height **5 m or more** above the finished floor level of the accessible area on either side:

| Requirement | Detail |
|---|---|
| Design intent | Prevent fall of glass on bond failure of structural sealant |
| Retaining devices | Feature capping, angle, bracket, insert, etc. at **any two opposing edges** |
| Strength | Retainer **and** associated glass resist **37% of design wind pressure** × partial load factor **1.0** |
| Design wind pressure | Wind Code **2019** wind **reference pressure without any adjustment factors** |
| Dead load | Still mechanically on setting blocks |

**SD:** Four-sided SSG above 5 m is not a pure “all-glass” look — mechanical retention at two opposite edges must appear in the aesthetic language (cap, fin, shadow gap bracket, etc.). Coordinate with façade consultant at concept, not at shop drawing stage.

#### 15.3 Hard-contact ban (§7.2)

Contact between glass and any harder substance **forbidden**. Gaskets / bushings softer than glass at all metal interfaces (frames, bolts, clamping plates).

#### 15.4 Framed infill (§7.2.1)

| Dimension | Minimum |
|---|---|
| Edge cover | **10 mm** (recommended ≥ glass thickness in contact) |
| Edge clearance | **6 mm** |
| Front and back clearances | **5 mm** each |

Frame and connections must take design load through glass. Ref: BS 6262.

#### 15.5 Adhesive / butt joints (§7.2.2)

Glass-to-glass right-angle silicone butt joints: glass can rotate in frame → design as simply supported.

#### 15.6 Point bolted supports (§7.2.3)

| Rule | Detail |
|---|---|
| Glass type | **Tempered** |
| Reverse curvature | Connector positions must not create reverse curvatures (high stress at bolts) |
| Cover | Clamping plates + gaskets both sides; ≥ **50 mm** diameter cover |
| Cantilever beyond bolts | Cantilever length ≤ **s/4** (𝑠 = span between bolted connectors) |
| Fixing to main frame | Capable of design loads through glass |
| Movement | Allow in-plane movement or provide restraint as designed (Fig. 7.4) |

#### 15.7 Clipped infill (§7.2.4)

| Rule | Detail |
|---|---|
| Max spacing 𝑋 | **600 mm** between fixings |
| Min clips per pane | **4** |
| Distance from corner | ≤ **𝑋/4** |
| Clip length | ≥ **50 mm** |
| Depth of cover to glass | ≥ **25 mm** |

#### 15.8 Holes in glass (§7.3)

| Rule | Limit |
|---|---|
| Edge to hole rim | ≥ max(**6 mm**, **2𝑡**) |
| Hole-to-hole (rim to rim) | ≥ max(**10 mm**, **2𝑡**) |
| Near corner ≥ 90° | Nearest hole edge ≥ **6.5𝑡** from tip of corner |
| Circular hole diameter | ≥ max(**6.4 mm**, **𝑡**) |
| Non-circular openings | Fillet radius ≥ **𝑡** |
| Bolt splice / bearing | Conventional peak stress up to **3×**; apply stress concentration factor **3.0**, or rigorous FE |
| Lateral-load bolted panes | FE of pane with hole/notch for accurate stress |
| Interface | Sufficient thickness of resilient gasket (less stiff than glass) |

All cutting / drilling / grinding **before** tempering (§4.2.3).

#### 15.9 Gaskets (§7.5.1) — **2020 Amend**

| Topic | Rule |
|---|---|
| Materials | Extruded silicone, EPDM, neoprene, or TPE **compatible with silicone sealant** |
| Both sides | Gaskets on both sides of the **glass pane** unless structurally glazed |
| Engagement | Continuous mechanical engagement to framing members |
| Dense / wedge | Min Shore A **70** (hollow) / **55** (solid) |
| Sponge | Min Shore A **35**; designed for **20–35%** compression; gap fillers only — **not** where performance relies on compression resistance |
| Wedge | Lock-in procedure to prevent disengagement |
| Structural sealant vicinity | Glazing gaskets, sealant backers in pockets, continuous spacer pads = black heat-cured silicone rubber |

#### 15.10 Setting blocks (§7.5.2)

| Rule | Detail |
|---|---|
| Material | Dense heat-cured silicone, EPDM, neoprene, or TPE compatible with silicone |
| Hardness | ≥ Shore A **80** |
| Support width | ≥ **80%** of glass thickness |
| Length | **25 mm per m²** of glass area; minimum **100 mm** each if panel width > **800 mm** |
| Location | Equidistant from centreline at **quarter points**; may move to **eighth points** to reduce transom bending, but ≥ **150 mm** from nearest vertical glass edge |
| Side blocks | Between mid-height and top corner; positively retained |
| Bolting / point fittings | Use FE for induced glass stresses |

---

### 16. Testing matrix architects must programme (§8)

| Test | When / what | Acceptance highlight |
|---|---|---|
| **Heat soak** (§8.1.1) | All tempered panes — BS EN 14179-1 | Hold 260±10°C ≥2 h; see §17 |
| **Fragmentation** (§8.1.2) | Each tempered batch after heat soak — BS EN 14179-1 §10 | ≥40 particles / 50×50 mm (t<15); ≥30 (t≥15); longest ≤100 mm |
| **GASP surface stress** (§8.1.3) | HS & tempered — ASTM C1279 / C1048 | HS 24–52 MPa; tempered ≥69 MPa; avg of 10 readings (5 locs × 2 dirs) |
| **Thickness / flatness / roller wave** (§8.1.4) | Manufacturer QC — ASTM C1036 / C1048 / C1651 | ≥ design min thickness; measure laminate / IGU layers separately |
| **Blemish** (§8.1.5) | ASTM C1036 | Rarely structural |
| **Boil test** (§8.1.6, Annex B2) | Before laminated production | 66±6°C 3 min → boiling 2 h; no bubbles/defects >12 mm from edge/crack |
| **Impact** (§8.1.7) | Barriers / balustrades — BS EN 12600 | **Class 1, no breakage**; asymmetric → test both faces unless one-sided risk only |
| **Bending** (§8.1.8) | Fritted / decorative — BS EN 1288-3 at room temp; composite action at **50°C** (Annex B1) | HOKLAS lab; FoS 2.0 on reduced strength; ≥5 specimens |
| **Sealant print review** (§8.2.1) | All SSG joints | Manufacturer reviews curing geometry; bite/thickness tabulated |
| **Adhesion** (§8.2.2) | ASTM C794 | Every sealant × all adjacent materials |
| **Compatibility** (§8.2.3) | ASTM C1087 | Sealant × finishes, coatings, gaskets, blocks, backer, concrete, steel, etc. |
| **CW system mock-up** (§8.3.1) | Before construction — HOKLAS | See §16.1 below |
| **Other systems** (§8.3.2) | As needed | Safety test with suitable loads to confirm design |

#### 16.1 Curtain wall performance mock-up (§8.3.1) — programme & cost

| Item | Requirement |
|---|---|
| Lab | Independent **HOKLAS**-accredited within scope; **prior to construction** |
| Height | ≥ **2-storey** height **or** full CW height with operable sash |
| Width | ≥ **3-module** width with **turning corner(s)** if any |
| Features | Architectural feature(s) if any |
| Sequence | Prep 𝑝₁ → repeated 𝑝₂ → safety 𝑝₃; both +ve and −ve; hold peaks ≥3 s; transition ≥1 s |
| 𝑝₁ | **0.5 × 𝑝₂** |
| 𝑝₂ (**2024 Amend**) | Net wind pressure **𝑃 on the mullion** of the representative portion per Wind Code **2019**; ≥ **5** pressure pulses |
| During repeated test — frame | Deflection ≤ §5.5.4 limits (L/180 or 20 mm ≤7.2 m; L/360 >7.2 m; cantilever L/90 or 20 mm) |
| During repeated test — glass | **No breakage**; pane deflection ≤ **L/60** |
| Safety 𝑝₃ | **1.4 × 𝑝₂** |
| Recovery | ≥ **95%** recovery 15 min after load removal; no separation, plastic deformation, or deleterious effect |

**SD:** Mock-up size (2 storeys × 3 bays + corner + features) must be in tender programme and cost plan. Include representative openables and special features — omitting them invalidates the test for those conditions.

#### 16.2 Annex B — laminated composite action test (awareness)

Specimen 360 × 1100 mm; 5 pcs per glass type; test at **50±3°C**; four-point bending (𝐿𝑏=200, 𝐿𝑠=1000); stress rate 2.0±0.4 MPa/s. Equivalent thickness → 𝜆_test; design 𝜆 ≤ min(𝜆_test, 0.7). **2024 Amend:** failure load notation 𝑊_max (was 𝐹_max).

Boil test (B2): three 300×300 mm specimens; 66±6°C 3 min then boiling 2 h.

---

### 17. Quality assurance & heat soak (§9) — tender / site hold points

#### 17.1 Factory QA (§9.1)

| Item | Requirement |
|---|---|
| Flat glass | ASTM C1036 (or equiv.) |
| HS / tempered | ASTM C1048 (or equiv.) |
| Factory | **ISO 9001** for HS and tempered |
| HS stress | Must stay **24–52 MPa**; reject if ≥52 MPa |
| Tempered QA scheme | Heat soak all panes; oven/equipment calibration; GASP; thickness/flatness/roller wave/fragmentation/impact; inspection/audit frequency by manufacturer **and** independent parties |

#### 17.2 Laminated / IGU QC (§9.2)

| Assembly | Key documents / tests |
|---|---|
| Laminated | Laminating / autoclave parameters (temp, pressure, time); boil test; especially strict if composite action used in design |
| IGU | Construction details, seals, gas, corners, spacers, process; ASTM **E2190** seal durability; secondary seal ASTM **C1249** for SSG |

#### 17.3 Heat soak process detail (§8.1.1 + §9.3)

| Phase / control | Requirement |
|---|---|
| Standard | BS EN 14179-1 for **all** tempered panes |
| Heating | Until last pane surface reaches **250°C** |
| Holding | All panes ≥250°C then hold **≥ 2 hours** at surface **260±10°C** |
| Cooling | Ends when oven air ≤ **70°C** |
| Heating rate | ≤ **3°C/min**; surface ≤ **290°C**; minimise time above **270°C** |
| Thermocouples | **8** monitoring (4 hottest + 4 coldest from calibration); insulated pads; calibrate 6-monthly at 100/200/300°C |
| Oven calibration | Typically yearly by independent lab experienced in heat-soak ovens; full load; one thickness or two consecutive thicknesses (not thick e.g. 22 mm alone); max glass weight / max dimension per calibration report |
| Largest / thickest pane | Monitored by one of the eight TCs |
| TC failure mid-process | Acceptable unless that TC was the highest/lowest heating-phase monitor |
| Compliance report | Manufacturer name; project; quantity & area; oven ID/location; calibration; 8 TC graphs (heat/hold/cool); breakage record; dates |
| QC supervisor | Independent data logger next to a calibration TC on largest/thickest pane; 1-min intervals; HOKLAS-calibrated logger |
| Discrepancy | If supervisor vs manufacturer > **5%** at holding → review/examine the process |
| Log book | All heat-soak details kept at factory |

#### 17.4 Structural sealant application QA (§9.4)

| Step | Requirement |
|---|---|
| Before application | Design drawings → manufacturer **print review** success; accessory samples → **compatibility**; substrate samples → **adhesion** |
| Application steps | Cleaning → priming → applying → tooling per manufacturer |
| Temperature | Optimum **10–35°C**; below 10°C watch dew point / frost |
| Factory two-part QC | Butterfly test, snap-time at equipment start-up; peel-in-adhesion on production materials; daily log |
| Deglazing test | Per manufacturer % of structurally glazed panes (on-site or factory before transport) |
| Deglaze checks | Bite size & thickness; adhesion to glass & frame; joint type/condition; appearance / colour uniformity / bubbles |

Incompatible accessories → discoloration / loss of adhesion → structural failure risk. Poor adhesion to glass/Al/SS → structural failure.

#### 17.5 Inspection, maintenance & repair (§9.5 + Annex D) — handover obligation

Above-pedestrian glazing makes condition a **public safety** issue. Annex D is good practice for owners — AP should ensure a **glazing section in the building maintenance manual** at handover.

**Two-track inspections (D1):**

| Track | Who | Frequency character | Purpose |
|---|---|---|---|
| **Routine** | Experienced management / maintenance staff (professionals preferred) | Frequent | Short-term safety/function; flag longer issues |
| **Planned** | Building professionals with glazing experience | Periodic, less frequent | Long-term strategy; avoid costly late repairs |

**Typical deterioration to watch (D2.1):** cracked/loose/broken/missing panes; scratches/chips; bulging/bowing/separation/delamination/rotation/displacement; metal corrosion / bimetallic; IGU fogging; laminate delamination; staining; missing/loose fixings; deteriorated gaskets; bad sealant; water behind CW/WW.

**Typical glass failure causes (D2.2):** under-thickness / overstress; thermal stress (~33°C ΔT ≈ 20.7 N/mm²); fin/rod buckling; edge/surface damage; deep scratches; weld splatter; windborne debris; **metal contact**; **NiS spontaneous tempered break**.

**Maintenance manual (D3.2) — for new buildings, written by the relevant designer** covering glazing systems, design documentation, management approach, record-keeping. If missing, owners should commission one ASAP.

**Minimum records (D3.4):** maintenance manual (glazing section); inspection/maintenance records; repair/modification records; approved drawings; component + manufacturer listing; data sheets/warranties; method statements / maintenance procedures.

**Routine scope (D4):** repair/replace broken; secure loose; clean drainage; identify staining; remove obscuring cladding if needed to see structure; escalate recurring / fall-risk issues to professionals.

**Planned scope (D5):** desktop review; detailed condition survey (NDT + selected destructive sealant tests); report + recommendations; update manual; design/cost/plan/supervise works; consult RSE if structural suspicion.

**SD / handover takeaway:** Budget maintainability (Access for External Maintenance CoP) **and** a designer-authored glazing O&M appendix — not a generic façade brochure.

---

### 18. SD checklist by project condition

#### 18.1 Every project with structural / façade glass

1. Map every glass location to §5.2.1 / §5.2.2 (laminated? multi-layer residual? >2.5 m² & ≥5 m?).
2. Movement strategy: interstorey drift, floor deflection, creep, temperature (tinted to 90°C).
3. Tempered anywhere → heat-soak + ISO 9001 factory in tender / QA plan.
4. Frit / sandblast / etch → 𝛾𝑠 0.5–0.625 + bending tests — do not assume clear-glass thickness.
5. Maintenance access + Annex D glazing manual in handover scope.
6. Coordinate Wind Code 2019, Loading Code barrier loads, FS Code fire glass, OTTV build-up, External Maintenance CoP.

#### 18.2 Curtain wall / window wall

7. Stick vs unitised decision with mock-up size (2 storeys × 3 modules + corners + features).
8. Fire/smoke stop between floors; corrosion; water/air; openables in mock-up.
9. Supporting member deflection: L/180 or 20 mm (≤7.2 m) often governs aluminium.
10. 2024: mock-up p₂ = net wind on mullion (Wind 2019).

#### 18.3 Structural sealant glazing

11. Dead load on setting blocks always.
12. Bite ≥6 mm; ratio 1:1–3:1; no long-term load on sealant.
13. ≥5 m height + 4-sided SSG → retainers on **two opposing edges** for **37%** reference wind (2020).
14. Print review + adhesion + compatibility + deglazing % before / during fabrication.

#### 18.4 Glass balustrades / barriers

15. Laminated; Class 1 impact no breakage within 1100 mm of FFL.
16. Infill: glass does not support handrail.
17. Free-standing: continuous clamps 100 mm wide × 12 mm thick metal, bolts ≤500 mm; clamp pocket in structure from GA.
18. Panic / congregating ≥2 panels: bridging handrail or residual laminated capacity.
19. Do not use pre-2024 weep-hole balustrade detail.

#### 18.5 Overhead / floors / stairs / canopies / skylights

20. Laminated multi-layer; residual capacity after one ply failure under characteristic loads.
21. Vibration comfort for walk-on glass.
22. Replacement access planned; damaged laminate can still fall as a sheet.

#### 18.6 Glass fins / atria / glass structure

23. 70 m² progressive-collapse cap; column/fin redundancy.
24. Fin major-axis strength −40%; LTB FoS 1.7; free-edge local buckling; restraints coordinated with architecture.
25. Corner side-wind; spider gasket; cable pre-tension always in tension.
26. Performance-based design + mock-up for complex systems.

#### 18.7 Point-fixed / clipped glass

27. Tempered for bolted; cover ≥50 mm dia; cantilever ≤ s/4.
28. Hole edge distances (2𝑡 / 6.5𝑡 / diameter ≥ 𝑡); stress concentration 3.0 or FE.
29. Clips: ≤600 mm; ≥4/pane; ≥50×25 mm cover.

---

### 19. What this Code does **not** set (use other docs)

| Topic | Go to |
|---|---|
| Characteristic wind / imposed / barrier loads | Wind Code 2019; Dead & Imposed Loads Code; B(C)R |
| Barrier height / occupancy horizontal load magnitudes | B(C)R ss. 36–38; Loading Code tables |
| Fire resistance period of glass | FS Code / fire-rated glass approvals |
| GFA / OTTV / daylight / ventilation | Cap. 123 / PNAP / OTTV CoP / B(P)R |
| Façade maintenance access geometry | CoP on Access for External Maintenance |
| Structural steel / Al / concrete frames | Respective structural CoPs (SUC, etc.) |
| Lift / fireman’s access | MOA / FS Code Part D |

---

### 20. Key referenced standards (quick index — Annex A)

| Use | Standard |
|---|---|
| Heat soak | BS EN **14179-1** |
| Impact / barriers | BS EN **12600** |
| Bending strength | BS EN **1288-3** |
| HS / tempered product | ASTM **C1048**; BS EN 1863 |
| Flat glass | ASTM **C1036** |
| Surface stress (GASP) | ASTM **C1279** |
| Roller wave | ASTM **C1651** |
| IGU performance | ASTM **E2190**; BS EN 1279 |
| SSG secondary seal | ASTM **C1249** / C1369 |
| Structural silicone | ASTM **C1184**; BS EN 13022-2; BS EN 15434 |
| Adhesion / compatibility | ASTM **C794** / **C1087** |
| Laminated durability | BS EN ISO **12543**; ANSI **Z97.1** |
| Fin buckling reference | AS **1288** App. C (basis of Annex C) |
| Glazing practice | BS **6262**; BS 5516 (sloping / patent) |
| Barriers (UK practice ref.) | BS **6180** |

---

*Source: Code of Practice for Structural Use of Glass 2018 (BD), with Amendments 2020 and February 2024. Summary is for schematic design coordination — not a substitute for RSE design or the full Code text.*

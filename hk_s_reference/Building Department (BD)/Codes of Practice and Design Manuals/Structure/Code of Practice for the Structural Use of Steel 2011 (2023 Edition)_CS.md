# Code of Practice for the Structural Use of Steel 2011
**Architect critical summary for schematic design**  
2011 Code (**2023 Edition**, March 2023) | Buildings Department | Limit-state design  
Companion: Explanatory Materials (`EMSUOS2011e.pdf`) · Amendments: April 2026 (`SUOS2011e_Amend202604.pdf`) — both in `source_reference/`

> Scope note: Deemed-to-satisfy guidance for structural steel buildings under the Buildings Ordinance / B(C)R. Cross-check **Dead & Imposed Loads**, **HKWC**, **HKCC**, **Foundation Code**, **FS Code / Fire Resisting Construction**, **CoP on Access for External Maintenance**, and BD steel PNAPs (e.g. APP-168).  
> **April 2026** (mandatory on top of 2023 Edition): tall-building accelerations → **HKWC** 1-yr & 10-yr peaks; CFST steel **235–690** / concrete **C25–C80** (+ QA if >C60); dissimilar-grade welds → consumables to the **lower** grade; footbridge vibration §13.6.4; mechanised/automatic welding.

---

## Regulatory Overview

This Code covers **limit-state design of structural steel buildings and allied structures** (including footbridges linking buildings), using hot-rolled, hollow, and cold-formed products from acceptable AU / CN / JP / US / BS-EN sources. It does **not** cover highway/railway bridges, nuclear or pressure vessels, fibre composites, or steel with yield **> 690 N/mm²** (ultra-high only by BA approval for proprietary ties etc.).

At schematic design, freeze **lateral system + diaphragm**, **span / beam / deck depth vs deflection–vibration–FRP**, **robustness tying / key elements**, **fire protection envelope**, **corrosion + maintenance access class**, and **façade-support movement strategy** before locking F-F, cores, mega-columns, outriggers, expansion joints, and cladding geometry.

---

## Critical main topics and subtopics

### 1. Scope, aims, and material ceilings (§1)

#### 1.1 What is in / out

| In | Out / limited |
|---|---|
| Structural steel **buildings** and allied structures | Road / rail bridges (use Highways Structures Design Manual) |
| Building-connecting **footbridges** (still cross-ref Highways manual) | Articulated access walkways, nuclear, pressure vessels |
| Hot-rolled sections, flats, plates, hot-finished & cold-formed hollows, cold-formed open / sheet profiles | Fibre composites |
| Associated concrete, grout, rebar, stainless, aluminium (to HK / equivalent standards) | Steel **Ys > 690 N/mm²** generally |

#### 1.2 Aims of structural design (§1.2.1) — the brief checklist

Overall stability · Strength · Integrity / ductility / **robustness** · Fire resistance · Serviceability · Durability · Maintainability · Buildability · Economy.

#### 1.3 Material strength classes (§1.1 + §3.1)

| Class | Yield | Use at SD |
|---|---|---|
| **Class 1** | Ys ≤ **460 N/mm²**, QA + reference standard | Normal use |
| **Class 2** | ≤ 460, QA but not full reference-standard match | Use only after satisfactory tests |
| **Class 3 uncertified** | — | **py = 170 N/mm²**; minor / restricted applications only |
| **Class 1H** | **460 < Ys ≤ 690** | Allowed with QA; **global elastic analysis** for those members; helps ULS in heavy columns / long beams; **does not** improve fatigue or SLS deflection/vibration |
| **Class UH** | Ys > **690** | Not covered; BA case-by-case (e.g. proprietary high-strength ties) |

Other ceilings:

| Topic | Limit |
|---|---|
| Composite beams / slabs (§10, 2023) | Concrete ≤ **C60** cube; steel ≤ **460**; **no lightweight concrete** |
| Cold-formed thin gauge (§11) | Design yield ≤ **550 N/mm²** |
| Fire engineering (§12) | Hot-rolled ≤ 460; cold-formed ≤ 550; concrete ≤ 60; rebar ≤ 500 |
| Encased composite columns | Steel 235–460; concrete C25–C60 |
| **CFST** (Apr 2026) | Steel **235–690**; concrete **C25–C80**; special QA / curing for concrete **> C60** |
| Design working life | Assumed **50 years**; >50 years needs special design / QC / documentation |
| Plastic analysis | **Not** permitted for uncertified steel or Ys > 690 |
| Steel E / α / density (§3.1.6) | **E = 205 000 N/mm²**; α = **14×10⁻⁶ /°C**; density **7850 kg/m³** |

**Essential / civic buildings (EM §E1.2.7):** Hospitals, police / fire stations, power / fuel depots, major civic HQ — discuss **>50-year** working life with the client early (bridges often use 120 years as a comparator).

#### 1.4 Uncertified steel — hard “no” list (§3.1.4)

Class 3 uncertified (**py = 170 N/mm²**, elastic only) is **not** for:

- Primary elements of **multi-storey** buildings  
- Primary structure of single-storey **long-span** buildings  
- **Primary** = main beams spanning onto columns; any beam **> 6 m**; columns supporting **> 25 m²** floor; **any** member of the lateral system  

No welding unless mechanical / chemical / hardness tests prove suitability.

#### 1.5 Brittle fracture — thick / welded / external steel (§3.2 + EM §E3.2)

| Rule | SD note |
|---|---|
| When it applies | Tension, welded, or fatigue members with **any tensile** stress cycle — **not** pure compression |
| HK external Tmin | **0.1°C** (use colder for cold stores / overseas) |
| Cold-formed CHS/RHS | Reduce Tmin by further **5°C** if significant transverse bending |
| Thickness vs Charpy | Table 3.7: thicker plate + higher stress + higher grade → need **J0 / J2 / QT** qualities, not as-rolled JR |
| HK rule of thumb (EM) | Grade **355 J0** at high tensile stress / welded detail often caps near **~40–50 mm**; 100 mm mega-plates need specialist toughness + NDT, not “thicker = stronger” |
| Mega-columns / cover plates | Welded cover plates + butt splices under wind tension are classic brittle-fracture traps — prefer full-penetration, defect-free details; omit stress-raising covers where possible |
| Through-thickness (§3.1.5) | Through-thickness tension **> 90%** of py, or thick **T-butts / heavy double fillets** → specify **Z-quality** (lamellar tearing) |
| Dissimilar grades (Apr 2026 §3.4) | Weld consumables sized to the **lower** grade of the two parents |

**SD takeaway:** Do not shrink depth hoping high-strength steel alone will pass deflection, vibration, or fatigue — and do not assume thick high-grade plate is freely available for exposed / welded tension without Charpy + Z-quality planning.

---

### 2. Design methods and responsibility (§1.2 + §2.1)

#### 2.1 Who owns what

One **Responsible Engineer** owns: overall conceptual structural system; primary vertical and lateral load paths to ground; overall stability; robustness / integrity against disproportionate collapse; compatibility of those systems. Detail design by competent engineers under that supervision.

Foundations: **HK Foundation Code** + GEO; holding-down bolts / baseplate anchorage per §9; foundation loads must state whether factored and which γf.

#### 2.2 Simple / continuous / semi-continuous (§2.1.2–2.1.4)

| Method | Joint assumption | SD consequence |
|---|---|---|
| **Simple design** | Nominally pinned; joints do not develop moments that hurt members | Needs a **separate** bracing / core system for all lateral and sway |
| **Continuous design** | Rigid joints; elastic or plastic analysis | Moment frames can provide lateral resistance; joints need stiffness + capacity; for Class 1H use **elastic global** analysis |
| **Semi-continuous** | Partial strength / stiffness | Joint moment, stiffness, rotation capacity from tests or calibrated advanced analysis; bolts/welds must not be the ductile fuse failure mode |

Alternatives: design justification by **loading tests** (§16); **performance-based design** if BA accepts justification against §1.2.1 aims.

---

### 3. Limit states, loads, and factors (§2 + §4)

#### 3.1 ULS vs SLS (Table 2.1)

| ULS | SLS |
|---|---|
| Strength (yield, rupture, buckling, mechanism) | Deflection |
| Stability (overturning, sliding, uplift, sway) | Human-induced vibration |
| Fire resistance | Wind-induced vibration |
| Brittle fracture & fatigue fracture | Durability |
| Cold-formed: excessive local deformation → treated as **ULS** | |

#### 3.2 Normal load combinations (Table 4.2 — architect-facing)

| Combination | Dead adverse | Imposed adverse | Wind | Temp. |
|---|---|---|---|---|
| 1 Dead + imposed | **1.4** | **1.6** | — | 1.2 |
| 2 Dead + lateral | **1.4** | — | **1.4** | 1.2 |
| 3 Dead + lateral + imposed | **1.2** | **1.2** | **1.2** | 1.2 |

Also: differential settlement γf = **1.4** (comb. 1–2) / **1.2** (comb. 3); beneficial earth/water γf ≤ **1.0**; adverse factors never below **1.2**.

#### 3.3 Other load effects that hit architecture early (§2.5)

| Action | SD note |
|---|---|
| Dead / imposed / wind | From B(C)R + HKWC |
| Earth & water | Actual site conditions; beneficial factor capped |
| Differential settlement | Include when ULS or SLS sensitive (transfers, long podium frames) |
| Temperature (HK average) | **+0.1°C to +40.0°C** average; façade / cable / pretension systems need clause 13.3 ranges (much hotter on dark / tinted surfaces) |
| Cranes | Overhead / tower / derrick / mobile — manufacturer envelope + typhoon; uplift restraint |
| Notional horizontal | See §4 below |
| Exceptional / key elements | Explosion **34 kN/m²** or vehicle impact |
| Construction / temporary works | Most adverse sequence; separate factors |

---

### 4. Robustness, tying, and key elements (§1.2.3 + §2.3.4 + §2.5.8–2.5.9)

#### 4.1 Four mandatory robustness provisions

1. Tension continuity tying — **horizontal and vertical**  
2. Resist minimum **notional horizontal** load  
3. Survive removal of a non-key vertical element via alternative paths (large permanent deformation OK)  
4. Design **key elements** where removal would take too much area  

Each portion between **expansion joints** = separate building for robustness.

#### 4.2 Horizontal tying rules

| Rule | Detail |
|---|---|
| Where | Every **principal floor**; roof too unless cladding ≤ **0.7 kN/m²** and roof only carries wind + imposed roof load |
| Layout | Continuous lines near edges and along **every column line**; re-entrant corners anchored into frame |
| Forms of tie | Steel members; rebar into concrete; **mesh in composite slab** with profiled sheets **stud-connected** to beams |
| Steel ties & ends | Factored tension ≥ **75 kN** (not additive) |
| Internal ties | **0.5 (1.4Gk + 1.6Qk) st L** ≥ 75 kN |
| Edge ties | **0.25 (1.4Gk + 1.6Qk) st L** ≥ 75 kN |
| Edge column anchorage | Greater of tie force, **75 kN**, or **1%** of max factored D+L in column above/below |
| Column continuity | Columns through at beam–column joints unless frame fully continuous in ≥1 direction |
| Column splices | Tension ≥ largest factored vertical reaction at a floor between splices |
| Braced systems | Distributed so large plan areas are not hung off **one** lateral-resisting point |
| Precast / heavy units | Anchored along span to each other or supports (Precast Concrete CoP) |

#### 4.3 Element removal / key elements

| If conditions a–c (tying / columns) not met | Check storey-by-storey hypothetical removal of each column |
|---|---|
| Collapse area limit | ≤ **15%** of floor/roof area **or 70 m²** (lesser), at that level **and** one adjoining level |
| Exceeds limit | Design as **key element** |
| Key element load | **34 kN/m²** explosion (or B(C)R vehicle impact), one direction at a time + attached reactions limited to what connections can transmit |
| Lateral restraint vital to a key element | That restraint is also a key element |

#### 4.4 Notional horizontal forces (Table 2.2)

| Structure | Minimum |
|---|---|
| Normal buildings | Greater of **0.5%** factored D+L or **0.5 kN/m²** on enclosing elevation |
| Temporary works / sway ultra-sensitive (scaffold, falsework, grandstands, platform floors) | Greater of **1.0%** or **1.0 kN/m²** |

Applied each floor/roof, one direction, with comb. 1; **not** with wind / overturning / pattern / temperature; does not feed foundation net reactions. Alternative: explicit geometric imperfection in P-Δ analysis (frame imperfection amplitude often **h/200**).

**SD takeaway:** Expansion joints, transfers, re-entrant corners, discontinuous columns, and mega-columns are robustness design drivers — not “detailing later.”

---

### 5. Serviceability — deflection, wind comfort, floor vibration (§5)

#### 5.1 Deflection limits (Table 5.1) — exceedance needs full justification

**a) Profiled steel sheeting**

| Condition | Limit |
|---|---|
| Construction, ponding **not** in calc | Span/**180** (≤ **20 mm**) |
| Construction, ponding considered | Span/**130** (≤ **30 mm**) |
| Roof cladding under D+W | Span/**90** (≤ **30 mm**) |
| Wall cladding lateral under wind | Span/**120** (≤ **30 mm**) |

**b) Composite slab**

| Condition | Limit |
|---|---|
| Imposed | Span/**350** (≤ **20 mm**) |
| Total + prop removal − slab self-weight | Span/**250** |

**c) Beams (imposed)**

| Condition | Limit |
|---|---|
| Cantilevers | Length/**180** |
| Plaster / brittle finish | Span/**360** |
| Other beams (not purlins/rails) | Span/**200** |
| Purlins / sheeting rails | To suit cladding |

**d) Horizontal drift**

| Condition | Limit |
|---|---|
| Topmost storey of buildings | Height/**500** |
| Relative inter-storey | Storey height/**400** |
| Single-storey portal (no human occupancy) / portal columns | To suit cladding |
| Crane runway columns | To suit crane |

**e–f) Cranes & trusses**

| Condition | Limit |
|---|---|
| Crane girder vertical (static wheel) | Span/**600** |
| Crane girder horizontal (top flange) | Span/**500** |
| Typical truss (no brittle panels) | Span/**200** |

Notes: precamber may be deducted; **ponding must be avoided**; long spans need vibration check; cladding / CW / partitions detailed for **actual** drift and movement.

#### 5.2 Wind-induced vibration — tall buildings (§5.3 + EM §E5.3.4)

| Trigger | Action |
|---|---|
| Low natural frequency or large height / least-dimension ratio | Dynamic + static analysis; HKWC |
| Slender / flexible / lightly damped; long afterbody; mass–stiffness eccentricity; aspect ~**≥ 5:1** | Cross-wind / lock-in risk → specialist + often wind tunnel |
| Drift vs finishes | **H/500** and **Hstorey/400** still apply; CW / partitions / finishes must absorb drift |
| Comfort — **2023 Edition** (historic) | Worst **10 min** of **10-year** wind: Residential **15 milli-g**; Office/Hotel **25 milli-g** |
| Comfort — **Apr 2026** (current) | **1-year and 10-year** peak accelerations ≤ **HKWC** limits — fixed milli-g table **withdrawn** |
| Often adequate without dynamic study | Top drift ≤ **H/500** under HKWC design wind for typical buildings — always building-specific |
| Quick frequency estimate (EM) | Lowest mode ≈ **f₀ = 46 / H** (H in metres) — flag tall / soft towers early |
| If exceeded | Add mass / stiffness / damping; change aerodynamic shape; agree client comfort vs HKWC minimum |

Communication / broadcasting towers: SLS set by antenna performance, not occupant comfort.

#### 5.3 Human-induced floor vibration (§5.4)

Check when deflection limits exceeded, or for lightweight / long-span floors, or vibration-sensitive uses (dance, aerobics, factory, etc.). Refer Annex A2.5. Apr 2026 adds footbridge vibration response (§13.6.4) and steel-frame vibration references.

**SD takeaway:** Thin long-span composite decks often fail **vibration before strength** — do not freeze F-F on strength depth alone.

---

### 6. Durability, corrosion, and protective systems (§5.5 + §14.6)

#### 6.1 Exposure classes (Table 5.2)

| Class | Type | Examples |
|---|---|---|
| 1 | Non-corrosive | Internal dry controlled; piles in non-corrosive undisturbed ground |
| 2 | Mild | Internal humid |
| 3 | Moderate | Steel in perimeter cladding; external dry climate |
| 4 | Severe | External rain/humidity; internal over pool / kitchen / water tank |
| 5 | Extreme | Marine; corrosive ground; salt water |

#### 6.2 Maintenance access class

| Class | Meaning |
|---|---|
| **A** | Easy / regular maintenance |
| **B** | Difficult / infrequent |
| **C** | Extremely difficult or **impossible** access |

#### 6.3 Protection system selection (Table 5.3)

| System | Typical exposure | Min. access class |
|---|---|---|
| Bare steel | 1 | n/a |
| Paint | 2–4 | B |
| Paint + cementitious / sprayed-fibre fire protection | 1–2 | B |
| Concrete encasement (also structural composite) | 1–4 (maybe 5) | C |
| Galvanize / metal spray | 3–4 | C |
| Stainless / weathering steel | 3–5 | C |
| Sacrificial thickness | 4–5 | C |
| Cathodic protection | 5 | B |

Practical rules:

- Hot-dip galvanizing ≥ **85 μm**; vent hollow sections; expect **distortion** from stress relief  
- **ISO 10.9+ bolts** — do **not** galvanize (sherardize + suitable paint)  
- High-strength steel **> 460** may crack in galvanizing  
- Always coordinate **corrosion coating ↔ fire protection** (compatibility, thickness, inspection access)  
- Detail to avoid water traps; design inspection / recoating routes (§13.8)

**SD takeaway:** Perimeter steel buried in cladding is often Class 3–4 with Class B/C access — paint-only is a future liability; align with BMU / external-maintenance CoP.

---

### 7. Analysis, sway classification, and imperfections (§6)

#### 7.1 Frame classification by λcr (elastic critical load factor)

| Classification | Condition (ordinary analysis) | Design implication |
|---|---|---|
| **Non-sway** | λcr ≥ **10** (advanced: ≥ **15**) | P-Δ may be ignored |
| **Sway** | **5** ≤ λcr < **10** (advanced: < 15) | Amplify moments / second-order methods |
| **Sway ultra-sensitive** | λcr < **5** | **Only** second-order P-Δ-δ or advanced analysis |

First-order indirect methods have further λcr floors (e.g. non-sway λcr ≥ 10, sway λcr ≥ 5 for certain procedures).

#### 7.2 Imperfections

- Frame: equivalent geometric imperfection (commonly **h/200**) **or** notional horizontal forces  
- Member bow / out-of-straightness for compression members  
- Bracing members sized for restraint forces  

#### 7.3 Connection modelling in analysis

Pinned · Rigid · Semi-rigid — model must match physical joint; masonry infill or profiled sheeting stiffness may be credited if justified.

**SD takeaway:** Soft moment-frame towers without adequate cores drift into sway / ultra-sensitive territory — core size and bracing locations are SD decisions.

---

### 8. Section classification and member behaviour (§7–§8) — what drives size

#### 8.1 Cross-section classes

| Class | Behaviour |
|---|---|
| **1 Plastic** | Can form plastic hinge with rotation capacity for redistribution |
| **2 Compact** | Can develop plastic moment but limited rotation |
| **3 Semi-compact** | Elastic extreme-fibre yield; no full plastic redistribution |
| **4 Slender** | Local buckling before yield — use **effective width** or **effective stress** |

Plastic global methods need Class 1 (and Class 2 limited); Class 1H members use elastic global analysis with classification still governing section capacity.

#### 8.2 Beams — architect-relevant rules

| Topic | Rule |
|---|---|
| Lateral restraint strength | Typically **2.5%** of max compression-flange force (or squash load) |
| System of restraints | Sum of restraints ≥ 2.5% flange force; each ≥ ~1.25% rules as detailed |
| Web openings / services | Designed to §8.2.3 — large ducts need early coordination; openings change shear/moment capacity and LTB |
| Castellated beams | Covered but special checks; not a free “deeper for free” move |
| Destabilizing loads (load above shear centre without restraint) | Longer effective lengths for LTB — e.g. bottom-flange hangers, some roof loads |
| Plate girders | Min web thickness for serviceability and flange buckling; stiffeners affect fire protection and finish |

#### 8.3 Columns / compression

| Topic | SD note |
|---|---|
| Effective length | Depends on sway vs non-sway end restraints (charts §6.6 / §8.7) |
| Slenderness | λ = LE / radius of gyration; buckling curves a0–d by section type |
| Simple construction | Often assumes beam reactions with eccentricity / notional moments |
| Combined axial + moment | Cross-section + member buckling interaction — transfer floors and outriggers are critical |

#### 8.4 Portal frames (§8.11)

In-plane and out-of-plane stability; haunches and eaves restraints affect clear height and cladding rails — coordinate early for industrial / low-rise.

---

### 9. Connections, baseplates, and anchors (§9)

| Topic | Architect / SD hook |
|---|---|
| Welded vs bolted | Site welding → noise, fire watch, NDT access; bolted → splice space and cover |
| Through-thickness / Z-quality | Thick T-butts, heavy double fillets, tension > **90%** py through thickness → lamellar tearing risk |
| Dissimilar grades (Apr 2026) | Consumables follow the **lower** parent grade |
| Fillet / butt weld strengths | Drive plate sizes at exposed architectural junctions |
| Bolt end / edge distances | Affects connection depth and cladding clearances |
| HSFG / preloaded bolts | Slip-critical joints for fatigue / vibration-sensitive structures |
| Hollow-section lattice joints | Complex geometry; architectural expression needs early RSE buy-in |
| **Column baseplates** | Size, thickness, grout, holding-down bolts — interface with waterproofing, plinths, finishes; **exposed** thick bases also need brittle-fracture grade |
| Anchors / hangers | Tension capacity, edge distances, fire, corrosion |

---

### 10. Composite construction — HK default deck (§10)

#### 10.1 Materials envelope

| Item | Limit |
|---|---|
| Structural steel in composite beams/slabs | ≤ **460 N/mm²** |
| Concrete | Normal weight **C25–C60** (2023); **no LWC** |
| Encased columns | Steel 235–460; C25–C60 |
| CFST (Apr 2026) | Steel **235–690**; concrete **C25–C80**; QA for >C60 |
| Shear studs | Headed studs primary; other connectors by test/reference |

#### 10.2 Depth rules that set F-F

| Rule | Value |
|---|---|
| Min overall slab depth **Ds** | ≥ **90 mm** |
| Concrete above top of ribs (Ds − Dp) | ≥ **50 mm** |
| Cover above top of shear connectors | ≥ **15 mm** |
| Underside of sheets | Corrosion protection for environment + site storage |

#### 10.3 Fire insulation thickness (nominal minima if no other data)

**Trapezoidal** — concrete thickness **above** sheets (excl. non-combustible screeds):

| FRP (h) | 0.5 | 1 | 1.5 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| mm | 60 | 70 | 80 | 95 | 115 | 130 |

**Re-entrant** — overall slab thickness:

| FRP (h) | 0.5 | 1 | 1.5 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| mm | 90 | 90 | 110 | 125 | 150 | 170 |

FRP duration itself from **Fire Resisting Construction / FS Code**.

#### 10.4 Construction stage — propping, ponding, loads

| Item | Value / rule |
|---|---|
| Basic construction load | ≥ **1.5 kN/m²**; for span < 3 m ≥ **4.5 / Lp** kN/m² |
| Partial factors (typical) | Construction load **γf = 1.6**; sheet + wet concrete self-weight **γf = 1.4** |
| Pattern on continuous sheets | End span full; adjacent span 1/3 construction load or unloaded (whichever critical) |
| Storage load (separate case) | ≥ **3.0 kN/m²** with sheet self-weight — **not** with wet concrete + construction load |
| Ponding | Extra concrete from sheet deflection added to permanent load on beams if Δ large |
| Sheet deflection | Table 5.1; if Δ > Ds/10 include ponding concrete in deflection calc |

Propped construction: expect more hogging reinforcement over supports for crack control. Mild exposure longitudinal support rebar ≥ **0.2%** of concrete area above sheets (HKCC mild).

#### 10.5 Shear connectors — detailing that hits slab edge & MEP

| Rule | Limit |
|---|---|
| Max longitudinal spacing (normal) | **600 mm** or as capacity requires |
| Grouped connectors | Mean spacing as above; max **8 Ds** with due force redistribution |
| Min stud spacing | **5d** along beam; **4d** between adjacent; staggered lines ≥ **3d** |
| Stud diameter vs flange | If not over web, d ≤ **2.5 ×** flange thickness |
| Stud height vs deck | Height ≥ **Dp + 35 mm**; for capacity formulae height capped at **2Dp** or **Dp + 75 mm** |
| Edge of concrete flange to nearest stud | Dimensional minima in §10.3.5 (keep slab edge / upstand coordinated) |
| U-bars at ends | ≥ **15 mm** below top of studs when required |
| Ribs // or ⊥ to beam | Different shape factors k; non-central studs in ribs → capacity drop |

#### 10.6 Effective width & analysis (SD span planning)

Composite beam effective flange width depends on span and beam spacing — wide bays with few beams may not mobilise full slab width. Continuous composite beams: moment redistribution limits by section class; propped vs unpropped changes camber and crack pattern.

**SD takeaway:** Lock FRP → deck type/depth → beam depth → F-F **together**. A “120 mm deck” can fail 2-hour FRP on trapezoidal profile.

---

### 11. Cold-formed steel (§11)

| Topic | SD note |
|---|---|
| Yield | Up to **550 N/mm²** for thin gauge |
| Use cases | Secondary members, purlins, rails, light frames, sheet piles, some hollows |
| Local buckling / flange curling | Controls thin sections — appearance and stiffness |
| Connections | Screws, rivets, bolts — different from hot-rolled practice |
| Footbridges | Cold-formed **should not** be used where fatigue predominates unless data available |

---

### 12. Fire-resistant design (§12)

#### 12.1 Principles

| Requirement | Meaning |
|---|---|
| Mechanical resistance | Members keep capacity through FRP; no structural integrity failure |
| Compartmentation | Separating members + **joints** maintain integrity and insulation for full FRP |
| Fire exposure | **Standard** fire (ISO-type time–temperature) **or** justified **natural** fire |
| Fire limit state | Accidental limit state |
| FRP source | Current CoP for Fire Resisting Construction |
| Protection thickness | Accredited **standard fire tests** + qualified assessment; or limiting-temperature / performance-based / simplified methods |
| Connections & stiffeners | Same protection thickness as primary member |
| Bracing needed at fire limit state | Remain functional unless alternate paths; prefer bracing inside other FR construction |
| High-rise beam–core connections | **Fire-protect** even if unprotected beams justified by fire engineering |

#### 12.2 Strength at elevated temperature (order of magnitude)

Hot-rolled steel strength reduction rises sharply above ~**400–500°C** (e.g. ~0.6 at 500°C / 0.5% strain; ~0.35 at 600°C). Fire protection or fire engineering must keep steel below critical temperature for the applied load ratio.

#### 12.3 Failure criteria in standard tests

Load-bearing members: limiting deflection and rate of deflection (e.g. flexural members often cited around **L/30** regime in assessment methods — exact criteria in §12.2). Separating elements: integrity + insulation.

**SD takeaway:** “Unprotected steel” strategies still leave connections, bracing, cores, and compartment junctions as coordination items (bulkheads, shaft walls, cover).

---

### 13. High-rise steel / composite buildings (§13.1)

#### 13.1 Common HK systems

1. Perimeter steel columns + composite floors + **concrete core**  
2. Perimeter **moment frames** + composite floors + core  
3. **Tube-in-tube**  
4. **Outriggers** + mega composite perimeter columns + core  
5. External mega trusses / space frames  
6. Giant portal / mega frames  

#### 13.2 Coordination traps

| Issue | Action |
|---|---|
| Overall overturning / uplift | B(C)R stability; tension at columns/core ↔ piles |
| P-Δ / P-δ | Budget second-order analysis for tall flexible towers |
| Outriggers | Differential shortening (steel columns vs concrete core) + creep; jacking/wedge lock stage is a design decision |
| Lift cores | Tighter verticality for high-speed lifts |
| Beam–core ties | ≥ internal tie formula, ≥ **75 kN**; ductile catenary; **fire protect** |
| Mega-column restraint | Often **1%** of max factored D+L in column (or non-linear buckling study) |
| Escape / refuge / evacuation lifts | Remain functional for egress duration under extreme events |
| Wind | §5.3; wind tunnel for non-conventional form / complex topography; consider future removal of neighbours |
| Non-structural elements | Pipes, CW, windows checked against sway |

---

### 14. Glass & façade supporting structures (§13.3)

| Requirement | Rule |
|---|---|
| Member deflection supporting glass/façade | ≤ **span/180** unless rigorous flexible-support analysis |
| Analysis | Remain **elastic** under ultimate factored loads |
| Movements | Main-structure drift, creep, settlement, thermal, wind, imposed |
| Temperature ranges (local) | External ambient **0–40°C**; internal **5–35°C**; dark sun surface **0–80°C**; light **0–60°C**; clear glass surface **0–50°C**; tinted **0–90°C** — ΔT from **installation** temperature |
| Contact | No direct steel-on-glass / granite / aluminium — flexible separators |
| Progressive panel failure | Sequential collapse must be avoided |
| Patch wind on trusses | Full / half wind patterns on spans/bays |
| Support arrangement | Suspended systems common; if propped along span or rigid both ends, interaction with main structure must be analysed |

**SD takeaway:** Mullion spans, CW brackets, and slab-edge details are governed by span/180 **and** interstorey drift — coordinate before freezing F-F.

---

### 15. Temporary works (§13.4)

| Topic | Rule |
|---|---|
| Risk | Collapse often from buckling, poor bracing, excessive out-of-plumb |
| Out-of-plumb ≤ 10 m height | Inclination **1%** (or equivalent notional force) |
| Out-of-plumb > 10 m | Reduced inclination formula (§13.4.3) |
| Second-order effects | Required for slender temporary systems |
| Fitness / sleeve / splice tolerance | Explicit in analysis |
| Clearance | Specified; design for wider tolerance if site reality demands |
| Used systems | Fitness for re-use controlled |
| Notional force | 1% / 1.0 kN/m² class when sway ultra-sensitive |

---

### 16. Long-span structures (§13.5)

| Topic | Guidance |
|---|---|
| Character | High span-to-depth ratio (stadia, hangars, large roofs) |
| Deflection (preliminary) | Often **span/360** under live+wind if no tighter brief; much tighter for hangar doors / operable roofs |
| Wind / vibration / fatigue | Roof elements and cables may need damping; fatigue possible |
| Maintenance access | Often very difficult → specify **high-durability** protection (Class C thinking) |
| Extreme events | Robustness and key-element thinking still apply |
| Dimensional tolerance | Interconnected long-span components need tight fabrication control |

---

### 17. Footbridges (§13.6)

| Topic | Guidance |
|---|---|
| Philosophy | Constructability, strength, SLS, fatigue, vibration, bearings |
| Vertical deflection (Table 13.1) | Decks generally: δmax **L/250**, δ2 **L/300**; roofs generally **L/200** / **L/250**; roofs frequently carrying people **L/250** / **L/300**; appearance-critical δmax **L/250** |
| Cantilevers | Use **2 ×** projecting length as L |
| Fatigue | Crowd-induced vibration may require fatigue check; cold-formed discouraged if fatigue dominates |
| Vibration | Critical for pedestrian comfort; Apr 2026 adds response requirements |
| Cross-ref | Highways Structures Design Manual still relevant for building links |

---

### 18. Crane support structures (§13.7)

| Topic | SD note |
|---|---|
| Vertical + horizontal dynamic / surge / crabbing | From §13.7 + manufacturer |
| Deflection | Span/600 vertical, Span/500 horizontal (Table 5.1) |
| Outdoor cranes | HKWC wind in working and typhoon conditions |
| Multiple cranes | Max reasonably simultaneous vertical + horizontal |
| Tower / derrick / mobile on permanent structure | Envelope of positions, slew, azimuth; uplift restraint |

---

### 19. Maintenance of steel structures (§13.8)

Design-in at SD:

- Access for inspection and recoating (Class A/B/C)  
- Avoid water traps and inaccessible interfaces  
- Corrosion ↔ fire protection compatibility  
- Health & safety for future maintenance  
- Link façade steel to **CoP on Access for External Maintenance** where applicable  

---

### 20. Fabrication, erection, accuracy (§14–§15)

| Topic | Coordination hook |
|---|---|
| Erection method statement | Craneage, splice locations, temporary bracing, sequence |
| Identification / handling / storage | Protect coatings and thin sections |
| Welding QA | Welder qualification, WPS, NDT scope/frequency (§14.3) |
| Shear stud welding | Through-deck welding quality controls composite action |
| Bolting | Ordinary vs preloaded; matching nut/washer standards |
| Baseplates / grouting | Interface with foundations and waterproofing |
| Erection stability | Temporary bracing until floors/diaphragms complete |
| Protective treatment | Paint, sprayed metal, galvanizing — §14.6 |
| Permitted deviations (§15) | Column plumb, beam level/alignment, splice fit — impact cladding, lifts, partitions |
| Temperature during erection | Account for thermal movement when fitting |

---

### 21. Loading tests and existing structures (§16–§17)

| Topic | When it matters |
|---|---|
| Loading tests (§16) | Novel systems, justification where calculation inappropriate; relative strength coefficient Annex B |
| Existing steel structures (§17) | Alteration / adaptive reuse; assessment load factors (adverse often **1.2**); material sampling for uncertified / unknown steel |

---

### 22. Fatigue — when architects should flag it (§2.3.3)

Consider fatigue for: crane-supporting members; crowd-loaded footbridges / floors with repetitive dynamic use; members with high stress ranges or severe stress concentrations; welded details with poor fatigue class; corrosive / immersed environments. Normal building ambient temperature cycles rarely govern. Damage-tolerant detailing and inspectability matter when fatigue is credible.

---

### 23. Schematic design checklist (architect × RSE)

1. **System:** core / braced / moment / outrigger / mega-frame; diaphragm continuity; expansion joints = robustness cuts.  
2. **Spans & depths:** Table 5.1 + vibration + FRP Tables 10.9/10.10 → F-F.  
3. **Lateral SLS:** H/500, Hstorey/400; tall / aspect ≥5:1 → HKWC accelerations (± wind tunnel); rough f₀ ≈ 46/H.  
4. **Frame stiffness:** aim to avoid sway ultra-sensitive (λcr < 5) unless second-order budget accepted.  
5. **Robustness:** continuous tying ≥ 75 kN; mega-columns 1% restraint; key elements if > 15%/70 m².  
6. **Fire:** FRP from FS/FRC CoP; protect connections, bracing, beam–core; compartment junctions.  
7. **Composite deck:** Ds ≥ 90 mm; ≥ 50 mm above ribs; construction load 1.5 kN/m² (or 4.5/Lp); prop strategy; no LWC.  
8. **Durability:** exposure + access class → coating / galvanizing / encasement; BMU / external-maintenance CoP.  
9. **Façade supports:** span/180; thermal ranges; no hard contact; movement joints for drift + creep.  
10. **Materials:** Class 1 ≤460 / Class 1H ≤690 / UH case-by-case; CFST C25–C80 (Apr 2026); Charpy + Z-quality for thick welded tension.  
11. **Uncertified steel:** never for primary multi-storey / long-span / lateral system (see §1.4).  
12. **Special uses:** footbridges (Table 13.1 + §13.6.4 vibration), cranes, long-span roofs, temporary works, existing frames.  
13. **Working life:** 50 years default; hospitals / essential services — discuss >50 years.  
14. **Amendments:** apply April 2026 before submission.

---

### 24. Quick reference — numbers architects quote most

| Item | Value |
|---|---|
| Design working life | **50 years** |
| Top drift / interstorey | **H/500** / **Hstorey/400** |
| Beam with brittle finish / typical beam | **Span/360** / **Span/200** |
| Glass/façade support member | **Span/180** |
| Min composite slab overall / above ribs | **90 mm** / **≥ 50 mm** |
| Horizontal tie minimum | **75 kN** |
| Collapse area limit | **15% or 70 m²** |
| Key element blast | **34 kN/m²** |
| Notional horizontal (buildings) | **0.5%** or **0.5 kN/m²** |
| Notional (temporary / ultra-sensitive) | **1.0%** or **1.0 kN/m²** |
| Non-sway / sway / ultra-sensitive λcr | ≥**10** / 5–10 / <**5** |
| Frame imperfection (typical) | **h/200** |
| Lateral restraint force (beams) | **2.5%** of flange force |
| Construction load on deck | **≥ 1.5 kN/m²** (or 4.5/Lp if span < 3 m) |
| Max stud spacing (normal) | **600 mm** |
| HK average temperature | **+0.1 to +40°C** |
| Steel yield ceiling (general / HSS) | **460 / 690 N/mm²** |
| Composite concrete (beams/slabs 2023) | ≤ **C60**, NWC only |
| CFST concrete (Apr 2026) | **C25–C80** (QA >C60) |
| Comfort accel (2023 text) | Res **15** / Office-Hotel **25** milli-g — **superseded Apr 2026 by HKWC** |
| Tall-building f₀ estimate (EM) | ≈ **46 / H** (H in m) |
| Footbridge deck δmax / δ2 | **L/250** / **L/300** |
| Long-span prelim deflection | Often **span/360** |
| Galvanizing min thickness | **85 μm** |
| Roof tie exemption cladding | ≤ **0.7 kN/m²** |
| Uncertified primary cut-offs | Beam **> 6 m**; column floor area **> 25 m²**; any lateral system |
| External Tmin (brittle fracture) | **0.1°C** (colder for cold store) |
| Through-thickness trigger | Tension **> 90%** py → Z-quality |
| Steel E / α | **205 000 N/mm²** / **14×10⁻⁶ /°C** |

---

*Schematic coordination only. Structural design, fire engineering, and BA submissions remain with the RSE / AP using the full Code, Explanatory Materials, April 2026 amendments, and current PNAPs.*

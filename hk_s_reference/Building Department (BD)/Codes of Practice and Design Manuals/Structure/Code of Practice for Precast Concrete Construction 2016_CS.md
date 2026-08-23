# Code of Practice for Precast Concrete Construction 2016
**Architect critical summary for schematic design**  
First issue April 2016 | Buildings Department  
Amendments: **November 2020** (corrosion cover → Concrete Code 2013; water seepage at connections; ASR mitigation expanded) · **June 2026** (bearing stress with confinement factor *m*; **AAMA 501.2** 100% field joint water test — PNAP APP-174)

> Scope note: Deemed-to-satisfy guidance for **structural and non-structural precast concrete** — façades, slabs, walls, stairs, beams, columns, volumetric modules, joints and connections. Design method is **Limit State** per **Code of Practice for Structural Use of Concrete 2013**; alternatives only with justifying calculations. Bridges/associated structures also check HyD **Structures Design Manual** (most onerous wins). Cross-check **B(C)R**, **Dead & Imposed Loads Code**, **Wind Code**, **FS Code** (cover / FRR of members **and** joint fillers), **PNAP APP-143** (QC / supervision), **APP-174** (amendments). RSE owns calculations; AP must lock **module grid, joint widths, façade lap, cast-in windows, tie/diaphragm strategy, topping + services depth, bearing nibs, and water-test programme** at SD.

---

## Regulatory Overview

This Code covers **design, construction and quality control of structural and non-structural precast concrete elements** (including joints and connections) for buildings and building works. Requirements apply equally to loadbearing frames and to non-structural façades / partitions — the latter still take self-weight and wind and must be designed like structural precast for connections and durability.

At schematic design, freeze **standardised panel/slab modules**, **joint width vs movement + full tolerance stack**, **lateral system (shear walls + floor diaphragms + continuous ties)**, **façade overlap (≥75 mm)**, **topping/conduit depth**, and **mock-up + AAMA 501.2 field water-test programme** before locking F-F, bay rhythm, window cast-in strategy, and crane/logistics envelope.

---

## Critical main topics and subtopics

### 1. Key definitions that change detailing language (§1.2)

| Term | Meaning for SD / detailing |
|---|---|
| **Equivalent monolithic system** | Precast frame/wall must have strength **and ductility** equivalent to comparable monolithic RC |
| **Isolated member** | Loss of one support → **no** secondary load path (needs larger bearing — see §5) |
| **Non-isolated member** | Can shed load to adjacent members if one support fails |
| **Simple / dry / bedded bearing** | Direct contact vs cementitious bedding — different allowable bearing stress |
| **Net bearing width** | Overlap after deducting ineffective (spalling) zones and construction inaccuracies |
| **Sealant classes** | Elastic / elastoplastic / plastoelastic / plastic — match to movement **rate**, not only amplitude |
| **Gasket / sealing strip / joint filler / bond breaker / back-up** | Different roles; polystyrene filler is **banned**; movement joints need bond breaker so sealant does not stick to back-up |

---

### 2. Planning decisions that freeze the architectural grid (§2.2 + §3.1)

#### 2.1 Conceptual planning

| Topic | SD constraint |
|---|---|
| **Standardisation** | Plan for repeated precast types; balance aesthetics vs mould reuse — unique one-offs kill programme/cost |
| **Buildability checklist** | Vehicle size limits; site access; crane capacity/reach; overhead lines/power; demoulding of large panels; propping/bracing; **joint widths** for safe alignment + movement + tolerances; jointing method; structural action; cost |
| **Voids & conduits** | Preform openings where practical; buried conduits **within** reinforcement layers — late chases are not free |
| **Layout drawings** | Complete plans, sections, elevations **and connection details** for every precast type |
| **Compatibility** | Split AP / RSE / façade / manufacturer responsibilities → **named party** for interface checks |
| **Demolition** | Prestressed systems need early demolition strategy |

#### 2.2 Production lead-in and shop drawings (§3.1)

| Item | Practical rule |
|---|---|
| Lead-in for moulds + trial units + connection proving | **Up to ~6 months** is not unusual — commit typology early |
| Delivery vs site storage | Factory output must match erection rate **and** available storage |
| Off-hours delivery | Flag early if site/transport rules force night deliveries (common for Guangdong factories) |
| Shop drawings must show | Shapes/dims; rebar/anchors/inserts; joints; production tolerances; lifting beams/frames/strongbacks; finishes; bearing seats; storage/lift/transport methods; **unique ID, location and orientation** marked on each unit |

**SD takeaway:** Module length/height, joint locations, cast-in windows, service openings, and mould-count strategy must be decided with RSE and manufacturer before GBP freeze — not during shop drawings.

---

### 3. Stability, drift, and robustness — before massing (§2.3)

#### 3.1 How precast buildings typically resist lateral load

Many precast frames are **pin-jointed** (no moment continuity like in-situ RC). Transverse stability then relies on **shear walls / sway frames** + **floors as horizontal plates** → **adequate ties between elements are mandatory**.

| Rule | Number / detail |
|---|---|
| Overall lateral deflection (wind only) | ≤ **H/500** of building height |
| Connection deformation | **Cumulative slip/deformation of connections at each level** must be **added** to analytical drift — total still ≤ H/500 (§2.3.2.2) |
| Notional horizontal (if wind does not govern) | **1.5%** of characteristic dead load at each floor (§2.3.1 / §2.5.1) |
| Temporary stability | Viable propping/bracing scheme for **every** erection stage, including sequencing and **timing of temporary-works removal** |
| High-risk cases | Long-span beams and high-rise — extra attention to temporary bracing |

**SD takeaway:** Soft-storey, discontinuous shear walls, large transfer floors, and expansion-joint breaks in diaphragm action must be resolved at SD with the RSE — not after panel types are ordered.

#### 3.2 Disproportionate collapse — continuous ties (§2.3.3 + §2.7.8)

Provide continuous **horizontal and vertical ties** (or equivalent). Ties may sit in topping, in precast, or both. Other loads may be ignored when sizing ties for these forces. Existing rebar in columns/walls/beams/floors may count toward tie area. Material γ for tie steel area = **1.0**.

| Tie type | Minimum tensile capacity |
|---|---|
| **Internal ties** (each floor & roof, two perpendicular directions) | Greater of \(T = \dfrac{(G_k+Q_k)}{7.5} \times \dfrac{l_c}{5} \times F\) or \(T = 1.0F\) (kN/m) |
| Internal tie spacing | Generally ≤ **1.5 \(l_c\)**; in walls within **0.5 m** of slab top/bottom; anchor to peripheral ties (except wall/column horizontals) |
| Single-direction cross/spine walls | \(l_c\) for force in wall direction = lesser of actual wall length **or** collapsed length between lateral supports / free edge |
| **Peripheral ties** | **1.0 F** kN per metre width; within **1.2 m** of building edge (or in peripheral wall) |
| **Horizontal ties to external bearing walls** (if peripheral tie not in that wall) | Greater of: lesser of **2.0 F** or \((h/2.5)F\); or **3%** of total design vertical load in wall/column at that level (*h* = clear storey height) |
| **Corner columns** | Tied in orthogonal directions per horizontal-tie rule |
| **Vertical ties** (each bearing wall/column) | Tensile force = max design dead + imposed from **any one storey** |
| Factor **F** | Lesser of **(20 + 4n)** or **60** (*n* = number of storeys) |

**Tie continuity / anchorage (§2.7.8.9–10):**

- Crossing ties: extend **12× bar dia** past the other tie, **or** full anchorage length beyond its centre-line.
- Re-entrant corners / abrupt construction changes: prove anchorage explicitly.
- Min in-situ thickness where ties run: ≥ bar dia (or **2×** at laps) + **2× max aggregate + 10 mm**.
- Continuity options: lap into in-situ between rough faces of same unit; lap into topping with stirrups ≥ tie tension; bars in topping with projecting stirrups from beams/slabs; or mechanical methods per §2.8.1.3.
- Precast floors/roofs **not** used as ties must still be **anchored** for their own dead weight into the tied structure.
- Place floor/roof ties to **minimise eccentricity**; corbel/nib end bars need full lap + construction-inaccuracy allowance.

**SD takeaway:** Isolated members (no alternate path) need **+20 mm** net bearing vs non-isolated (§2.7.9.5). Re-entrant corners and discontinuous column lines need early tie strategy.

---

### 4. Durability, cover, movement — façade and joint drivers (§2.4 + Nov 2020 amd)

#### 4.1 Durability factors to brief at SD

Shape/size · concrete constituents · cover · exposure · fire · protection/maintenance · production · transport/storage/install · **joint details**.

| Topic | SD implication |
|---|---|
| Shape | Good drainage — no standing pools / trapped moisture; avoid sharp corners and sudden section changes (stress concentrations → cracking/spalling); check slender units for buckling during lift |
| **Fire cover** | Per **FS Code** |
| **Corrosion cover** | Per **Concrete Code 2013** (Nov 2020 — not B(C)R alone); cover to brackets/fixings ≥ rebar cover |
| Joint fillers / sealants FRR | Must match **fire resistance of the precast members** |
| Fixings without adequate cover | Galvanised mild steel or stainless |
| Inaccessible connections | Corrosion-protect for life — no “inspect later” assumption |
| Connection fill | Prevent corrosion, cracking, spalling **and water seepage** (Nov 2020) |
| Thermal gradient panels | Reinforcement in **both faces** |
| Indirect effects | Early thermal, creep, shrinkage, temperature differentials — either limit cracking/deformation **or** provide bearings/movement joints; if restraint inevitable, design for it |

#### 4.2 Materials — ASR & chlorides (§2.6 + Nov 2020)

**Materials:** B(C)R **and** Concrete Code 2013; design properties from Concrete Code 2013.

**ASR (alkali-silica):** reactive alkali ≤ **3.0 kg/m³** Na₂O equivalent; HOKLAS mix design + certificates to AP/RSE. Nov 2020 also requires: expert advice before reactive aggregates; non-reactive aggregate per CS1; **and/or** reduce moisture ingress. Carbonate aggregates → specialist advice (alkali-carbonate risk).

**Chloride limits (Table 2.3)** — Cl⁻ % by mass of cement (incl. pfa/ggbs):

| Use | Max Cl⁻ |
|---|---|
| Prestressed / steam-cured | **0.10%** |
| Sulphate-resisting cement | **0.20%** |
| Embedded metal + OPC/RHC | **0.35%** |

---

### 5. Loads architects must brief — construction often governs (§2.5 + §2.7)

#### 5.1 Permanent and construction loads

| Load | Rule |
|---|---|
| Permanent | B(C)R + Dead & Imposed Loads Code |
| Construction imposed | Minimum **1.5 kN/m²** (increase for plant/storage) |
| Notional horizontal | ≥ **1.5%** characteristic dead |
| Accidental | Earth movement, construction-vehicle impact, etc. |

Temporary stages often **govern** member size: semi-precast slabs carrying self-weight + construction before topping; lower floors/stairs supporting props to upper levels; halvings under back-propping. Structural action/framing may differ in temporary stages → higher stresses.

#### 5.2 Demoulding equivalent load factors (Table 2.1) — flexural design of element only

| Product / finish | Exposed aggregate + retarder | Smooth mould (form oil) |
|---|---|---|
| Flat, removable sides, no rebates | **1.2** | **1.3** |
| Flat, with formed rebates/reveals | **1.3** | **1.4** |
| Fluted with proper draft | **1.4** | **1.6** |
| Sculptured | **1.5** | **1.7** |

Verify with manufacturer; add imposed/wind under correct combinations. Lifting-insert design uses Table 2.4, not these factors.

#### 5.3 Handling / transport / erection factors (Table 2.2)

| Stage | Factor on self-weight |
|---|---|
| Yard handling | **1.2** |
| Transportation | **1.5** (higher if poor roads) |
| Erection | **1.2** |

#### 5.4 Lifting inserts & bracing FoS (Table 2.4) — ultimate

| Item | FoS |
|---|---|
| Bracing members | **2** |
| Bracing connections / inserts cast into precast | **3** |
| Lifting inserts, normal | **4** |
| Lifting inserts, multiple use (e.g. manhole covers) | **5** |

Proprietary inserts preferred; rebar lifting eyes only if specifically designed. Design so **failure of any one insert** does not drop the element. Anchorage affected by edge distance, openings, concrete strength/thickness, embedment, cracking, nearby rebar/tendons, tensile stress field — get manufacturer SWL for the actual condition. Extra local rebar per Concrete Code + manufacturer.

**Bracing design (§2.7.6):** construction ≥ **1.5 kN/m²** + Wind Code wind.

#### 5.5 Design for movement (§2.7.7) — set joint matrix early

Causes: creep · early thermal shrinkage · long-term shrinkage · differential settlement · seasonal thermal · internal/external ΔT. Not all movements coexist — use timescales, ambient temperature, and **age of units at joint formation**. Include eccentricities from production/erection tolerances and cumulative moments at joints. Specify tolerances for precast **and** interfacing members; design units and joints for those tolerances.

**SD takeaway:** Do not thin slabs or shorten bearings on permanent loads alone — temporary stack and demoulding factors may set thickness, nib depth, and mould finish choice (sculptured finishes cost structure as well as aesthetics).

---

### 6. Bearings — geometry that eats clear span (§2.7.9 + June 2026 amd)

#### 6.1 Three integrity measures

1. Overlap of reinforcement in reinforced bearings  
2. Restraint against loss of bearing due to movement  
3. Allowance for cumulative production + erection tolerances (§3.17)

#### 6.2 Net bearing width

| Case | Rule |
|---|---|
| Non-isolated | Greater of (ultimate reaction) / (effective bearing length × ultimate bearing stress) **or 40 mm** |
| Isolated member | Non-isolated + **20 mm** |
| Effective bearing length | Least of: bearing length; **½ length + 100 mm**; **600 mm** |

Increase for free movement or rotation about the support. Nominal seating on drawings = net width **+ spalling allowances + construction inaccuracies**.

#### 6.3 Ultimate bearing stress — **use June 2026 values**

| Bearing type | 2016 original | **June 2026** \(f_{cb}\) |
|---|---|---|
| Dry on concrete | 0.4 \(f_{cu}\) | **0.27 m \(f_{cu}\)** |
| Bedded on concrete | 0.6 \(f_{cu}\) | **0.40 m \(f_{cu}\)** |
| Steel plate (each dim ≤40% of corresponding concrete dim) | 0.8 \(f_{cu}\) | **0.80 m \(f_{cu}\)** |

\(m = \sqrt{A_2/A_1} \le 2\) (confinement / load-spread — Fig. 2.5a). Intermediate values allowed for flexible bedding. Based on **weaker** of the two surfaces.

#### 6.4 Spalling allowances (Tables 2.5–2.6)

| Support / member condition | Distance assumed ineffective |
|---|---|
| Steel support | **0** from outer edge |
| Concrete ≥ grade 30 (general) | **15 mm** |
| Concrete < grade 30 (general) | **25 mm** |
| RC outer edge <300 mm deep, vertical loop ≤12 mm | Nominal end cover to outer-face rebar |
| Same, vertical loop ≥16 mm | Nominal cover + **inner bend radius** |
| Supported member: straight bar / horiz. loops / vert. loops ≤12 mm | Greater of **10 mm** or nominal end cover |
| Tendons or straight bars exposed at end | **0** |
| Supported member: vert. loops ≥16 mm | Nominal end cover + inner bend radius |

Chamfers within spalling zones may be discounted when measuring edges.

#### 6.5 Detailing flags

| Topic | Rule |
|---|---|
| Clearance / tolerance buffer | Combined clearance ≥ **√(sum of individual tolerances²)** |
| Steel shims | **Not** in spalling-prone zones; **remove after grouting**; detail for easy removal; if left in, design load path through shims |
| Wall load over end of supported member | **Bedded** bearing required |
| Horizontal forces at bearing (creep, shrinkage, temp, misalignment, out-of-plumb) | Sliding bearings, extra lateral rebar at top of support, **or** continuity ties between supported ends |
| Rotation at flexural end supports | Suitable bearings; allow for increased moments/stresses |
| Corbels | Design/detail per Concrete Code |
| Anchorage of slab ends on corbels/nibs | Full lap + construction-inaccuracy allowance |

**SD:** Thin architectural “bearing ledges” fail once net + spalling + tolerance are added. Freeze nib depth with RSE using **2026 \(f_{cb}\)**.

---

### 7. Structural connections (§2.8.1) — robustness of the joint itself

| Topic | SD / detailing rule |
|---|---|
| Catastrophic connection failure | Avoid connections whose failure collapses the structure — use an appropriate alternate detail |
| Fire & durability of connection | ≥ members being connected |
| Grout at interface | Free-flowing, self-compacting, **non-shrink** |
| Semi-precast balconies / lost forms | Construction-joint prep and specification are critical — monitor intent through to site details |
| Compression connection concrete area | Greater of **75%** of contact area **or** area of in-situ (excl. intruding slab/beam) — solid bearing portions of slab/beam may be included if properly bedded; **≤ 90%** of wall/column area |
| Shear ≤ **0.23 N/mm²** (in-plane) | No rebar needed if units restrained from separating; roughen smooth moulded faces |
| Shear ≤ **0.45 N/mm²** under compression | No rebar if rough as-cast faces |
| Castellated shear ≤ **1.3 N/mm²** on min root area | Prevent separation by steel ties or normal compression; limit key taper |
| Shear with reinforcement | \(V = 0.6 F_b \tan\alpha_f\); \(F_b =\) lesser of 0.87\(f_y A_s\) or anchorage value |
| \(\tan\alpha_f\) (Table 2.7) | Smooth **0.7**; rough/castellated without continuous in-situ strips **1.4**; with continuous strips **1.7** |
| Couplers | Cover ≥ rebar cover; locking device if vibration risk |
| Sleeves | Tensile/compressive capacity by test; alignment critical; cover ≥ rebar; watch congestion / bursting |
| Welding / loops / grouted apertures | Per Concrete Code + manufacturer/tests |
| Appendix A | Illustrative only — prove each connection for applied actions; note pinned vs moment intent |

---

### 8. Joints & façades — the AP’s primary SD package (§2.8.2)

#### 8.1 Sealant joints

| Rule | Number / note |
|---|---|
| Absolute minimum sealant joint width | **5 mm** (practicable minimum) |
| Common panel-to-panel gap | **≥ 12 mm** |
| Structural movement joints | Often **≥ 50 mm** (needs non-slumping sealant) |
| Elastic sealant | Min thickness **5 mm**; width:thickness **never > 1:1**; optimum **2:1** |
| Application | No free water on concrete; primers per manufacturer; remove form oils, curing compounds, silicone waterproofing admixtures, coatings that kill bond |
| Surface prep | Water jet, sand blast, wire brush, or retarder as needed; chamfers reduce edge damage |
| Back-up / bond breaker | Closed-cell foam, bond-breaker tape, or filler + tape — sealant must **not** adhere to back-up in movement joints |
| Expanded polystyrene | **Not** acceptable as joint filler |
| Joint filler properties | Compressible; non-extruding; resilient; non-staining; **no cellulose** (termite); damage-resistant; not a fire hazard |
| Sealant choice vs movement | Frequent/rapid → **elastic**; massive high-inertia slow movement → elastoplastic / plastoelastic / plastic may suffice |
| Failure modes to brief | Climate, environment, substrate incompatibility, abrasion, traffic |

#### 8.2 Gaskets

- Always under **compression** for proper function.
- Prefer **primary + secondary** contact points with air space between.
- Continuity at H/V junctions: factory **ladder/grid** gaskets; site limited to simple protected butt joints; else drainage + weather protection + adequate overlaps.
- Movement joints: maintain compression over full movement range without excessive set — e.g. cellular neoprene compress ≤ **50%** of uncompressed thickness.
- Natural rubber needs synthetic skin for weather; cellular materials need UV skin for durability; life may be **shorter than building life** — specify inspection/replacement in maintenance manual.
- Installation compression forces can be large — design components for gasket force.
- Do not stretch if avoidable; allow recovery before trim; clean surfaces; manufacturer lubricant only.

#### 8.3 Sealing strips

| Type | SD note |
|---|---|
| Mastic strips | Need initial + in-service compression; **unsuitable** if joint opens beyond assembled size |
| Impregnated/coated cellular (often pre-compressed) | Stay compressed per manufacturer over full movement; joint faces **parallel**; install depth:width ~**2:1**; in-service ≤ **1:1** — provide enough joint depth |

#### 8.4 Façade lap (critical architectural detail)

**Minimum overlap upper / lower precast façade panels: 75 mm** (upstand profile) — §2.8.2.7. This drives panel edge profile and storey-height joint geometry at SD.

#### 8.5 Maintenance of joints (§2.8.2.9)

Design for inspection, repair, replacement **without major disruption** to occupants (temporary removal of some interior finishes may be acceptable). Building maintenance manual must include: inspection schedule; expected replacement schedule; joints whose neglect causes major consequential damage; how to maintain; product identification.

#### 8.6 Watertightness testing — mock-up **and** site

**Factory / mock-up (§4.3.1)** — for façade units **not** monolithically connected to in-situ:

| Item | Requirement |
|---|---|
| Standards | ASTM E331 (static) + E547 (cyclic), modified for HK |
| Differential pressure | **20%** of max inward design wind, **≥ 0.77 kPa** |
| Water rate / duration | **3.4 L/min/m²** for **15 min** |
| Sampling | **0.5%** of each joint/panel type **or one** of each, whichever greater |
| Failure | Damp/leak during test **or within 2 hours** |
| Remedial | Identify cause; revise system; retest to pass; if any unit fails, RSE sets **additional** sampling rate |

**Completed joints on site (Table 2.7a — June 2026 / AAMA 501.2)** — panels-to-panels, panels-to-in-situ, panels-to-windows:

| Item | Requirement |
|---|---|
| Samples | **100%** |
| Nozzle pressure | **205–240 kPa** |
| Hose diameter | **19 mm** |
| Duration | **5 min per 1.5 m** joint length (slow nozzle travel) |
| Nozzle distance | **305 ± 25 mm** |
| Failure | Interior damp/leak during test **or within 2 hours** → remedy and **retest** until all pass |

Consider including panel-to-panel joints in window test assemblies. Rain inspection remains useful; hose spray alone is **not** a substitute for AAMA 501.2 after the 2026 amendment.

**SD takeaway:** Budget mock-up + full joint field-test programme; coordinate cast-in windows with joint geometry so testing is efficient.

---

### 9. Composite slabs / toppings — thickness that sets F-F (§2.9 + §3.16.9)

| Topic | SD constraint |
|---|---|
| Design basis | Concrete Code; props must keep stresses/deflections within limits |
| Relative stiffness | If component concrete strengths differ by **> 10 N/mm²**, use transformed section |
| Pre-tensioned units made continuous with in-situ over supports | Ignore prestress compression over tendon transmission length at ends |
| Differential shrinkage | Check tensile stresses; for T-beam + in-situ flange in normal indoor buildings, approx. **100×10⁻⁶** if no better data |
| Horizontal shear force | From ultimate moment — compression/tension above or at interface as applicable |
| Average → local \(v_h\) | Distribute average interface shear in proportion to vertical shear diagram; \(v_h\) ≤ Table 2.8 |
| Nominal links (if used) | ≥ **0.15%** of contact area; T-beam flange links spacing ≤ greater of **4× min topping** or **600 mm**; anchor both sides |
| Excess shear | All force in reinforcement: \(A_h = 1000\,b\,v_h / (0.87 f_y)\) |
| Prestressed + in-situ composite vertical shear | Principal tension in prestressed unit ≤ **0.24√\(f_{cu}\)** (with 0.8× prestress compression, sequence allowed for) |
| **Structural topping thickness** | Nominal **≥ 40 mm**; local absolute min **25 mm** |
| Conduits in topping | **Increase** topping — do not steal from 40/25 mm mins |
| Level correction | **Never** thin topping below minimum to absorb erection tolerance |
| Workmanship | Well vibrate onto dampened surface (no standing water) |
| Semi-precast cleansing before topping | Water jet ≥ **10,000 kPa (100 bar)**; check soffit cracks; repair **through-cracks** before topping |

**Table 2.8 — design ultimate horizontal shear at interface (N/mm²)** — γₘ ≈ 1.5 included:

| Precast surface | Grade 25 | Grade 30 | Grade ≥40 |
|---|---|---|---|
| **No links** — as-cast / as-extruded | 0.4 | 0.55 | 0.65 |
| No links — brushed/screeded/rough-tamped | 0.6 | 0.65 | 0.75 |
| No links — washed / retarder + cleaned | 0.7 | 0.75 | 0.80 |
| **Nominal links** — as-cast / as-extruded | 1.2 | 1.8 | 2.0 |
| Nominal links — brushed/screeded/rough-tamped | 1.8 | 2.0 | 2.2 |
| Nominal links — washed / retarder + cleaned | 2.1 | 2.2 | 2.5 |

**SD takeaway:** Semi-precast + topping + finishes + services often drives F-F more than permanent span tables — protect the 40 mm topping and joint depth in the section.

---

### 10. Non-structural precast & ductility (§2.10–2.11)

| Topic | Rule |
|---|---|
| Façades / non-loadbearing partitions | Design for **self-weight + wind** and connections per §§2.1–2.9; Appendix B typical façade install details |
| Moment frames / structural walls with precast | Adopt **equivalent monolithic** systems |
| Connections | **Strong connections** — deform beyond elastic limit without excessive strength/stiffness loss; flexural yield **away from** connection; allow yield penetration as for cast-in-place; ductility detailing per Concrete Code |

---

### 11. Moulds, finishes, cast-in frames — aesthetic & programme risk (§3.2–3.6)

#### 11.1 Moulds

| Topic | Practical rule |
|---|---|
| Steel mould economics (façade) | Often economical only at **~200+** panels from one steel mould — complexity/finish may override |
| Mould design critical | Stiffness for tolerances; 3D restraint; demoulding mechanisms; temperature effects — mould failure wastes units and programme |
| Re-check moulds | Full dimensional re-check after ~**100** castings (more often if needed) |
| Release agents | Must not discolour finish or kill adhesion of later tiling; follow manufacturer timing |
| Recesses / sleeves / boxouts | Material, shape, size, location on shop drawings |

#### 11.2 Surface finishes & tiles

| Finish type | SD note |
|---|---|
| Common types | Off-form plain; patterned; tiled; tooled / sand-blasted / acid-etched |
| Trial units | **Mandatory** before mass production — expect several iterations to agree quality |
| Quality drivers | Mix; form material; release agent; placing/compaction; curing |
| Tiles in mould (flat cast) | Often grout joints then adhesive on tile backs; place concrete **within adhesive open time** (critical when rebar goes in after adhesive) |
| Tiles after casting | Thin-bed adhesive per manufacturer; remove release agents/curing compounds first |
| Waterproofing agents in concrete | Can kill tile bond — specialist advice |

#### 11.3 Prefabricated metal frames (windows etc.)

- Protect frame surfaces from fresh concrete; coating on contact face if supplier recommends.
- Provide **lugs** for bond into concrete; fix so frame cannot move or deform during pour.
- Cast-in accuracy: templates for threaded bars, bolts, inserts, sleeves, base plates.
- Tight-tolerance connection systems → **mock-up elements** before mass production.

#### 11.4 Tiled finish QC (§4.3.3)

Yard trial panels: no hollow sound on tap; pull-off tests as specified; cover-meter survey under tiles. Agree panel count, tests, and acceptance **before** manufacture. Production acceptance testing before erection — pull-off is **destructive** and hard to reinstate to original appearance.

---

### 12. Demoulding, curing, handling, storage, transport (§3.9–3.15)

#### 12.1 Minimum concrete strength for lifting (Table 3.2)

| Application | Min strength |
|---|---|
| None specified, fine-controlled crane, non-prestressed | **10 N/mm²*** |
| Significant impact / high acceleration | **15 N/mm²*** |
| As specified in project docs | As specified |
| Concentric prestress (piles, wall panels, thin slabs) | **20 N/mm²** |
| Eccentric prestress (tees, deep flooring) | **25 N/mm²** |
| Bridge beams / highly stressed prestress | **30 N/mm²** or as specified |

\*Depends on anchor length / manufacturer. Vertical/tilting moulds often governed by **insert capacity**, not flexure. Prestressed: anchor lifting devices in **compression zones** unless specifically designed otherwise. Initial lift: slow/gradual to overcome suction without impact.

#### 12.2 Curing

| Method | Rule |
|---|---|
| Normal | ≥ **4 days** — delay demould; impermeable sheet; curing membrane; damp absorbent; or frequent water (no alternate wet/dry; no cold water on warm concrete) |
| Steam | Wait **4 h** after placing with no extra heat; then heat ≤ **10°C per ½ hour**; concrete ≤ **70°C**; cool no faster than heat rate; free steam circulation, not aimed at concrete or cubes |

#### 12.3 Storage & transport (architect logistics)

| Topic | Rule |
|---|---|
| Storage ground | Hard, level, clean, drained; room for vehicles/cranes |
| Dunnage | Support points per shop drawings if critical; prevent twist/distortion; non-staining; protect lifting points and keep them accessible |
| Guangdong factories | Common — plan road/water transport, PRC permits, HK transport regs |
| On transporters | Edge protection; secure against overturn/shift; non-staining padding under chains; no unwanted stress from truck/barge flexure |
| Strength before load-out | Sufficient strength before loading for transport |

---

### 13. Erection — temporary works that affect design (§3.16)

| Topic | SD / sequencing flag |
|---|---|
| Erection drawings before work | Sequence; method; tolerances; rigging; strength/age; permanent connections; propping |
| Critical sequence for stability or access | Note on drawings; minimise multiple handling; consider trial erection |
| Missing/damaged lifting inserts | Stop — designer assesses alternate system; check temporary use of permanent fixings does not compromise long-term performance |
| Bracing | Prefer fix braces **before** lift; if after, keep on crane until braces on; FoS per Table 2.4; competent person per Site Safety Supervision Plan |
| Levelling shims | Durable; full construction load; **avoid** direct concrete-to-concrete or concrete-to-steel bearing; solid foundation (not thin site concrete); height ≤ **30 mm** unless stability proven; where possible ≥ **300 mm** from ends (thin walls — corner breakout); **steel shims removed** before final grout |
| Propping | Full support for completed floor self-weight + construction concentrations unless noted otherwise; props in place, levelled for camber, braced **before** erecting beams/floors; vertical + braced against sidesway/buckling |
| Beams | Often need full end propping; mid-span prop omission (to reduce end dead moments) must be noted on contract **and** precast layout drawings |
| One-sided floor loading on beams | May roll beam on props → separate props each edge |
| Hollow-core without inserts | Lifting clamps/strops/slings — wear inspection; mark lifting points on drawings |

---

### 14. Tolerances architects must leave space for (§3.17)

Final construction tolerance ≥ production + erection, and must **not exceed** Concrete Code construction tolerances.

#### 14.1 All elements — production (unless otherwise specified)

| Dimension | Tolerance |
|---|---|
| Length ≤ 2000 mm | ±**6 mm** |
| Width/height ≤ 250 mm | ±**4 mm** |
| Thickness/depth ≤ 500 mm | ±**6 mm** |

#### 14.2 Façade / wall — production

| Dimension | Tolerance |
|---|---|
| Length/height ≤2 m | ±**3 mm** |
| 2–3 m | ±**6 mm** |
| 3–4.5 m | ±**9 mm** |
| 4.5–6 m+ | **+10 / −12 mm** |
| Thickness ≤500 mm | **+6 / −3 mm** |
| Thickness 500–750 mm | **+8 / −5 mm** |
| Bow ≤3 m / 3–6 m / 6–12 m | **6 / 9 / 12 mm** |
| Squareness (shorter side ≤1 / 1–2 / >2 m) | **3 / 5 / 6 mm** |
| Twist ≤3 / 3–6 / 6–12 m | **6 / 9 / 12 mm** |
| Cast-in window position | ±**6 mm** |

#### 14.3 Façade / wall — erection

| Item | Tolerance |
|---|---|
| Position on plan (x, y) | ±**5 mm** |
| Verticality per element | ±**6 mm** |
| Joint width (nominal 20 mm) | ±**5 mm** |
| Completed building H/W/L | within **0.1%** |
| Storey profile line (front) | **0.1%**; max deviation ±**10 mm** |

#### 14.4 Stairs (flight landing to landing)

| Item | Tolerance |
|---|---|
| Position on plan (≤15 m to ref.) | ±**10 mm** |
| Clear span length on plan | ±**12 mm** |
| Flight width | ±**6 mm** |
| Vertical height of flight | ±**10 mm** |
| Waist thickness | **+6 / −3 mm** |
| Consecutive rise | ±**5 mm** |
| Consecutive going | ±**8 mm** |
| Tread level across going / across width | ±**4 / ±5 mm** |

#### 14.5 Volumetric precast

| Item | Tolerance |
|---|---|
| Plan from nearest grid | ±**15 mm** |
| Length/width ≤30 m | ±**25 mm**; each further 30 m ±**20 mm** |
| Height to structural roof ≤30 m | ±**40 mm**; each further 30 m ±**15 mm** |
| Wall/column plumb ≤0.5 / 0.5–3 / 3–30 / >30 m | ±**10 / 15 / 20** mm; then pro-rata ±20 per 30 m |
| Surface profile ≤3 / 3–15 / >15 m | ±**10 / 15 / 20 mm** |
| Twist (diagonal ≤15 m) | **20 mm**; +**10 mm** per further 10 m diagonal |
| Squareness (short side ≤3 m) | ±**20 mm**; then 20×L/3 per extra 2.5 m |
| Level vs TBM ≤8 / 8–15 / 15–30 m | ±**10 / 15 / 20 mm** |

#### 14.6 Lifting device location (Table 3.1)

| Unit | Tolerance |
|---|---|
| Pile / floor slab | **150 mm** |
| Beam along / across | **300 / 25 mm** |
| Column along / on end | **300 / 25 mm** |
| Wall/façade in face / edge across thickness / edge longitudinally | **25 / 5 / 25 mm** |

**SD:** Joint width on drawings must absorb **production + erection + movement + sealant geometry** — a “tight 8 mm architectural joint” is usually non-compliant.

---

### 15. Quality control & AP/RSE duties (§4 + APP-143)

| Topic | Requirement |
|---|---|
| Factory | **ISO 9001** QA covering materials (incl. proprietary lifting anchors), lab calibration, production, equipment, sampling/testing, inspection & audit frequency |
| Traceability | Serial number, casting date, grade, rebar details, final location, delivery docs; mark date + serial on each unit; RFID optional |
| Leaving factory | Certified QA documentation with units/batches |
| Testing | Concrete CS1; rebar CS2; grout CS1 — HOKLAS (or mutual-recognition) labs |
| Grout strength | 100 mm cubes ≥ grade of adjoining concrete |
| Site acceptance | Integrity (damage in transit); dimensional tolerance; surface finish |
| AP/RSE | Satisfy units match approved drawings/spec; qualified supervision of fabrication, erection, examination; may step up supervision/testing |
| Continuous factory supervision | Contractor provides continuous supervision of production |
| Load testing (§4.3.2) | If poor workmanship or visible defects at critical sections — method agreed with RSE |
| Cross-ref | **PNAP APP-143** Precast Concrete Supervision Plan and audit regime |

---

### 16. Architect’s SD freeze checklist

1. **Module & mould strategy** — repeated types; panel size vs transport/crane; ~200+ for steel mould economics; ~6-month lead-in; trial finishes.  
2. **Lateral system** — shear walls + diaphragm floors + continuous ties; H/500 **including connection slip**.  
3. **Joint matrix** — typical ≥12 mm; movement joints often ≥50 mm; sealant class vs movement rate; gasket primary/secondary; maintenance access + replacement schedule.  
4. **Façade** — ≥**75 mm** vertical lap; drainage; both-face rebar if high thermal gradient; cast-in window lugs/protection; mock-up water test.  
5. **Bearings / nibs** — net ≥40 mm (isolated +20) + spalling + √Σt² clearance; use **2026 \(f_{cb}=…m f_{cu}\)**; shim rules (≤30 mm; ≥300 mm from ends; remove steel).  
6. **Topping** — protect **40 mm** nominal / **25 mm** local; conduits increase depth; 100 bar clean + crack repair before pour.  
7. **Openings & services** — preformed; buried conduits only within rebar layers.  
8. **Water testing** — ASTM mock-up (0.5%/type, ≥0.77 kPa, 3.4 L/min/m² × 15 min) + **100% AAMA 501.2** field joints (2026).  
9. **Cover / FRR / materials** — Concrete Code 2013 corrosion cover; FS Code fire; joint fillers match member FRR; ASR ≤3.0 kg/m³ + HOKLAS.  
10. **Temporary works / sequence** — propping that loads lower precast; one-sided floor loading; brace-before-release; critical erection sequence on drawings.  
11. **Tolerance stack** — façade production + erection + 0.1% building envelope; stairs rise/going; volumetric grid ±15 mm.  
12. **QA programme** — ISO factory, traceability, tiled-finish trials, APP-143 supervision plan.

---

### 17. Amendment delta card (keep on the drawing issue sheet)

| Amendment | What changed for SD |
|---|---|
| **Nov 2020** | Corrosion cover → **Concrete Code 2013**; connection fill must stop **water seepage**; materials per B(C)R **+** Concrete Code 2013; ASR options expanded (expert advice / CS1 non-reactive / moisture control) still with **≤3.0 kg/m³** alkali |
| **June 2026 (APP-174)** | Bearing \(f_{cb} = 0.27/0.40/0.80\,m f_{cu}\) with \(m=\sqrt{A_2/A_1}\le 2\); **100%** completed panel/window joints tested to **AAMA 501.2** (Table 2.7a); Annex A standards updated |

---

*Not a substitute for the full Code, Appendices A–C, APP-143/APP-174, or RSE design. Numbers above are the SD-critical constraints from CoP Precast Concrete Construction 2016 as amended Nov 2020 and June 2026.*

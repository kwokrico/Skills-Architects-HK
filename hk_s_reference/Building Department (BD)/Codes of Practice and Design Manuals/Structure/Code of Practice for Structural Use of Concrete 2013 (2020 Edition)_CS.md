# Code of Practice for Structural Use of Concrete 2013
**Architect critical summary for schematic design**  
2013 Code (**2020 Edition**, December 2020) | Buildings Department  
Later circular amendments: **June 2023** (coupler test ref; beam link anchorage alternative) · **April 2024** (strut-and-tie; coupler elongation; minor mix / detailing) — mostly RSE detailing; apply on top of this Edition.

> Scope note: Deemed-to-satisfy guidance for **reinforced and prestressed concrete** buildings made with **normal-weight** aggregates under the Buildings Ordinance / B(C)R. Cross-check always with **Dead & Imposed Loads Code**, **Wind Code (HKWC)**, **FS Code** (member size & cover for FRP), **Precast Concrete Construction CoP**, **Structural Use of Steel** (composite), and PNAP / APP letters on concrete submissions.  
> RSE owns calculations; AP must lock **lateral system**, **transfer strategy**, **F-F / slab depth vs deflection**, **flat-slab openings vs punching**, **exposure → grade & cover**, **cantilever typology**, **core/wall ductility congestion**, and **robustness / tying** before freezing massing and façades.

---

## Regulatory Overview

This Code covers **limit-state design, construction and quality control of RC and prestressed concrete buildings and structures** using normal-weight aggregates — strength, serviceability, durability and fire resistance (not thermal or acoustic performance). It assumes a **50-year design working life** unless the brief states otherwise.

At schematic design, lock **cores / shear walls vs sway frames**, **transfer level and Hs/700 drift**, **slab/beam depth from span/d ratios**, **exposure class → cover & concrete grade**, and **balcony / canopy / A/C platform detailing** — these drive F-F height, transfer depth, façade joints, and coastal / wet-area specifications before GBP.

---

## Critical main topics and subtopics

### 1. What is in / out of scope (§1.1)

| In scope | Out of scope / use another code |
|---|---|
| RC & prestressed **buildings** with normal-weight aggregate | Lightweight, heavy, no-fines, aerated, GFRC |
| Strength, SLS, durability, fire resistance | Thermal / acoustic performance |
| | Bridges → HyD Structures Design Manual |
| | Steel–concrete composite → Structural Use of Steel CoP |
| | Precast systems → Precast Concrete Construction CoP |
| | Membrane, dams, pressure vessels, reservoirs, special composites |

**High strength concrete (HSC):** grade **above C60 up to C100**. **Normal strength:** ≤ **C60**. Grades from **C20** to **C100** (Table 3.1); lowest RC grade with normal-weight aggregate = **C20**.

**SD takeaway:** Do not brief “lightweight concrete floors” or exotic concretes under this Code without a separate BA-accepted route.

---

### 2. Design aims that freeze the brief (§2.1)

Structure must, for the design working life:

1. Carry construction + in-use loads / deformations  
2. Remain fit for purpose  
3. Be durable for its environment  
4. Resist required **fire resistance period**  
5. Avoid **disproportionate collapse** from accident / misuse  

Plus: **robustness**, **ductility**, **50-year** working life (modify if brief ≠ 50 yrs), and early definition of **exposure + maintenance**.

---

### 3. Limit states architects must leave room for (§2.2)

| Limit state | What governs SD |
|---|---|
| **ULS** | Strength, stability, buckling, overturning — cores, columns, transfer |
| **FLS** | Fire integrity — check if cover ≠ FS Code **or** concrete **> 60 MPa** |
| **SLS** | Deflection, cracking, vibration, wind acceleration, durability |

**SLS deflection / cladding:** Deflections must be compatible with finishes, partitions, glazing and cladding — agree movement joints and soft edges early (§2.2.4.2).

**Prestressed crack classes (§2.2.4.4):** Class 1 = no tensile stress; Class 2 = tension, no visible cracks; Class 3 = crack width ≤ **0.1 mm** (very aggressive / sea) or **0.2 mm** (other).

---

### 4. Loads & combinations that set member sizes (§2.3)

#### 4.1 Characteristic loads

| Load | Source |
|---|---|
| Dead \(G_k\) | Dead & Imposed Loads Code |
| Imposed \(Q_k\) | Dead & Imposed Loads Code |
| Wind \(W_k\) | Wind Effects Code |
| Earth \(E_n\) | Geotech / normal practice |

#### 4.2 ULS load factors (Table 2.1) — know the pattern

| Combination | Dead (adv/ben) | Imposed (adv/ben) | Earth | Wind |
|---|---|---|---|---|
| 1 Dead + imposed | 1.4 / 1.0 | 1.6 / 0 | 1.4 | — |
| 2 Dead + wind | 1.4 / 1.0 | — | 1.4 | **1.4** |
| 3 Dead + imposed + wind | 1.2 / 1.0 | 1.2 / 0 | 1.2 | **1.2** |

Beneficial earth/water: \(\gamma_f\) ≤ **1.0**. Combinations 2 & 3: horizontal load not less than **notional** load (§4.3 below).

#### 4.3 Robustness design loads (§2.3.1.4) — hard numbers

| Item | Rule |
|---|---|
| **Notional horizontal** at every floor & roof | **1.5%** of characteristic dead weight of storey tributary (mid-height to mid-height / roof) |
| **Key element** | Design for **34 kN/m²** from any direction (no \(\gamma_f\)); projected face area |
| Supporting key element laterally | That support is also a key element |
| Attached components to key element | Also **34 kN/m²** reactions |
| Vehicular impact | Per B(C)R 17; ULS \(\gamma_f\) = **1.25** |
| Exceptional / post-damage loads | Dead + **1/3** wind + **1/3** imposed (or **100%** imposed if storage / permanent IL) |

**SD:** Columns / walls next to drop-offs, podium driveways, loading bays → bollards or key-element sizing from day one.

#### 4.4 SLS permanent imposed (deflection) (§2.3.3.3 / §7.1.3.3)

| Use | Treat as permanent |
|---|---|
| Domestic / office | **25%** of imposed |
| Storage | **≥ 75%** of imposed |

#### 4.5 Differential settlement (§2.3.1.6)

Flag early if: pad foundations in soft ground; **mixed foundation types**; different depths; flexible pile caps. Treat induced loads as **permanent**.

---

### 5. Robustness / disproportionate collapse — plan the ties (§2.2.2.3 + §6.4)

Every building needs:

1. No inherent weak layout  
2. Notional horizontal resistance (§4.3)  
3. **Effective horizontal ties** — peripheral, internal, to columns/walls (§6.4.1)  
4. Identify **key elements** if layout cannot avoid them; else detail so any non-key vertical can be removed without collapsing more than a **limited portion** (vertical ties / bridging)  

**Expansion joints:** Each structurally independent section between joints needs its **own** tying system.

| Tie type | SD-relevant rule |
|---|---|
| **Internal** | Each floor & roof; two approx. orthogonal directions; spacing ≤ **1.5 \(l_r\)**; force ≥ greater of \(0.5(G_k+Q_k)\,l_r\,F_t/7.5\) or \(1.0 F_t\) (kN/m) |
| **Peripheral** | Continuous; force **\(1.0 F_t\)**; within **1.2 m** of edge or in perimeter wall |
| **External column / wall** | Greater of **\(2.0 F_t\)** (or \((l_s/2.5)F_t\) if less) or **3%** of ultimate vertical load at that level |
| **Corner columns** | Ties in **two** directions |
| **Vertical** | Continuous lowest→highest; tensile capacity ≥ max ultimate D+L from **any one storey** |
| **\(F_t\)** | Lesser of **(20 + 4\(n_o\))** or **60** (\(n_o\) = storeys) |

**SD takeaways:** Re-entrant corners, discontinuous columns, transfer floors, and mega-columns need early tying / key-element strategy. Do not assume the steel-code **70 m² / 15%** area formula appears here — SUC uses “limited portion” + ties / bridging language.

---

### 6. Materials that affect depth & programme (§3)

#### 6.1 Concrete grades (Table 3.1)

C20 → C100 in 5 N/mm² steps. Brief **grade by exposure** (§7), not by “standard C35 everywhere.”

#### 6.2 Elastic modulus (Table 3.2) — lateral / transfer checks

Two columns of \(E_c\): general use vs **checking overall building deflection / relative lateral deflection at transfer** (§5.5). Higher grade → stiffer, but HSC brings fire-spalling rules (§8).

| Grade | \(E_c\) general (kN/mm²) | For overall / transfer deflection |
|---|---|---|
| C35 | 23.7 | 25.1 |
| C45 | 26.4 | 27.7 |
| C60 | 30.0 | 31.1 |
| C80 | 34.2 | 35.1 |
| C100 | 37.8 | 38.7 |

Thermal expansion ≈ **10×10⁻⁶ /°C**. Creep & shrinkage: HK granite factor **cs = 2.5** on shrinkage — expect **larger long-term movement** than overseas textbooks; budget joints and cladding gaps.

#### 6.3 Reinforcement (§3.2)

| Grade | \(f_y\) (N/mm²) |
|---|---|
| 250 (plain) | 250 |
| **500B / 500C** (ribbed) | **500** |

\(E_s\) = **200 kN/mm²**. Couplers: Type 1 (general) / Type 2 (ductility zones §9.9).

#### 6.4 Welded fabric Grade 500A — restricted (§3.3.3)

Only in limited slab/wall locations; **not** in lateral-system sections, **not** in flat-slab column strips / robustness ties; **no moment redistribution**. Do not use as default mesh for transfer / core slabs.

---

### 7. Durability — exposure → cover & grade (lock at SD) (§4.2)

#### 7.1 Exposure conditions (Table 4.1)

| Cond. | Name | Typical HK locations |
|---|---|---|
| **1 Mild** | Internal; external protected (tiles / paint / render); permanently wet (not sea); non-aggressive soil | Typical dry interiors |
| **2 Moderate** | High humidity interiors (**bathrooms, kitchens**); external severe rain / cyclic wet–dry (**fair-face, dry-fixed cladding, curtain wall**)* | Wet rooms; rain-exposed structure behind CW |
| **3 Severe** | Sea spray / airborne coastal; corrosive fumes | Near coast |
| **4 Very severe** | Frequent sea / flowing pH≤4.5; tidal zone to 1 m below LLW | Marine / tidal |
| **5 Abrasive** | Machinery, metal-tyred vehicles, solids in water | Industrial floors / ramps |

\*Cement bedding for finishes is **ignored** for exposure. External “protected” needs a real finish system — mosaic/paint/render — not hope.

#### 7.2 Nominal cover & lowest grade (Table 4.2) — architect cheat sheet

Nominal cover = design cover to **all steel including links**; actual ≥ nominal − **5 mm**. Also ≥ bar diameter, ≥ aggregate size. Cast against earth ≥ **75 mm**; against blinding ≥ **40 mm** (excl. blinding).

| Exposure | C30 | C35 | C40 | C45 | C50 | ≥C55 |
|---|---|---|---|---|---|---|
| **1** slabs | 30 | 25 | 25 | 25 | 25 | 25 |
| **1** other | 30 | 30 | 30 | 25 | 25 | 25 |
| **2** | 40 | 35 | 35 | 30 | 30 | 30 |
| **3** | — | — | **50** | 45 | 45 | 45 |
| **4** | — | — | — | — | **55** | **50** |

Also: max free w/c and min cementitious content in same table (e.g. Cond. 2 @ C35 → w/c **0.60**, cement ≥ **330 kg/m³**). Prestressed: not below **C30**; cementitious ≥ **300 kg/m³**.

**Cover must also satisfy FS Code fire** and bond (§4.2.4.1 / §4.3) — take the **largest**.

#### 7.3 Shape & bulk (§4.2.2.1)

Avoid ponding / rundown on exposed concrete. Thin sections, one-sided hydrostatic pressure, partial immersion, and edges/corners are more vulnerable. Pours with min dimension **> 600 mm** and cementitious ≥ **400 kg/m³** → heat-of-hydration strategy.

#### 7.4 Cementitious content caps (§4.2.6.1)

| Concrete | Cap / note |
|---|---|
| Normal ≤ C60 | Total cementitious **> 550 kg/m³** only with special shrinkage/thermal design |
| HSC > C60 | Portland cement mass in cementitious generally ≤ **450 kg/m³** |
| Low-rise foundations, non-aggressive soil | Min **C20** if cementitious ≥ **290 kg/m³** |

pfa **25–35%** or ggbs **35–75%** of cementitious is normal; longer curing → programme impact.

#### 7.5 Chloride & alkali (§4.2.7)

| Use | Max Cl⁻ (% of cement mass) |
|---|---|
| Prestressed / steam-cured | **0.1** |
| Sulphate-resisting cement | **0.2** |
| Normal RC | **0.35** |

Reactive alkali ≤ **3.0 kg/m³** Na₂Oeq. No calcium chloride in RC/PSC.

---

### 8. Fire resistance & HSC spalling (§4.3)

| Topic | SD rule |
|---|---|
| Cover & min member size for FRP | Per **FS Code** — may exceed durability cover |
| Concrete **> 60 MPa** | Investigate strength loss & **spalling**; FLS check often required |
| Silica fume in HSC | ≤ **6%** of cementitious |
| Spalling control (≥1 of A–D) | **A** mesh cover 15 mm (wires ≥2 mm, ≤50×50; main cover ≥40) · **B** ≥1.5 kg/m³ PP fibres (6–12 mm, 18–32 μm, melt <180°C) · **C** proven protective layer · **D** proven mix |
| **> C80** | ≥1 fire test: main bars must not be exposed for design FRP; moisture ≥ in-service max |

**SD:** Specifying C70–C100 columns/walls for slender towers triggers fire-engineering and mix constraints — budget early with RSE / fire consultant.

---

### 9. Structural system rules that set geometry (§5)

#### 9.1 Member classification (§5.2.1.1)

| Element | Rule of thumb |
|---|---|
| Beam | Span ≥ **2×** depth (simple) or **2.5×** (continuous); else **deep beam** |
| Slab | Min panel dim ≥ **5×** thickness |
| One-way slab | Two free parallel edges, **or** 4-side support with long/short **> 2** |
| Column vs wall | Depth ≤ **4×** width → column; else wall |
| Ribbed / waffle | Rib spacing ≤ **1500 mm**; rib depth ≤ **4×** width; flange ≥ max(span/10 between ribs, **50 mm**) [**40 mm** with permanent blocks]; transverse ribs ≤ **10×** overall depth clear |

#### 9.1a Effective spans & flanges (§5.2.1.2) — early geometry checks

| Topic | Rule |
|---|---|
| Effective span | Clear span + \(a_1+a_2\) from support conditions (Fig. 5.3) — not always c/c |
| Monolithic support critical moment | At face of rectangular support, or **0.2φ** inside face of circular; ≥ **0.65** of full fixed-end moment |
| T/L flange effective width | Depends on \(l_{pi}\) between zero moments; cantilever length \(l_3\) ≤ **½** adjacent span; adjacent span ratio between **2/3** and **1.5** |
| Continuous over non-moment support | Design support moment may reduce by \(F_{Ed,sup} S_w/8\) |

#### 9.2 Moment redistribution (§5.2.9)

Allowed for grade ≤ **C70** with conditions; resistance ≥ **70%** of elastic envelope. Frames **> 4 storeys** providing lateral stability: redistribution capped at **10%**, resistance ≥ **90%**.

#### 9.3 Shear walls (§5.4)

Walls providing lateral stability: global analysis with **eccentricity to shear centre**, wall interaction, asymmetry, sway comfort (§7).

#### 9.4 Transfer structures (§5.5) — HK critical

Transfer = horizontal element redistributing vertical loads where grid / walls **discontinue**. Analysis must address pour sequence, temporary loads, differential shortening, local wall stiffness, deflection, **lateral shear**, sidesway — and:

> **Relative lateral deflection at transfer vs storey below ≤ \(H_s/700\)**  
> (\(H_s\) = height of storey **below** the transfer)

**SD:** Fix transfer level (typically podium/tower interface) before unit modules, risers, and parking grids. Deep transfer (**~1.5–3 m** typical in practice) eats F-F and plant — coordinate with RSE at concept.

#### 9.5 Precast (§5.6)

Use **Precast Concrete Construction CoP** — not this Code alone.

---

### 10. Serviceability — deflection, wind comfort, vibration (§7.3)

#### 10.1 Vertical deflection limits (§7.3.1)

| Criterion | Limit |
|---|---|
| Sag under quasi-permanent loads (appearance / utility) | **span/250** (relative to supports) |
| Pre-camber (formwork) | Generally ≤ **span/250** upward |
| After construction (damage to adjacent parts) | Typically **span/500** quasi-permanent |

#### 10.2 Deemed-to-satisfy span / effective depth (Table 7.3)

| Support | Rectangular beam | Flanged \(b_w/b\)≤0.3 | Solid slab |
|---|---|---|---|
| **Cantilever** | **7** | **5.5** | **7** |
| Simply supported | 20 | 16 | 20 |
| Continuous | 26 | 21 | 26 |
| End span | 23 | 18.5 | 23 |

- Two-way slabs: check on **shorter** span.  
- Spans **> 10 m**: multiply Table 7.3 by **10/span** if post-fitout deflection matters; **cantilevers > 10 m → calculation required**.  
- Stair without stringers: span/d may be **+15%** if flight ≥ **60%** of span (§6.6.2.1).  
- Further modifiers for steel stress / compression steel (Tables 7.4–7.5) — RSE.

**Quick SD depths (effective ≈ overall − cover − bar/2):**  
Simply-supported 8 m solid slab → \(d\) ≈ 8000/20 = **400 mm** → overall ~450 mm before finishes. Continuous office bay better. Cantilever 1.5 m slab → \(d\) ≈ 1500/7 ≈ **215 mm** → then check §9.4 minimums.

#### 10.3 Wind response (§7.3.2)

| Check | Limit |
|---|---|
| Top deflection (static characteristic wind) | **H/500** (\(H\) from highest floor excl. plant/roof features) |
| Peak acceleration (1-in-10-yr, 10-min) — residential | **0.15 m/s²** |
| Peak acceleration — office / hotel | **0.25 m/s²** |

Detail partitions, cladding and finishes for **storey drift** under characteristic wind. Tall/slender → dampers need dynamic analysis.

#### 10.4 Vibration (§7.3.3)

Floor natural frequency **< 6 Hz** (or footbridge **< 5 Hz**) → consider dynamic analysis. Long-span amenity floors / gyms need early brief.

#### 10.5 Crack widths (Table 7.1)

| Exposure | RC / unbonded PSC | Bonded PSC |
|---|---|---|
| 1–3 | **0.3 mm** (Cond.1 may relax if appearance OK) | **0.2 mm** |
| 4 | 0.3 mm | 0.2 mm |
| Water tanks (building works) | **0.2 mm** | — |

Early thermal cracking: avoid **infill bays** (restraint R ≈ 0.8–1.0); give pours a free end (§7.2.4).

---

### 11. Cantilevers, balconies, canopies, A/C platforms (§1.4 + §9.4) — AP hotspot

“Cantilever projecting structure” = canopy, balcony, bay window, A/C platform, etc.

| Span | Min thickness / typology |
|---|---|
| Beam support | **300 mm** at support |
| Slab ≤ 500 mm | **110 mm** |
| 500–750 | **125 mm** |
| 750–1000 | **150 mm** |
| 1000–1200 | **175 mm** |
| **> 1200 mm** | Prefer **beam-and-slab**; pure slab needs more stringent control |

Must also satisfy §7.3 deflection. Ribbed bars; slabs: bars **both faces, both directions**. Min top tension steel **0.25%** (≥10 mm bars); spacing ≤ **150 mm**.

**Weathered cantilevers:** no ponding; waterproofing; fall ≥ **1:75**; drainage; exposure **≥ Cond. 2**; crack width ≤ **0.1 mm** **or** HY steel stress ≤ **100 N/mm²** under working load.

**External weathered slab span > 750 mm:**

1. Waterproof concrete ≥ **C35**  
2. Main bars **hot-dip galvanized** (BS EN ISO 1461)  
3. Waterproof membrane + protected screed (1:3, w/c ≤ 0.65) or equal  

**Construction:** Cast **monolithically** with supporting member; no construction joint on external support edge if avoidable. Detail for **future demolition/replacement** without compromising main structure (esp. over streets). Supporting wall must be thick/stiff enough for moment + bar anchorage.

---

### 12. Beams & deep beams — geometry rules (§5.2.1.1 + §6.1.2 + §9.2)

| Rule | Number / implication |
|---|---|
| Normal beam vs **deep beam** | Span ≥ **2×** overall depth (simple) or **2.5×** (continuous); shorter → deep beam (strut-and-tie / specialist — April 2024 adds §6.9 strut-and-tie) |
| Max tension or compression steel | **4%** of gross concrete area (§9.2.1.3) |
| At laps in one layer | Sum of bar diameters ≤ **40%** of section breadth |
| Beams > **750 mm** deep | Side face bars for crack control (size ≥ √(sb·b/fy); spacing ≤ **250 mm**) |
| Monolithic “simple” support | Still design for ≥ **15%** of max span moment partial fixity (§9.2.1.5) |
| Tension bar clear spacing | ≤ 70 000 βb/fy and ≤ **300 mm** (or ≤ 47 000/fs ≤ 300) |

**SD:** Transfer / coupling / link beams often behave as deep beams — do not assume ordinary beam depth rules. Congested deep beams need early coordination of MEP penetrations (prefer framed openings, not random cores through webs).

---

### 13. Solid slabs — min steel, spacing, edges (§9.3)

| Item | Rule |
|---|---|
| Min long. steel each direction | **0.24%** (fy 250) or **0.13%** (fy 500), × αmin (≥1) |
| Secondary (one-way) | ≥ **20%** of principal (except near supports with no transverse moment) |
| Max bar spacing (general) | Principal ≤ min(**3h**, **400 mm**); secondary ≤ min(**3.5h**, **450 mm**) |
| At concentrated load / max moment | Principal ≤ min(**2h**, **250 mm**); secondary ≤ min(**3h**, **400 mm**) |
| Crack spacing waiver | No further check if h ≤ **250** (G250) / **200** (G500) mm, or As/bd < **0.3%** |
| End support top steel (partial fixity) | ≥ **50%** mid-span moment capacity (≥ min steel); extend ≥ **0.15l** or **45φ** into span |
| Intermediate support bottom steel | **40%** of mid-span bottom continuous through |
| Shear links in slabs | **Not** in slabs **< 200 mm** thick (§9.3.2 / Table 6.8 note) |
| Free edge | Longitudinal + transverse edge bars (Fig. 9.4) |

**SD:** Thin amenity / podium slabs that rely on punching links need ≥ **200 mm** — otherwise thicken, enlarge columns, or add drops/heads.

---

### 14. Ribbed / waffle / voided slabs (§5.2.1.1 + §6.1.4)

| Geometry | Limit |
|---|---|
| Rib centres | ≤ **1.5 m** |
| Rib depth (excl. topping) | ≤ **4×** rib width |
| Min rib width | Cover + bars + fire (FS Code) |
| Flange / topping (analysis idealisation §5) | ≥ max(**1/10** clear between ribs, **50 mm**); **40 mm** OK with permanent blocks |
| Transverse ribs (for discrete-element waiver) | Clear spacing ≤ **10×** overall slab depth |

#### Structural topping minima (Table 6.9)

| Slab type | Min topping |
|---|---|
| Permanent blocks, rib clear ≤500 mm, mortar ≥1:3 or 11 MPa | **25 mm** |
| Same, not mortar-jointed | **30 mm** |
| Other permanent-block slabs | Greater of **40 mm** or **1/10** clear between ribs |
| No permanent blocks (removable forms / voids) | Greater of **50 mm** or **1/10** clear |

If support moment steel cannot be provided: design as simply supported series + ≥ **25%** of mid-span steel over support extending **≥ 15%** of span each side.

Topping mesh recommendation: ≥ **0.12%** each way; wire spacing ≤ **½** rib centres. Waffle ribs with single bar often need no links (except shear/fire); multi-bar ribs → links ~1–1.5 m.

**SD:** Coffered/waffle soffits cut dead load and depth but constrain lighting / sprinkler / duct zones — lock rib module with M&E at SD.

---

### 15. Flat slabs — drops, openings, punching (§6.1.5) — expand

Flat slab = slab on columns **without beams** (solid or waffle). Codified equivalent-frame method assumes generally **rectangular** column grid with long/short span ≤ **2**.

#### 15.1 Heads & drops

| Feature | Rule that matters at SD |
|---|---|
| **Column head** effective size | Limited by head depth: \(l_{h,max}=l_c+2(d_h-40)\) mm — shallow heads do little for design width |
| **Drop** for moment redistribution | Smaller plan dimension of drop ≥ **1/3** of smaller surrounding panel dimension; smaller drops still help **punching** only |
| Panel strips | Column strip + middle strip (Fig. 6.9); drop width can redefine column strip |
| Edge / corner moment transfer | Needs edge beam **or** effective slab strip \(b_e\) (Fig. 6.10) — free edges are weak |
| Marginal beam / wall > **1.5×** slab thickness | Beam/wall takes direct load + **¼** panel load; adjacent half-column strip moments = **¼** of normal |

#### 15.2 Openings in flat-slab panels (§6.1.5.5) — freeze riser locations

| Location of hole | Allowed only if |
|---|---|
| Encroaching on **column head** | **Never** |
| Outside (b)–(d) rules | Must be **fully framed** with beams to columns |
| In area bounded by column strips | Greatest dim parallel to panel CL ≤ **0.4l**; moments redistributed |
| Common to **two** column strips (near column) | Aggregate length/width ≤ **1/10** of column-strip width; reduced shear perimeter |
| Common to column + middle strip | Aggregate ≤ **¼** of column-strip width |

Openings within **6×** effective depth of a column: part of shear perimeter across the opening is **ineffective** (§6.1.5.7). Adjacent hole wider than **¼** of column side needs careful perimeter reduction.

**Internal column punching (braced, ≈equal spans):** often take \(V_{eff} \approx 1.15 V_t\) without full Mt calc — still drives thickness.

**SD decision tree:**

```
Riser / stair / duct opening near column?
  → Inside column head footprint? → MOVE IT
  → In two-column-strip zone? → ≤10% strip width or frame with beams
  → Else check 0.4l / ¼ strip rules + punching perimeter
Slab < 200 mm and punching critical?
  → Thicken / drop / larger column / add beams — links not reliable
```

---

### 16. Columns — braced / slender / min eccentricity (§6.2.1 + §9.5)

#### 16.1 Classification

| Term | Definition |
|---|---|
| **Braced** (in a plane) | Lateral stability of whole structure provided by walls/bracing in that plane |
| **Short** | \(l_{ex}/h\) and \(l_{ey}/b\) both < **15** (braced) or < **10** (unbraced) |
| **Slender** | Otherwise — extra moments from deflection |
| Size vs wall | Larger dimension ≤ **4×** smaller → column; else design as wall |

#### 16.2 Effective height \(l_e = \beta\,l_o\) (Tables 6.11–6.12)

End condition scale 1 (stiff beams ≥ column depth, moment-resistant foundation) → 4 (free cantilever).

| | Braced β (approx.) | Unbraced β (approx.) |
|---|---|---|
| Stiff–stiff (1–1) | **0.75** | **1.2** |
| Soft–soft (3–3) | **1.0** | — |
| Free top (4) | — | **2.2** |

#### 16.3 Hard limits

| Limit | Rule |
|---|---|
| Clear height between restraints | \(l_o\) ≤ **60×** min column thickness |
| Unbraced cantilever column | \(l_o \le 100b^2/h\) and ≤ **60b** |
| Min design eccentricity | Greater of **0.05×** section dim in plane and **20 mm** (cap 20 mm) |
| If average \(l_e/h\) of columns at a level > **20** | Bases / connecting members must take slender additional moments |

#### 16.4 Reinforcement (§9.5)

| Item | Rule |
|---|---|
| Long. steel | **0.8%–6%** (vertically cast); **8%** horizontally cast; **10%** at laps |
| Min bars | **4** rectangular / **6** circular; ≥ **12 mm**; one per polygonal corner |
| Links | ≥ max(**6 mm**, **φ_long/4**); spacing ≤ min(**12φ_small**, lesser column dim, **400 mm**) |
| Laps | Sum of sizes in layer ≤ **40%** of breadth |

**SD:** Slender lobby / atrium columns and unbraced podium columns inflate section size for second-order effects — prefer bracing walls or stockier proportions early. Column size also driven by **durability cover + fire** before ULS calc (§6.2.1.1(a)).

---

### 17. Walls — stability, slenderness, stocky shortcuts (§6.2.2 + §9.6)

| Rule | Detail |
|---|---|
| Multi-storey stability | Must **not** rely on **unbraced walls alone** in any direction |
| Lateral support force | Static reaction to horizontal loads **+ 2.5%** of ultimate vertical load in wall/column at support |
| Rotation restraint at support | Concrete wall-to-wall detail, **or** floor bearing on ≥ **⅔** wall thickness / moment connection |
| Min transverse eccentricity | ≥ **h/20** or **20 mm** (except short braced ≈symmetric) |
| Stocky braced wall + ≈equal slabs | Simplified capacity eqn 6.59 if spans differ ≤ **15%** |
| Max \(l_e/h\) reinforced walls (Table 6.15) | Braced <1% steel: **40**; braced ≥1%: **45**; unbraced: **30** |
| Plain walls max \(l_e/h\) | **30** (braced or unbraced) |
| Unbraced plain wall \(l_e\) | **1.5 \(l_o\)** (top slab at right angles) or **2 \(l_o\)** otherwise |
| Vertical steel | Min **0.4%**, max **4%**; spacing ≤ min(**3t**, **400 mm**); half each face if min governs |
| Tension zone under ULS | Bars in **two layers** |

**SD:** “Thin architectural party wall as only lateral system” fails the unbraced-alone rule — provide orthogonal bracing or a core.

---

### 18. Ductility detailing — why cores get thicker (§9.9)

Applies to members in the **lateral load-resisting system** (single-storey walls and non-lateral members exempt).

#### 18.1 Beams in critical zones

- Critical zone = from column face over **2× beam depth**  
- Max tension steel in zone ≤ **2.5%** gross  
- Link spacing inside zone ≤ min(**150 mm**, **8φ** long.)

#### 18.2 Columns in critical zones

Extent from max-moment point scales with axial ratio \(N/(A_g f_{cu})\):

| \(N/(A_g f_{cu})\) | Critical length factor × greater section dim |
|---|---|
| ≤ 0.1 | **1.0** |
| 0.1–0.3 | **1.5** |
| 0.3–0.6 | **2.0** |

Type 2 couplers required in ductility zones; Type 1 restricted (e.g. not below **H/4** above floor in some cases — see Figs 9.8–9.9).

#### 18.3 Walls — confined boundary elements

Critical zone: to ceiling of **lowest** floor (or **second** lowest depending on case). Confined boundary types 1–3 by steel ratio (**0.6% / 0.8% / 1%** of boundary area) and confinement detailing (Fig. 9.11).

| Axial compression ratio \(N_{cr}\) in critical zone | Boundary type |
|---|---|
| 0 < \(N_{cr}\) ≤ **0.38** | Type **2** in critical zone; Type **1** elsewhere |
| **0.38** < \(N_{cr}\) ≤ **0.75** | Type **3** in critical zone **and** storey above; Type **1** elsewhere |

**SD:** Heavily loaded core toes and coupling-beam ends are rebar-congested — allow thicker walls / larger cores / higher grade concrete rather than fighting bar congestion in GBP.

---

### 19. Foundations in this Code (pad & pile caps) (§6.7 + §9.7)

Companion **Foundations CoP** governs geotech capacity; SUC covers RC design of bases.

| Topic | Architect-relevant rule |
|---|---|
| Rigid pad / pile cap assumption | Uniform reaction if concentric; linear if eccentric |
| Pad critical section | At **face of column/wall** |
| Punching on pads | As flat-slab punching; openings near columns reduce perimeter |
| Pile spacing > **3φ** | Punching check required; tension steel within **1.5φ** of pile centre for truss analogy |
| Shear critical section in pile cap | Vertical section **0.2φ inside** pile face (Fig. 6.19) |
| Widely spaced piles | Only steel within 1.5φ of pile counts as truss tie |
| Tie beams (§9.7) | Also design for min **10 kN/m** downward if soil can settle away |
| Cover against earth | Nominal ≥ **75 mm**; against blinding ≥ **40 mm** (§4.2.4.1) |

**SD:** Large pile spacing → thick caps; transfer walls on pile groups need cap rigidity story with RSE. Mixed pad+pile → differential settlement (§4.5).

---

### 20. Stairs (§6.6) — expanded

| Topic | Rule |
|---|---|
| Loading | UDL on plan; intersecting well flights share common area **50/50** |
| Wall embedment ≥ **110 mm** | Deduct **150 mm** strip next to wall from loaded area |
| Monolithic effective span (no stringer) | \(l_a + 0.5(l_{b1}+l_{b2})\); each \(l_b\) ≤ support breadth and ≤ **1.8 m** |
| Simply supported effective span | Lesser of c/c supports or clear + effective depth |
| Section depth | Min thickness **perpendicular to soffit** |
| Span/d relief | **+15%** if flight occupies ≥ **60%** of span |
| Construction tolerance (§10.2) | Structural clear span ±**14 mm**; finished ±**12 mm**; consecutive going ±**10 mm**; waist ±**8 mm** |

---

### 21. Corbels, nibs & beam–column joints (§6.5 + §6.8)

| Element | SD note |
|---|---|
| **Corbel** | \(a_v < d\); outer contact depth ≥ **½** root depth; horizontal resistance ≥ **½** vertical load; strut-and-tie |
| **Continuous nib < 300 mm** | Design as short cantilever slab; load at outer edge of bearing |
| Prefabricated / steel beam seats | Horizontal tie into support member required |
| Beam–column joints | Congestion + ductility links — larger columns at transfer / podium often needed |

---

### 22. Prestressed concrete — SD class & geometry (§2.2.4.4 + §12)

| Class | SLS tension / cracking |
|---|---|
| **1** | No flexural tensile stress |
| **2** | Tension allowed, **no visible cracks** |
| **3** | Crack width ≤ **0.1 mm** (very aggressive/sea) or **0.2 mm** (other) |

- Class 1 & 2 usually governed by SLS tension; Class 3 by ULS or deflection.  
- Concrete strength at prestress **transfer** ≥ **25 N/mm²**.  
- Prestressed grade not below **C30**; cementitious ≥ **300 kg/m³** (§4).  
- Slender PT beams: check lateral stability during lifting/handling.  
- PT flat slabs: still coordinate punching / openings as §15; ducts reduce effective depth.  
- Redistribution limited in Class 1 & 2.

**SD:** PT for long office spans (≈9–12 m) is common — lock tendon profiles vs MEP and column-head drops early; Class 1 roofs / water-retaining need thicker / more PT.

---

### 23. Cantilevers, balconies, canopies, A/C platforms (§1.4 + §9.4) — AP hotspot

“Cantilever projecting structure” = canopy, balcony, bay window, A/C platform, etc.

| Span | Min thickness / typology |
|---|---|
| Beam support | **300 mm** at support |
| Slab ≤ 500 mm | **110 mm** |
| 500–750 | **125 mm** |
| 750–1000 | **150 mm** |
| 1000–1200 | **175 mm** |
| **> 1200 mm** | Prefer **beam-and-slab**; pure slab needs more stringent control |

Must also satisfy §7.3 deflection. Ribbed bars; slabs: bars **both faces, both directions**. Min top tension steel **0.25%** (≥10 mm bars); spacing ≤ **150 mm**.

**Weathered cantilevers:** no ponding; waterproofing; fall ≥ **1:75**; drainage; exposure **≥ Cond. 2**; crack width ≤ **0.1 mm** **or** HY steel stress ≤ **100 N/mm²** under working load.

**External weathered slab span > 750 mm:**

1. Waterproof concrete ≥ **C35**  
2. Main bars **hot-dip galvanized** (BS EN ISO 1461)  
3. Waterproof membrane + protected screed (1:3, w/c ≤ 0.65) or equal  

**Anchorage:** Full anchorage length; if continuous slab without designed rotational restraint, anchorage starts at **far face** of support and top bars continue to nearest contraflexure — no stress-based bond reduction.

**Construction:** Cast **monolithically** with supporting member; no construction joint on external support edge if avoidable. Detail for **future demolition/replacement** without compromising main structure (esp. over streets). Supporting wall must be thick/stiff enough for moment + bar anchorage.

---

### 24. Construction tolerances — coordinate cladding, lifts, stairs (§10.2)

Guidance on achievable accuracy (specify tighter where needed):

| Element | Typical permissible deviation |
|---|---|
| Wall thickness / column plan ≤1 m | ±**8 mm** |
| Wall verticality ≤3 m / ≤7 m | **17 / 16 mm** |
| Column verticality ≤3 m / ≤7 m | **12 / 16 mm** |
| Suspended floor level vs target | ±**25 mm**; soffit ±**19 mm** |
| Floor-to-soffit height | ±**23 mm** |
| Window/door opening ≤3 m W×H | ±**14 / 20 mm** |
| Building length/width ≤40 m | ±**26 mm** |
| Foundations / pile caps position & size | ±**50 mm** |
| Frame columns / lift walls / stair wells on plan | ±**12 mm** |
| Lift walls | Critical — agree with lift supplier early |

**SD:** Curtain-wall brackets, stone cladding, and lift shafts need tolerance stack-up (structure + bracket + panel) — do not design zero-gap interfaces to theoretical grid.

---

### 25. Curing, hot weather, joints, HSC programme (§10.3)

| Topic | Rule |
|---|---|
| Min curing (Table 10.3) | PC: **3–4** days (avg/poor); other cements **4–6**; “good” damp/protected may waive special curing |
| Place temperature | Fresh concrete ≤ **30°C** unless justified |
| HSC > **C60** | Adiabatic curing test; max temp rise **40°C** or thermal analysis + cooling; early mist curing against plastic shrinkage |
| pfa / ggbs | Longer curing critical for durability |
| Construction joints | Minimise; full compaction; plan with early-thermal free ends (§7.2.4 — avoid infill bays) |
| Movement joints | Also robustness boundaries (§5) — each jointed block needs own ties |
| Analyse each construction stage (§5.1) | Transfer pour, backpropping, early strike |

---

### 26. Fire load factors & FLS (§2.3.2.7 + §2.2.3)

When FLS check required (cover ≠ FS Code **or** \(f_{cu}\) > **60 MPa**):

| Load | \(\gamma_f\) |
|---|---|
| Dead | **1.00** |
| Permanent imposed / storage | **1.00** |
| Escape stairs & lobbies (non-permanent) | **1.00** |
| Other non-permanent imposed | **0.80** (may **0.50** with justification) |
| Wind | **0.33** |

Material \(\gamma_m\) at FLS reduced (e.g. concrete flexure **1.10**, steel **1.00** — Table 2.3).

---

### 27. SD decision checklist (use before freezing massing)

```
1. Lateral system: shear walls / core? sway frame?
   → multi-storey cannot rely on unbraced walls alone
   → ductility §9.9 boundary elements & redistribution caps
2. Transfer? → level, depth, Hs/700, pour sequence, riser/module alignment
3. Floor system: solid / flat slab / ribbed / PT?
   → Table 7.3 depth + finishes → F-F
   → flat slab: long/short ≤2; openings vs column strips; ≥200 mm if links needed
4. Exposure map: wet rooms, CW soffits, coastal, basements → Table 4.2 cover/grade
5. Fire FRP vs HSC (>60 / >80) → FS Code sizes + spalling method A–D
6. Cantilevers / balconies / A/C platforms → §9.4 thickness, galvanizing, fall 1:75
7. Tall building comfort → H/500 + 0.15/0.25 m/s²; cladding storey-drift joints
8. Robustness → continuous tying; Ft; key elements 34 kN/m²; impact protection
9. Columns/walls → short vs slender; le/h limits; min eccentricity; core toe congestion
10. Foundations → pad vs pile cap depth; 75 mm earth cover; tie beams; Foundations CoP
11. Tolerances → CW / lift / stone interfaces (±12–25 mm structure)
12. Precast / steel composite? → companion CoP
13. Programme → curing (esp. HSC/pfa), hot-weather 30°C, early thermal pours
```

---

### 28. Companion documents (do not design from SUC alone)

| Document | Role |
|---|---|
| Dead & Imposed Loads Code | \(G_k\), \(Q_k\) |
| Wind Effects Code | \(W_k\), accelerations cross-check |
| FS Code | FRP periods, min sizes, cover |
| Precast Concrete Construction CoP | Precast |
| Structural Use of Steel CoP | Composite & steel |
| Foundations CoP / GEO | Geotech capacity, piles, settlement |
| CS1 / CS2 / CS3 | Concrete testing, rebar, aggregates |

---

*Source: Code of Practice for Structural Use of Concrete 2013 (2020 Edition), Buildings Department. Amendments June 2023 and April 2024 noted above. This summary is for schematic-design coordination only — structural design and certification remain RSE responsibility.*

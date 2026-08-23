# Code of Practice for Oil Storage Installations
**Architect critical summary for schematic design**  
1992 | Building Authority Hong Kong

> Read with: Building (Oil Storage Installations) Regulations; Building (Construction) Regulations; Dangerous Goods Ordinance Cap. 295 / DG licences (FSD); FSD Minimum FSI CoP; Water Pollution Control Ordinance Cap. 358; Waste Disposal (Chemical Waste) (General) Regulation Cap. 354. Fire fighting / FSI detail is **outside** this CoP — Director of Fire Services rules.

---

## Regulatory Overview

This CoP covers **above-ground** oil storage installations and associated works for petroleum products in Hong Kong — any **static tank ≥ 110,000 litres**, or a group containing such a tank — including the bunded area, drainage, pipelines within the bund, and receipt/issue pipelines to related jetties. Primary design drivers are **pollution containment** (coastal / restricted waters) and **fire/explosion safety distances**; general building structure still follows Building (Construction) Regulations.

---

## Critical main topics and subtopics

### 1. SD kill-switches — product class & capacity gate

| Class (flash point) | Definition | SD implication |
|---|---|---|
| **Class 1** | Flash point **< 23°C** | Full safety-distance tables; floating roof mandatory above capacity threshold |
| **Class 2** | **23–66°C** inclusive | Spacing mainly operational; **≥ 10 m** (or **6 m** if total facility < 7,000 m³) from outer boundary; space from Class 1 tanks per Class 1 tables |
| **Class 3** | **≥ 66°C** | Spacing by construction / ops convenience only |
| **Heated product** | Artificially heated **above** its flash point | Treat as **Class 1** |

| Gate | Rule |
|---|---|
| Installation trigger | Tank / group with tank **≥ 110,000 L** above ground |
| Floating roof mandatory | Class 1 tanks **> 1,000 m³** capacity |
| Future-proof Class 2 | If Class 2 tanks may later hold Class 1 → **plan to Class 1** distances now |

---

### 2. Safety distances — massing drivers (horizontal, nearest points)

#### 2.1 Class 1 — fixed roof (default / larger facilities)

| Factor | Min distance |
|---|---|
| Between groups of small tanks (each ≤ 10 m dia; group aggregate ≤ **8,000 m³**; no Class 2/3 heated above flash) | **15 m** |
| Between such a group and any tank outside the group | **15 m** |
| Between tanks not in a small-tank group | Half dia of larger, or dia of smaller, or **15 m** — **whichever least**, but **never < 10 m** |
| Tank ↔ filling point / filling shed / building | **15 m** |
| Tank ↔ outer boundary / non-hazardous area / fixed ignition source | **15 m** |

Within a qualifying small-tank group, tank-to-tank spacing is construction/ops only.

#### 2.2 Class 1 — floating roof

| Factor | Min distance |
|---|---|
| Between two floating-roof tanks | **10 m** (larger tank ≤ 45 m dia); **15 m** (larger > 45 m dia) |
| Floating ↔ fixed roof | Same formula as fixed-roof inter-tank (half larger / dia smaller / 15 m least; **≥ 10 m**) |
| Floating tank ↔ filling / shed / building **without** ignition source | **10 m** |
| Floating tank ↔ boundary / non-hazardous / fixed ignition | **15 m** |

**Height uplift:** tank height **> 18 m** → multiply Table 2 distances by **height / 18**.

#### 2.3 Class 1 — total installation capacity **< 7,000 m³** (relaxed)

| Factor | Min distance |
|---|---|
| Tanks ≤ 10 m dia **and** ≤ 14 m high | Construction / ops only |
| Larger tanks | Half larger / dia smaller / 15 m least; **≥ 10 m** |
| Tank ↔ filling / shed / building | **15 m**; may reduce to **≥ 6 m** if tanks ≤ 10 m dia |
| Tank ↔ boundary / non-hazardous / fixed ignition | **15 m**; may reduce to **≥ 6 m** if tanks ≤ 10 m dia |
| Class 2 ↔ outer boundary | **≥ 6 m** (vs 10 m for larger facilities) |

#### 2.4 Class 2 / 3 (all capacities)

| Product | Rule |
|---|---|
| Class 2 | Inter-tank: ops convenience; from Class 1: use Class 1 table; outer boundary **≥ 10 m** (≥ 6 m if facility < 7,000 m³) |
| Class 3 | Ops convenience only |

**Override:** predicted foundation load-spread / differential settlement may force **greater** tank spacing than the tables.

---

### 3. Floating roof definition (Class 1 > 1,000 m³)

Acceptable as floating-roof tank only if:

| Option | Requirement |
|---|---|
| Open-top | Pontoon or double-deck metal floating roof per **API 650** |
| Fixed roof + internal floater | Fixed metal roof with top/eaves ventilation (**API 650**) **plus** pontoon/double-deck floater **or** metal floating cover with liquid-tight metal flotation that still covers liquid when **half flotation is lost** |

**Treat as fixed roof:** internal metal pan/cover that fails 2.3(ii), or plastic-foam flotation (except seals) — even if foam is metal/fibreglass encapsulated.

---

### 4. Bunded areas — containment & fire walls

#### 4.1 Volume (excludes displacement of other tanks and foundations)

| Contents | Min bund containment |
|---|---|
| **Class 1** | **≥ 105%** of largest tank max operating capacity; **self-contained** — no weirs/overflows to other areas (may still hold Class 2/3 tanks inside) |
| **Class 2 / 3** | **≥ 100%** of largest tank; volume of **connected** bunds may count if relief spillways/weirs can carry overflow from largest tank releasing **100% in 15 minutes** |

#### 4.2 Fire-wall compartments (Class 1 — limit fire spread)

| Element | Limit |
|---|---|
| Fire wall height (from outside ground) | **2.0–3.7 m** |
| Class 1 capacity per compartment — **fixed roof** | **≤ 60,000 m³** |
| Class 1 capacity per compartment — **floating roof** | **≤ 120,000 m³** |
| If under those caps | Bund walls may serve as fire walls; no further compartmentation needed |

Locate walls for close firefighting approach; provide adequate MOE **over** fire walls.

#### 4.3 Wall / floor construction (pollution-critical)

| Item | Rule |
|---|---|
| Design fluid density for bund strength | Treat petroleum = **water** |
| Earth/rock embankment | Profile/compaction per **BS 6031:1981**; impermeable surfacing; protect inner face (concrete blinding / precast / etc.) |
| Acceptable facing example | Reinforced sand-cement render **≥ 50 mm**, 4:1 sand:cement, light mesh, panelled with sealed joints |
| RC / prestressed / masonry bund walls | Per Building (Construction) Regs; masonry that absorbs product → impermeable render |
| Expansion joints in bund wall | **≤ 30 m** centres; water seals at all wall/base joints |
| Concrete bund floor | **≥ 125 mm** reinforced on solid ground; steel **≥ 0.25%** plain / **≥ 0.20%** deformed or HY mesh each way |
| Joint sealants | **No bitumen** in Class 1 bunds; elsewhere renew embrittled bitumen; other sealants petroleum- + UV-resistant |
| Compacted granular rock as floor | **Not permitted** |
| Membrane required when | Granular soil under basin; drinking/ecological water table; nearby waterways; nearby buildings; seepage to low ground or off property |
| Membrane performance | Continuous impermeable joins to bund wall/pad; UV + physical protection blanket; abandon if differential settlement would rupture without reliable prevention |
| Alt. floor materials | OK if product penetrates **≤ 50%** of thickness in **48 hours** |

---

### 5. Foundations & settlement (layout can override spacing tables)

| Topic | SD / design note |
|---|---|
| Standards | **BS 2654:1984**, **API 650**; Building (Construction) Regs |
| Profiles | Cone-up (centre high) or cone-down (to central sump) |
| Compacted granular pad | Sound granular material in **150 mm** layers, 6–10 t roller; top permeable drainage layer; **50 mm** bitumen-sand weatherproof (not rigid plaster/concrete) |
| Pad edge fall | **≥ 1:10** across **≥ 500 mm**, then **1:1.5** down to bund floor; peripheral seal after water test |
| Concrete ring wall | For shell load distribution + surge/fill horizontal forces (**API 650 App. B**); **no perforations**; flexible sealed joint if surrounded by bund paving |
| Settlement | Design for predicted settlement on tank + connecting pipework; differential vs pipe racks / adjoining tanks/buildings may **increase** spacing beyond Table mins |
| Bearing pad level | Above depth stormwater could reach steel tank base |
| Water under bottom | Permanent barrier + flexible accessible peripheral seal (HK tropical marine + seawater fire tests are aggressive) |

---

### 6. Tanks, valves, leak detection

| Item | Requirement |
|---|---|
| Vertical welded steel | **BS 2654:1984** or **API 650** |
| Horizontal steel | **BS 2594:1975** + App. to **BS 799 Part 5:1975** |
| Leak detection | **Each tank** — suitable system |
| Jetty / pipeline terminal valves | Steel bodies throughout; clear position indication if non-rising spindle; heatable if product may solidify |
| Corrosion | External paint systems; underside protection (bitumen pre-paint + pad barrier + peripheral seal) |

---

### 7. Drainage & interceptors — hard process rules

#### 7.1 Zoning principle

| Area type | Drainage |
|---|---|
| Clean areas (remote yards, offices, roadways outside contamination risk) | Normal storm/sewage |
| Contaminable areas (bunds, filling, pipe racks/trenches, kerbed pump/hose points) | Controlled discharge → **interceptor** → outfall |

#### 7.2 Bund drainage (critical)

| Rule | Detail |
|---|---|
| **No automatic discharge** | Never auto-drain bund surface water |
| Allowed methods | **Manual** non-auto pumps after rain; **or** gravity valves/penstocks that require **manual** activation (motorised OK if manually started) |
| Containment integrity | Zero leakage when pumps off / valves closed |
| Valve access | Operate from **outside** bund; discharge to open pit/channel **visible** from operator; rising spindle / indicating headstock shows **fully closed** |
| Intermediate sand traps in bund | **Not recommended** (retain product/sludge) |
| Walkways | To all tanks/valves before bund is emptied |
| Weatherproof signs | At every valve/penstock — purpose + when open/closed |
| Design storm | Max flow for **1-in-10-year** HK rainstorm |
| Contaminated piped drains | Continuously **surcharged**, horizontal, water seal **≥ 50 mm** (fire-spread control); open channels must run dry after rain |
| Self-cleaning open drains | Min velocity **0.75 m/s** at ¼ depth (where used) |
| Floating-roof drains | Primary + emergency per BS 2654 / API 650; size for **1-in-10-year** intensity; compatible with fixed fire-water |

#### 7.3 Unbunded high-risk + pumps

| Item | Rule |
|---|---|
| Loading bays / package filling | Interceptor before public drain / watercourse / sea |
| Storm bypass on interceptor | Only for **large** unbunded catchments where first flush carries most pollutant |
| First-flush design (if bypass) | Treat first **(t+2)** minutes of 1-in-10-year storm; **t** = time of concentration from farthest point (minutes) |
| Pumps / hose points | Concrete floor + perimeter kerbs → sump + outlet valve → interceptor (or steel drip pan for isolated pumps) |

#### 7.4 Interceptor checklist

| Must | Detail |
|---|---|
| Location | **Outside** bunds; all bund water through interceptor |
| Bypass | None for bund drainage (except unbunded rule above); bund water must not enter bypass |
| Capacity | Max expected surface water + product under controlled bund-valve flow; outfall quality per **Director of Environmental Protection** (API/IP / multi-plate OK if quality met) |
| Access | Prefer open chambers with guardrail; if covered, clear view of inlet, chambers, outlet |
| Outlet control | Valve/penstock between outlet weir and outfall; clear open/closed indication; operable with interceptor full |
| Sample point | At each outlet valve |
| Product removal | Means to remove floating product |

---

### 8. Fire fighting, electrical, security (interface items)

| Topic | Architect / layout note |
|---|---|
| FSI | Per **Director of Fire Services** — not detailed in this CoP |
| Tank layout | Spacing ≠ accessibility — layout must satisfy FSD for firefighting approach |
| Electrical / lightning / static | Institute of Petroleum **Electrical Safety Code**; static also European Model Code Part II:1980 §9 (or Authority-approved equivalent) |
| Security fence | **≥ 1.8 m** high within lot; enclose tanks, pumps, loading/unloading |
| Emergency exits in fence | **≥ 2** exits, separated by **≥ 5 m**; gates open **outwards**; **not** self-locking |

---

### 9. Pipelines & jetty interface

| Item | Rule |
|---|---|
| Fabrication | Appropriate BS or API; adequate safety factor |
| Preference | All-welded; allow thermal expansion/contraction |
| Settlement | Flexibility for pipelines to major tanks |
| Segregation | Isolating flanges/blanks/spades — adequate strength + clear location/setting indication |
| Associated works | Include receipt/issue pipelines to related jetties |

---

### 10. Marine pollution equipment (if berthing vessels)

| Equipment | Minimum |
|---|---|
| Boom length | **≥ 2.5 ×** max permitted vessel length; internationally recognised type + anchorage; desirably connectable to government ‘unicorn’ booms |
| Dispersant (Type III concentrate) | ≤150k DWT: **8,000 L**; ≤100k: **5,500 L**; ≤50k: **2,700 L**; coastal/<10k: **1,100 L** (Type II: multiply by dilution factor) |
| Dispersant licences | Gov-approved type; supplier + user licences from **DEP** |
| Oil skimmer | **1** unit; open-sea capable; **≥ 10 m³/h** medium fuel oil; ancillary storage **≥ 18 m³** |
| Sorbent | **≥ 1,000** pads **or** **≥ 500 m**; hydrocarbon-only; pads **≥ 450 mm** wide × **≥ 4 mm** thick |
| Maintenance | Per manufacturer, or inspect **≤ 6 months** |

---

### 11. Licensing / ops hooks that affect early design

| Item | Implication |
|---|---|
| Operating instructions | BA must accept before licence; English **and** Chinese; fire/explosion/pollution procedures |
| Contingency plan | Fire Order + spillage plan (sensitive receptors, alert chain, containment/recovery, disposal, equipment, training) |
| Drills | Full-scale **≤ 12 months**; familiarization at intervening **6 months** |
| Bund valves normally closed | Except supervised storm discharge; closed end of day; closed while tank receiving stock |
| Chemical waste | Tank sludge / oily waste → Cap. 354; register with DEP; temporary storage needed |
| Effluent | WPCO Cap. 358 licence in Water Control Zones (or DEP consent outside); Technical Memorandum standards |
| Post-repair water test | Fill to max capacity; hold level **48 hours** |

---

**SD takeaway:** Classify products (flash / heated = Class 1) and total capacity (**< / ≥ 7,000 m³**) before drawing tank grids. Lock **safety distances** (10–15 m band + height/18 uplift for tall floaters), **floating roofs** for Class 1 **> 1,000 m³**, bund volume (**105% / 100%**), Class 1 compartment caps (**60k / 120k m³**), fire-wall height (**2–3.7 m**), and a **non-automatic** bund drain → **interceptor** path. Fence exits, FSD approach, settlement-driven spacing, and (if marine) boom/dispersant/skimmer kit all need site area from day one — do not treat this as a tank-only diagram.

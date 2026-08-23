# Technical Requirements for Plumbing Works in Buildings
**Architect critical summary for schematic design**  
April 2026 version | Water Supplies Department / Water Authority

> Read with: [Technical Requirements for Plumbing Works in Buildings (April 2026) (English).pdf](Technical%20Requirements%20for%20Plumbing%20Works%20in%20Buildings%20(April%202026)%20(English).pdf); WWO Cap. 102 / WWR Cap. 102A; Appendix 1A (essential plumbing design checklist); Figs. 5–6, 14–15, 17–18, 21, 24–32, 36, 41–42. Clauses marked `*` = WWO/WWR statutory; `#` = WA mandatory for approval. Part B material standards omitted — design constraints only.

---

## Regulatory Overview

This document consolidates the former Handbook on Plumbing Installation for Buildings, Hong Kong Waterworks Standard Requirements, and related WSD circulars into one WA approval standard for **inside service** and **fire service** plumbing in local buildings (fresh water for domestic, trade, shipping, construction, flushing, and firefighting; salt water typically for flushing/FS).

At schematic design, the hard triggers are building height **> 12 m** (indirect supply for all floors — FW and flushing), dedicated **meter / master-meter / tank / pump** space in communal zones, and **FS separated from potable at the lot boundary**.

---

## Critical main topics and subtopics

### 1. Layout killers early (§2)

| Rule | SD implication |
|---|---|
| `#2.1.1(c)` Communal service **shall not** run through individual premises | Risers, meters, and communal pipe ducts sit in **communal** cores/corridors from day one |
| `#2.1.1(e)` One consumer’s inside service **shall not** pass through another’s premises | No flat-to-flat pipe shortcuts; plan horizontal/vertical routes before unit layouts freeze |
| `*2.1.2` Fresh water purposes | Domestic / trade / shipping / construction / flushing / firefighting — programme the correct plant for each |

**SD takeaway:** Pipe duct and meter-room strategy is a massing constraint, not a late M&E coordination item. Use Appendix 1A as the new-building plumbing checklist.

---

### 2. Height / supply mode trigger (§4.2.2 / §4.3.4)

Building height follows Cap. 121 NTEH meaning (footnotes 7 & 10). Applicable to new Form WWO 542 on/after **1 Jan 2019** (with limited earlier WWO 132 exceptions).

| Height | Fresh water `#4.2.2` | Flushing `#4.3.4` |
|---|---|---|
| **≤ 12 m** | Direct **or** indirect (storage tank / sump+pump / hydro-pneumatic) — Fig. 5–6 | Indirect only: direct-to-roof tank **or** sump/hydro — Fig. 14 |
| **> 12 m** | **Indirect only** for **all floors** (sump+pump / hydro / WA-approved equivalent) — Fig. 6 | Same — sump+pump / hydro / WA-approved for **all floors** |

| Residual pressure | Value |
|---|---|
| Fresh water at connection `#4.2.2.3` | Design to WA-advised minimum; typically **15–20 m** head |
| Salt flushing at connection `#4.3.4.3` | Min **15 m** head |

| Pressure / pumps | Rule |
|---|---|
| Draw-offs `#4.2.4.7` / `#4.3.5.6` | **No** draw-off ≥ **6 bar** → PRVs or break-pressure tanks |
| New sump+pump `#4.2.4.9` / `#6.3.1` | **Standby / duplicate** pumpset; capacity ≥ designed outflow of tank served |

**SD takeaway:** Mid- and high-rise = G/F or basement **sump tank + pump room** + roof **storage tanks** for both FW and flushing. Low-rise can stay direct for FW only if ≤12 m.

---

### 3. Meter rooms and positions (§3.1–3.2)

#### 3.1 Where meters go

| Case | Location |
|---|---|
| Direct supply `#3.1.4` | Communal meter room/box/cabinet at convenient accessible location |
| Indirect supply `#3.1.4` | Communal meter room/box/cabinet at **roof** (or other convenient communal) |
| Roof meters + pressure &lt; 15 m `#3.1.5` | Fullway gate valves before meters |
| Sump+pump with roof meters `#3.2.1.1(c)` | Sump **and** roof storage **before** meter positions |
| Salt water `#3.1.9` | Not metered, but **meter position** still required near lot boundary / connection |
| Master meter max `#3.1.13` | **300 mm** |
| Trade min meter sizes `#3.1.11` | Chinese restaurants **50 mm**; other restaurants / fast food / meat / laundry **25 mm** |

#### 3.2 Architectural & M&E for meter rooms/boxes (`#3.2.2`)

| Item | Hard rule |
|---|---|
| Purpose | Dedicated to meters only (incl. vacant + check positions); grouped |
| Foreign BS | **No** drainage stacks, fire hoses, cables, ducts through room — only lighting, ventilation, drainage, smart metering for meter use |
| Aisle depth | Face of meter group to opposite wall/door opening: **≥ 1000 mm** clear, no obstacles |
| Inward door opposite meters | **≥ 600 mm** from meters to fully open door |
| Door clear | **W ≥ 800 mm, H ≥ 2000 mm** |
| Meter box/cabinet depth | Clear depth from outside face **≤ 800 mm**; readable without leaning in |
| Access | Entrance from **communal** area; safe free uninterrupted access |
| Lock / handle | Lock **0.9–1.1 m** AFFL; free egress if self-closing; cylindrical/spherical handles only (Fig. 41–42) |
| Signage | 「水錶」 / “Water Meters”, font **≥ 30 mm** |
| Multiple rooms | **Master-key** locks |
| Village-type | Meters at **boundary**, accessible from public area |
| Illumination | **≥ 120 lux** at meters |
| Ventilation | Mech vent **≥ 6 ACH** |
| Drainage | Adequate drainage for floor-level rooms/boxes |
| Flange clearance `#3.2.2.7` | **≥ 150 mm** both ends of meter flange |
| Group meter height `#3.2.4.1` | **300–1500 mm** AFFL |
| Corridor meters `#3.2.4.1` | **750–1500 mm** AFFL; clearances per Fig. 36 |
| Display board `#3.2.3.1` | Top ≤ **1800 mm**, bottom ≥ **500 mm** AFFL; waive if ≤3 meters |
| Landscape meters `#3.2.6` | Above ground; working headroom **≥ 2 m** in front of box |

**SD takeaway:** Meter rooms are dedicated rooms with fixed geometry — do not share with other MEP. Size by flat count early; roof meter rooms are typical for indirect systems.

---

### 4. Master / check / sub-meters (§3.3)

| Trigger | Requirement |
|---|---|
| New development **> 1 building block** `#3.3.2.1` | Master meters for **FW + TMF + FS** |
| Single-block / detached village `#3.3.2.2` | MM **not** required if pipe to meters exposed or in trench/duct; branch &lt; **6 m** from tee may be buried |
| **All new government premises** `#3.3.2.3` | MM always (WWO 542 on/after 1 Jan 2021), including single-block |
| Sub-meter chambers `#3.3.3.2` | On underground branches by building-cluster **≤ 5 blocks** same type; **not** needed if ≤5 blocks same type only (Figs. 24–25) |
| TMF `#3.3.3.3` | No sub-meter chambers |
| Fold into building `#3.3.3.4` | No separate SM chamber if check meter room &lt; **6 m** from tee, or all pipe exposed |

| Master meter arrangement | Detail |
|---|---|
| Count `#3.3.4.1` | One MM per **FW / TMF / FS** inlet at **lot boundary** |
| Location `#3.3.4.2` | **At-grade** where feasible (justify if not) |
| Box vs room `#3.3.4.9` | MM ≤ **100 mm** → box/cabinet (Fig. 31); MM **&gt; 100 mm** → **master meter room** |
| FS vs potable `#3.3.4.12` | FS **separated from potable at lot boundary**; FS unaffected by potable interruption |
| Strainer `#3.3.4.14` | Upstream of **all** MM |
| Check meter `#3.3.5` | Near end of communal service per block for FW, flushing, FS — accessible communal |
| Buried covers `#4.2.4.2` / `#5.4.1.5` | HyD: **450 mm** non-carriageway / **900 mm** carriageway |

**SD takeaway:** Multi-block estates need up to three at-grade boundary MM positions (FW/TMF/FS) plus per-block check meters. Dual potable/FS entries are a site-plan driver.

---

### 5. Flushing water plant (§4.3)

| Rule | Detail |
|---|---|
| Separate system `#4.3.3.1` / `*4.3.5.2` | Flushing = separate plumbing; **separate** storage tank |
| Materials `*4.3.5.1` | All tanks/pipes salt-water capable (BO requires flushing for new buildings) |
| Height trigger | Same **12 m** rule as §2 above |
| Inlet `#4.3.5.3` | ≥ **40 mm**; before meter exposed/in duct to lot boundary |
| Meter `#4.3.5.4` | Communal, **as close as possible** to FW meters |
| TMF `#4.3.3.3` | Meters required; usually whole building |
| Mixed/independent + TMF `#4.3.5.5` | Tank arrangement per Fig. 15 |
| Storage sizing | See §7 / Table 6.2.5.2.1 — min **250 L** |

**SD takeaway:** Dual tank farms (FW + flush) on roof/sump; co-locate flush meter with FW meters; salt-resistant finishes in flush plant.

---

### 6. Fire service connections (§5)

| Rule | Detail |
|---|---|
| Independent connection `#5.4.1.1` | FS from fresh **or** salt; **entirely independent** of other site supplies |
| Boundary → MM/check `#5.4.1.4–5` | Exposed or drained trench/duct; cover **450 / 900 mm** |
| Valves `#5.4.1.6` | Fullway gate + NRV as close as possible to Gov connection |
| Sprinkler/drencher dual `#5.4.2.2` | Dual from unrestricted industrial ring; outside zone: twin (unrestricted + distribution) where practicable |
| No unrestricted main `#5.4.2.3` | FSD may require FS tank as secondary; single or dual to that tank |
| Sharing `#5.4.2.4` | Sprinkler/drencher from Gov mains **not** feed other FS (e.g. hose reels); **common suction tank** for sprinkler + HR OK with FSD endorsement |
| FH/HR `#5.4.3.1` | **Not** direct from Gov mains; HR in glass-front cabinet, glass ≤ **1.5 mm**, frangible, striker nearby |
| Common tank ban `#5.4.3.2` | **No** common tank for firefighting + flushing/other when Gov supply involved |
| Street FH `#5.4.4.2` | Follow Fig. 21 |
| FS ring mains `#5.4.5` | Large industrial → unrestricted if practical, else dual; no other service off ring without WA approval |

**SD takeaway:** Separate FS entry at boundary; never share FS tank with flushing on Gov supply; sprinkler dual/twin street-main strategy affects site utility layout.

---

### 7. Cisterns, pumps, PRVs (§6)

#### 7.1 Location / separation / access

| Rule | Detail |
|---|---|
| Access `*6.2.1.1` | Easily accessible; permanent or portable ladder |
| Top-access headroom `#6.2.1.1.4` | **≥ 800 mm** above cistern |
| Adjoining potable / non-potable `*6.2.1.2.1` | **Physical break** (separate walls/slabs; tie beams OK if no contamination path) |
| Stacking `#6.2.1.2.2` | Non-potable **not** above potable in same compartment; if forced: physical break + WA justification |
| Covers `#6.2.3` | Lockable close-fitting; potable: double upstand interlocking; double-sealed covers required except irrigation / cleansing / AC make-up / flushing / FS-only |

#### 7.2 Inlet / outlet / overflow (layout)

| Rule | Detail |
|---|---|
| Outlet vs inlet `#6.2.4.1.1` | Outlet opposite inlet where possible |
| Freeboard `*6.2.4.2.9` | Shutoff **25 mm** below overflow invert; inlet invert ≥ **25 mm** above overflow top |
| Outlet invert `#6.2.4.3.1` | ≥ **30 mm** above floor (&lt;5000 L); ≥ **100 mm** (≥5000 L) |
| Overflow `*6.2.4.4.2` | ≥1 size larger than inlet, never &lt; **25 mm**; conspicuous; **not** to drain/sewer/other cistern |
| Discharge `#6.2.4.4.3–4` | Communal visible area **or** overflow alarm to 24h manned office |
| Warning pipe `#6.2.4.4.8–9` | ≥ **25 mm**, below overflow; to conspicuous exterior (roof) / outside pump room (sump) or 24h office |
| Mesh `#6.2.4.4.10` | Openings ≤ **2 mm** |

#### 7.3 Storage sizing (SD drivers) — `#6.2.5`

| Item | Criterion |
|---|---|
| Sump : roof `#6.2.5.1` | Recommended **≈ 1 : 3** (or justify) |
| Flushing `#6.2.5.2` (WWO 542 ≥ 1 Jan 2019) | Min **250 L** total. Residential WC **30 L**/apparatus; Commercial urinal **30 L**, WC **40 L**/apparatus |
| Domestic sump+pump `#6.2.5.3` | ≤10 flats: **135 L/flat** (min total incl. sump **500 L**); &gt;10 flats: **+90 L** each additional |
| Industrial `#6.2.5.4–5` | Separate process vs ablution systems (**no interconnect**); capacity = **1-day demand** |
| Twin-tank `#6.2.6.2` | Capacity **&gt; 5000 L** → twin-tank (subject to plant space); each compartment own inlet/outlet/overflow/drain |
| Duplicate pumps `#6.3.1` | Required for sump+pump |
| PRV `#6.5` | Bypass second PRV (except FS); pressure indicator; fault alarm to 24h office (except FS) |

**Trade/commercial storage highlights** (Table 6.2.5.6.1):

| Use | Storage |
|---|---|
| Food shop | Small **900 L** / Large **1800 L** |
| Restaurant | **25 L/seat** |
| Barber / beauty | **135 L/chair** |
| School drinking | **4.5 L/head** |
| Clinic | **250 L** (surgery) |
| Dentist | **250 L**/unit |
| Office / cinema | **45 L/point** |
| Hotel | Single **45 L** / Double **70 L**/room (H+C) |
| Boarding | **25 L/bed** (H+C) |
| Changing room | **90 L/shower** (H+C) |
| Hospital | 1-day demand per authority |
| Laundry | L × 120 min × N / T |

**SD takeaway:** Size roof + sump from flat/fixture count at concept; &gt;5000 L forces twin cells and double pipe sets; keep flush/FS tanks structurally separated from potable.

---

### 8. Hot water layout hooks (§4.2.7)

| Situation | Rule |
|---|---|
| Heater test ≥ 1.5× max static `*4.2.7.1.1` | Non-pressure / cistern-type / compliant unvented electric / instantaneous may connect direct — no local cistern |
| Test &lt; 1.5× on direct supply `*4.2.7.1.2` + `#4.2.7.1.3` | Heater from cold cistern; **45 L separate mains cistern per flat** |
| Pressure-type thermal storage (non-compliant unvented) on direct `#4.2.7.1.4–5` | Storage cistern; **45 L/flat** |
| Roof-tank / sump-pump flats `#4.2.7.1.6–7` | No separate HW cistern if dedicated downfeed (or branch from oversized downfeed **above** heater top) |
| Top-floor gas geysers `#4.2.7.1.8` | Low-pressure governors if head &lt; **5 m** to highest HW outlet |
| Mixers `*4.2.7.1.9` / `#4.2.7.2.3` | Cold from **same source** as HW; centralized: separate downfeed, outlet slightly **lower** than HW feed |
| Central HW feed `#4.2.7.2.1–2` | Cold feed from roof cistern / sump booster = **HW only** source |
| Expansion `#4.2.7.2.4–5` | Expansion pipe to atmosphere above cistern; **not** replaced by safety/air/relief valves |

**SD takeaway:** Direct-supply towers with pressure heaters need per-flat 45 L cisterns or switch to roof-tank downfeeds. Centralized HW needs dual downfeeds from the roof cistern.

---

### 9. Backflow / concessionary uses (§4.2.3 / §4.2.5)

**Break tank required** (Table 4.2.3.7.2) for schematic space planning:

| Installation | Device |
|---|---|
| Commercial ag / insecticide / hydroponics | **Break tank** |
| Gardens / nurseries / large landscape / sports fields | **Break tank** (Note 8 standpipe exceptions) |
| Cooling towers | **Break tank** |
| Industrial processes | Break tank **or** RPZ |
| Smart WCs | Break tank **or** equivalent |
| RPZ without maintenance program `#4.2.3.5.2` | Use **break tank** instead |

**Concessionary supply mode** (Table 4.2.5.2.1 highlights):

| Usage | Mode |
|---|---|
| Pools, features, lakes | Off-tank |
| Point irrigation | Mains OK (anti-vac + NRV); planting ≥ **30 m²**; 20 m hose per point |
| Drip irrigation | Off-tank; one connection unless barriers / spacing **&gt; 40 m** |
| Automatic irrigation `#4.2.5.4a` | **Off-tank required** |
| Building / carpark cleansing | Off-tank; carpark cleansing from fresh cistern + separate meter (or building cleansing system) — Fig. 6A |
| Public draw-offs `#4.2.5.4` | Locked external protective box |

**SD takeaway:** Cooling towers, automatic irrigation, and large landscape trigger extra break/off-tanks — allocate plant early.

---

### 10. WELS product grades (§7)

Does not drive room sizes; drives FF&E schedules at SD.

| Product / location | Grade |
|---|---|
| Showers (bathrooms/toilets of all premises; domestic kitchens scope per `#7.3.1`) | **G1 or G2** |
| Kitchen sink taps | **G1–G3** |
| Basin taps (bathrooms/toilets) | **G1 or G2** |
| Urinal flushing valves | **G1 or G2** |
| WC — domestic toilets | **G1 or G2** |
| WC — non-domestic without auto-flush | **G1 or G2** |
| WC — non-domestic with auto-flush, or disabled | **G1–G3** |
| Fallback `#7.4` | Non-compliant tap/shower + WELS flow controller as compliant “combined” device |

Public/communal lavatory basins `#6.7.1.2`: self-closing non-concussive **or** IR auto taps.

---

### SD space checklist

1. **Height &gt; 12 m** → FW + flush **indirect** (sump + roof tanks + standby pumps) for all floors.
2. **Meter rooms**: dedicated; door **800 × 2000**; aisle **1000 mm**; meters **300–1500 mm**; box depth **≤ 800 mm**; **120 lux** / **≥ 6 ACH** / drain.
3. **Multi-block** → at-grade MM for FW / TMF / FS; MM **&gt; 100 mm** needs room; FS split from potable at boundary.
4. **Flush tank** separate, salt-capable, sized by §6.2.5.2 (min 250 L); meter near FW meters.
5. **Domestic tanks** by §6.2.5.3; **&gt; 5000 L** twin-tank; top access **800 mm** headroom; potable / non-potable separation.
6. **FS**: independent connection; sprinkler dual/twin rules; HR **not** mains-fed; no FS + flush common tank on Gov supply.
7. **Draw-offs ≤ 6 bar** → PRV floors or break-pressure tanks; PRV with bypass + 24h fault alarm (except FS).
8. **WELS** grades locked into kitchen/bath fixture schedules; cite Figs. **5–6**, **14–15**, **24–32**, **36**, **17–18**, **21**, **41–42**.

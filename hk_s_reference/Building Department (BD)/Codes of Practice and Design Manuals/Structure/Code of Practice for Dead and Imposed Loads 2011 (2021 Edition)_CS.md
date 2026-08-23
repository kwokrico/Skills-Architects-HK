# Code of Practice for Dead and Imposed Loads 2011
**Architect critical summary for schematic design**  
First issue May 2011 | Buildings Department  
This revision: **July 2021** (incorporates 2014 Corrigenda, 2016 Amendments, 2020 Amendments)

> Scope note: Deemed-to-satisfy guidance for **dead loads** and **minimum imposed loads** on buildings, building works, streets and street works. Values quoted from the Building (Construction) Regulation are statutory minima; other Code provisions are deemed to satisfy the Buildings Ordinance and related regulations. All tabulated loads are **unfactored / characteristic**. Does **not** cover wind (Wind Code 2019) or construction loads. Pair with SUC / Steel / Glass / Wind codes for combinations and member design. RSE owns calculations; AP must lock **floor-use class map, roof access type, greenery DL, vehicle class + fire path, partition-on-plan strategy, barrier category, and balcony/UP typology** at SD — these drive slab depth, transfer structure, carpark hierarchy, façade edges, and GBP notes before massing freezes.

---

## Regulatory Overview

This Code sets the **minimum vertical and horizontal live-load envelope** for Hong Kong building, street and associated works design: dead-load composition rules; imposed loads by **floor-use Class 1–8**; vehicle traffic Classes 6A–6E; roof/canopy Classes 7A–7D; affiliated elements (balconies, UPs, stairs, AC hoods); movable-partition allowances; beam/column load reduction; protective-barrier and vehicle-barrier horizontal loads; surcharges on retaining structures; industrial dynamic extras; and a performance path for unlisted uses.

At schematic design, lock **intended use per floor plate** (not zoning label alone), **accessible vs inaccessible roofs**, **heaviest vehicle into the structure**, whether partitions appear on BD plans, and barrier category for every public edge — misclassifying office / retail / assembly / plant / carpark / refuge early under-sizes structure or forces late redesign.

---

## Critical main topics and subtopics

### 1. Scope, symbols and rules that constrain SD before numbers (§1, §3.1)

#### 1.1 What this Code does / does not do (§1.1)

| Covered | Not covered / elsewhere |
|---|---|
| Dead + imposed loads for building, street, building works, street works | **Wind** → Wind Code |
| Minimum IL by use (incl. B(C)R values in §3 tables) | **Construction loads** → designer must still allow |
| Horizontal loads on person / vehicle barriers | Material member design → SUC / Steel / Glass |
| Surcharges on slopes / retaining | Highway / railway structures → HyD **SDM**; marine → CEDD **Port Works Design Manual** |

Unprescribed uses: adopt IL from **reliable information / data** or §4 performance path → **Building Authority acceptance**.

| Reliable information (examples) | Reliable data (examples) |
|---|---|
| CEDD Port Works Design Manual (marine) | Research from recognised academic institutions |
| HyD Structures Design Manual for Highways and Railways (SDM) | International standards / codes |
| | Accredited laboratory reports |
| | Supplier / manufacturer technical literature |

#### 1.2 Symbols architects will see on RSE notes (§1.2)

| Symbol | Meaning |
|---|---|
| `qk` | Uniformly distributed imposed load (kPa) |
| `Qk` | Concentrated load (kN) or line load (kN/m) |
| `M` | Gross mass of heaviest vehicle (kg) — vehicle barriers |
| `v` | Vehicle velocity normal to barrier (m/s) |
| `δc` / `δb` | Vehicle deformation / barrier deflection (mm) |
| `γ` | Factor increasing impact force at foot of long straight ramps |
| `L` | Loaded length (m) for Class 6B–6D UDL |

#### 1.3 Application rules that change structural sizing (§1.1.3, §3.1)

| Rule | SD implication |
|---|---|
| All Code loads are **unfactored**; treat as characteristic for limit-state design | Do not confuse with ultimate factors in material codes |
| IL = greatest applied load likely from **intended use** over service life (excl. dead & wind; includes adjacent ground forces per B(C)R) | Brief real fit-out, not marketing label |
| Tabulated IL are **minima** — raise if equipment / display / storage heavier | Banks, kitchens, stages, medical kit, art, UPS |
| Apply **`qk` OR `Qk`**, whichever worse — **separately** (not additive as one case) | Punching, edge beams, local cantilevers can govern |
| Place UDL on area(s) for **most adverse** effect; place `Qk` at worst position; `Qk` spread over Code contact patch | Transfer slabs, long spans, continuous beams — adverse patterning |
| Where permanency is doubtful → treat as **imposed**; **no** §3.7 reduction | “Future plant / loose fill / temporary heavy” ≠ dead load |
| Construction loads out of scope | Façade install, roof maintenance, formwork still need designer allowance |

---

### 2. Dead loads — what must sit in the DL budget (§2)

#### 2.1 What counts as dead load (§2.1.1)

Include all permanent items acting continuously with insignificant time variation:

| Category | Examples |
|---|---|
| Structure | Frames, slabs, walls, foundations |
| Affixed structural elements | Windows, claddings, other permanent construction |
| Non-structural permanent | Finishes, roofings, surfacing, linings, kerbs, suspended ceilings, insulation, earth, ballast |
| Permanent equipment | Fixtures, fittings, permanently fixed wiring & reticulated services |
| Plan-indicated partitions | Positions shown on BD approval plans |
| Greenery systems | Soil fill, waterproofing, drainage for gardening / planting |

#### 2.2 Tanks, doubt, and partitions (§2.1.2–2.2.2)

| Item | Classification |
|---|---|
| Tank / receptacle **shell** | Dead |
| Tank / receptacle **contents** | Imposed |
| Partitions **shown** on BD plans | Dead — calculate from drawn layout |
| Partitions **envisaged but not shown** | Imposed — §3.6 |

**SD takeaway:** Showing partitions on GBP vs leaving open-plan is a **load classification decision**, not only an interiors choice. Drawn walls = DL; flexible fit-out = IL + no reduction.

#### 2.3 Roofings, greenery, cladding, finishes (§2.2.3–2.2.4)

| Topic | Rule |
|---|---|
| Roofings | Membrane, protective screed, tiles — from component density × thickness × area |
| Greenery | Soil + waterproofing + drainage + **plants** = **dead** |
| Claddings | Al / metal, polished granite, limestone, marble + fixings |
| Finishes | In-situ plaster/screeds, prefabricated wall panels, suspended ceilings, timber & other floors |

**SD:** Heavy stone façade, thick screed, raised floor, saturated green-roof soil — lock build-ups with RSE / landscape before freezing FFL–FFL and transfer depth.

#### 2.4 Columbarium niches (§2.2.5)

| Niche type | Minimum dead load |
|---|---|
| Lightweight (wood / lightweight metal) | ≥ **2.0 kN per m length per m height** |
| Heavy (e.g. concrete) | ≥ **4.5 kN per m length per m height** |

Plus urn weight. Niche walls are structural loads, not décor. Non-niche circulation areas still take Class 3C IL (**4.0 kPa**).

---

### 3. Floor-use classification — lock the brief (§3.1.9, Table 3.1)

| Class | Use | Typical SD trigger |
|---|---|---|
| **1** | Domestic / residential activities | Flats, hotel bedrooms, hospital / elderly wards |
| **2** | Offices & non-industrial workplaces | Offices, labs, clinics, banking halls, commercial kitchens |
| **3** | People may congregate | Schools, F&B, assembly, footbridges, refuge, stages |
| **4** | Shopping | Department stores, markets, shops |
| **5** | Storage / equipment / plant / industrial | Stack rooms, warehouses, workshops, UPS, refuse |
| **6** | Vehicular traffic | Carparks, ramps, L/UL, EVA onto structure |
| **7** | Roofs | Accessible vs inaccessible; canopies |
| **8** | Affiliated building elements | Balconies, UPs, stairs, corridors, AC hoods |

**SD workflow:**

```
Draw floor-use class map on every GA
  → Class 1–5 rooms (incl. refuge, F&B, plant, UPS)
  → Class 6 vehicle envelope + max vehicle + fire path
  → Class 7 roof access / amenity / greenery
  → Class 8 balcony / UP / stair / AC typology
  → Barrier category on every edge (§3.8)
```

---

### 4. Class 1–5 minimum imposed loads (§3.2, Table 3.2)

Concentrated `Qk` for Class 1–5: applied on plan over any square with **50 mm** side.

#### 4.1 Class 1 — Domestic / residential

| Examples of specific use | qk (kPa) | Qk (kN) |
|---|---|---|
| Domestic uses | **2.0** | **2.0** |
| Dormitories | **2.0** | **2.0** |
| Private sitting rooms, bedrooms, toilets in hotels / motels / guesthouses | **2.0** | **2.0** |
| Wards, bedrooms, toilets in hospitals / nursing homes / elderly residential care | **2.0** | **2.0** |
| Bathrooms | **2.0** | **2.0** |
| Pantries | **2.0** | **2.0** |
| Kitchens (domestic) | **2.0** | **2.0** |

**Jacuzzi / spa in bathrooms:** assess **separately** and individually (water + tub + structure — not absorbed in 2.0).

**SD:** Hotel guestroom = 2.0; hotel **public** F&B / ballroom / lobby jump to Class 3. Domestic kitchen ≠ commercial kitchen (Class 2 = **4.0**).

#### 4.2 Class 2 — Offices & other non-industrial workplaces

| Examples of specific use | qk | Qk |
|---|---|---|
| Medical consulting or treatment rooms | **2.5** | **3.0** |
| Hospital operating theatres and X-ray rooms | **2.5** | **3.0** |
| Laboratories | **3.0** | **4.5** |
| Light workrooms (no central power-driven machines; no storage) | **3.0** | **4.5** |
| Offices for general use | **3.0** | **4.5** |
| Rooms for lightweight electrical & electronic installations | **3.0** | **4.5** |
| Meter rooms **not** for storage | **3.0** | **4.5** |
| Pantries | **3.0** | **4.5** |
| Banking halls | **4.0** | **4.5** |
| Kitchens and laundries **not** in domestic buildings | **4.0** | **4.5** |
| Projection rooms | **5.0** | **4.5** |

**SD misclassification traps:**
- “Office for storage / normal filing” → Class 5 at **5.0**, not Class 2 at 3.0.
- Open-plan Grade A: **3.0 + ≥1.0 partition** (§3.6) unless walls drawn as permanent.
- Banking hall / commercial kitchen / laundry = **4.0** from concept.
- Projection / AV rooms = **5.0**.

#### 4.3 Class 3 — Floors where people may congregate

Sub-class by furniture / activity pattern — do not collapse all “public” into one number.

##### 3A — Floors with tables

| Use | qk | Qk |
|---|---|---|
| Childcare centres and kindergartens | **2.5** | **3.0** |
| Classrooms, lecture rooms, tutorial rooms, computer rooms | **3.0** | **4.5** |
| Internet computer services centres | **3.0** | **4.5** |
| Leisure / recreational / amusement areas **not** usable for assembly (e.g. private clubs with cubicles, restricted patrons) | **3.0** | **4.5** |
| Massage, sauna, bath houses | **3.0** | **4.5** |
| Reading rooms **without** book storage | **3.0** | **4.5** |
| Cafés, mahjong parlours, amusement games centres | **4.0** | **4.5** |
| Restaurants, night-clubs, lounges, bars, canteens, fast food, dining rooms **not** in domestic premises | **4.0** | **4.5** |

Water pools and fountains in bath houses → assess **separately**.

##### 3B — Floors with fixed seating

Seating is “fixed” if removal and re-use of the space for other purposes are **unlikely**.

| Use | qk | Qk |
|---|---|---|
| Assembly areas with fixed seating | **4.0** | **4.5** |
| Chapels, churches, places of worship with fixed seating | **4.0** | **4.5** |
| Concert halls | **5.0** | **4.5** |
| Conference rooms, waiting rooms | **5.0** | **4.5** |
| Grandstands | **5.0** | **4.5** |
| Public halls, theatres, cinemas | **5.0** | **4.5** |

Grandstands also need §3.8.2 crowd horizontal loads.

##### 3C — Floors without obstacles for moving people

| Use | qk | Qk |
|---|---|---|
| Columbaria (areas other than niches) | **4.0** | **4.5** |
| Art galleries and museums | **5.0** | **4.5** |
| Assembly areas **without** fixed seating | **5.0** | **4.5** |
| **Refuge floors** | **5.0** | **4.5** |
| Footbridges between buildings; footpaths; terraces; plazas; pedestrian traffic areas | **5.0** | **4.5** |
| Open areas in gardens (incl. short grass turf suitable for foot traffic) | **5.0** | **4.5** |

##### 3D — Floors with possible physical activities

| Use | qk | Qk |
|---|---|---|
| Billiard rooms and bowling alleys | **3.0** | **4.5** |
| Dance practice rooms | **3.0** | **4.5** |
| Dance halls, karaoke establishments, discotheques, gymnasia | **5.0** | **4.5** |
| Ice rinks, ball courts, golf driving ranges | **5.0** | **4.5** |
| Stages; television studios used as stages | **7.5** | **9.0** |

Ice weight → assess **separately**. Stages / TV stages = **7.5 / 9.0** — never hide a performance platform inside “multi-purpose” without telling RSE.

**SD takeaways (Class 3):**
- **Refuge floor = 5.0 kPa**, not empty plant.
- Podium F&B / bar / disco / cinema / plaza edges = **4.0–5.0**, not domestic 2.0.
- Fixed vs unfixed seating changes assembly from 4.0 → 5.0 and barrier category.
- Footbridges and garden turf decks = **5.0** pedestrian IL + barrier rules.

#### 4.4 Class 4 — Shopping

| Use | qk | Qk |
|---|---|---|
| Department stores, supermarkets, markets, shops for display and sale of merchandise | **5.0** | **4.5** |

**Note 1 (Code):** Stacking / storage areas → Class 5 examples, not Class 4 sales floor.

**SD:** Retail floor 5.0; stockroom / warehouse behind → height-driven Class 5 (often much heavier).

#### 4.5 Class 5 — Storage, equipment, plant, industrial

**Storage height** = height of space between floor and physical constraint (ceiling, soffit, roof, or other obstruction).

| Use | qk | Qk |
|---|---|---|
| Library rooms with book storage (**excluding** stack rooms) | **5.0** | **4.5** |
| Offices for storage and normal filing | **5.0** | **4.5** |
| Refuse storage | **2.5 per m** storage height | By material weight, **≥ 9.0** |
| Stack rooms in book stores and libraries | **3.5 per m**, but **≥ 10.0** | By material, **≥ 9.0** |
| Cold storage | **5.0 per m**, but **≥ 15.0** | By material, **≥ 9.0** |
| Paper storage in printing plants | **8.0 per m** | By material, **≥ 9.0** |
| Battery rooms and UPS rooms | **10.0 per m** | By material, **≥ 9.0** |
| General storage / warehouses (other than listed) | **2.5 per m** | By material, **≥ 9.0** |
| Plant rooms, boiler rooms, fan rooms, motor rooms and the like | **7.5** | **9.0** |
| Workshops / factories — light weight loads | **5.0** | **9.0** |
| Workshops / factories — medium weight loads | **7.5** | **9.0** |
| Workshops / factories — heavy weight loads | **10.0** | **9.0** |
| Printing plants | **12.5** | **9.0** |

**Worked height examples (architect briefing):**

| Room | Clear storage height | Min qk |
|---|---|---|
| UPS room, 3.0 m to soffit | 3.0 m | **30.0 kPa** |
| Cold store, 4.0 m | 4.0 m | **20.0** (rule) but floor **≥ 15.0** anyway → **20.0** |
| Library stack, 2.5 m | 2.5 m | 3.5×2.5 = 8.75 → raise to **≥ 10.0** |
| General warehouse, 6.0 m | 6.0 m | **15.0** |

**SD:** Locate UPS, cold store, stacks, refuse, heavy plant over ground / transfer / dedicated structure. Industrial ≥ **7.5 kPa** changes column reduction (§3.7.3.2) and triggers load notices (§3.11). No §3.7 reduction for storage floors.

---

### 5. Class 6 — Vehicular traffic and parking (§3.3)

#### 5.1 Classify by heaviest vehicle that can access the area (Table 3.3)

Aligned with Road Traffic (Construction and Maintenance of Vehicles) Regulations (Cap. 374A).

| Class | Accessible to vehicles not exceeding | Example vehicles |
|---|---|---|
| **6A** | **3,000 kg** GVW | Private cars, taxis, van-type LGV, motorcycles |
| **6B** | **5,500 kg** | Light goods vehicles; light buses (≤16 passengers) |
| **6C** | **24,000 kg** | Medium goods; single-/double-deck buses; coaches |
| **6D** | **30,000 kg** | Fire engines; refuse collection vehicles; rigid HGV |
| **6E** | Other than 6A–6D | Articulated heavy goods → HyD **SDM** highway loading |

| Area type | Classification rule |
|---|---|
| Loading / unloading areas | 6B / 6C / 6D by vehicle use |
| Driveways **leading to** L/UL | Same class as the L/UL they serve |
| Fire-engine accessible areas | Class by vehicle **plus** patch checks below |

#### 5.2 Fire-engine patch loads (§3.3.3) — in addition to class loads

| Patch | Load | Contact area |
|---|---|---|
| Wheel / axle check 1 | **230 kN** | **950 mm × 750 mm** |
| Wheel / axle check 2 | **100 kN** | **300 mm × 300 mm** |

**SD:** EVA / fire appliance onto podium, transfer, or basement roof → decide path before setting structural depth. “Carpark only” plates that admit fire engines become 6D + patches.

#### 5.3 Class 6A loads (Table 3.4)

| qk | Qk | Contact |
|---|---|---|
| **3.0 kPa** | **20.0 kN** | Any **200 mm** square |

**Double-deck parking:** `qk` = **twice** Table 3.4 → **6.0 kPa**.

#### 5.4 Class 6B / 6C / 6D loads (Tables 3.5–3.6)

| Class | qk | Qk | Contact |
|---|---|---|---|
| **6B** | Table 3.6 by loaded length L | **30 kN** | **200 mm** square |
| **6C** | Table 3.6 | **60 kN** | **300 mm** square |
| **6D** | Table 3.6 | **80 kN** | **300 mm** square |

Minimum IL may alternatively follow recognised engineering principles (Code note).

**Full Table 3.6 — minimum UDL qk (kPa) vs loaded length L:**

| L (m) | 6B | 6C | 6D |
|---|---|---|---|
| 0 to 5 | **13.9** | **34.7** | **46.6** |
| 6 | 11.4 | 29.9 | 39.4 |
| 7 | 9.7 | 26.6 | 34.4 |
| 8 | 8.6 | 24.0 | 30.6 |
| 9 | 7.7 | 22.0 | 27.8 |
| 10 | 7.0 | 20.5 | 25.5 |
| 12 | 6.0 | 17.9 | 21.9 |
| 14 | 5.3 | 16.0 | 19.4 |
| 16 | 4.8 | 14.6 | 17.6 |
| 18 | 4.4 | 13.5 | 16.2 |
| 20 | 4.1 | 12.6 | 15.1 |
| 25 | 3.6 | 11.0 | 13.1 |
| 30 | **3.2** | 9.9 | 11.8 |
| 35 | 3.2 | 9.1 | 10.9 |
| 40 | 3.2 | 8.5 | 10.2 |
| 45 | 3.2 | 8.0 | 9.6 |
| 50 or above | 3.2 | **7.6** | **9.2** |

Intermediate L: linear interpolation or Appendix C curves.

#### 5.5 How to measure loaded length L (§3.3.6.2, App. B) — architect must understand

| Rule | Detail |
|---|---|
| Default | L = **shorter side** of the loaded area; also = full base length of the **adverse area** |
| Continuous construction | If multiple adverse areas, take adverse area or combination using load for full base length **or sum** of selected adverse base lengths — worst effect |
| Exception | Direction of traffic **will not change** for life of structure due to physical constraint (e.g. access ramp, except reverse flow) → measure L **along traffic** |

Appendix B shows L = shorter of L1/L2 for: slab mid-span & support moments; cantilever slab; secondary & main beam mid-span/support/shear; cantilever beam; column axial load.

**SD:** Short-span carpark slabs (L ≤ 5 m) see the **highest** UDL (13.9 / 34.7 / 46.6). Tight grids under trucks are punishing — discuss span vs class with RSE at concept.

#### 5.6 Appendix C loading-curve formulas (for RSE; AP awareness)

| Class | Formula bands |
|---|---|
| **6B** | 0–5 m: **13.9**; 5–30 m: `exp(5.158 L^-0.413) − 0.335`; &gt;30 m: **3.2** |
| **6C** | 0–5 m: **34.7**; 5–10 m: `exp(5.200 L^-0.241) + 0.675`; 10–50 m: `exp(5.450 L^-0.259) + 0.346`; &gt;50 m: **7.6** |
| **6D** | 0–5 m: **46.6**; 5–10 m: `exp(5.660 L^-0.237) − 1.099`; 10–50 m: `exp(6.279 L^-0.300) + 2.200`; &gt;50 m: **9.2** |

#### 5.7 Class 6E — articulated / beyond 6D (§3.3.7)

Use latest HyD **SDM** HA or HB loading by intended use. If **not** designed for HB, modified HA is acceptable:

| Modification | Requirement |
|---|---|
| Lane width for UDL intensity | Notional lane width **3 m** (transform SDM Fig. 3 / Table 17 intensity to UDL) |
| Knife-edge load | **40 kN/m**, perpendicular to loaded length |
| UDL + knife-edge | Act **together** at position of most adverse effect |
| Notional lanes | Fully load all lanes causing most adverse effect |
| Single wheel | **100 kN** on **300 mm** square, worst position; assessed **separately** from UDL + knife-edge |
| Secondary vehicle loads | Centrifugal, traction, braking, skidding — **need not** be considered for **car parking structures** |

#### 5.8 Vehicle SD decision tree

```
What is the heaviest vehicle that can physically reach this plate?
  → Cap access (clearance, barriers, signage) to match class
  → Private cars only → 6A (3.0 / 20; ×2 if stackers)
  → LGV / light bus → 6B (Table 3.6 + 30 kN)
  → Bus / MGV → 6C
  → Fire engine / RCV / rigid HGV → 6D + fire patches if fire access
  → Articulated HGV → 6E / SDM

Split grades where possible:
  Car-only basement ≠ truck L/UL driveway (do not paint whole podium 6C/6D)
```

---

### 6. Class 7 — Roofs and canopies (§3.4)

#### 6.1 Roof sub-classes (Table 3.7)

| Class | Meaning |
|---|---|
| **7A** | Inaccessible roofs / flat roofs — access only as necessary for **maintenance** |
| **7B** | Accessible roofs (access beyond maintenance) **or** for Class 1–6 use |
| **7C** | Accessible flat roofs or Class 1–6 use — uses **not** specified in B(C)R |
| **7D** | Canopies |

`Qk` on roofs: **50 mm** square (§3.4.3).

#### 6.2 Minimum loads (Table 3.8)

##### 7A — Inaccessible

| Roof slope | qk (kPa) | Qk (kN) |
|---|---|---|
| ≤ **5°** | **2.0** | **1.5** |
| &gt; 5° to ≤ **20°** | **0.75** | **1.5** |
| &gt; 20° to &lt; **40°** | Linear interpolate **0.75 → 0** | **1.5** |
| ≥ **40°** | **0** | **1.5** |

##### 7B — Accessible / Class 1–6 use

| Roof slope | qk | Qk |
|---|---|---|
| ≤ **20°** | Table 3.2 / 3.4 / 3.5 by use, but **≥ 2.0 kPa** and **≥ 1.5 kN** | as use / min |
| &gt; 20° to &lt; **40°** | Interpolate **2.0 → 0** | **1.5** |
| ≥ **40°** | **0** | **1.5** |

##### 7C — Accessible flat / unspecified B(C)R uses

Same as Table 3.2 / 3.4 / 3.5 by use, floors **≥ 2.0 kPa** and **≥ 1.5 kN**.

##### 7D — Canopies

| Type | qk | Qk | Note |
|---|---|---|---|
| Lightweight (glass, metal sheet, etc.) | **0.75** | **1.5** | Does **not** include uncontrolled construction debris during maintenance |
| Concrete canopy | **2.0** | — | **Does** include accumulations of materials / debris during maintenance |

#### 6.3 Ceiling / truss elements supporting people (§3.4.4)

Bottom chords of roof trusses, ceiling joists/hangers, skylight ribs, frames/coverings of ceiling access hatches and similar — if they must support people: design for **1.5 kN** concentrated at worst position, **together with** Table 3.8 loads.

#### 6.4 Roof SD decision tree

```
Roof garden / amenity / F&B / sports / parking on roof?
  → Accessible → 7B/7C → use Class 1–6 loads (≥2.0/1.5)
  → Plus greenery soil etc. as DEAD (§2.2.3)

Maintenance-only pitched metal roof?
  → 7A by slope (often 0.75 or less)

Glass / metal entrance canopy (not working platform)?
  → 7D lightweight 0.75/1.5

Concrete canopy used as maintenance deck?
  → 7D concrete 2.0 (debris included)
```

---

### 7. Class 8 — Affiliated building elements (§3.5, Table 3.9)

`Qk` on **50 mm** square unless otherwise stated.

| Element | qk (kPa) | Line / concentrated |
|---|---|---|
| Projecting window hoods; AC hoods (lower & upper slabs); AC platforms | — | **1.5 kN/m** along **outer edge** |
| Utility platforms | Same as floors they serve, **≥ 4.0** | **2.0 kN/m** outer edge |
| Balconies | Same as floors they serve, **≥ 3.0** | **2.0 kN/m** outer edge |
| Stairs, landings, corridors | Same as floors they serve, **≥ 3.0 and ≤ 5.0** | **4.5 kN** |
| Maintenance catwalks | — | **1.0 kN** at **1 m** centres |

**Corridor / stair capping logic:** follow served floor, but never below **3.0** and never above **5.0**. Example: domestic flat 2.0 → corridor/stair **3.0**; shopping 5.0 → corridor **5.0**; plant 7.5 → corridor still capped at **5.0** for Class 8 element (plant room itself remains 7.5).

**SD:**
- Flat interior 2.0 ≠ balcony **≥3.0** ≠ UP **≥4.0**.
- Outer-edge line loads govern cantilever rebar, slab thickness, and curtain-wall / railing interface — brief façade at SD.
- AC hoods: **1.5 kN/m** edge even if “only” for outdoor units.

---

### 8. Partitions not indicated on building plans (§3.6)

Where building must support partitions but positions are **not** on BD approval plans, treat weight as **imposed UDL** on plan, **in addition to** other IL:

| Rule | Value |
|---|---|
| (a) Geometry-based | ≥ **1/3** of weight per metre length of partitions, uniformly distributed per m² |
| (b) Office floor floor | Also **≥ 1.0 kPa** |

These partition IL **do not qualify** for §3.7 reduction.

**SD worked case — Grade A open office:**
- General office IL **3.0** + partition allowance **≥1.0** → brief RSE **≥4.0** total UDL before fit-out concentration, unless partitions are drawn as permanent DL.

---

### 9. Reduction of distributed imposed loads (§3.7)

#### 9.1 Loads that never qualify for reduction (§3.7.1)

| Excluded load type |
|---|
| Floor loads from plant / machinery specifically allowed for |
| Factory / workshop floor loads **&lt; 7.5 kPa** (see also §3.7.3.2) |
| Floor loads from **vehicles** |
| Floor loads from storage and filing in offices |
| Forces from **dynamic** effects |
| Floor loads from **storage** |
| Floor loads from partitions **not** indicated on plan |
| Loads treated as imposed due to permanency doubt (§2.1.3) |

#### 9.2 Beams (Table 3.10) — beam design only

Reduced beam loads **must not** be used for design of vertical members supporting those beams.

| Floor area supported by single span of beam (m²) | % reduction of total distributed IL |
|---|---|
| Less than **45** | **0** (no interpolation below 45) |
| 45 | 5 |
| 90 | 10 |
| 135 | 15 |
| **180** | **20 maximum** |

Intermediate areas ≥45 m²: linear interpolation.

#### 9.3 Vertical members — general (Table 3.11)

Applies to every floor (including roof) with loads qualifying for reduction, carried by the member.

| No. of floors (incl. roof) with reducible IL | % reduction on **all** those floors |
|---|---|
| 1 | 0 |
| 2 | 5 |
| 3 | 10 |
| 4 | 15 |
| 5 | 20 |
| 6 | 25 |
| 7 | 30 |
| 8 | 35 |
| Over 8 | **40 maximum** |

#### 9.4 Workshops / factories ≥ 7.5 kPa on every floor (Table 3.12)

| No. of floors (incl. roof) | % reduction | Floor |
|---|---|---|
| 1 | 0 | Reduced IL per floor **never &lt; 7.5 kPa** |
| 2 | 10 | |
| 3 | 20 | |
| Over 3 | **25 maximum** | |

**SD:** Tall residential / office towers get column relief; podiums full of Class 5/6, storage, vehicles, and unindicated partitions **do not**. Do not sell “efficient structure” against a heavy podium use map.

---

### 10. Horizontal imposed loads on protective barriers (§3.8)

#### 10.1 Person barriers — partitions, glass walls, CW, lightweight structures, barriers (§3.8.1)

Design for Table 3.13 loads **when separately applied**, or wind (where applicable), **whichever is more adverse**.

| Category | Line load (kN/m) | Infill UDL (kPa) | Infill concentrated (kN) |
|---|---|---|---|
| Areas where congregation of people is **not** expected | **0.75** | **1.0** | **0.5** |
| People may congregate but overcrowding **not** expected | **1.5** | **1.5** | **1.5** |
| Areas **susceptible to overcrowding** | **3.0** | **1.5** | **1.5** |

**Line load application height:** **1.1 m** above floor level **or** top edge of protective barrier, **whichever is lower**.

| Category | Code examples |
|---|---|
| Congregation not expected | Internal domestic areas; offices; stairs; landings |
| Congregate, not overcrowding | Areas with fixed seating or tables; balconies; utility platforms; edges of roofs; footbridges or footpaths **≤ 3 m** wide |
| Susceptible to overcrowding | Theatres; cinemas; discotheques; bars; shopping areas; assembly areas; footbridges or footpaths **&gt; 3 m** wide |

**SD:**
- Podium mall void, wide landscaped deck, shopping edge → **3.0 kN/m**, not domestic 0.75.
- Footpath / bridge width **crosses 3 m** → barrier category jumps 1.5 → 3.0.
- Glass balustrade / CW at atrium = structural + human-load from SD (coordinate Glass Code).
- Barrier vs wind: take the worse — harbourfront CW may be wind-governed; crowded mall void often barrier-governed.

#### 10.2 Grandstands / stadiums / reviewing stands (§3.8.2)

In addition to vertical IL:

| Platform type | Horizontal load |
|---|---|
| With seats | Separate cases (not simultaneous), at floor level at each row: **0.35 kN/m** of seating along seats **or** **0.15 kN/m** perpendicular to seats |
| Without seats | **0.25 kPa** of plan area in **any** direction |

#### 10.3 Vehicle barriers — impact force (§3.8.3)

$$F = \frac{0.5\,M\,v^{2}}{\delta_{c} + \delta_{b}} \quad (\mathrm{kN})$$

| Class | M (kg) | v (m/s) | Design bumper height above floor (mm) |
|---|---|---|---|
| **6A** | 3,000 | **3.0** | **600** |
| **6B** | 5,500 | **2.5** | **800** |
| **6C** | 24,000 | **1.5** | **1,200** |
| **6D** | 30,000 | **1.5** | **1,200** |
| **6E** | Per Cap. 374A | **1.5** | **1,200** |

| Parameter | Rule |
|---|---|
| `δc` | **100 mm** unless better evidence |
| `δb` | Actual deflection for flexible barriers; **0** for rigid |
| Application | F normal to barrier, uniform over any **1.5 m** length, at bumper height |
| Alongside access ramp (oblique) | Use **½ F**; still normal to barrier over 1.5 m at bumper height |

**Ramp-end amplification (Table 3.15):** barriers at **lower end** of straight ramp:

| Ramp length | Factor γ on F |
|---|---|
| &lt; **10 m** | **1.0** |
| 10–20 m | Linear interpolate **1.0 → 2.0** |
| &gt; **20 m** | **2.0** |

**Indicative F (architect awareness, rigid barrier δb = 0, δc = 100):**

| Class | Approx. F (kN) before γ |
|---|---|---|
| 6A | 0.5×3000×3² / 100 = **135** |
| 6B | 0.5×5500×2.5² / 100 ≈ **172** |
| 6C | 0.5×24000×1.5² / 100 = **270** |
| 6D | 0.5×30000×1.5² / 100 = **338** |

Long straight ramp (&gt;20 m) can **double** these. Soft / flexible barriers reduce F via larger `δb` but need proven deflection.

**SD:** Carpark perimeter, ramp ends, and landscaped decks over parking need barrier strategy + bumper-height clearance from façade, planters, and glazing. Do not place fragile CW on the impact line at 600–1200 mm AFFL.

---

### 11. Surcharges and earth retaining (§3.9)

#### 11.1 Minimum surcharges (Table 3.17)

| Category | Surcharge (kPa) |
|---|---|
| Public roads (highways and roads) | **20** |
| Private roads | **10** |
| Footpaths isolated from roads; cycle tracks; play areas | **5** |

#### 11.2 Adjacent buildings with shallow foundations (§3.9.2)

| Situation | Rule |
|---|---|
| Actual loads derivable from records | Use **actual** surcharge |
| No records | Assess from existing uses & structural forms, minimum **10 kPa per storey** |

Other surcharges beyond Table 3.17 where applicable. Lateral earth loads / landslide debris impact → soil mechanics; reference GEO **Geoguide 1**.

**SD:** Basement / site formation next to public road → **20 kPa** surcharge from day one. Next to undocumented multi-storey neighbour → **10 kPa × storeys**.

---

### 12. Dynamic loads (§3.10)

Code IL already allow for **small** dynamic effects — usually enough without further check.

**Not covered:** rhythmical / synchronised crowd movement; some machinery — use specialist literature.

#### 12.1 Industrial / workshop / factory with no machinery data (§3.10.2)

| Design purpose | Additional imposed load |
|---|---|
| Slabs and beams **only** | Vertical UDL **+2.5 kPa** |
| Structural frames and foundations | Horizontal force = **10%** of that 2.5 kPa vertical, on **N** floors causing most adverse effect |

| N rule | Detail |
|---|---|
| N | Whole number **≥ 0.2 ×** total number of floors subject to dynamic effects |
| Wind | This horizontal force may be assumed **not** to act together with wind |

**Example:** 10 dynamic floors → N ≥ 2; apply 0.25 kPa horizontal equivalent (10% of 2.5) on the 2 worst floors for frame/foundation.

---

### 13. Notice as to load — industrial / warehouse (§3.11)

| Requirement | Detail |
|---|---|
| Where | Every storey of every **industrial building or warehouse** |
| Form | Permanent bilingual notice (English + Chinese), incised/embossed durable materials |
| Letter height | Legible, **≥ 15 mm** |
| Location | Each staircase **or** other conspicuous appropriate place |
| Content | Designed distributed imposed load in **kg/m²** |
| Conversion | **1 kPa → 102 kg/m²**; **exclude** dynamic-effect extras of §3.10 |
| Split floors | Different IL on parts of same floor → separate notice on each part |

**SD / OP:** Designed IL must match tenancy fit-out limits and signage. Changing industrial use upward after OP may need structural reassessment + new notices.

---

### 14. Imposed loads not prescribed — performance path (§4)

If use not in Code and no reliable data: performance-based IL subject to **BA acceptance**.

Design IL = greatest load likely in service life, determined by either:

1. **Measured loads** + probability-based analysis with **≤ 5%** probability of exceedance during service life; or  
2. Assessment of intended use from:
   - assembly of people;
   - accumulation of equipment and furnishings; and
   - storage of materials.

**SD:** Unusual venues, temporary exhibition halls with unknown exhibits, specialty medical, heavy art — open BA discussion early; do not invent a Class 2/3 number.

---

### 15. Densities for early dead-load budgets (Appendix A)

| Materials | Density (kN/m³) |
|---|---|
| Concrete — plain (NWA, ±PFA) | **23.6** |
| Concrete — reinforced / prestressed | **24.5** |
| Brickwork | **21.7** |
| Concrete blocks | **20.6** |
| Aluminium | **27.2** |
| Brass / bronze / copper | **83.3 / 87.7 / 87.7** |
| Iron (cast / wrought) | **70.7 / 75.4** |
| Lead | **111.0** |
| Steel | **77.0** |
| Zinc | **70.0** |
| Cement mortar | **23** |
| Gypsum / lime mortar | **18** |
| Lime-cement mortar | **20** |
| Granite / marble / basalt | **29 / 27 / 30** |
| Sandstone / slate | **25 / 28** |
| Timber | Supplier specs |
| Hardboard / chipboard / plywood | **11 / 8 / 6** |
| Blockboard / wood-wool | **5 / 6** |
| Glass | **26** |
| Soil | **20** |
| Acrylic sheet | **12** |
| Asphaltic concrete / mastic asphalt / hot rolled asphalt | **25 / 18 / 23** |

**SD:** 30 mm granite cladding ≈ 0.03 × 29 ≈ **0.87 kPa** + fixings; 150 mm saturated soil on green roof ≈ 0.15 × 20 ≈ **3.0 kPa** before plants/drainage — both eat into structural capacity early.

---

### 16. Cross-topic SD checklist — freeze with RSE before massing locks

| Decision | Why it matters | Typical consequence if wrong |
|---|---|---|
| Floor-by-floor **use class map** (refuge, F&B, retail, plant, UPS, stacks) | Sets 2.0 vs 5.0 vs 7.5–30+ kPa | Transfer redesign; lost headroom |
| Partitions on plan vs open-plan **+≥1 kPa** office | DL vs IL; reduction eligibility | Under-designed office slabs |
| Roof: inaccessible / amenity / F&B / greenery depth | 7A vs 7B/7C + soil DL | Ponding / overstress / retrofit props |
| Balcony vs UP vs AC hood typology | ≥3.0 / ≥4.0 + edge line loads | Cantilever failure / CW clash |
| Stairs / corridors vs served use (3.0–5.0 cap) | Class 8 vs room IL | Corridor under-design in domestic; over-design myths in plant |
| Carpark: max vehicle + fire path + L/UL route | 6A vs 6C/6D + 230 kN patches | Demolish/rebuild slabs |
| Double-deck stackers | 6A qk ×2 = **6.0** | Missed in carpark brief |
| Barrier category every edge (esp. decks &gt;3 m) | 0.75 / 1.5 / **3.0** kN/m | Non-compliant glass / railings |
| Ramp length to end barrier | γ up to **2.0** on impact F | Inadequate vehicle barrier |
| Adjacent roads / buildings surcharge | 5 / 10 / 20 kPa; 10/storey | Basement wall under-design |
| Industrial ≥7.5 + dynamics + notices | Table 3.12; +2.5; kg/m² signs | OP / tenancy compliance gap |
| Unlisted specialty use | §4 + BA | Late rejection of GBP loads |

---

### 17. Quick reference — common SD load picks

| Situation | Start with |
|---|---|
| Residential flat | **2.0 / 2.0**; balcony ≥**3.0** + 2.0 kN/m edge; UP ≥**4.0** + 2.0 kN/m |
| General office (walls not on plan) | **3.0 + ≥1.0 partition** |
| Banking / commercial kitchen | **4.0** |
| Shopping / plaza / refuge / footbridge | **5.0** |
| Restaurant / bar | **4.0**; overcrowding barrier **3.0 kN/m** |
| Stage | **7.5 / 9.0** |
| Plant room | **7.5 / 9.0** |
| UPS (per m height) | **10.0 × height** |
| Private-car basement | **6A: 3.0 / 20**; stacker **6.0** |
| Fire appliance on podium | **6D + 230 kN & 100 kN patches** |
| Maintenance-only flat roof ≤5° | **7A: 2.0 / 1.5** |
| Roof garden | Accessible use IL (≥2.0) **+** greenery DL |
| Lightweight metal canopy | **7D: 0.75 / 1.5** |
| Domestic stair/corridor | **3.0 / 4.5** (Class 8 floor) |

---

*Source: Code of Practice for Dead and Imposed Loads 2011 (2021 Edition), Buildings Department. This summary is for schematic-design briefing only — verify critical values against the current BD PDF and Building (Construction) Regulation before submission.*

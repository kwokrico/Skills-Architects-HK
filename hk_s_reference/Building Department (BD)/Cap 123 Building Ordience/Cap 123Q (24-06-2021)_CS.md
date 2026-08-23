# Cap 123Q — Building (Construction) Regulation
**Architect critical summary for schematic design**  
Consolidated version: 24 June 2021 | Cap. 123 sub. leg. Q | In force 1 February 2021 (L.N. 5 of 2020)

> Scope note: Cap 123Q is the **operative construction-performance rulebook** for buildings, streets, building works and street works. It replaced repealed Cap **123B**. It is **performance-based** — many hard numbers live in BD Codes of Practice accepted under **PNAP APP-53** (Loading Code, Wind Code, Concrete/Steel/Foundations CoPs, FS Code, External Maintenance CoP, etc.). Cap 123Q is **not** Cap 123A (plan/consent admin), **not** Cap 123C (demolition site safety), **not** Cap 123F (PR/SC/planning), and **not** Cap 618 (lift equipment). Use this before schematic design to lock occupancy load classes, partition strategy, envelope combustibility & CW fixing, external M&R access, >600 mm barriers, geotech / Mid-Levels dig limits, and lift-shaft building fabric.

---

## Regulatory Overview

Cap 123Q applies to the **materials, loads, structural design methodology, geotechnics, foundations, site formation, external enclosure, moisture control, fire-resisting construction principles, protective barriers, lift/escalator building interface, and miscellaneous works** (ground treatment, wells, chimneys/flues, fireplaces, vermin, person-entry ducts) of building works and street works under the Buildings Ordinance. It covers **all building and street works** within Cap 123 — every occupancy and construction type that needs BD approval — and sets Schedule Tables 1–3 as the statutory floor for imposed loads, multi-storey load reduction, and horizontal barrier loads.

---

## Critical main topics and subtopics

### 1. Key definitions that change the brief (s. 2 + linked sections)

| Term | Meaning | SD implication |
|---|---|---|
| **Carriageway** | Part of a private street, cul-de-sac or access road used / intended for **vehicular** traffic | Triggers Class 6 vehicle loads + vehicle-barrier formula (s. 9(3)) on internal roads / ramps |
| **Foundation** | Part of building / street / works that is **in direct contact with the ground** **and** transmits load to the ground | Footings, piles, rafts, and street-works foundations all in scope — not only “building piles” |
| **Dead load** | See s. 4 — permanent nature | Finishes + permanent partitions count as dead, not imposed |
| **Imposed load** | See s. 5 — everything except dead & wind, **including forces from adjacent ground** | Lateral earth on basement walls is an imposed-load design issue |
| **Wind load** | See s. 6 — pressure **or suction**, any direction | Suction uplift on canopies / roofs is statutory |
| **Site investigation** | Physical characteristics of the site — includes **documentary studies, site surveys and ground investigation** | Desk study + survey alone are part of SI; GI is not the whole duty |
| **Inaccessible roof / area** (s. 36(2)) | Not for human occupation; access **only** for maintenance / repair personnel | Barrier Division exempt; Class 7 inaccessible-roof loads apply if roof qualifies |
| **Cladding** (s. 26) | Facing / architectural decoration **additional** to structural elements | Stone / GRC / metal rain-screen = cladding Part 8 rules |
| **Curtain wall** (s. 26) | Non-load-bearing enclosure **fixed onto** a load-bearing structure | Unitised / stick CW — not a load-bearing wall |
| **Non-combustible materials** (s. 26) | Pass a **recognized non-combustibility test** | Spec path must cite a recognised test (APP-53 materials) |
| **Load-bearing** (for Part 8) | Bears load **other than** self-weight or wind on its own surface | A wall that only carries itself + wind is **not** “load-bearing” for CW support purposes — CW must fix to true structure |
| **Minor retaining wall** (s. 22) | Δh ≤ **1.5 m** + upper ground ≤ **15°** + **no** foundation/structure surcharge | Only then s. 24 drainage extras drop out |
| **Bulk excavation** (s. 25) | Any excavation **except** GI, utility trenches, drains, sewers, pile installation | Basement box / open cut / caisson wall dig = bulk dig in Scheduled Area 1 |
| **Restricted space** (s. 39) | Lift: shaft + space for associated equipment/machinery; Escalator: associated equipment/machinery space | Must be inaccessible except inspection / maintenance / repair / rescue |
| **Storage height** (Sch. Note 2) | Floor to ceiling / soffit / roof / other physical obstruction limiting stack height | Clear storey height on GPs **sets** storage kPa |

---

### 2. Materials — performance + testing duty (Part 2, s. 3)

| Statutory duty | What it means at SD |
|---|---|
| (a) Nature & quality suitable for intended use / purpose | Match material to exposure (marine, wet room, fire, structural) — no “provisional TBD cladding” without a compliance path |
| (b) Adequately mixed or prepared | Concrete / mortar / adhesives — site QA is a Cap 123Q duty |
| (c) Applied, used or fixed to perform intended functions | Fixing sequence, substrate, and workmanship are compliance — especially cladding dowels & CW anchors |
| Adequately tested by **recognized tests** | Product certificates / type tests must be from recognised methods (APP-53 list is the practical route) |

**SD takeaway:** Exotic or non-listed materials need **BD agreement in principle early** (APP-53 §§2–3 alternative-path logic) — do not leave to DD.

---

### 3. Load definitions architects must brief correctly (Part 3, ss. 4–6)

| Load | Statutory content | Hard rule |
|---|---|---|
| **Dead** (s. 4) | Permanent nature; total weight of walls, floors, roofs, finishes, **permanent partitions**, other permanent constructions | Use reliable unit weights — include finishes & fixed partitions in early weight assumptions |
| **Imposed** (s. 5) | Load other than dead or wind; greatest applied load likely from intended use / purpose (**including forces exerted by adjacent ground**) | Table 1 is the floor; real use / plant / display can be **higher** (s. 7(3)) |
| **Wind** (s. 6) | Effects of wind pressure **or suction**; based on building response to winds from **any** direction | Wind magnitude return period **≥ 50 years**; use Wind Effects CoP via APP-53 |

---

### 4. How imposed loads are applied (s. 7) — not just “pick a kPa”

#### 4.1 Greater-adverse-effect rule (s. 7(1))
For any building / street / works, minimum imposed load = whichever produces the **greater adverse effect**:
- **Distributed** load from Table 1 Col. 3, applied uniformly on plan; **or**
- **Concentrated** load from Col. 4 on any square with a **50 mm** side (or other dimension stated in Col. 4); **or**
- **Line load** from Col. 4 where specified

#### 4.2 Floating partitions — positions not on plan (s. 7(2))
If floor will support partitions but positions are **not** indicated on the plan:
- Treat partition weight as **additional** uniformly distributed imposed load; **and**
- That load must be **≥ 1/3** of the weight per metre length of the partitions, uniformly distributed per m²; **and**
- If the floor is for **office** purposes → **not less than 1 kPa**

**SD choice:** Fix partition layouts on GP (and treat as dead if permanent) **or** budget ≥1 kPa office floating-partition surcharge + structural capacity for fit-out churn. Floating partition loads **cannot** be reduced under s. 8(5)(g).

#### 4.3 Equipment / machinery / display override (s. 7(3))
If equipment, machinery or displaying items will produce an imposed load **greater than Table 1**, that actual load **must** be taken into account.  
**Also:** those floors **cannot** take multi-storey imposed-load reduction (s. 8(5)(a)).

---

### 5. Minimum imposed loads — Schedule Table 1 (complete occupancy map)

Use the **greater** of distributed (kPa) or concentrated / line (kN) effect. Default concentrated patch = **50 mm** square; vehicle Class 6 = **200 mm** square.

#### Class 1 — Domestic / residential sleep — **2 kPa / 2 kN**
| Use |
|---|
| Floors for domestic uses |
| Dormitories |
| Private sitting rooms, bedrooms and toilet rooms in hotels, motels and guesthouses |
| Wards, bedrooms and toilet rooms in hospitals, nursing homes and residential care homes for elderly persons |
| Bathrooms (Jacuzzi load assessed **separately**), pantries and kitchens in **domestic** premises |

#### Class 2 — Institutional / office / light work
| Use | Dist. kPa | Conc. kN |
|---|---|---|
| Medical consulting or treatment rooms | 2.5 | 3 |
| Hospital operating theatres and X-ray rooms | 2.5 | 3 |
| Laboratories | 3 | 4.5 |
| Light workrooms with neither central power-driven machines nor storage | 3 | 4.5 |
| Offices for **general** use | 3 | 4.5 |
| Rooms for lightweight electrical and electronic installations | 3 | 4.5 |
| Rooms for meters and **not** for storage | 3 | 4.5 |
| Pantries in offices or non-industrial workplaces | 3 | 4.5 |
| Banking halls | 4 | 4.5 |
| Kitchens and laundries **not** in domestic premises | 4 | 4.5 |
| Projection rooms | 5 | 4.5 |

#### Class 3 — Education / assembly / leisure
| Use | Dist. kPa | Conc. kN |
|---|---|---|
| Childcare centres and kindergartens | 2.5 | 3 |
| Billiard rooms and bowling alleys | 3 | 4.5 |
| Classrooms, lecture rooms, tutorial rooms, computer rooms and reading rooms **without** book storage | 3 | 4.5 |
| Internet computer services centres | 3 | 4.5 |
| Dance practice rooms | 3 | 4.5 |
| Leisure, recreational and amusement areas that **cannot** be used for assembly | 3 | 4.5 |
| Massage rooms, sauna rooms and bath houses (**water pools / fountains assessed separately**) | 3 | 4.5 |
| Assembly areas **with** fixed seating | 4 | 4.5 |
| Chapels, churches and places of worship with fixed seating | 4 | 4.5 |
| Columbaria (**other than** areas for niches) | 4 | 4.5 |
| Restaurants, nightclubs, lounges, bars, canteens, fast food shops and dining rooms **not** in domestic premises | 4 | 4.5 |
| Cafes, mahjong parlours and amusement game centres | 4 | 4.5 |
| Art galleries and museums | 5 | 4.5 |
| Grandstands | 5 | 4.5 |
| Public halls | 5 | 4.5 |
| Theatres and cinemas | 5 | 4.5 |
| Concert halls | 5 | 4.5 |
| Conference rooms and waiting rooms | 5 | 4.5 |
| Assembly areas **without** fixed seating | 5 | 4.5 |
| Dance halls and discotheques | 5 | 4.5 |
| Footbridges between buildings | 5 | 4.5 |
| Footpaths, terraces, plazas and areas used for pedestrian traffic | 5 | 4.5 |
| Open areas in gardens (including short grass turf suitable for foot traffic) | 5 | 4.5 |
| Karaoke establishments | 5 | 4.5 |
| Gymnasia | 5 | 4.5 |
| **Refuge floors** | 5 | 4.5 |
| Ice rinks (**weight of ice assessed separately**), ball courts and golf driving ranges | 5 | 4.5 |
| Stages and television studios used as stages | **7.5** | **9** |

> **Note (1) Fixed seating:** seating is “fixed” only if removal of the seating **and** use of the space for other purposes are **unlikely**. Removable banquet seating → treat as **without** fixed seating (5 kPa).

#### Class 4 — Retail — **5 kPa / 4.5 kN**
Department stores, supermarkets, markets and shops for display and sale of merchandise.

#### Class 5 — Storage / plant / industrial (storey height drives kPa)
| Use | Dist. load | Conc. |
|---|---|---|
| Library rooms with book storage (**excluding** library stack rooms) | 5 kPa | 4.5 kN |
| Offices for storage and normal filing purposes | 5 kPa | 4.5 kN |
| Stack rooms in bookstores and libraries | **3.5 kPa per m** storage height, **min 10 kPa** | By material weight, **≥ 9 kN** |
| Cold storage | **5 kPa per m**, **min 15 kPa** | ≥ 9 kN |
| Paper storage in printing plants | **8 kPa per m** | ≥ 9 kN |
| Battery rooms and UPS rooms | **10 kPa per m** | ≥ 9 kN |
| Refuse storage or general storage (other than above), including warehouses | **2.5 kPa per m** | ≥ 9 kN |
| Plant rooms, boiler rooms, fan rooms, motor rooms and the like | **7.5 kPa** | 9 kN |
| Factories / workshops / similar industrial — light weight | 5 kPa | 9 kN |
| — medium weight | 7.5 kPa | 9 kN |
| — heavy weight | 10 kPa | 9 kN |
| — printing plants | **12.5 kPa** | 9 kN |

#### Class 6 — Vehicles
| Use | Dist. | Conc. |
|---|---|---|
| Car parking, carriageways, floors, driveways, ramps — vehicles **≤ 3 000 kg** gross | 3 kPa | **20 kN** on any **200 mm** square |
| Vehicles **> 3 000 kg** gross | By recognized engineering principles | Same |

#### Class 7 — Roofs & canopies
| Roof type | Dist. kPa | Conc. kN |
|---|---|---|
| Inaccessible, slope ≤ 5° | 2 | 1.5 |
| Inaccessible, >5° to ≤20° | 0.75 | 1.5 |
| Inaccessible, >20° to <40° | Linear interpolate 0.75 → 0 | 1.5 |
| Inaccessible, ≥40° | 0 | 1.5 |
| Other roofs (not Class 1–6 uses), slope ≤20° | 2 | 1.5 |
| Other roofs, >20° to <40° | Linear interpolate 2 → 0 | 1.5 |
| Other roofs, ≥40° | 0 | 1.5 |
| Canopies | **0.75** | **1.5** |

> **Note (3):** Canopy minima **do not** include uncontrolled piles of construction materials during maintenance/repair — still design for buildability / temporary works separately.

> If a roof is used as Class 1–6 (roof garden plaza, parking deck, restaurant terrace) → use **that class**, not Class 7.

#### Class 8 — Projections & circulation
| Element | Dist. | Conc. / line |
|---|---|---|
| **Utility platforms** | Same as floors they give access to, **but not less than 4 kPa** | **Line 2 kN/m** along outer edge |
| **Balconies** | Same as floors they give access to, **but not less than 3 kPa** | **Line 2 kN/m** along outer edge |
| Stairs, landings and corridors | Same as floors they give access to, **not less than 3 and not more than 5 kPa** | 4.5 kN |
| Projecting window hoods, A/C hoods (lower & upper slabs), A/C platforms | — | **Line 1.5 kN/m** along outer edge |
| Maintenance catwalks | — | **1 kN** at **1 m** centres |

**SD takeaway:** Label every floor zone with intended use **and** Table 1 class on early plans. Classic traps: general office 3 → filing 5; domestic kitchen 2 vs F&B kitchen 4; refuge floor **5**; plant **7.5**; UP **≥4** even if flat is 2.

---

### 6. Reduction of imposed loads (s. 8 + Schedule Table 2)

#### 6.1 Column / pier / wall / foundation reduction (Table 2)
Applies to **distributed** imposed load on roof + every floor carried by the member under consideration.

| No. of floors (incl. roof) with loads qualifying for reduction | Classes 1, 2, 3, 4 & 7 | Factories / workshops Class 5(4) with distributed IL **≥ 7.5 kPa** |
|---|---|---|
| 1 | 0% | 0% |
| 2 | 5% | 10% |
| 3 | 10% | 20% |
| 4 | 15% | **25% maximum** |
| 5 | 20% | 25% max |
| 6 | 25% | 25% max |
| 7 | 30% | 25% max |
| 8 | 35% | 25% max |
| Over 8 | **40% maximum** | 25% max |

#### 6.2 Beam reduction (s. 8(2)–(3))
If a **single span** of beam supports **≥ 45 m²** of floor at any level — for designing **that beam only**:
- **5%** for each complete 45 m² supported; **and**
- **Not more than 20%** total for that floor

#### 6.3 Factory floor floor (s. 8(4))
For factories/workshops designed for distributed IL **≥ 7.5 kPa**: after Table 2 reduction, total IL must **not** fall below the value if **all** floors had been designed for **7.5 kPa without** Table 2 reduction.

#### 6.4 Never reduce (s. 8(5)) — absolute list
| (a) | Floors supporting equipment / machinery / displaying items under s. 7(3) |
| (b) | Factories / workshops designed for distributed IL **< 7.5 kPa** |
| (c) | Floors used by **vehicles** |
| (d) | Office areas used for **storage and filing** |
| (e) | Forces produced by **dynamic effects** |
| (f) | Floors used for **storage** purposes |
| (g) | Loads from partitions whose positions are **not** indicated on plan |

---

### 7. Protective barrier loads & vehicle barriers (s. 9 + Schedule Table 3)

#### 7.1 Person barriers (s. 9(1)–(2) + Table 3)
A protective barrier installed to restrict / control movement of **persons** must resist the **minimum horizontal imposed loads** in Table 3 when **separately** applied. If wind applies → take **relevant imposed load or wind**, whichever produces greater adverse effect.

| Item | Category | Line load (kN/m) | Infill UDL (kPa) | Infill concentrated (kN) |
|---|---|---|---|---|
| 1 | Areas where congregation of people is **not** expected | 0.75 | 1 | 0.5 |
| 2 | Areas where people **may** congregate but overcrowding is **not** expected | 1.5 | 1.5 | 1.5 |
| 3 | Areas **susceptible to overcrowding** | **3** | 1.5 | 1.5 |

**Line load application height (Table 3 Note):** at **1.1 m** above floor level **or** at the top edge of the barrier — **whichever is the lower**.

**SD mapping examples:**
- Private domestic balcony / corridor → often Item 1
- Office lift lobby / typical mall corridor → often Item 2
- Stadium / theatre foyer / MTR-adjacent plaza / crowded shopping atrium edge → Item 3

#### 7.2 Vehicle barriers (s. 9(3))
For carriageway, floor, driveway or ramp used by vehicles — design for greatest anticipated impact, subject to:
- Min design impact force = **[0.5 M v² / (δc + δb)] kN**  
  - *M* = gross mass (kg) of heaviest vehicle allowed  
  - *v* = velocity normal to barrier (m/s)  
  - *δc* = deformation of vehicle (mm)  
  - *δb* = deflection of barrier (mm)
- Impact force uniformly distributed over any length of **1.5 m**, acting horizontally at **bumper height**

**SD takeaway:** Lock heaviest vehicle class (private car vs LGV vs fire appliance on EVA ramps) before sizing carpark / ramp barriers.

---

### 8. Dynamic effects — industrial (s. 10)

Forces from dynamic effects are **additional** imposed loads.

| Path | Rule |
|---|---|
| Preferred | Determine from information about the specific factory / workshop / industrial building |
| Default if not so determined | **Slabs & beams:** +**2.5 kPa** vertical (for that design only) |
| | **Frames & foundations:** additional **horizontal** force = **10%** of the 2.5 kPa imposed in the slab/beam rule, acting simultaneously on a whole number of floors that produces greatest adverse effect, where that number ≥ **0.2 ×** total number of floors subject to dynamic effects |
| Wind interaction | Horizontal dynamic force **may be assumed not to act together with wind load** |

Dynamic forces themselves **must not** be reduced under s. 8 (see s. 8(5)(e)).

---

### 9. Load notices & overloading ban (ss. 11–12)

#### 9.1 Industrial buildings & warehouses — permanent load notices (s. 11)
| Rule | Detail |
|---|---|
| What | Notice stating **designed distributed imposed load** (weight per m², **excluding** dynamic effects) |
| Where | Permanently & conspicuously at **each staircase of every storey**, or another appropriate place |
| Split floors | If different parts of a floor have different design loads → notice **at each part** |
| Form | Legible; durable materials |

**SD:** Coordinate notice locations with wayfinding / staircase lobby design — not an afterthought sticker.

#### 9.2 Overloading (s. 12)
No building / street / works may be subject to a load beyond its proper bearing capacity — **except** loads required for testing.

---

### 10. Design methodology, strength, stability, construction methods (Part 4, ss. 13–16)

| Section | Statutory duty | SD implication |
|---|---|---|
| **s. 13** Design methodology | Conform to laws of mechanics + recognized engineering principles + recognized engineering practices | Structural system must be defendable under APP-53 CoPs |
| **s. 14** Strength & serviceability | Structure must safely **sustain** and **transmit to ground** combination of dead + imposed + wind; adequate FoS | Early grid / transfer / basement strategy must carry full load combo |
| | Must **not** cause cracks, deflection, deformation or other movement that adversely affects intended use / performance of the works **or** any other building, structure, land, street or services | Neighbour settlement / façade distress is a Cap 123Q design duty |
| | Must **not** cause damage to self or others; must **not** render inadequate the FoS of any other building / street / works | ELS / demolition interface / party-wall schemes need this narrative |
| **s. 15** Stability | Adequate **margin of safety against instability** | Slender towers, temporary works, progressive collapse / robustness narrative |
| **s. 16** Construction methods & procedures | Appropriate methods + precautionary measures | Buildability is statutory |
| | Not complied with if FoS / margin of safety of any building/structure/land/street/services is rendered inadequate; or damage caused; or crack / undue deformation / movement (temporary **or** permanent) exceeds **acceptable dimensional tolerance** | Temporary works (ELS, façade install, transfer props) must stay within tolerance — programme & method affect SD assumptions |

---

### 11. Site investigation (Part 5, s. 17)

| Rule | SD implication |
|---|---|
| SI of a site for building / street works must provide **adequate geotechnical and any other relevant data** for design & construction | Do not freeze basement depth / pile type / retention without SI scope |
| Must conform to **recognized standards** | GI to GEO / BD accepted standards (Foundations CoP path) |
| Includes documentary studies, site surveys **and** ground investigation (s. 2) | Historical maps, utilities, adjacent foundations, slope records count |

**Foundation construction may not start without SI compliance** (see s. 18(5)).

---

### 12. Foundations (Part 6, ss. 18–20)

#### 12.1 Foundation performance (s. 18)
Foundation must:
1. Safely sustain combination of dead + imposed + wind from the works **and any other loads** exerted on it  
2. Safely transmit those loads to the ground  
3. Take into account: **ground conditions**; **installation method**; **group effects** of the foundation system  
4. Have adequate FoS  
5. **Not** impair stability of, damage, or reduce FoS of any other building / structure / land / street / services  
6. Be preceded by SI under s. 17  
7. Rest on ground capable of safely sustaining dead + imposed + wind + other foundation loads with adequate FoS  

#### 12.2 BA on-site tests (s. 19)
If BA doubts design assumption or load-carrying capacity → may require on-site tests on foundation **or** on founding ground (test loads or other suitable method).

#### 12.3 Proof tests (s. 20)
Representative foundation units **must** be adequately tested by proof tests, by method appropriate to type:
- Imposition of test loads; **and/or**
- Core drilling of completed **cast-in-place** concrete foundation; **and/or**
- Any other suitable method

**SD takeaway:** Budget programme + cost for pile proofs / cores; aggressive founding assumptions invite s. 19 BA tests.

---

### 13. Site formation & retaining walls (Part 7, ss. 21–25)

#### 13.1 Site formation works (s. 21)
- Adequate margin of safety of the works **and the remainder of the site** during **and after** construction  
- Must not damage or reduce margin of safety of any building / structure / land / street / services  

#### 13.2 Minor retaining wall — all three must apply (s. 22)
| Criterion | Limit |
|---|---|
| Difference between upper and lower ground next to wall | **≤ 1.5 m** |
| Average inclination of ground on upper side | **≤ 15°** to horizontal |
| Surcharges from foundation or other structures | **Must not** impose loading on the wall |

Only then is it a **minor retaining wall** → s. 24 drainage extras do **not** apply. Anything taller, steeper, or surcharge-loaded = full retaining-wall package.

#### 13.3 Retaining wall design (s. 23) — all walls (including minor for design strength)
Must safely support earth/fill + other loads under **most onerous** loading during construction **and** throughout service life; recognized engineering principles; based on SI (s. 17).  

Adequate FoS against **all four**:
1. Sliding  
2. Overturning  
3. Ultimate bearing failure  
4. Failure on a surface **passing beneath** the wall  

Must not impair stability of or damage any building / structure / land / street / services.

#### 13.4 Non-minor retaining wall extras (s. 24)
| Item | Rule |
|---|---|
| Filter placed against soil | Allow water through; **restrain migration of soil particles** |
| Drainage system (if provided to reduce water pressure) | Performance maintainable throughout **service life** of the wall |
| Backfill | Material that can be compacted to form a **stable** fill |
| Upper **and** lower ground levels next to wall | Channels of suitable size **or** paving to carry seepage / surface water |
| Outfall | Channels / paving laid to adequate gradient → **surface water drain** |

#### 13.5 Mid-Levels bulk excavation — Scheduled Area No. 1 (s. 25)
| Term | Meaning |
|---|---|
| **Bulk excavation** | Any excavation **except** GI, public utility trenches, drains, sewers, pile installation |
| **Cumulative adverse effect** | Overall adverse effects on hillside stability from bulk excavation at **2 or more** sites in the area |

Bulk excavation in **area number 1 of the scheduled areas** must be limited to a level that **minimizes** the cumulative adverse effect on the hillside.

**SD takeaway:** Flag Mid-Levels / Scheduled Area 1 before assuming deep basement — BA will scrutinise cumulative hillside impact, not only your plot.

---

### 14. External wall, cladding, curtain wall (Part 8, ss. 26–31)

#### 14.1 External wall (s. 27)
| Must | Detail |
|---|---|
| Materials | **Permanent**, **impervious**, and **non-combustible** |
| Maintenance access | Adequate means of access to **outer surface** of the wall **or any projection** from it for maintenance / repair |

→ Deemed-to-satisfy path: **Code of Practice on Access for External Maintenance 2021** (ss. 27(2), 28(5), 31(3), 34(3)).

#### 14.2 Cladding (s. 28) — full checklist
| # | Requirement |
|---|---|
| 1 | Constructed of **non-combustible** materials |
| 2 | Suitable **thickness, strength and durability** |
| 3 | Fixed & supported in suitable manner **and sequence** so as to maintain long-term stability & integrity |
| 4 | Permanently provided with **sufficient flexible joints horizontally and vertically** for differential movement vs structure |
| 5 | Fixed with suitable **metal dowels and fixings** |
| 6 | Dowels/fixings permanently fixed onto **structural elements** throughout service life |
| 7 | Dowels/fixings **adequately protected against corrosion** |
| 8 | If weather-exposed → adequate access to outer surface / projections for M&R |

**SD takeaway:** No adhesive-only / non-structural substrate logic; movement-joint grid is an elevation design issue from SD; corrosion protection for marine / polluted exposure.

#### 14.3 Curtain wall — design (s. 29)
| Duty | Rule |
|---|---|
| Loads | Safely sustain dead + imposed + wind; safely transmit to **load-bearing structure** of the building |
| Deflection | Without causing deflection / deformation that may **damage the wall or impair its stability** |
| Methodology | Recognized engineering principles for design & structural use of materials |
| Water | Provision for **collection and discharge** of water seepage or condensed water |

#### 14.4 Curtain wall — materials (s. 30)
| Duty | Rule |
|---|---|
| Combustibility | Constructed of **non-combustible materials only** |
| Electrolytic / chemical action | If materials may react in contact → surface satisfactorily treated **or** separated to prevent corrosion |
| Anchors & fixings | Suitable materials; adequately protected against corrosion |

#### 14.5 Curtain wall — fixing of supports & maintenance (s. 31)
| Duty | Rule |
|---|---|
| Allowed fixing methods **only** | (a) **Cast-in anchorage** in a **structural concrete** member; **or** (b) **Welding or bolting** to a **structural steel** member |
| Host structure | Fixing must **not** impair structural integrity of the host member or adversely affect its performance |
| Access | Adequate means of access to outer surface / projections for M&R |

**SD kill switches:**
- CW support on blockwork / finishes / non-structural metal studs → **fails s. 31**
- Free-form / deep-recess façades without M&R access strategy → **fails ss. 27/28/31** (use External Maintenance CoP ≤500 mm hand-reach, BMU, etc.)
- Combustible rainscreen / combustible insulation as “cladding” without non-combustibility path → **fails ss. 27–30**

---

### 15. Protection against moisture and water (Part 9, ss. 32–34)

| Section | Element | Rule |
|---|---|---|
| **s. 32** | Walls that may be in contact with damp | Adequate protection to prevent moisture penetration |
| **s. 33(1)** | Ground surface **within** external walls | Cover with suitable material to prevent moisture penetration |
| **s. 33(2)** | Outside ground → adjoining floor | Adequate means to prevent ingress of water |
| **s. 33(3)** | Exterior ground surface (**except landscaped area**) | Paving laid to adequate gradient → surface water drain |
| **s. 33(4)** | Room provided with water supply | Floor constructed to prevent water penetration |
| **s. 33(5)** | Balcony (**including utility platform**) and verandah floors | Constructed to prevent water penetration |
| **s. 34(1)** | Roof | Designed & constructed to be **weatherproof** |
| **s. 34(2)** | Roof → adjoining floor | Prevent ingress of water |
| **s. 34(3)** | Roof / projections from roof | Adequate means of access for maintenance / repair |

**SD takeaways:**
- Wet rooms, UPs, balconies = waterproofing **statutory**, not only finishing schedule  
- Landscaped areas are carved out of the external paving rule — still need drainage design  
- Roof M&R access (s. 34(3)) is the same family as EW access — stairs to accessible roof, walkways, BMU parking  

---

### 16. Fire resisting construction — principle mandate (Part 10, s. 35)

Cap 123Q states **performance duties only**. Detailed FRR, compartmentation, MOE geometry → **Code of Practice for Fire Safety in Buildings** (+ related PNAPs) via APP-53.

On fire, the building must be designed and constructed so as to:

| Clause | Duty |
|---|---|
| (a) | Inhibit spread of fire **within** the building **and to buildings nearby** |
| (b) | Provide adequate resistance to spread of fire and smoke **between different buildings** and **between different uses** in the building |
| (c)(i) | Maintain stability to allow adequate time for **safe evacuation** |
| (c)(ii) | Maintain stability to allow adequate time for **rescue and firefighting** |
| (c)(iii) | Maintain stability to **avoid consequential damage** to buildings nearby |
| (d) | Provide adequate resistance to spread of fire **over the roof** to any other building, having regard to the **location** of the building |

**SD takeaway:** Use mixing, party-wall / separation distance, roof disposition vs neighbours, and structural fire stability are Cap 123Q geometry — not only an FSI schedule item. Feed FS Code next for numbers.

---

### 17. Protective barriers — when compulsory & how they must behave (Part 11 Div. 1, ss. 36–38)

#### 17.1 Exemptions — Division does **not** apply (s. 36(1))
| Exempt | Why it matters |
|---|---|
| Stage in an assembly hall | Stage edge uses other controls |
| Vehicle parking bay for **loading and unloading of goods** | Not every carpark bay — specifically L/UL goods bay |
| **Inaccessible roof** | Maintenance-only roof (s. 36(2) definition) |
| **Inaccessible area** | Not for human occupation; maintenance/repair only |
| Any space (**other than an accessible roof**) within domestic premises for occupation by **1 family** | Single-family domestic interiors exempt; **accessible roofs still in** |

#### 17.2 Must provide (s. 37)
1. At the edge of a **balcony, verandah, floor, roof, staircase, landing or projection** — to restrict / control movement of persons, objects **and vehicles**; **and**  
2. If difference between 2 adjacent levels (whether or not within a building) **exceeds 600 mm** → protective barrier at the **higher** level  

#### 17.3 Design performance (s. 38)
Barrier required under s. 37 must be designed and constructed so as to:
- Prevent a person or object from falling, rolling, sliding or slipping **through the gap**; **and**
- Prevent a person from **climbing over**

**Cross-links for geometry / openings / glass barriers:** PNAP APP-69 / APP-110, Loading Code Table for barriers, Cap 123F reg. 3A where relevant, External Maintenance CoP (fall ≥2 m → guard-rails/toe-boards unless Cap 123Q barrier provided). Cap 123Q sets **when** and **load/performance**; detailed rail height / opening sizes live in accepted CoPs / PNAPs.

**SD takeaway:** **600 mm** is the schematic hard number for steps, terraces, planter edges, sunken courts, podium drops — **including outdoor** areas. Then size Table 3 category for crowd density.

---

### 18. Lifts & escalators — building interface (Part 11 Div. 2, ss. 39–41)

#### 18.1 Scope — applies unless excluded (s. 39(1))
Applies to a building in which a lift or escalator is / is to be installed, **other than**:

| (a) | Amusement device, including amusement ride under Cap 449 |
| (b) | Belt, bucket, scoop or roller conveyor or similar machine |
| (c) | Hoist (incl. skip hoist) used mainly for charging furnaces or similar |
| (d) | Hoist used solely for lifting / feeding material directly into a machine |
| (e) | Lift with travel **≤ 3.5 m** that does **not** pass through any floor and is used **solely** for carriage / stacking / loading / unloading of goods or materials |
| (f) | Lift with travel **≤ 3.5 m** that does **not** pass through any floor and is used **solely** for raising motor vehicles |
| (g) | Construction-site lift provided solely for persons employed in construction and/or materials for construction |
| (h) | Ramp connected to a wharf or pier |
| (i) | Stage or orchestra lift |
| (j) | Stairlift with guided carriage travelling substantially along a flight of stairs (wheelchair or not) |
| (k) | Lifting platform for persons with a disability (wheelchair or not) if travel between levels and difference highest–lowest **≤ 2 m** |

#### 18.2 Building design duties (s. 40)
Building must be designed and constructed so as to:
1. Provide adequate **structural strength, space, protection, access and ventilation** for safe **operation, inspection and maintenance** of the lift / escalator; **and**  
2. Ensure **restricted space** is inaccessible except for inspection, maintenance, repair or rescue  

If a lift / escalator is **added after completion** → design & construction relating to the addition must still comply with s. 40(1).

#### 18.3 Warning notices (s. 41)
| Notice | Location |
|---|---|
| Caution against danger of entering restricted space **and** interfering with operation | Permanently at conspicuous location of every door / access to restricted space |
| Caution against using lift when there is a fire | Permanently at conspicuous location of **every lift entrance** |
| Form | Legible; durable materials |

**SD takeaway:** Shaft, pit, overrun, machine room / MRL space, ventilation, rescue access, and notice locations are Cap 123Q **building fabric** — brief lift consultant at concept so cores are not redrawn post-GP. Equipment rules remain Cap **618**.

---

### 19. Miscellaneous works that bite early (Part 12, ss. 42–47)

#### 19.1 Ground treatment (s. 42)
| Rule | SD implication |
|---|---|
| If ground treatment improves load-carrying capacity → give BA **adequate proof** of suitability of method & materials | Jet grout / compaction / soil mix = BA evidence path |
| After treatment → BA may require adequate tests of the ground | Programme risk |
| If treatment may affect any building / structure / land / street / services → adequate precautionary measures | Neighbour protection narrative |

#### 19.2 Wells (s. 43) — full list
| # | Rule |
|---|---|
| 1 | Must **not** be sunk or reopened except with **BA permission** |
| 2 | Design / construction / operation must not impair stability of or damage any building / structure / land / street / services |
| 3 | Must **not** be sunk in vicinity of septic tank, cesspool, sewage sump, or in contaminated ground |
| 4 | Adequate means to prevent surface water or sullage from entering from top opening |
| 5 | Properly lined to prevent contamination |
| 6 | If likely adversely affected by particle accumulation → suitable filter |
| 7 | Designed & constructed to prevent **unauthorized entry** |

#### 19.3 Chimney and flue (s. 44) — threshold & rules
**Applies if** chimney/flue internal diameter, breadth or width **> 200 mm** **or** height **> 3 m**.

| Element | Rules |
|---|---|
| **Chimney** | Constructed / positioned / shielded to prevent ignition of any part of this or any other building; outer surface temperature must not reach a level that may endanger a person in or near the building |
| **Flue** (inside or outside) | Same ignition prevention; positioned / shielded to minimize accidental damage to flue and danger to persons |
| **Termination** | Position so products of combustion will **not** enter windows, openings, fresh-air inlets, mechanical ventilation inlets or exhausts of this **or any other** building |
| **Products of combustion** include | Smoke; fumes from stove / oven / other cooking apparatus; **vitiated air** |

**SD takeaway:** Restaurant / kitchen flue terminations vs neighbour windows and own MV inlets are Cap 123Q geometry — coordinate early with B(P)R projections and FS Code.

#### 19.4 Fireplace (s. 45)
Hearth or fireplace recess must be constructed so as to prevent a fire in the building or any other building.

#### 19.5 Habitation by vermin (s. 46)
Building must be constructed so as **not** to provide a place of habitation for vermin (detailing of cavities, pipe penetrations, refuse areas).

#### 19.6 Person-entry ducts (s. 47)
If duct size allows a person to enter:
- Must be fitted with an **access opening**; **and**
- Must be constructed to **bear the weight of the person**

**SD takeaway:** Large services ducts / cable tunnels need structural floor loading + access doors on plans — not “void only.”

---

### 20. Codes of Practice that supply the schematic numbers (via PNAP APP-53)

Cap 123Q states *performance*; APP-53 names documents BA treats as compliant. At SD, design to current APP-53 editions (verify latest PNAP):

| Domain | Primary accepted document |
|---|---|
| Dead / imposed loads | CoP for Dead and Imposed Loads 2011 (2021 Ed.) — aligns with Cap 123Q Schedule |
| Wind | CoP on Wind Effects in Hong Kong 2019 |
| Concrete | CoP Structural Use of Concrete 2013 (2020 Ed.) |
| Steel | CoP Structural Use of Steel 2011 (2023 Ed.) |
| Foundations | CoP for Foundations 2017 |
| Precast | CoP for Precast Concrete Construction 2016 |
| Structural glass | CoP for Structural Use of Glass 2018 |
| Fire resisting / MOE interface | CoP for Fire Safety in Buildings 2011 (current Ed.) |
| External M&R access | CoP on Access for External Maintenance 2021 (2024 Ed.) — deemed to satisfy ss. 27(2), 28(5), 31(3), 34(3) |

Other materials (masonry, timber, aluminium, stainless, GRC, stone cladding, etc.) — APP-53 Appendix A full list; agree alternatives with BD early.

---

### 21. Schematic-design go / no-go gate (architect checklist)

Before freezing occupancy mix, envelope, levels, basement cut, or consultant briefs:

1. **Confirm statute** — Cap 123B is repealed; cite Cap **123Q** + APP-53 CoPs on submissions.  
2. **Map every floor zone to Table 1 class** — office vs filing, domestic vs F&B kitchen, refuge (5), plant (7.5), storage-by-height, stages (7.5), retail (5).  
3. **Lock partition strategy** — shown layouts or office ≥1 kPa floating surcharge (s. 7(2)); floating partitions **not** reducible (s. 8(5)(g)).  
4. **Flag no-reduction uses** — vehicles, storage, filing, dynamic industrial, equipment/displays (s. 8(5)).  
5. **UP ≥ 4 kPa / balcony ≥ 3 kPa** + **2 kN/m** edge line; A/C hoods **1.5 kN/m** edge (Class 8).  
6. **Wind ≥ 50-year** return + Wind CoP for cladding / CW / canopy suction (s. 6).  
7. **GI / SI before foundation narrative** — documentary + survey + GI; schedule RGE if slopes, retention, deep dig, Scheduled Area 1 (ss. 17–18, 25).  
8. **Retaining walls** — if not all three minor criteria → full filter / drainage / dual-level channels (ss. 22–24); FoS against four failure modes (s. 23).  
9. **Mid-Levels Scheduled Area 1** — limit bulk excavation for cumulative hillside effect (s. 25).  
10. **Envelope** — EW / cladding / CW **non-combustible**; CW supports only cast-in concrete **or** weld/bolt to structural steel (ss. 27–31).  
11. **External M&R access** — BMU / gondola / cherry picker / access windows / walkways per External Maintenance CoP; ≤500 mm hand-reach; allocate AC platforms / roof access early.  
12. **Moisture** — ground cover, wet-room floors, balcony/UP waterproofing, roof weatherproof + access (ss. 32–34).  
13. **Level difference > 600 mm** → protective barrier at higher level; size Table 3 crowd category; design against pass-through and climb-over (ss. 37–38).  
14. **Vehicle barriers** — lock max vehicle mass / speed for carpark & ramp edges (s. 9(3)).  
15. **Fire geometry** — inhibit internal / neighbour / use-to-use / roof spread; stability for escape & firefighting (s. 35) → FS Code numbers.  
16. **Lift / escalator cores** — space, strength, protection, access, ventilation; restricted-space security; fire + restricted-space notices (ss. 40–41); check s. 39 exclusions.  
17. **Industrial / warehouse** — design load notices at every storey staircase (s. 11); dynamic +2.5 kPa default if no plant data (s. 10).  
18. **Chimneys / flues >200 mm or >3 m** — termination clear of windows / FA / MV of this and neighbours (s. 44).  
19. **Person-entry ducts** — access opening + person load capacity (s. 47).  
20. **Cross-link companions** — Cap 123A (plans/certs), Cap 123C (demolition), Cap 123F (PR/SC), Cap 123N (minor works), FS Code, Cap 618 (lift equipment), PNAP APP-53 / APP-110 / APP-163.

---

### Source

Building (Construction) Regulation (Cap. 123Q), consolidated version for the Whole Chapter (24-06-2021) (English).  
In force 1 February 2021; Cap 123B repealed concurrently (L.N. 8 of 2020).  

Companion controls (do not confuse): Cap 123 (Ordinance), Cap 123A (Administration), Cap 123B (repealed), Cap 123C (Demolition Works), Cap 123F (Planning), Cap 123N (Minor Works), PNAP APP-53, CoP for Dead and Imposed Loads, CoP on Wind Effects, CoP for Fire Safety in Buildings, CoP on Access for External Maintenance, Cap 618 (Lifts and Escalators).

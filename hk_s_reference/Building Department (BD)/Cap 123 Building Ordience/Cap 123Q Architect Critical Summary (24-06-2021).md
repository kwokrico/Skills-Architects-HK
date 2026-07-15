# Cap 123Q — Building (Construction) Regulation
**Architect critical summary for schematic design**  
Consolidated version: 24 June 2021 | Cap. 123 sub. leg. Q | Commenced 1 February 2021

> Scope note: Cap 123Q is the **design-and-build performance rulebook** for building works and street works — loads, structure, foundations, site formation, envelope, moisture, fire resistance principles, protective barriers, and lift/escalator building interface. It is **not** the BD plan/consent package (Cap 123A), **not** demolition site safety (Cap 123C), **not** planning volume (Cap 123F), and **not** the detailed Fire Safety Code / PNAP APP suite. Use this before schematic design to lock occupancy load classes, envelope material strategy, level-difference barriers, curtain-wall fixing logic, and geotech triggers.

---

## Regulatory Overview

Cap 123Q applies to the **construction quality and structural/user-safety performance** of buildings, streets, building works and street works under the Buildings Ordinance. It sets compulsory rules for materials, dead/imposed/wind loads (with Schedule Tables 1–3), strength and stability, site investigation, foundations, site formation and retaining walls, external walls / cladding / curtain walls, moisture and water exclusion, fire-resisting construction principles, protective barriers, and building provisions for lifts and escalators.

---

## Critical main topics and subtopics

### 1. Materials — performance + testing duty (s. 3)

| Requirement | SD implication |
|---|---|
| Nature & quality suited to intended use | Do not specify speculative or unproven envelope / structure products without a recognised performance path |
| Adequately mixed / prepared | Site QA is statutory, not optional |
| Applied / fixed so they perform as intended | Fixing sequence and workmanship are compliance issues (esp. cladding / curtain wall) |
| Adequately tested by **recognized tests** | Budget recognised product tests / certificates early (fire, strength, non-combustibility) |

---

### 2. Load definitions architects must brief correctly (ss. 4–6)

| Load type | What it is | Design hard rule |
|---|---|---|
| **Dead load** (s. 4) | Permanent weight: walls, floors, roofs, finishes, **permanent partitions**, other permanent construction | Calculate from reliable unit weights — include finishes & fixed partitions in early massing weight assumptions |
| **Imposed load** (s. 5) | Everything else except wind — including **forces from adjacent ground** | Use greatest load likely from intended use; Schedule Table 1 is the floor; heavier equipment / displays override Table 1 (s. 7(3)) |
| **Wind load** (s. 6) | Pressure **or suction**, any direction | Base on building response; wind magnitude return period **≥ 50 years** |

**Imposed load application (s. 7):** Take whichever produces the **greater adverse effect** — uniform distributed load **or** concentrated / line load from Table 1.

#### 2.1 Floating partitions (positions not on plan) (s. 7(2))

When partition locations are **not** shown on plan, treat partition weight as additional uniformly distributed imposed load:
- ≥ **1/3** of partition weight per metre length, spread per m²; **and**
- for **office** floors: **not less than 1 kPa**

**SD takeaway:** Either fix partition layouts on GP, or budget ≥1 kPa office partition allowance + structural capacity for fit-out churn.

---

### 3. Minimum imposed loads — Schedule Table 1 (schematic occupancy map)

Use the **greater** of distributed (kPa) or concentrated (kN) effect. Concentrated load is normally on any **50 mm** square (vehicle areas: **200 mm** square).

#### Class 1 — Domestic / residential sleep (2 kPa / 2 kN)
Domestic; dormitories; private hotel/motel/guesthouse sitting rooms, bedrooms, toilets; hospital/nursing home/RCHE wards, bedrooms, toilets; domestic bathrooms (Jacuzzi separate), pantries, kitchens.

#### Class 2 — Institutional / office / light work
| Use | Dist. kPa | Conc. kN |
|---|---|---|
| Medical consulting / treatment; OT / X-ray | 2.5 | 3 |
| Labs; light workrooms (no central power machines / storage); general offices; light E&M rooms; meter rooms (not storage); office/non-industrial pantries | 3 | 4.5 |
| Banking halls; kitchens & laundries **not** domestic | 4 | 4.5 |
| Projection rooms | 5 | 4.5 |

#### Class 3 — Education / assembly / leisure
| Use | Dist. kPa | Conc. kN |
|---|---|---|
| Childcare / kindergarten | 2.5 | 3 |
| Classrooms, lecture / tutorial / computer / reading (no book storage); internet centres; dance practice; non-assembly leisure; billiard / bowling; massage / sauna / bath house (**pools/fountains separate**) | 3 | 4.5 |
| Fixed-seat assembly / worship; restaurants, bars, canteens, F&B (not domestic); cafes, mahjong, amusement centres; columbaria (not niches) | 4 | 4.5 |
| Art galleries / museums; grandstands; public halls; theatres / cinemas; concert halls; conference / waiting | 5 | 4.5 |
| Assembly **without** fixed seating; dance / disco; footbridges; footpaths / terraces / plazas; garden open areas (incl. short-grass turf); karaoke; gymnasia; **refuge floors**; ice rinks (**ice weight separate**), ball courts, golf ranges | 5 | 4.5 |
| Stages & TV studios used as stages | **7.5** | **9** |

> **Fixed seating note:** seating counts as fixed only if removal and reuse of the space for other purposes are **unlikely**.

#### Class 4 — Retail (5 kPa / 4.5 kN)
Department stores, supermarkets, markets, shops for display and sale.

#### Class 5 — Storage / plant / industrial (watch storey height)
| Use | Dist. load | Conc. |
|---|---|---|
| Library rooms with book storage (not stack rooms); offices for storage / normal filing | 5 kPa | 4.5 kN |
| Bookstore / library **stack rooms** | **3.5 kPa per m storage height**, min **10 kPa** | ≥ 9 kN (by material weight) |
| Cold storage | **5 kPa per m**, min **15 kPa** | ≥ 9 kN |
| Printing plant paper storage | **8 kPa per m** | ≥ 9 kN |
| Battery / UPS rooms | **10 kPa per m** | ≥ 9 kN |
| Refuse / general / warehouse storage (else) | **2.5 kPa per m** | ≥ 9 kN |
| Plant / boiler / fan / motor rooms & the like | **7.5 kPa** | 9 kN |
| Factories / workshops — light / medium / heavy / printing | **5 / 7.5 / 10 / 12.5 kPa** | 9 kN |

> **Storage height** = floor to ceiling / soffit / roof / other physical obstruction that limits stack height. Clear storey height on schematic plans **directly drives imposed load**.

#### Class 6 — Vehicles
| Use | Dist. | Conc. |
|---|---|---|
| Vehicles ≤ **3 000 kg** gross | 3 kPa | **20 kN** on **200 mm** square |
| Vehicles > 3 000 kg | By engineering principles | By engineering principles |

#### Class 7 — Roofs & canopies
| Roof type | Dist. kPa | Conc. kN |
|---|---|---|
| Inaccessible, slope ≤ 5° | 2 | 1.5 |
| Inaccessible, >5° to ≤20° | 0.75 | 1.5 |
| Inaccessible, >20° to <40° | Interpolate 0.75 → 0 | 1.5 |
| Inaccessible, ≥40° | 0 | 1.5 |
| Other roofs (not Classes 1–6 uses), slope ≤20° | 2 | 1.5 |
| Other roofs, >20° to <40° | Interpolate 2 → 0 | 1.5 |
| Other roofs, ≥40° | 0 | 1.5 |
| Canopies | **0.75** | **1.5** (excludes uncontrolled construction-material piles during maintenance) |

#### Class 8 — Projections & circulation
| Element | Dist. | Conc. / line |
|---|---|---|
| **Utility platforms** | Same as accessed floor, **≥ 4 kPa** | **2 kN/m** along outer edge |
| **Balconies** | Same as accessed floor, **≥ 3 kPa** | **2 kN/m** along outer edge |
| Stairs, landings, corridors | Same as accessed floor, **≥ 3 and ≤ 5 kPa** | 4.5 kN |
| A/C hoods / platforms / projecting window hoods | — | **1.5 kN/m** outer edge |
| Maintenance catwalks | — | **1 kN** at 1 m centres |

**SD takeaway:** Label every floor zone with intended use **and** Table 1 class on early plans — load jumps (office 3 → filing 5 → stack/cold by height) change structure early.

---

### 4. Load reduction — when structure can shed imposed load (s. 8 + Table 2)

#### Allowed (column / pier / wall / foundation carrying multi-floor distributed imposed load)

| No. of floors (incl. roof) qualifying | Classes 1–4 & 7 | Factories/workshops Class 5(4) ≥ 7.5 kPa |
|---|---|---|
| 1 | 0% | 0% |
| 2 | 5% | 10% |
| 3 | 10% | 20% |
| 4 | 15% | **25% max** |
| 5–8 | 20–35% | 25% max |
| >8 | **40% max** | 25% max |

#### Beam reduction (s. 8(2)–(3))
Single-span beam supporting **≥ 45 m²** floor at a level: **5% per complete 45 m²**, max **20%** for that floor — beam design only.

#### Never reduce (s. 8(5))
- Equipment / machinery / display loads under s. 7(3)
- Factories / workshops designed for **< 7.5 kPa**
- Floors used by **vehicles**
- Office **storage / filing**
- **Dynamic** effects
- **Storage** floors
- Partition loads where positions are **not** shown on plan

**Factory floor (s. 8(4)):** If designed ≥ 7.5 kPa, after reduction total must not fall below all floors at **7.5 kPa without Table 2 reduction**.

---

### 5. Protective barrier loads & vehicle barriers (s. 9 + Table 3)

#### Person barriers (Table 3) — apply separately; also check wind if applicable (take greater)
| Category | Line load (kN/m) | Infill UDL (kPa) | Infill point (kN) |
|---|---|---|---|
| Congregation **not** expected | 0.75 | 1 | 0.5 |
| May congregate, overcrowding **not** expected | 1.5 | 1.5 | 1.5 |
| Susceptible to **overcrowding** | **3** | 1.5 | 1.5 |

Line load acts at **1.1 m** above floor **or** top of barrier — **whichever is lower**.

#### Vehicle barriers (s. 9(3))
Min design impact force: **[0.5 M v² / (δc + δb)] kN**  
- *M* = heaviest allowed vehicle gross mass (kg)  
- *v* = velocity normal to barrier (m/s)  
- *δc*, *δb* = vehicle & barrier deformation (mm)  
Force uniform over **1.5 m** length, horizontally at **bumper height**.

---

### 6. Dynamic effects — industrial floors (s. 10)

Additional imposed loads. If not derived from building-specific plant data:
| Design target | Additive force |
|---|---|
| Slabs & beams | **+2.5 kPa** vertical |
| Frames & foundations | Additional **horizontal** = **10%** of that 2.5 kPa, on whole-number of floors ≥ **0.2 ×** total dynamic floors (max adverse); **need not act with wind** |

Permanent **designed load notices** (s. 11) required in industrial buildings & warehouses — durable, at each staircase per storey (or suitable place); split by floor zone if loads differ. Exclude dynamic effects from the posted figure.

**No overloading** beyond proper bearing capacity except for testing (s. 12).

---

### 7. Structure performance — design methodology gate (ss. 13–16)

| Section | Hard rule |
|---|---|
| s. 13 Methodology | Conform to laws of mechanics + recognized engineering principles & practices |
| s. 14 Strength & serviceability | Sustain & transmit dead + imposed + wind to ground; adequate factor of safety; no adverse crack/deflection/damage to self **or neighbours**; do not reduce neighbours’ FoS |
| s. 15 Stability | Adequate **margin of safety against instability** |
| s. 16 Construction methods | Appropriate methods + precautions; temporary **or** permanent state must stay within dimensional tolerance; no neighbour damage / FoS loss |

**SD takeaway:** Neighbour vibration / settlement / façade impact is a Cap 123Q duty from schematic — not only a construction courtesy.

---

### 8. Site investigation & foundations (ss. 17–20)

| Rule | SD implication |
|---|---|
| s. 17 GI must give adequate geotech + other relevant data to recognized standards | Do not freeze massing / basement depth without GI scope |
| s. 18 Foundation must take ground conditions, **installation method**, and **group effects**; site investigation **before** construction; ground must safely take all loads with FoS | Pile / footing strategy is a SD decision; protect adjacent buildings/services |
| s. 19 BA may require on-site tests if design assumptions doubted | Conservative assumptions reduce BA test risk |
| s. 20 Proof tests on **representative foundation units** (load / core drill cast-in-place / other suitable) | Programme time + cost for pile proofs |

---

### 9. Site formation & retaining walls (ss. 21–25)

#### Site formation (s. 21)
Adequate margin of safety for works **and remainder of site** during and after construction; no damage / FoS loss to buildings, land, streets, services.

#### Minor retaining wall exemption threshold (s. 22) — all three must apply
1. Upper–lower ground difference **≤ 1.5 m**; **and**
2. Upper ground average inclination **≤ 15°**; **and**
3. No foundation / structure surcharge on the wall  

Only then is the wall a **minor retaining wall** (drainage rules in s. 24 do not apply).

#### Retaining wall design (s. 23)
Safely support earth/fill + other loads under most onerous construction & service conditions; GI-based (s. 17); FoS against **sliding, overturning, bearing failure, and deep failure beneath**.

#### Non-minor retaining wall extras (s. 24)
| Item | Rule |
|---|---|
| Filter against soil | Pass water; restrain particle migration |
| Drainage to relieve water pressure | Performance maintainable for **service life** |
| Backfill | Compactable to stable fill |
| Upper **and** lower levels | Channels of suitable size **or** paving → surface water drain at adequate gradient |

#### Mid-Levels bulk excavation (s. 25) — Scheduled Area No. 1
**Bulk excavation** = any excavation **except** GI, utility trenches, drains, sewers, pile installation.  
Must be limited to minimize **cumulative adverse effect** on Mid-Levels hillside stability from multiple sites.

**SD takeaway:** Flag Mid-Levels / Scheduled Area 1 early — basement bulk cut is regulated as a hillside cumulative issue, not just a site yardstick.

---

### 10. External wall, cladding, curtain wall (ss. 26–31) — envelope hard rules

| Definitions (s. 26) | |
|---|---|
| **Cladding** | Facing / architectural decoration additional to structural elements |
| **Curtain wall** | Non-load-bearing enclosure fixed to load-bearing structure |
| **Non-combustible** | Passes a **recognized non-combustibility test** |
| **Load-bearing** (for this Part) | Bears load other than self-weight or wind on its own surface |

#### External wall (s. 27)
- Materials: **permanent, impervious, non-combustible**
- **Adequate access** to outer surface (and projections) for maintenance / repair

#### Cladding (s. 28)
| Must | Detail |
|---|---|
| Non-combustible; suitable thickness / strength / durability | Spec early |
| Fixed & supported to maintain long-term stability & integrity | Sequence matters |
| Flexible joints H + V for differential movement | Movement joint set on elevation strategy |
| Suitable **metal dowels & fixings** permanently into structure; corrosion-protected | No decorative adhesive-only logic |
| If weather-exposed: access for maintenance | Gondola / BMU / cradles / ladders planned in SD |

#### Curtain wall (ss. 29–31)
| Topic | Rule |
|---|---|
| Loads | Sustain & transmit dead + imposed + wind to load-bearing structure without damaging deflection |
| Water | Collect & discharge seepage / condensation |
| Materials | **Non-combustible only**; electrolytic separation / surface treatment; corrosion-protected anchors |
| Support fixing | Only by **cast-in anchorage in structural concrete** **or** **weld/bolt to structural steel** |
| Fixing effect | Must not impair host member integrity / performance |
| Access | Outer surface maintenance / repair access required |

**SD takeaway:** Curtain wall support must land on **real** structure (cast-in or structural steel) — cannot rely on blockwork / finishes. Access / BMU is statutory for EW, cladding, CW, and roofs (s. 34).

---

### 11. Moisture & water protection (ss. 32–34)

| Element | Rule |
|---|---|
| Walls in contact with damp | Adequate moisture-penetration protection |
| Ground within external walls | Cover with suitable material against moisture |
| Outside ground → adjoining floor | Prevent water ingress |
| Exterior ground (except landscaped) | Paving to gradient → surface water drain |
| Rooms with water supply | Floors prevent water penetration |
| Balcony (incl. utility platform) & verandah floors | Prevent water penetration |
| Roof | Weatherproof; prevent ingress to adjoining floor; **maintenance access** to roof / projections |

---

### 12. Fire resisting construction — principle mandate (s. 35)

Cap 123Q states performance duties only; detailed FRR / compartmentation live in the Code of Practice for Fire Safety in Buildings and related PNAPs. On fire, the building must:
1. Inhibit spread **within** the building and to **nearby** buildings  
2. Resist fire & smoke spread **between buildings** and **between different uses** inside  
3. Maintain stability long enough for evacuation, rescue / firefighting, and to avoid consequential damage to neighbours  
4. Resist fire spread **over the roof** to other buildings, having regard to location  

**SD takeaway:** Use separation, roof disposition, and use-mixing as fire geometry from day one — Cap 123Q makes neighbour and use-separation a structural/envelope duty, not only an FSI checklist item.

---

### 13. Protective barriers — where they are compulsory (ss. 36–38)

#### Exempt (s. 36) — barriers Division does **not** apply
- Assembly hall **stage**
- Vehicle parking bay for **loading / unloading** of goods
- **Inaccessible** roof or area (maintenance/repair access only; not for human occupation)
- Spaces (other than accessible roof) in **1-family domestic** premises

#### Must provide (s. 37)
1. At edge of balcony, verandah, floor, roof, staircase, landing or projection — to control persons, objects, **and vehicles**; **and**
2. Wherever adjacent level difference **> 600 mm** — barrier at the **higher** level

#### Design (s. 38)
- Prevent falling / rolling / sliding / slipping **through** gaps; **and**
- Prevent climbing **over**

**SD takeaway:** The **600 mm** level-difference rule is the schematic hard number for steps, terraces, planter edges, and sunken courts — including outdoor areas. Size guardrails for Table 3 category (congregation / overcrowding). Detailed barrier geometry (height, openings) continues under Cap 123B / codes of practice — Cap 123Q sets when and how they must perform under load.

---

### 14. Lifts & escalators — building interface only (ss. 39–41)

Division 2 applies where a lift / escalator is (to be) installed, **except** a long list of non-regulated devices (amusement rides, conveyors, furnace hoists, goods lifts ≤ **3.5 m** travel not through floor, car lifts ≤ 3.5 m not through floor, construction-site lifts, pier ramps, stage/orchestra lifts, stairlifts, disability lifting platforms with travel ≤ **2 m**, etc.).

| Duty | Requirement |
|---|---|
| s. 40 Building design | Adequate structural strength, **space**, protection, **access**, **ventilation** for safe operation / inspection / maintenance; **restricted space** (shaft + machine spaces) inaccessible except inspection / maintenance / repair / rescue |
| Retrofit lifts | Same rules when added after completion |
| s. 41 Notices | Durable notices: danger of entering restricted space / interfering with operation; and **do not use lift in fire** at every lift entrance |

**SD takeaway:** Machine rooms / MRL pits / shaft ventilation and rescue access are Cap 123Q building fabric — coordinate with Cap 618 lift contractor early so structural cores are not redrawn post-GP.

---

### 15. Miscellaneous hooks that bite early (ss. 42–47)

| Topic | Critical constraint |
|---|---|
| **Ground treatment** (s. 42) | Prove method & materials to BA; BA may require ground tests; protect neighbours if treatment may affect them |
| **Wells** (s. 43) | BA permission to sink / reopen; not near septic / cesspool / sewage sump / contaminated ground; prevent surface sullage entry; lining; filter if particle risk; prevent unauthorized entry; no stability damage |
| **Chimney / flue** (s. 44) — if internal dia/breadth/width **> 200 mm** **or** height **> 3 m** | Position/shield against ignition & outer-surface burn risk; flue termination so products of combustion **do not** enter windows, openings, FA inlets, MV inlets/exhausts of this or other buildings |
| **Fireplace** (s. 45) | Hearth / recess prevent fire to this or other buildings |
| **Vermin** (s. 46) | Construction must not provide vermin habitation |
| **Person-sized ducts** (s. 47) | Access opening + structure to bear a person’s weight |

---

### 16. Schematic-design go / no-go gate (architect checklist)

Before freezing occupancy mix, envelope, levels, or basement cut:

1. **Map every floor zone to Table 1 class** — especially filing vs general office, kitchen vs domestic, refuge floor (5 kPa), plant (7.5), storage-by-height, stages (7.5).
2. **Lock partition strategy** — shown layouts or office ≥1 kPa floating-partition surcharge (s. 7(2)); floating partitions **cannot** take multi-storey load reduction (s. 8(5)(g)).
3. **Flag no-reduction uses** — vehicles, storage, filing, dynamic industrial, equipment displays.
4. **Utility platforms ≥ 4 kPa** and balconies **≥ 3 kPa** + **2 kN/m** edge line — do not under-design domestic projections.
5. **GI before foundation narrative** — schedule RGE if slopes, retention, deep excavation, or Scheduled Area 1 (ss. 17–18, 25).
6. **Retaining walls > minor threshold** get full drainage / filter / dual-level channels (ss. 22–24); FoS against four failure modes (s. 23).
7. **Envelope materials non-combustible** for EW / cladding / CW; CW supports only cast-in concrete or weld/bolt to structural steel (ss. 27–31).
8. **Maintenance access** for EW, cladding, CW, roof — BMU / cradle / ladder strategy is statutory.
9. **Level difference > 600 mm** → protective barrier; size load category (Table 3) for assembly / street plaza density.
10. **Fire geometry** — inhibit internal / neighbour / use-to-use / roof spread; stability for escape & firefighting (s. 35) — feed FS Code compartmentation next.
11. **Lift / escalator cores** — shaft restricted space, ventilation, access, fire warning notices (ss. 40–41).
12. **Cross-link companions** — Cap 123A (plan packages & certs), Cap 123B (detailed construction standards where still relevant / historic), Cap 123C (demolition), Cap 123F (PR/SC), FS Code / Cap 95 / Cap 502 (fire services detail), Cap 618 (lift equipment).

---

### Source

Building (Construction) Regulation (Cap. 123Q), consolidated version for the Whole Chapter (24-06-2021) (English).  
Companion controls (do not confuse): Cap 123 (Ordinance), Cap 123A (Administration), Cap 123B (Construction — older detailed regs where still applicable in practice references), Cap 123C (Demolition Works), Cap 123F (Planning), Cap 123N (Minor Works), Code of Practice for Fire Safety in Buildings, Cap 618 (Lifts and Escalators).

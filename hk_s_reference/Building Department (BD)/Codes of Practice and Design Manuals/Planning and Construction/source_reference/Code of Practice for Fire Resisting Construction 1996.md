# Code of Practice for Fire Resisting Construction 1996
**Architect critical summary for schematic design**  
January 1996 revision (first issue November 1989) | Building Authority / Buildings Department

> Scope note: Guidance on compliance with **Part XV of the Building (Construction) Regulations** — passive fire resisting construction only (compartmentation, FRP, separations, openings, shafts, façades, basements, bridges/tunnels, doors, refuge floors). Means of escape, means of access, and active FSI are in other Codes. **Superseded for new work by FS Code 2011 Part C** (unified MOE + FRC + MOA); keep this summary for legacy A&A, historic approvals, and understanding the FRP logic that Part C inherited.

---

## Regulatory Overview

This Code sets the **passive fire-resisting envelope** for buildings: maximum compartment volumes, fire resistance periods (FRP) by use class, separation between uses/occupancies, protection of openings and shafts, façade/spandrel rules, basements, bridges/tunnels, fire doors, and refuge floors. It applies wherever Building (Construction) Regulations Part XV fire-resisting construction requirements must be demonstrated to the Building Authority.

Compliance is by **prescriptive provisions** (deemed reliable) or an **alternative / fire engineering approach** for special size, height, use, design, construction or location — assessed against MOE, MOA, FSI, FRC, size, height, use, location and management as a package.

---

## Critical main topics and subtopics

### 1. Lock use class + compartment volume first (Tables 1 & 2)

Every FRP, separating wall, and basement strategy hinges on Table 2 use class and Table 1 volume. Set these before fixing cores, atria, warehouses, or podium stacking.

#### 1.1 Maximum compartment volume (Table 1)

| Use | Max compartment volume |
|---|---|
| **Bulk storage / warehouse** | **7 000 m³** if compartment floor is **above basement** and building height ≤ **30 m** (B(P)R 23(1)); **3 500 m³** if at **basement** level **or** height **> 30 m** |
| **All other uses** | **28 000 m³** |

Oversized compartments → case-by-case only, with enhanced MOE / MOA / FSI / improved FRP (Table 1 Note).

#### 1.2 Fire resistance period by use (Table 2)

| Class | Use | Compartment volume | Min FRP |
|---|---|---|---|
| **1** | Domestic | ≤ 28 000 m³ | **1 hour** |
| **2** | Hotel bedrooms | ≤ 28 000 m³ | **1 hour** |
| **3** | Office | ≤ 28 000 m³ | **1 hour** |
| **4–8** | **4** Shop / restaurant / hotel foyer; **5** PPE; **6** Hospital; **7** Place of assembly; **8** Carparking | ≤ **7 000 m³** | **1 hour** |
| **4–8** (larger) | Same as above | **> 7 000 m³** but ≤ **28 000 m³** | **2 hours** |
| **9** | Bulk storage / warehouse | ≤ **7 000 m³** | **2 hours** |
| **10** | Industrial undertaking (excl. bulk storage / warehouse) | ≤ **28 000 m³** | **2 hours** |

**SD takeaways:**
- Classes **4–8** jump from **1 hr → 2 hr** once compartment volume exceeds **7 000 m³** — split retail / F&B / PPE / carpark volumes early or accept thicker structure.
- Warehouse / bulk storage are volume-capped much tighter than “all other uses,” and start at **2 hr**.
- Different use classes → separate per §8; special hazards → §14; uses not listed → BA case-by-case (Note 3).

---

### 2. Basement FRP override — always 4 hours (§6.2)

| Item | Rule |
|---|---|
| Every element of construction in a basement | FRP ≥ **4 hours** |
| Every basement compartment wall / floor | FRP ≥ **4 hours** |
| Separation between basement and any adjoining storey | FRP ≥ **4 hours** |

If basement is united with G/F (and upper storeys of same use), **all** those united storeys + the slab separating the uppermost united storey from the storey above must also take the **basement FRP** (§15.1).

**SD takeaway:** One continuous retail volume from B1 through G/F forces **4 hr** structure through the podium — usually a massing killer. Prefer a hard **4 hr** slab cut at basement ceiling.

---

### 3. Single-storey unprotected steel — rare exemption (§6.3)

Unprotected steel allowed only if **all** apply:
- Single-storey building
- Volume ≤ **7 000 m³**
- Height ≤ **7.5 m**
- Clear open space ≥ **6 m** to adjoining building **or** site boundary

External columns/beams still need corrosion consideration separately.

---

### 4. Separation between uses (§8) — podium stacking driver

| Situation | Separation FRP |
|---|---|
| Parts of building in **different Table 2 use classes** | Longer of the two Table 2 FRPs, **never < 2 hours** |
| Ancillary small offices, caretakers’ quarters, small storage / loading in an **industrial** building | **No** such separation required |

**SD takeaway:** Flat over shop, office over carpark, hotel over retail = **≥ 2 hr** compartment floors/walls even when each use alone would only need 1 hr.

---

### 5. Separation between occupancies (§9) — multi-tenant / flat corridor rules

| Rule | Requirement |
|---|---|
| Different occupancy types | Walls/floors FRP ≥ compartment element FRP, **capped at 2 hours** |
| Retail **or** office tenancies under **common effective management** + common fire alarm (sprinkler or break-glass actuated) | Separation **waived** (BA must accept management) |
| Internal corridor serving rooms/flats of different occupancies (**except shopping arcades**) | Corridor walls ≥ **1 hr**; door ≥ **½ hr**; fixed lights ≥ **½ hr** only if sill ≥ **1.8 m** |
| Balcony approach (unless escape already in **two directions**) | Same as corridor: walls ≥ **1 hr**; door ≥ **½ hr**; fixed lights ≥ **½ hr** @ ≥ **1.8 m** |

---

### 6. Protection of adjoining buildings / boundary (§7) — massing & window setbacks

| Condition | Enclosure / opening rule |
|---|---|
| Buildings on **same site** < **1.8 m** apart | Treat as adjoining; within 1.8 m → **imperforate** external wall/roof at **same FRP as internal elements** |
| Openings in that 1.8 m zone | Fixed lights ≥ **½ hr** (stair/lobby ≥ **1 hr**), and ≥ **900 mm** from any lower-FRP part of the adjoining building |
| Unprotected openings | Only if ≥ **1.8 m** from unprotected openings of adjoining building |
| Within **900 mm** of **common boundary** | Imperforate wall/roof at internal-element FRP |
| Openings near boundary | Fixed lights ≥ **½ hr** (stair/lobby ≥ **1 hr**) if ≥ **450 mm** from boundary |

See Diagram 1. **SD takeaway:** Tight twin-tower / party-wall schemes lock blank FR walls and kill curtain-wall continuity near the gap.

---

### 7. Openings through compartment walls & floors (§10)

| Opening type | Protection |
|---|---|
| Door / fire shutter in compartment wall (communication, **not** combining compartments) | Same FRP as wall for **integrity + insulation**; insulation waived if total opening width ≤ **25%** of wall length |
| Escalator / non-required stair perforating floors | May be unenclosed in **one** compartment if enclosed in the other by walls ≥ **longer** of the two compartment FRPs; door/shutter ≥ **½** enclosing-wall FRP |
| Ramp crossing compartment wall | Fire shutter ≥ **longer** of the two FRPs; drenchers only if shutters impractical (FSD satisfaction) |
| A/C, vent ducts, electrical trunking, pipes, wires through compartment wall/floor | Fire dampers / fire stops to maintain wall/floor FRP; combustible ducts/pipes/insulation → enclosure at **full** wall/floor FRP; access doors ≥ **½** enclosure FRP |
| Same through **non-compartment** FR walls/floors without enclosure | Sealing system around service, FRP ≥ wall/floor, BS 476 Pt 20 assessed, moisture-stable, life ≥ service life, firmly fixed |
| Fire shutters / dampers | Construction to BA; operation/test/maintain to **Director of Fire Services** |

---

### 8. Vertical shafts (§11) — cores, lifts, required stairs

#### 8.1 Liftwells

| Item | Rule |
|---|---|
| Liftwell enclosure (except landing doors, ventilation, machine/pulley room openings) | Walls/floors ≥ **2 hours** |
| Seal around frames, indicators, call buttons | Maintain wall FRP |
| Landing / other liftwell doors | Integrity ≥ **1 hour**; insulation also where Diagram 2 requires (**F** vs **S** arrangements) |

#### 8.2 Required staircases + intercepting lobbies

| Item | Rule |
|---|---|
| Separation from rest of building | Walls ≥ FRP of elements of connected compartment |
| Door to accommodation | Integrity ≥ **lesser of ½ wall FRP or 1 hour**; insulation ≥ **½ hour** |
| Open stair from balcony approach | Door not required if stair open to external air ≥ **50%** of plan perimeter (balustrade top to soffit of flight above) |
| Services in stair enclosure | Emergency services only (hydrants, sprinklers, emergency lights, exit signs) unless enclosed at stair-wall FRP; access door integrity ≥ lesser of ½ wall or 1 hr; insulation ≥ ½ hr |
| Stair structure inside compliant enclosure | Need **not** have FRP but must be **non-combustible** |
| Single-stair building, G/F not domestic/office | Stair G–1/F separation at **longer** of the use FRPs + **450 mm** return wall at main entrance along G/F occupancy frontage |

#### 8.3 External wall of required stair / lobby (§11.6–11.8)

| Distance **d** to street opposite / boundary / weaker wall or unprotected opening / other building on site | Stair/lobby external wall |
|---|---|
| **d > 6 m** | May be unprotected; openings unprotected |
| **d ≤ 6 m** | FRP ≥ stair separating-wall FRP; imperforate except fixed light ≤ **25%** of that storey’s external wall area (FRP ≥ ½ stair wall), or discharge door at G/F / roof ≥ **½** wall FRP |

If stair external wall continues in same plane as weaker general façade → remaining FR stair/lobby walls must **project ≥ 450 mm** at the junction (not beyond façade at G/F discharge). Diagrams 3–4.

---

### 9. Inter-floor / atrium / façade fire spread (§12) — SD killers

#### 9.1 Unprotected floor openings (escalators, atria, circulation stairs) — §12.1

| Item | Rule |
|---|---|
| Vertical barrier around opening | Depth ≥ **450 mm** down from floor soffit (or ≥ **450 mm** below false ceiling if present) |
| Barrier FRP | ≥ **1 hour** |
| Alternatives if headroom blocks barrier | Smoke reservoirs, open/perforate ceilings, dynamic smoke extract, detector-operated devices — BA case-by-case with proven effectiveness + post-completion management |

#### 9.2 Curtain wall / multi-storey envelope — §12.2

| Item | Rule |
|---|---|
| Curtain wall / similar spanning >1 storey | Entirely **non-combustible** |
| Void between curtain wall and floor edge | Solidly infilled at **each floor** with non-combustible material FRP ≥ **floor FRP** |

#### 9.3 Spandrel — §12.3 (Diagram 7)

External wall at any floor separated from wall of floor below by spandrel that is:
- Height ≥ **900 mm**; and
- Non-combustible with FRP ≥ intervening floor FRP

**SD takeaway:** Full-height vision glass without 900 mm FR spandrel (or equivalent floor-edge fire stop) fails. Coordinate early with façade consultant.

---

### 10. Roofs (§13)

| Condition | Requirement |
|---|---|
| All roofs + roof structure members | **Non-combustible** |
| Single-staircase building, highest floor > **13 m** above ground | Roof FRP ≥ **1 hour** |
| Roof used / intended as refuge floor (or part) | Roof FRP ≥ **2 hours** |

---

### 11. Special hazards (§14)

| Hazard | Enclosure |
|---|---|
| Electrical / hazardous installations or dangerous goods stores | Non-combustible ≥ **2 hours**; **4 hours** where adjoining required staircases; doors ≥ **1 hour** |
| Other high fire-risk areas associated with normal occupancy | Non-combustible ≥ **2 hours** |
| Domestic flat with **single exit door**, kitchen adjacent to that door | Kitchen walls ≥ **1 hour**; kitchen door ≥ **½ hour** |

---

### 12. Basement smoke outlets (§15.2–15.4) — plant / layout drivers

#### 12.1 Without dynamic smoke extract

| Criterion | Rule |
|---|---|
| Spacing | ≤ **30 m** apart; along street frontages or adjacent to external walls |
| Position | High level; even perimeter distribution; create through-draught |
| Coverage | Every basement compartment |
| Aggregate area | ≥ **0.5%** of floor served; **≥ 2.5%** if bulk storage / warehouse |
| Least dimension | ≥ **1 m** |
| Location vs stairs | As far as possible from required-stair discharge; indicated on external face |
| Cover | Stall-boards / pavement lights easily broken by firefighters; if inaccessible outdoors → unobstructed or metal grille/louvre (**not aluminium**) |

#### 12.2 With dynamic smoke extract (FSD satisfaction)

| Criterion | Rule |
|---|---|
| Number | ≥ **1 outlet per 3 500 m³** compartment volume, and ≥ **1 per floor** |
| Access | Readily accessible to firefighters |
| Other | Still follow §15.2 except area % and aluminium rule where incompatible |

Smoke outlet shafts through other storeys: FRP / enclosure ≥ longer of storey served or storeys passed; adjoining shafts similarly separated; unenclosed shafts → hard-body impact test BS 5669.

---

### 13. Bridges & tunnels (§16)

#### 13.1 Bridges uniting buildings

| Arrangement | Requirement |
|---|---|
| Default | Fire shutter ≥ **2 hr** at **each** end + by-pass lobby (walls ≥ **2 hr**, doors ≥ **1 hr**) |
| Double shutter (2 hr each end) | By-pass lobby **not** required unless bridge **> 18 m** (then bridge treated as integral with the building **without** shutters) |
| Bridge structure | Non-combustible; FRP ≥ **lower** of the two buildings |
| Façade near junction | No opening within **900 mm** of bridge junction; walls in that zone non-combustible ≥ **2 hr** |
| Exemption | Wholly non-combustible bridge with side barriers/parapets ≤ **1.2 m** high only |

#### 13.2 Tunnels

Same logic at **4 hr** shutters / lobby walls and **2 hr** lobby doors; tunnel itself non-combustible ≥ **4 hr**. Double 4 hr shutters waive lobby unless tunnel **> 18 m**.

---

### 14. Fire doors (§17)

| Item | Rule |
|---|---|
| All FR doors | **Self-closing** |
| Required stair / intercepting lobby doors | Must **remain closed** |
| Other FR doors | May be held open only if released manually **and** by smoke detection or fire alarm (FSD) |
| Signage (unless hold-open compliant) | Both sides: “FIRE DOOR / TO BE KEPT CLOSED” + Chinese equivalent; letters ≥ **10 mm** |
| Edge fit | Close fit to impede smoke/flame; bottom gap ≤ **4 mm** |
| Test | BS 476 : Part 22 : 1987; integrity (+ insulation if required); each side separately (lift doors: landing side only) |
| Hinges | Melting point ≥ **800°C** unless proven in assembly test |
| Uninsulated glazing (where insulation not required) | ≤ **25%** of door leaf area |
| Aggregate door openings in wall | ≤ **½** of overall wall area — else doors need **full wall FRP** |

---

### 15. Refuge floors (§18)

| Item | Rule |
|---|---|
| Refuge area separation | Walls/floors ≥ **2 hours** from rest of building, including shafts/ducts through the floor |
| Shafts/ducts | Must **not** open directly onto the refuge floor |
| Open side (where required open) | Not within **6 m** (direct or diagonal) of: opposite street side; common boundary; same-building wall < 2 hr FRP or unprotected opening without ≥ 1 hr fixed light; or other building on site |

*(Frequency / area of refuge floors is controlled by the MOE Code / later FS Code Part B — not this FRC document.)*

---

### 16. FRP criteria & deemed-to-satisfy tables (Table 3 + Tables A–F)

#### 16.1 What must pass the fire test (Table 3) — schematic shorthand

| Element | Stability | Integrity | Insulation | Exposure |
|---|---|---|---|---|
| Frame / beam / column | Y | N | N | Exposed faces |
| Floor (incl. compartment) | Y | Y | Y | Each side |
| Roof forming exit / acting as floor | Y | Y | Y | Underside |
| Loadbearing wall (not separating/compartment) | Y | N | N | Each side |
| External wall / compartment wall / protected shaft·lobby·corridor | Y* | Y | Y | Each side |
| Fire shutter / fire stop / barrier | N | Y | N | Each side |
| Smoke outlet shaft | Y | — | — | From outside; cross-section ≤ **75%** original = stability failure |
| Duct/pipe/wire enclosure or sealing | N | Y | N | From outside |
| Door (unless specified) | N | Y | N† | Each side (lift: landing only) |
| Fixed light | Y* | Y | Y | Each side |
| Services enclosure in stair/lobby | N | Y | Y | Each side |

Y* = stability only if loadbearing. † Insulation may be required when specified (e.g. some lift-door Diagram 2 cases; door aggregate >½ wall area).

Test basis: **BS 476 : Parts 20–24 : 1987**. Non-table products need HOKLAS/BA laboratory test report or BA-recognised assessment.

#### 16.2 Tables A–F — hand to RSE / specifier, not for SD dimensioning

Deemed-to-satisfy minimum thicknesses / covers / protection for **1 / 2 / 4 hour** construction:

| Table | Content |
|---|---|
| **A** | Wholly non-combustible walls (solid brick, RC, hollow clay/concrete blocks) |
| **B** | Walls not wholly non-combustible (wood wool, plasterboard cores, framed + plaster/board) |
| **C** | Floors & landings (RC / prestressed depths & covers) |
| **D** | Steel column/beam solid & hollow protection |
| **E** | RC / prestressed columns & beams (size + cover by exposure) |
| **F** | RC stair waist thickness + cover |

**SD takeaway:** Architect locks **FRP hours** and compartment boundaries; RSE sizes concrete cover / steel protection from A–F (or tested systems). Do not assume 100 mm slab = 1 hr without checking Table C covers.

---

### 17. Schematic design checklist (lock before GA freeze)

1. Assign **Table 2 use class(es)** and forecast **compartment volumes** (esp. retail/warehouse).
2. Decide basement cut: accept **4 hr** united podium vs hard separation at B/G.
3. Map **use separations ≥ 2 hr** at every stack change (domestic / office / retail / carpark / industrial).
4. Size atria / voids with **450 mm × 1 hr** barriers (or BA-accepted smoke strategy).
5. Fix façade: **900 mm** FR spandrel + floor-edge fire stop at curtain wall.
6. Protect stair/lobby external walls within **6 m** of boundaries, streets, other walls/buildings.
7. Plan twin buildings / boundary windows against **1.8 m / 900 mm / 450 mm** rules.
8. Locate basement smoke outlets (area %, 30 m spacing, clear of stair discharge).
9. If bridge/tunnel links: budget **2 hr / 4 hr** shutters, lobbies, and 900 mm blank façade zones.
10. Flag special hazards (DG, plant, kitchens at single-exit flats) for **2–4 hr** boxes.
11. Refuge floors: **2 hr** box + **6 m** open-side clearances; coordinate area/frequency with MOE/FS Code.
12. For **new** projects after 2011, migrate these constraints into **FS Code 2011 Part C** (FRR terminology, updated tables) — do not submit FRC 1996 alone as the current DTC path.

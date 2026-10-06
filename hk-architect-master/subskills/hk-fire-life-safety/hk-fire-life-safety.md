---
name: hk-fire-life-safety
description: Hong Kong fire safety — FS Code 2011, BO Cap.123 Reg.41, FSD/BD approval, means of escape, sprinklers, compartmentation, scissor stairs, smoke control, and existing-building upgrades under Cap. 502, Cap. 572, and Cap. 636.
disable-model-invocation: true
---

# HK Fire Life Safety

Primary codes: Code of Practice for Fire Safety in Buildings 2011 (FS Code) + Buildings Ordinance Cap. 123 Reg. 41. Approving authorities: FSD (fire services installations) + BD (means of escape).

For **Fire strategy and travel distance**, use `hk-fire-life-safety`. For other topics, see the routing table below.

## When to Use This Skill

FS Code 2011, MOE, sprinklers, compartmentation, smoke control — building fire code.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Fire strategy and travel distance | `hk-fire-life-safety` | `—` |
| Construction site safety | `—` | `hk-construction-health-safety` |
| FSI handover / FSD inspection | `—` | `hk-fsd-licensing-compliance` |

## Halt criteria

- FSD/BD approval requires AP and fire consultant — advisory only here.
---

## 1. Means of Escape (BO Reg. 41 + FS Code)

### 1.1 Travel Distance

| Occupancy | Sprinklered | Unsprinklered |
|---|---|---|
| Domestic (residential) | 45 m | 30 m |
| Non-domestic (office/retail) | 60 m | 45 m |
| Assembly / PPE | 30 m | 20 m |
| Industrial | 45 m | 30 m |

### 1.2 Exit Width

| Occupant Load | Min Exit Width |
|---|---|
| ≤ 50 persons | 750 mm |
| 51–200 persons | 1050 mm |
| > 200 persons | 1050 mm + 150 mm per 50 persons above 200 |

### 1.3 Corridor Width

| Use | Min Width |
|---|---|
| Residential common corridor | 1050 mm |
| Non-domestic corridor | 1200 mm |
| Dead-end corridor (sprinklered) | Max 15 m |
| Dead-end corridor (unsprinklered) | Max 6 m |

---

## 2. Staircases

| Parameter | Requirement |
|---|---|
| Min width | 1050 mm (residential); 1200 mm (non-domestic) |
| Max riser | 175 mm |
| Min going | 250 mm |
| Handrail height | 900–1000 mm |
| Fire resistance | 2 hr (>25 storeys); 1 hr (others) |
| Pressurisation | Required for buildings > 30 m height |
| Scissor stairs | Accepted by FSD for HK high-rise residential; each flight must be a separate fire compartment |

---

## 3. Sprinkler Requirements

| Building Type | Threshold |
|---|---|
| Domestic (residential) | > 13 storeys or > 40 m height |
| Non-domestic | > 230 m² per floor or > 3 storeys |
| Composite building | Per most stringent applicable use |
| Basement | All basements used for occupation |

---

## 4. Fire Compartmentation

| Element | Fire Resistance |
|---|---|
| Compartment wall/floor (high-rise > 25 storeys) | 2 hr |
| Compartment wall/floor (others) | 1 hr |
| Staircase enclosure door | FD60 (1 hr) min |
| Lift lobby door | FD30 (30 min) |
| Service penetrations | Intumescent seals; maintain compartment rating |

---

## 5. Fire Services Installations (FSD)

| Installation | Requirement |
|---|---|
| Hose reel | Max 30 m coverage radius; all buildings > 230 m²/floor |
| Hydrant | Within 90 m of any point on site; FSD confirms coverage |
| Sprinkler | Per Section 3 thresholds |
| Fire alarm | All buildings; addressable system for > 5 storeys |
| Smoke extraction | Required for basements, atriums, and enclosed car parks |
| Emergency lighting | All escape routes; min 1 lux at floor level |

---

## 6. HK-Specific Anti-Patterns

| Anti-Pattern | Failure Mode | Fix |
|---|---|---|
| **Scissor stair without compartment separation** | FSD rejects: each scissor flight must be a separate fire compartment with FD60 door | Design scissor stairs with full compartment wall between flights from ground to roof |
| **Travel distance measured incorrectly** | Measured in straight line, not along actual path; BD/FSD rejects | Measure along actual walking route; include all direction changes |
| **Composite building with single fire strategy** | Residential and commercial portions require separate MOE strategies | Separate compartments, separate staircases, separate FSD submissions for each use |
| **Pressurisation omitted for >30 m building** | FSD requires staircase pressurisation; omission causes rejection | Include pressurisation system in M&E brief from concept stage |

---

## 7. Existing-stock fire upgrade ordinances

These statutes force retrofit of existing buildings. They do not replace the FS Code for a new Buildings Ordinance submission.

| Ordinance | What it hits | What it is not |
|---|---|---|
| **Cap. 502** Fire Safety (Commercial Premises) | Prescribed commercial premises: Schedule 1 uses with total floor area **over 230 m²**, in a building of any age; and specified commercial buildings whose plans were first submitted, or which were built without such plans, **on or before 1 March 1987** | Not the FS Code. Not Cap. 572. Upgrade standards are the **1994–96** codes locked in the Schedules |
| **Cap. 572** Fire Safety (Buildings) | Pre–1 March 1987 **composite and domestic** buildings. Owners (and some occupiers) retrofit fire service installations and passive construction to Schedules 1–3 | Does not approve a new building. An open direction is a title, programme, occupation, and financing constraint |
| **Cap. 636** Fire Safety (Industrial Buildings) | The **whole** of a pre–1 March 1987 industrial building, judged on original industrial construction intent and age, including vacant floors | Does not apply if Cap. 502 or Cap. 572 already applies to the **whole** building. Schedule-locked to the **2011 / 2012 / 2015** standards named in the Ordinance, not “whatever the current FS Code PDF says today” |

Schedule 1 uses that can be prescribed commercial premises under Cap. 502 are only: banking (not merchant banking), off-course betting, jewelry or goldsmith with a security area, supermarket / hypermarket / department store, and shopping arcade. An ordinary office, restaurant, or small shop is not prescribed commercial premises unless it is one of those five and clears the area test. For an arcade, sum all shops and the passageways between them. Include basements, balconies, and wall thickness; disregard a floor used only for parking or only for lift, escalator, or air-conditioning machinery.

Cap. 502 and a specified commercial building can stack on the same building. A building used exclusively as a hotel, school, hospital, car park, elderly or disability home, factory, godown, utility, or cinema is outside the “commercial building” definition, as is a building partly domestic or industrial.

### 7.1 Certification and Cap. 572 installation paths

| Path | Practice point from the FSD circular |
|---|---|
| Cap. 572 fire service drawings | Certify on **FSI/314C** to the sprinkler rules and the Minimum Fire Service Installations code named on that form |
| Cap. 636 upgrades | Use **FSI/314D**, not FSI/314B or FSI/314C, and route through the Buildings Department industrial-building unit named in the circular |
| Cap. 502 / 572 / 636 completion | From 1 January 2025, acceptance uses **BI/RC (Rev. 2024)** (Part B signed by the owner or occupier) and **BI/RC/a** (registered fire service installation contractor certificate under Cap. 95B regulation 9). FS251 is not required for these three ordinances. Issue BI/RC/a within 14 days of completion |
| Low-rise composite podium without tank space | Direct-feed hose reel may be proposed; coordinate Water Supplies Department backflow prevention and the hydraulic calculation at schematic stage |
| Low-rise hose-reel tank | Size from response time. Confirm built-up versus dispersed risk with FSD before allocating plant volume. **500 L** is the stated minimum for dispersed or isolated zones |
| Tall-building hose-reel tank | Volume may be halved to **4,500 L** where an emergency vehicular access and a nearby hydrant are accepted, or a fresh-water incorporation path may be pursued |
| Mid-rise | A no-tank pump-from-mains path exists. Budget backflow prevention, pressure-reducing valves, hydraulic calculations, and duplicated power. Fresh-water incorporation remains the preferred tall-building alternative to the 9,000 L / 4,500 L tanks |
| Low-rise without hose-reel or fire-alarm space | An Internet-of-things fire detection system plus portable extinguishers may be pursued. Sprinklers and automatic cut-off devices still apply where the direction requires them |

Improvised sprinklers need fire-alarm linkage. Relaxations are case-by-case, not automatic. Structural or technology excuses must be engineered; they are not assumed.

---

*Sources: Code of Practice for Fire Safety in Buildings 2011 (BD/FSD), Buildings Ordinance Cap. 123 Reg. 41, PNAP APP-130, Fire Safety (Commercial Premises) Ordinance Cap. 502 (13 December 2024), Fire Safety (Buildings) Ordinance Cap. 572 (13 December 2024), Fire Safety (Industrial Buildings) Ordinance Cap. 636 (10 September 2020), FSD Circular Letters 2/2007, 3/2007, 2/2016, 5/2016, 3/2017, 7/2020, 4/2023, 5/2024, and 3/2026.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-fire-life-safety.md`, `references/catalogues/fsd-circulars.md`. The master router links these files directly.

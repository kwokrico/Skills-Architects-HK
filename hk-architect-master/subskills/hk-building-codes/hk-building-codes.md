---
name: hk-building-codes
description: Hong Kong Buildings Ordinance Cap. 123, BO Regulations, PNAP letters, GFA/plot ratio calculations, means of escape, fire safety code, and barrier-free access requirements.
disable-model-invocation: true
---

# HK Building Codes

Covers Buildings Ordinance Cap. 123, key Regulations, PNAP administrative guidelines, GFA/PR calculations, means of escape, fire safety, and barrier-free access.

For **GFA exemptions APP-2**, use `hk-building-codes`. For other topics, see the routing table below.

## When to Use This Skill

BO Cap. 123, PNAP, GFA/plot ratio, MOE quick rules, and statutory development parameters.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| GFA exemptions APP-2, PR, site coverage | `hk-building-codes` | `—` |
| MWCS Class I–III items | `—` | `hk-minor-works` |
| Full fire engineering strategy | `—` | `hk-fire-life-safety` |
| OZP zoning and s.16 | `—` | `hk-spatial-planning` |

## Halt criteria

- Halt if OZP Notes or lease GFA cap unknown for compliance conclusion.
---

## 1. Buildings Ordinance Cap. 123 — Key Provisions

| Regulation | Subject | Key Requirement |
|---|---|---|
| Reg. 30 | Lighting & ventilation (domestic) | Min window area = 1/10 floor area; min headroom 2.5 m |
| Reg. 30A | Lighting & ventilation (non-domestic) | Min window area = 1/10 floor area; min headroom 3.0 m |
| Reg. 41 | Means of escape | Travel distance, exit widths, dead-end corridors |
| Reg. 46 | Car parking headroom | Min 2.0 m clear (2.3 m practical) |
| Reg. 72 | Projections over streets | Max 1.5 m canopy; no projection below 3.5 m AFL |
| Reg. 23 | Site coverage | Per OZP / HKPSG; measured at ground level |
| Reg. 20 | Plot ratio | Domestic + non-domestic PR per OZP annotation |

---

## 2. GFA Calculation (BO Definition)

**Gross Floor Area** = sum of area of each floor measured to outer face of external walls, including:
- All enclosed floor space
- Staircases, lift shafts, plant rooms (unless exempt)
- Covered car parks (unless exempt under PNAP APP-2)

### 2.1 Key GFA Exemptions (PNAP APP-2)

| Item | Exemption Limit | Conditions |
|---|---|---|
| Balcony | ≤ 2 m depth; aggregate ≤ 1/2 of unit facade width | Open on ≥ 1 long side; aggregate cap per building |
| Bay window | ≤ 0.5 m projection; ≤ 50% of facade width per floor | Non-habitable; open on ≥ 1 side |
| Utility platform | ≤ 1.5 m × 2.0 m per unit | Kitchen/laundry only |
| Covered public walkway | Full exemption if publicly accessible 24/7 | Per PNAP APP-2 conditions |
| Plant room / lift overrun | Full exemption | Must not breach BHR |
| Caretaker unit | ≤ 35 m² per building | One per building |
| Refuse chamber | Full exemption | Per EPD/BD standards |

### 2.2 Plot Ratio Calculation

```
Permissible GFA = Site Area × Plot Ratio (from OZP)
Domestic GFA + Non-domestic GFA ≤ Permissible GFA
(Domestic and non-domestic PRs are separate caps where both apply)
```

- Verify OZP annotation for site-specific PR; HKPSG values are defaults
- PR measured on GFA basis (post-exemptions do not reduce PR count unless explicitly stated)
- Bonus PR possible for: public transport interchange, public open space dedication (per OZP)

---

## 3. Means of Escape (BO Reg. 41 + FS Code 2011)

### 3.1 Travel Distance

| Occupancy | Max Travel Distance (sprinklered) | Max Travel Distance (unsprinklered) |
|---|---|---|
| Domestic (residential) | 45 m | 30 m |
| Non-domestic (office/retail) | 60 m | 45 m |
| Assembly / place of public entertainment | 30 m | 20 m |

### 3.2 Exit Width

| Occupancy Load | Min Exit Width |
|---|---|
| ≤ 50 persons | 750 mm |
| 51–200 persons | 1050 mm |
| > 200 persons | 1050 mm + 150 mm per 50 persons above 200 |

### 3.3 Dead-End Corridors

- Max 6 m (unsprinklered); 15 m (sprinklered) — measured from last exit door to dead end
- Corridor width: min 1050 mm (residential common); 1200 mm (non-domestic)

### 3.4 Staircase Requirements

| Parameter | Requirement |
|---|---|
| Min width | 1050 mm (residential); 1200 mm (non-domestic) |
| Max riser | 175 mm |
| Min going | 250 mm |
| Handrail height | 900 mm (min) – 1000 mm (max) |
| Fire resistance | 2 hr (high-rise > 25 storeys); 1 hr (others) |
| Pressurisation | Required for buildings > 30 m height |

---

## 4. Fire Safety (Code of Practice for Fire Safety in Buildings 2011)

### 4.1 Sprinkler Requirements

| Building Type | Threshold |
|---|---|
| Domestic (residential) | Required if > 13 storeys or > 40 m height |
| Non-domestic | Required if > 230 m² per floor or > 3 storeys |
| Composite building | Per most stringent applicable use |

### 4.2 Fire Compartmentation

| Element | Fire Resistance Rating |
|---|---|
| Compartment wall / floor | 2 hr (high-rise); 1 hr (low-rise) |
| Fire door (staircase enclosure) | FD60 (1 hr) minimum |
| Service penetrations | Intumescent seals; maintain compartment rating |

### 4.3 Hose Reel & Hydrant

- Hose reel: max 30 m coverage radius; required in all buildings > 230 m² per floor
- Hydrant: within 90 m of any point on site; FSD to confirm coverage

---

## 5. Barrier-Free Access (Design Manual: Barrier Free Access 2008)

| Element | Requirement |
|---|---|
| Entrance threshold | ≤ 13 mm |
| Ramp gradient | 1:12 max; 1:20 preferred; max rise 500 mm per flight |
| Ramp width | Min 1200 mm clear |
| Lift car | Min 1100 mm (W) × 1400 mm (D) |
| Accessible WC | 1500 mm turning circle; grab rails per DMBA Fig. |
| Tactile guide path | Required at public entrances and circulation |
| Parking (accessible) | Min 1 per 50 spaces; 3300 mm wide stall |

---

## 6. PNAP Reference Index

| PNAP | Subject |
|---|---|
| APP-2 | Gross floor area and non-accountable gross floor area |
| APP-40 | Sustainable building design guidelines (setback, greenery) |
| APP-41 | Barrier-free access (Design Manual: Barrier Free Access 2008) |
| APP-130 | Lighting and ventilation — performance-based approach (operative rule in hk-daylighting-design) |
| APP-152 | Sustainable Building Design Guidelines |
| ADV-36 | Amenity features (balconies, utility platforms) |
| ADV-49 | Green and innovative buildings |

---

## 7. Cap. 123 family an architect actually opens

| Instrument | What it controls |
|---|---|
| Cap. 123 | Parent ordinance, including approval, consent, orders, and the MBIS/MWIS notice powers in ss.30B–30E |
| Cap. 123A | Administration, forms, and plan processing |
| Cap. 123F | Planning regulations: plot ratio, site coverage, projections, lighting and ventilation, means of escape hooks |
| Cap. 123G | Private streets, cul-de-sacs, access roads, pedestrian ways, and service lanes. Not public-road standards and not Cap. 123F intensity |
| Cap. 123H | Refuse and material-recovery chambers and chutes — `hk-building-services` |
| Cap. 123I | Sanitary fitments, plumbing, drainage works, and latrines |
| Cap. 123J | Ventilating systems |
| Cap. 123K | Oil storage installations, with the 1992 oil-storage code |
| Cap. 123L | Appeals |
| Cap. 123M | Statutory OTTV hook for commercial buildings and hotels — numbers in APP-67, see `hk-building-sustainability` |
| Cap. 123N / 123O | Minor works, and the fees regulation |
| Cap. 123P | Mandatory building and window inspection — `hk-mandatory-inspection` |
| Cap. 123Q | Operative construction-performance regulation. It replaced repealed Cap. 123B. It is performance-based; hard numbers live in codes accepted under PNAP APP-53 |
| Cap. 123C | Demolition works |
| Cap. 123D / 123E | Older lift and escalator building regulations, kept as repealed texts. Live control is Cap. 618 |

Cap. 123B is repealed. Do not cite it as the current construction regulation.

### 7.1 Private streets (Cap. 123G) — schematic locks

Measure a dead-end along the carriageway centre line from the thoroughfare junction, not along the lot boundary. Keep dead-ends at or under **120 m**, or budget private-street widths from the start. Reduced access roads are for small low-rise clusters. Estate spines generally need the default **5.0 m** carriageway plus at least one **1.6 m** footpath. A pedestrian way must keep **3.5 m** clear after bollards and other protection. Phased estates must show a continuous street chain from day-one occupation.

### 7.2 New Territories application (Cap. 121)

Cap. 121 applies Cap. 123 to the New Territories (excluding New Kowloon), then allows a Lands Department certificate of exemption that switches off named Cap. 123 controls only if the finished building stays inside the Schedule dimensional envelopes and the certificate conditions are met. Building exemption is not automatic site-formation or drainage exemption. Three certificates may be needed (building, site formation, and drainage). Joint Practice Notes 4, 5, and 7 do not apply to Cap. 121 exempted buildings.

## 8. Joint Practice Notes 1 to 9

Optional or streamlining notes. They are not a grant of planning permission, lease modification, or Buildings Ordinance approval.

| Note | Architect lock |
|---|---|
| JPN 1 | Optional GFA and site-coverage exemptions for listed green features on new projects that do not yet have an occupation permit. Hotels and non-domestic portions of composite buildings are not “residential”. All concessions sit under PNAP APP-151. Budget the APP-151 cap before stacking balcony, corridor, and sky garden. A sky-garden void connected to a residents’ recreational facility can sit outside that cap on tall residential |
| JPN 2 | Second incentive package. Modular integrated construction was removed in July 2022; use JPN 8. Hotels have no utility-platform concession. Utility-platform re-entrant limit is **1,500 mm** (a balcony’s limit is 2,300 mm). Prefabricated external wall of 150 mm and a utility platform of 0.75 m² both sit under the APP-151 overall cap |
| JPN 3 | Who processes the landscape submission, as against site coverage of greenery under APP-152. The Buildings Ordinance gives the Building Authority no power to impose landscape. Protect ground-level planting, podium gardens, and tree zones on the landscape layout plan |
| JPN 4 | Aligns maximum plot ratio and GFA, accountability, and checking across Buildings Department, Lands Department, and Planning Department. Applies to new general building plans or major revisions submitted on or after **18 October 2021**. Not for Cap. 121 exempted buildings |
| JPN 5 | Building-height restriction as a statutory-plan parameter (Planning Department lead). Does not change the Building Authority’s interpretation of building height for intensity or fire safety. Applies to new general building plans or major revisions on or after **15 May 2019**. Not for Cap. 121 exempted buildings |
| JPN 6 | Checking of building separation and building setback. The dimensions are in PNAP APP-152. Site coverage of greenery is JPN 3 |
| JPN 7 | Site-coverage restriction across the Buildings Ordinance, the outline zoning plan, and the lease. Not for Cap. 121 exempted buildings. Read with Lands Administration Office Practice Note 3/2020A where the lease contains a maximum GFA or plot ratio |
| JPN 8 | Modular integrated construction — `hk-mic-dfma` |
| JPN 9 | Bonus plot ratio pilot for private redevelopment in seven old districts named in the 2025 Policy Address. Administrative only. Freeze the path first: if “Flat” is not always permitted, section 16 permission has to exist before the lease-modification file, and the letter must still be executed inside three years. Test **700 m²** and the bonus base as two different areas. Government land, non-building area, and pre-pilot demolition or sale drop out of the 20% even when they help the size test; a retained graded historic building stays in both. Bonus GFA is 0.2 times the plan maximum (or the “R(A)” / over-61 m First Schedule fallback) on the bonus base only, never on a higher existing-building plot ratio. Encashment is a 10-year premium credit, not extra floor area. Do not stack this 20% on a receiving site under a transfer-of-plot-ratio cap without checking that scheme’s maximum GFA |

---

*Sources: Buildings Ordinance Cap. 123 (consolidated 1 March 2026) and Cap. 123A–123Q, Cap. 121 (2 August 2012), Joint Practice Notes Nos. 1–9, PNAP APP-2, APP-40, APP-67, APP-130, APP-151, APP-152, Code of Practice for Fire Safety in Buildings 2011, Design Manual: Barrier Free Access 2008, HKPSG.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-building-codes.md`, `references/catalogues/pnap-index.md`. The master router links these files directly.

---
name: hk-building-services
description: HK building services — BEAM Plus IEQ/EU, CoP EE 2021 HVAC, HK Wiring Regulations (220V/50Hz), WSD/DSD drainage, EPD air/water compliance, FSD fire services coordination.
disable-model-invocation: true
---

# HK Building Services

Key authorities: EMSD (electrical/energy), WSD (water supply), DSD (drainage), EPD (environment), FSD (fire services). Primary codes: CoP EE 2021, HK Wiring Regulations, WSD Waterworks Regulations, DSD Stormwater Drainage Manual.

For **MEP systems and BD/FSD interfaces**, use `hk-building-services`. For other topics, see the routing table below.

## When to Use This Skill

HVAC, plumbing, drainage, electrical, and FSD installation coordination.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| MEP systems and BD/FSD interfaces | `hk-building-services` | `—` |
| FSI testing and Fire Certificate | `—` | `hk-fsd-licensing-compliance` |
| Fire compartmentation / MOE | `—` | `hk-fire-life-safety` |
---

## 1. HVAC (CoP EE 2021 + BEAM Plus)

| Parameter | Requirement |
|---|---|
| Chiller COP | ≥ 5.0 (BEAM Plus EU credit); ≥ 4.0 (BEC baseline) |
| Ventilation rate | BEAM Plus IEQ: ≥ 10 L/s/person (office); ≥ 8 L/s/person (retail) |
| HVAC zoning | Min 4 perimeter zones (N/E/S/W) + interior zone per floor |
| Ceiling void (office) | 600–750 mm for duct distribution |
| Ceiling void (residential) | 300–400 mm |
| Cooling load (CZ 1A) | Design for 33°C DB / 28°C WB outdoor; 24°C / 50% RH indoor |

---

## 2. Electrical (HK Wiring Regulations)

| Parameter | HK Standard |
|---|---|
| Supply voltage | 220V single-phase / 380V three-phase, 50 Hz |
| Supply authority | CLP (Kowloon/NT) or HKE (HK Island/Lamma) |
| Wiring regulations | IEE Wiring Regulations as adopted by EMSD |
| Metering | Separate meters per unit (residential); sub-metering for BEAM Plus EU credit |
| Emergency power | Diesel generator or UPS for essential services; FSD requires for fire services |

---

## 3. Plumbing & Water Supply (WSD)

| Aspect | Requirement |
|---|---|
| Water supply pressure | WSD mains typically 2.5–4.0 bar; booster pumps for high-rise |
| Water efficiency | WSD Water Efficiency Labelling Scheme (WELS); BEAM Plus WU credit |
| Low-flow fixtures | ≤ 6 L/flush (WC); ≤ 8 L/min (shower) for BEAM Plus WU |
| Rainwater harvesting | BEAM Plus WU credit; for irrigation and toilet flushing |
| Greywater recycling | BEAM Plus WU credit; EPD approval required |

---

## 4. Drainage (DSD Standards)

| Aspect | Requirement |
|---|---|
| Stormwater/foul separation | Mandatory; separate systems to street drains and sewers |
| Stormwater design | DSD Stormwater Drainage Manual; 200-yr return period for major drains |
| Foul drainage | Connect to public sewer; EPD approval for trade effluent |
| Grease trap | Required for all F&B kitchens; FEHD and DSD requirements |
| Roof drainage | Primary + secondary overflow; min 1:60 fall |

---

## 5. FSD Coordination (Fire Services Installations)

| Installation | FSD Requirement |
|---|---|
| Sprinkler system | FSD approval; separate submission from BD MOE |
| Hose reel | FSD approval; 30 m coverage radius |
| Fire alarm | FSD approval; addressable system for > 5 storeys |
| Smoke extraction | FSD approval for basements, atriums, car parks |

**Construction sequencing:** **First fix** (套管預埋) runs inside every standard floor cycle before concrete pour (lanes 3 and 4); **second fix** and system testing follow in MEP phasing (lane 6). Keep FSD submission separate from BD MOE. Load `hk-construction-programme` for embed and sectional MEP sequencing.

---
| Emergency generator | FSD requires for fire services power supply |

---

## 6. EPD Compliance

| Aspect | Ordinance |
|---|---|
| Boilers / generators | Air Pollution Control Ordinance Cap. 311; EPD approval for fuel-burning equipment |
| Cooling towers | Legionella control; WSD/EPD guidelines |
| Noise from plant | Noise Control Ordinance Cap. 400; plant room attenuation required |
| Trade effluent | Water Pollution Control Ordinance Cap. 358; EPD licence for discharge |

---

## 7. Lifts and escalators (Cap. 618)

Shaft, pit, and machine-room dimensions are not numbered in the Ordinance. Lock them to the current safety code of practice issued under section 145, and keep the use-permit duties on top of that code. Building works for lifts and escalators are also in the BD code of practice (2011, 2020 edition).

| Point | Rule |
|---|---|
| What is a lift | A passenger lift, a larger goods lift, and a mechanized car-parking system are lifts and need the use-permit path. A service lift is inside Cap. 618 only while it stays at or below 250 kg, 1 m², and 1.2 m |
| Travel | A goods or vehicle lift that travels more than 3.5 m, or that passes through a floor, is inside Cap. 618 even if it never carries passengers |
| No passengers | Goods lifts, service lifts, and mechanized parking systems are the Schedule 4 list. Passenger travel in them is prohibited |
| Permit display | Conspicuous in-car position on every passenger lift. A goods lift, service lift, or mechanized parking system has the permit at the main landing, not in the car |
| Major alteration | Changing travel, rated load, rated speed, control type, guide-rail size, door interlocks, or the driving machine stops normal use until a resumption permit is issued |
| Repealed building regulations | Cap. 123D (escalators) and Cap. 123E (lifts) are the older building regulations. Live lift and escalator safety control is Cap. 618 |

Energy efficiency of lift and escalator installations is a Cap. 610 installation, not a Cap. 618 dimension.

## 8. Electricity and gas (space-planning gates)

**Cap. 406** regulates who may do electrical work and when a supply may be connected. It does not set switchroom clearances or bathroom zones; those sit in the wiring regulations (Cap. 406E) and the wiring code. Draw the fixed installation only up to the socket. Name a registered electrical contractor. A standby generator or photovoltaic system that supplies only the owner's own installation is not registered under section 21, but it must be maintained in continuous safe working order and is still a fixed installation under Cap. 406E. Allow time for the supplier's safety inspection before energising.

**Cap. 51** regulates town gas, liquefied petroleum gas, natural gas, and mixtures. Cylinder storage whose aggregated nominal water capacity is more than **130 litres** is a store. A vessel of more than **150 litres** water capacity is bulk liquefied petroleum gas. An LPG store, including the pipework that leaves it, is a notifiable gas installation, as is a pressure-regulating installation of **30 standard cubic metres per hour** or more fed from intermediate or high pressure. Approved gas codes are the practical test of the regulations they support.

## 9. Water supply (Cap. 102 and Cap. 102A)

Draw the fire service and the inside service as separate systems. The consumer's pipe stops at the connexion: the control valve nearest the main, and everything between that valve and the main, is part of the main. A shared riser is a communal service and cannot be connected until there is an approved consumer and an approved agent. An unapproved installation or alteration, or a layout in which waste or pollution of the supply is likely, is a ground for a repair notice and for disconnection of both the fire service and the inside service. New construction and any alteration that could affect a reliable and adequate supply, or water quality, needs written Water Authority permission and a designated person. On leased land, confirm against the section 23 map in the Land Registry whether the lot is a gathering ground before freezing site drainage. Use a fire service only for fire fighting.

## 10. Refuse chambers (Cap. 123H)

Cap. 123H sizes refuse storage and material recovery chambers, vehicular-access triggers, floor-by-floor recovery rooms, and refuse-chute geometry. A single-staircase building, a single-family building, or a site of 500 m² or less is the early exemption path. A multi-stair domestic tower needs a refuse storage and material recovery room on every typical floor from the first core diagram. The chamber door must be in an outer wall. Reserve a vertical exhaust duct and roof terminal. A hopper lobby on a typical floor needs a permanent open-air ventilation strategy; do not place hoppers in a pressurised or fully enclosed air-conditioned common area without that open-air solution.

---

*Sources: CoP EE 2021 (EMSD), Electricity Ordinance Cap. 406 and Cap. 406E, Gas Safety Ordinance Cap. 51 and Cap. 51B / 51C, Lifts and Escalators Ordinance Cap. 618, Code of Practice for Lift Works and Escalator Works (2021 Edition), Code of Practice for Building Works for Lifts and Escalators 2011 (2020 Edition), Waterworks Ordinance Cap. 102 and Cap. 102A, Building (Refuse Storage and Material Recovery Chambers and Refuse Chutes) Regulations Cap. 123H, Noise Control Ordinance Cap. 400, Air Pollution Control Ordinance Cap. 311.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-building-services.md`. The master router links these files directly.

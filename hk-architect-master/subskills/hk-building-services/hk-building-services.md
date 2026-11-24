---
name: hk-building-services
description: HK building services — BEAM Plus IEQ/EU, CoP EE 2021 HVAC, HK Wiring Regulations (220V/50Hz), WSD/DSD drainage, EPD air/water compliance, FSD fire services coordination.
disable-model-invocation: true
---

# HK Building Services

For **Cap. 56 pressure equipment, Cap. 303 radiation apparatus or Cap. 446 main watercourses**, read [specialist plant and drainage](../../references/hk-specialist-plant-drainage.md) before fixing plant rooms or drainage layouts. For **Caps. 311/311A air and fuel-burning plant, 358 discharge and 403 refrigerants**, read the relevant section of [environmental site controls](../../references/hk-environmental-site-controls.md), which links the integrated statutory summaries. These approvals are separate from ordinary services coordination. For fuel/chemical inventories also check [Cap. 295 dangerous goods](../../references/hk-dangerous-goods-controls.md).

Key authorities: EMSD (electrical/energy), WSD (water supply), DSD (drainage), EPD (environment), FSD (fire services). Primary codes: CoP EE 2021, HK Wiring Regulations, WSD Waterworks Regulations, DSD Stormwater Drainage Manual.

For **MEP systems and BD/FSD interfaces**, use `hk-building-services`. For other topics, see the routing table below.

## When to Use This Skill

Use section 13 for FM requirements and architectural operational handoffs; technical operations, commissioning and maintenance procedures go to **Skills-MEP-Engineer-HK**.

**Role boundary:** Refer MEP calculations, equipment sizing, FSI engineering and control-sequence design to **Skills-MEP-Engineer-HK**. Keep spatial requirements, design interfaces and evidence requests here. Apply the [master referral rule](../../SKILL.md#specialist-role-referrals); state the referral and do not supply the specialist answer from local background tables.

Use section 12 for smart-building/BMS coordination briefs, control interfaces and acceptance planning. Controls design remains with the appointed specialists.

HVAC, plumbing, drainage, electrical, and FSD installation coordination.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| MEP systems and BD/FSD interfaces | `hk-building-services` | `—` |
| FSI testing and Fire Certificate | `—` | `hk-fsd-licensing-compliance` |
| Fire compartmentation / MOE | `—` | `hk-fire-life-safety` |
| Utility reserves and district cooling in a new development area | `—` | HKPSG Chapter 7, via [hkpsg](../../references/catalogues/hkpsg.md). Do not treat that chapter as a building-services code |
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

## 11. Inputs to an integrated indoor-environment review

Coordinate through the [integrated indoor-environment brief](../hk-building-sustainability/hk-building-sustainability.md#6-integrated-indoor-environment-and-occupant-comfort-brief). The architect sets spatial and interface requirements; the appointed MEP engineer establishes system sizing, ventilation, thermal/moisture control and testing criteria.

**Request:** uses/occupancy/hours, outside-air and exhaust arrangements, nearby pollution sources, opening modes, plant condition/capacity, maintenance records and client/FM control preferences. Missing existing-system records trigger investigation, not assumed capacity.

Review source control, intake/exhaust interfaces, distribution, cooling/dehumidification, condensation, plant noise and maintenance access. Compare simultaneous modes: opening a facade while cooling runs changes the assessment; a quiet sealed room still needs reviewed ventilation. Coordinate transfer paths/attenuators, ceiling space and maintenance with the architect and specialists.

**Return:** assumptions; criteria/source; calculations/investigations needed; space/power/drainage/access implications; controls/user instructions; commissioning checks under stated conditions; unresolved interfaces/owners. Sensor readings, equipment labels or occupant anecdotes alone do not establish overall IAQ or thermal performance.

## 12. Smart-building coordination brief

Use for new buildings or occupied-building upgrades in Hong Kong. Start with the [user and operational brief](../hk-building-programming/hk-building-programming.md#6-smart-building-user-and-operational-brief). The architect coordinates spaces, device locations and user interfaces; MEP/controls/ICT/security specialists design systems, sequences and integration. A dashboard or installed sensor does not establish energy savings, IAQ performance or successful commissioning.

**Inputs:** agreed user journeys, occupancy/hours, asset/system inventory, existing BMS/network capabilities, system ownership, integration permissions, client/FM operational needs, maintenance arrangements, commissioning scope and applicable safety/security constraints. In occupied premises establish access, outage limits and fallback arrangements before any proposed change.

1. Translate each user outcome into an interface: sensing, display/action, responsible system, operator override, abnormal behaviour and verification. Avoid collecting occupancy/personal data without an identified need and client/ICT privacy review.
2. Map points/protocols and system boundaries with specialists; identify unavailable interfaces or proprietary dependencies. Reserve device, panel, cabling, power, cooling and maintenance space with the architect.
3. Have specialists establish control sequences, calibration, permissions, network segregation and recovery procedures. Record conflicting commands and priority rules. Life-safety functions require their own competent design/approval process; a convenience controller must not bypass them.
4. Coordinate installation, access, occupant communications, outages and rollback for refurbishment. This skill does not authorise remote live-system changes or automated commands.
5. Agree witnessed tests for normal, peak/unoccupied and fault modes, including sensor/communications/power loss and manual override where relevant. Set project-specific acceptance criteria and evidence; do not infer success from a green screen icon.
6. Review results with client/FM and specialists; resolve defects, hand over configuration/version records, training, maintenance and access ownership. Keep outstanding functions excluded from acceptance and promised savings conditional on measured evidence.

| Interface | Architect's role | Specialist/owner | Verification evidence |
|---|---|---|---|
| Occupancy-controlled comfort/lighting | Rooms, zones, user controls and accessible device locations | MEP/controls with client/FM | Agreed operating scenarios, calibration and functional tests |
| Access/security and door systems | Door hardware, circulation and user journey | Security/ICT plus fire/accessibility reviewers | Reviewed interfaces, emergency/override behaviour and witnessed tests |
| Metering and monitoring | Plant/device space and service access | MEP/metering and FM | Point identity, units, timestamps, plausible trends and verified meter mapping |
| Data/network handover | Coordinate requirements and physical interfaces | Client ICT/privacy lead and system integrator | Permissions, integration limitations, configuration and recovery documentation |

**Decision record:** use-case ID; room/system; outcome; inputs/outputs; responsible owner; interface and version; normal/fault mode; test/criterion; evidence; unresolved issue; acceptance status. Refer comfort/air-quality effects to the existing integrated IEQ workflow.

**Hypothetical case:** a tenant proposes occupancy sensors to switch off cooling in meeting rooms. Confirm ventilation and humidity needs, after-hours use, overrides and loss-of-sensor behaviour with MEP/FM. Do not approve a simple “vacant = off” rule or claim savings from the vendor brochure. Return a reviewed sequence/test brief and unresolved integration questions.

**HK reference:** [EMSD Technical Guidelines on Retro-commissioning, 2023](https://www.emsd.gov.hk/filemanager/en/content_718/Technical_Guidelines_Retro-commissioning.pdf), section 5, discusses measurement/monitoring and access provisions supporting later RCx. This is context for verification and maintainability, not a universal smart-building certification requirement. Source reviewed 24 November 2026.

## 13. FM design review and operational handoff

Retain architectural plant-space, access and user-interface coordination. Refer technical maintenance procedures, isolation, commissioning, fault diagnosis and controls to **Skills-MEP-Engineer-HK**. Refer support/load issues to **Skills-Structural-Engineer-HK** and asset-model/data configuration to **Skills-BIM Manager-HK**. Apply the [master referral rule](../../SKILL.md#specialist-role-referrals); do not issue a specialist procedure followed by a disclaimer.

**Inputs:** FM requirements, reviewed systems/asset list, current drawings, specialist access/replacement envelopes, operating modes, O&M and commissioning evidence, warranty/service responsibilities and occupied-area/outage constraints.

At design review, compare plant/panel locations and access routes against specialist requirements, including removable components and access for inspection. Identify architectural changes needed before ceilings, doors or enclosures are fixed. Ask MEP/FM to establish service clearances, isolation arrangements, replacement needs and operator training rather than choosing them here.

At handover, check that records describe the installed system and its actual identifiers, controls and access. Ask competent specialists to demonstrate the agreed operating/fault scenarios and training; the architect records attendance, evidence and unresolved architectural interfaces without directing live plant. Do not change settings, switchgear or safety functions through this workflow.

**Handoff record:** asset/zone; as-built reference; specialist requirement; access provision; O&M/test/training evidence; authorised operator/contact; open limitation; owner/due date; status. Link to [operational readiness](../hk-practical-completion-snagging/hk-practical-completion-snagging.md#11-operational-readiness-and-aftercare-handoff) and the existing smart-building record, avoiding duplicate contradictory statuses.

**HK context:** [EMSD O&M best-practice resources](https://bestpractice.emsd.gov.hk/en/) provide discipline-specific material for competent teams. Checked 24 November 2026. They do not establish that every recommendation is a statutory obligation or transfer MEP duties to the architect.

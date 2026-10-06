---
name: hk-spatial-planning
description: Hong Kong spatial planning — OZP zoning, HKPSG standards, planning applications (s.16/s.12A), air ventilation assessment, urban design guidelines, and development control.
disable-model-invocation: true
---

# HK Spatial Planning

Covers Outline Zoning Plans, HKPSG, planning applications, AVA, and urban design development control.

For **Planning application / zoning**, use `hk-spatial-planning`. For other topics, see the routing table below.

## When to Use This Skill

OZP, s.16/s.12A, TPB, AVA, HKPSG development control.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Planning application / zoning | `hk-spatial-planning` | `—` |
| BO GFA after planning permission | `—` | `hk-building-codes` |
| Lands lease modifications | `—` | `hk-lease-compliance` |

## Halt criteria

- Halt if OZP for site unknown — do not assume zone defaults.
---

## 1. Statutory Planning Framework

| Instrument | Authority | Purpose |
|---|---|---|
| Outline Zoning Plan (OZP) | Town Planning Board (TPB) | Zoning, PR, site coverage, BHR, special restrictions |
| Development Permission Area (DPA) Plan | TPB | Rural NT areas; interim control |
| Outline Development Plan (ODP) | PlanD | Non-statutory; new development areas |
| Layout Plan | PlanD | Detailed land use within development areas |

---

## 2. OZP Zones & Default Development Parameters

| Zone | Typical Use | Default Domestic PR | Default Non-Domestic PR |
|---|---|---|---|
| R(A) | High-density residential | 5.0 | — |
| R(B) | Medium-density residential | 3.0 | — |
| R(C) | Low-density residential | 1.0 | — |
| C(1) | High-density commercial | — | 9.5 |
| C(2) | Medium-density commercial | — | 6.5 |
| OU (annotated) | Mixed/special uses | Per OZP annotation | Per OZP annotation |
| G/IC | Government, institution, community | Per schedule | Per schedule |
| O | Open space | — | — |
| V | Village type development | NTEH policy | — |

> Always read the OZP Notes and Explanatory Statement — site-specific restrictions override HKPSG defaults.

---

## 3. Planning Applications

### 3.1 Section 16 Application (Permission)

- Required for: Column 2 uses in OZP; development exceeding default PR/BHR
- Submitted to TPB; public inspection period 3 weeks
- TPB decides within 2 months (extendable)
- Approval valid 2 years (extendable by s.16A)

### 3.2 Section 12A Application (Amendment)

- To amend OZP zoning or restrictions
- Higher threshold; requires TPB to be satisfied amendment is suitable
- Timeline: 6–18 months typical

### 3.3 Planning Conditions

Common conditions attached to s.16 approvals:
- Submission of AVA / traffic impact assessment (TIA)
- Landscape master plan
- Design, disposition & appearance (DDA) approval
- Phasing plan

---

## 4. Air Ventilation Assessment (AVA)

| Aspect | Requirement |
|---|---|
| When required | Major development in urban areas; PlanD may require as planning condition |
| Method | Pedestrian Wind Environment (PWE) study; CFD or wind tunnel |
| Metric | Pedestrian-level wind speed; Lawson comfort criteria |
| Key concern | Podium wall effect blocking sea breeze corridors |
| Mitigation | Building gaps ≥ 20% of site frontage; podium setbacks; permeable ground floor |

### 4.1 Prevailing Wind Directions (HK)

| Season | Dominant Wind |
|---|---|
| Summer (Apr–Sep) | S / SE (sea breeze); typhoon risk |
| Winter (Oct–Mar) | NE / N (continental; cooler) |

Design for summer ventilation (S/SE) while providing shelter from winter NE winds.

---

## 5. HKPSG Urban Design Guidelines (Chapter 11)

| Guideline | Requirement |
|---|---|
| Ridgeline protection | No development to visually intrude on natural ridgelines from key vantage points |
| Harbour view corridors | Maintain visual corridors to Victoria Harbour per HKPSG Fig. 11.1 |
| Building separation | Min 15 m between residential towers (HKPSG recommendation) |
| Podium height | ≤ 15 m to maintain human scale at street level |
| Greenery ratio | Site greenery coverage ≥ 20–30% (PNAP APP-40) |
| Active frontage | Ground floor commercial/community use along primary streets |

---

## 6. Development Control Checklist

- [ ] OZP confirmed: zone, PR, site coverage, BHR, special restrictions, s.16 required?
- [ ] Lease conditions checked (Lands Dept): permitted use, gross floor area cap, height restriction
- [ ] HKPSG Chapter 11 urban design guidelines reviewed
- [ ] AVA required? Commission at feasibility stage
- [ ] TIA required? Engage TD/HyD early — execution: `hk-traffic-coordination`
- [ ] Drainage impact assessment: DSD consultation
- [ ] Heritage: AAB grading check; AMO consultation if Grade 1/2/3 or proposed monument nearby

---

## 7. Airport height (Cap. 301 and Cap. 301D)

Cap. 301 does not print a building height in metres. Height limits and prohibited areas exist only in an order under section 3, with a plan deposited at the Land Registry. Cap. 301D sets the restricted height as the height above Hong Kong Principal Datum shown in red on the Airport Height Restriction Plan 2021 sheet for that area. Do not take a metre figure from the Order. There is none in the text.

A mast, pole, pile driver, scaffold, hoist, crane, or other structure projecting skywards is a building for this Ordinance. Test roof plant, signage, and site cranes against the height order, not only the occupied floors. A section 3(1)(a) area prohibits all such buildings. A section 3(4) exemption is a short notice (2 months, extendable by further periods of 2 months), not a permanent design approval.

Plans approved on or after **31 May 2022** are outside the Order’s paragraph (a) saving for earlier approvals. Minor works or designated exempted works completed on or after that date are outside paragraphs (e) and (f). An existing building that exceeds a later height order can be ordered down on dates set by the Director-General after consultation with the Director of Buildings.

In Kowloon, New Kowloon, and any further area prescribed by a Gazette order, do not design facade, roof, or feature lighting that flashes, cuts off, or appears suddenly or intermittently and is exposed to the sky, unless it is a navigational or signal light, under 200 cd, or covered by written authority or a Gazette exemption. Reserve structure, power, and access for warning lights and aircraft beacons. Do not rely on a retained tree or a green roof to sit in front of a warning light; the occupier can be required to remove it.

Cap. 404, the Temporary Control of Density of Building Development (Kowloon and New Kowloon) Ordinance, is omitted as expired. Do not use it as a density cap.

Outline zoning plan Notes and the lease can be stricter than the master schedule of notes and the Town Planning Board guidelines. Read the site plan.

---

*Sources: Town Planning Ordinance Cap. 131, HKPSG chapters 1–12, Town Planning Board guidelines, OZP Master Schedule of Notes, PNAP APP-40, Hong Kong Airport (Control of Obstructions) Ordinance Cap. 301 (15 October 2020) and Cap. 301D (31 May 2022), Cap. 404 (expired).*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-spatial-planning.md`. The master router links these files directly.

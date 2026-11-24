---
name: hk-spatial-planning
description: Hong Kong spatial planning — OZP zoning, HKPSG standards, planning applications (s.16/s.12A), air ventilation assessment, urban design guidelines, and development control.
disable-model-invocation: true
---

# HK Spatial Planning

For **Cap. 127 foreshore/sea-bed undertakings, Cap. 476 marine parks/reserves and Ramsar wetlands**, read [coastal and wetland controls](../../references/hk-coastal-wetland-controls.md) at feasibility stage. Map temporary as well as permanent works and keep planning, Lands, AFCD, MD and EPD decisions separate. For a designated main watercourse, also read [Cap. 446 land drainage](../../references/hk-specialist-plant-drainage.md#cap-446--land-drainage-ordinance).

Covers Outline Zoning Plans, HKPSG, planning applications, AVA, and urban design development control.

For **Planning application / zoning**, use `hk-spatial-planning`. For other topics, see the routing table below.

## When to Use This Skill

**Role boundary:** Refer planning-led masterplans, specialist planning strategies/applications and impact studies to **Skills-Urban-Planner-HK**. Keep architectural feasibility inputs and coordination of supplied planning constraints here. Apply the [master referral rule](../../SKILL.md#specialist-role-referrals); state the referral and do not supply the specialist answer from local background tables.

OZP, s.16/s.12A, TPB, AVA, HKPSG development control.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Planning application / zoning | `hk-spatial-planning` | `—` |
| Street, harbour edge, ridgeline, visual impact | `—` | `hk-urban-space-statutory` |
| BO GFA after planning permission | `—` | `hk-building-codes` |
| Lands lease modifications | `—` | `hk-lease-compliance` |

## Halt criteria

- If the site's OZP is unknown, withhold site-specific planning or compliance conclusions and identify the missing plan and Notes. Continue with a general approvals checklist where useful; do not assume zone defaults.
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

> Always read the OZP Notes and Explanatory Statement. The rows above are outline-zoning-plan shorthand, not the HKPSG Chapter 2 density zones. Chapter 2 uses zones R1 to R4. Its Main Urban Area table includes 8/9/10, 7.5, 6.5, 6 and 3.6. New Town and New Development Area R1 is 6.5, with a figure up to 8 only where the area is comprehensively planned and has no infrastructure constraint. Rural rows run down to 0.4. Domestic plot ratio is on net site area. Apply the more stringent of the statutory plan and the First Schedule. Catalogue: [hkpsg](../../references/catalogues/hkpsg.md).

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

## 4. Air ventilation assessment

Joint Technical Circular No. 1/06 (19 July 2006) compares options by wind velocity ratio. It prints no pass/fail benchmark, no Lawson comfort criterion, and no gap as a percentage of site frontage. The local average velocity ratio takes precedence over the site average. Permeability dimensions are PNAP APP-152. Align blocks within 30 degrees of the prevailing wind when applying HKPSG Chapter 11. The design response is in `hk-urban-space-statutory`.

---

## 5. Urban design

Street, footpath, ridgeline, harbour edge, visual impact, and public open space in a private development are in `hk-urban-space-statutory`. Chapter 11 does not print a podium height, a 15 m tower gap, a Figure 11.1 corridor width, or a greenery percentage. PNAP APP-40 is hotel development. Greenery percentages are PNAP APP-152.

---

## 6. Development Control Checklist

- [ ] OZP confirmed: zone, PR, site coverage, BHR, special restrictions, s.16 required?
- [ ] Lease conditions checked (Lands Dept): permitted use, gross floor area cap, height restriction
- [ ] Urban-space rules reviewed in `hk-urban-space-statutory` (Chapter 11 is guidance only)
- [ ] Chapter 5 industry, Chapter 10 conservation, and Chapter 12 miscellaneous uses checked when the site is industrial, a conservation zone, a cavern, a petrol filling station, a potentially hazardous installation, a vehicle workshop, port back-up, or land under a flyover. Street widths in Chapter 5 refer to Chapter 8. Chapter 10 prints no buffer width. Chapter 12 prints no under-flyover clearance. Catalogue: [hkpsg](../../references/catalogues/hkpsg.md)
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

*Sources: Town Planning Ordinance Cap. 131, HKPSG chapters 1–12, Town Planning Board guidelines, OZP Master Schedule of Notes, PNAP APP-152, Technical Circular No. 1/06, Hong Kong Airport (Control of Obstructions) Ordinance Cap. 301 (15 October 2020) and Cap. 301D (31 May 2022), Cap. 404 (expired).*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-spatial-planning.md`. The master router links these files directly.

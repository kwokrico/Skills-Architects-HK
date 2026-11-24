---
name: hk-urban-space-statutory
description: Hong Kong urban-space rules for streets, footpaths, public realm, harbour edge, views, and public open space in private developments. Points building metres to APP-152 and APP-101, and zoning to spatial planning.
disable-model-invocation: true
---

# HK Urban Space Statutory

Live rules for the street, the public realm, the harbour edge, and public views. An HKPSG (Hong Kong Planning Standards and Guidelines, 香港規劃標準與準則) figure is guidance until it is written into the outline zoning plan, the lease, or a Town Planning Board permission. Chapter 11 does not set a podium height, a tower separation, or a greenery percentage.

For **street, footpath, harbour-front, ridgeline, visual impact, or public open space in a private development**, use `hk-urban-space-statutory`. For other topics, see the routing table below.

## When to Use This Skill

**Role boundary:** Refer planting/soil/root/hardscape design to **Skills-Landscape-Architects-HK**, and planning-led masterplans or specialist planning studies to **Skills-Urban-Planner-HK**. Keep building/public-realm interfaces and architectural constraints here. Apply the [master referral rule](../../SKILL.md#specialist-role-referrals); state the referral and do not supply the specialist answer from local background tables.

For podium/ground-level landscape interfaces, use section 10. Its design-coordination checklist supplements the statutory/planning routes; it is not a new set of numerical controls.

| Question type | Use this skill | Use instead |
|---|---|---|
| Street, footpath, carriageway layout, harbour-front, ridgeline, visual impact, public open space in a private development | `hk-urban-space-statutory` | `—` |
| Zone, plot ratio, section 16 or 12A | `—` | `hk-spatial-planning` |
| Why a control was introduced | `—` | `hk-urban-planning-history` |
| Which planning idea should guide the scheme | `—` | `hk-urban-planning-theory` |
| Building separation, setback, or site coverage of greenery in metres | `—` | `hk-building-sustainability` (PNAP APP-152) |
| Full-site-coverage podium height | `—` | PNAP APP-101 and Building (Planning) Regulation 20(3) |
| Open-space area per person | `—` | `hk-building-programming` (HKPSG Chapter 4) |
| Traffic-impact submission | `—` | `hk-traffic-coordination` |
| Architectural theory | `—` | `hk-design-theory` |

Catalogue: [hkpsg](../../references/catalogues/hkpsg.md).

## 1. Where the number is printed

| Question | Instrument that prints the rule |
|---|---|
| Zone, plot ratio, building height on the plan | Outline zoning plan Notes and the lease. Domestic plot-ratio guidance is HKPSG Chapter 2, in `hk-spatial-planning` |
| Podium of full site coverage | Building (Planning) Regulation 20(3), explained by PNAP APP-101. Chapter 11 does not print 15 m |
| Building separation, street setback, site coverage of greenery | PNAP APP-152. Not Chapter 11, and not PNAP APP-40 (that note is hotel development) |
| Open-space area per person | HKPSG Chapter 4, in `hk-building-programming` |
| Footpath and carriageway width | HKPSG Chapter 8, below. Crossing width and footway crossfall are the Transport Planning and Design Manual (TPDM, 運輸策劃及設計手冊) |
| Ridgeline | HKPSG Chapter 11 and the eight strategic viewing points, below |
| Harbour edge | Harbour Planning Principles and the draft Harbour Planning Guidelines, below |
| Public open space in a private development | Development Bureau guidelines, below. The lease or deed of dedication controls hours and obligations |
| Visual impact | Town Planning Board guideline PG-No. 41A, below |

## 2. Streets (HKPSG Chapter 8, December 2025)

Rail is the backbone. Place intensive uses within a 500 m walk of a station. A walk up to 1,000 m is a reason to consider a travellator early. Footpaths use three zones: Through Zone, Street Furniture and Greening Zone, and Building Frontage Zone. The Through Zone is for walking and stays clear. An urban Through Zone is 3 m wherever possible. If the three-zone total cannot be achieved, the clear width is still 3 m.

Commercial, commercial/residential, and Residential Zone 1 near a station, cinema, or similar generator, for the highest flow band:

| Zone | Width |
|---|---|
| Through Zone, very high flow | 4.5 m |
| Building Frontage Zone | 0.5 m at place significance P1; allowance 1.0 m at P2 and 1.0 m at P3 |
| Street Furniture and Greening Zone | 2.0 m at P1 and P2; allowance 3.0 m at P3 |

Through Zone only, for the other land-use rows:

| Land use | Through Zone | Flow |
|---|---|---|
| Residential Zone 1 | 3.5 m | High |
| Residential Zone 2 | 3 m | Medium |
| Residential Zone 3 | 3 m | Low to medium |
| Rural | 2 m | Very low |
| Business | 4.5 m | Medium |
| General industrial | 4.5 m | Medium |
| Special industrial | 3.5 m | Low to medium |
| Rural-based industrial | 2.5 m | Low |

A footpath that also takes emergency or service vehicles is generally 6 m and is designed for the vehicle. A shared-surface street operates below 25 km/h. A low-speed zone is 30 km/h or below. A building canopy is at least 2 m wide, preferably 2.5 m, with a preferred vertical clearance of 3.5 m.

Minimum urban carriageway widths, adopted from the TPDM. A street that will be public, or will carry public transport, is designed to the TPDM and the Highways Department, not to the private-street table.

| Road type | Single carriageway | Dual carriageway |
|---|---|---|
| Expressway and trunk | — | 7.3 m (2-lane); 11.0 m (3-lane); 14.6 m (4-lane) |
| Primary distributor | — | 6.75 m (2-lane); 10.0 m (3-lane); 13.5 m (4-lane) |
| District distributor | 7.3 m (2-lane); 10.3 m where the peak-hour note applies | 6.75 m (2-lane); 10.0 m (3-lane); 13.5 m (4-lane) |
| Local distributor | 7.3 m (2-lane); 10.3 m where the peak-hour note applies | 6.75 m (2-lane); 13.5 m (4-lane) |

The wider 10.3 m single carriageway applies where two-way peak-hour flow exceeds 1,600 vehicles and is under 2,400. A 3-lane single carriageway is not recommended. Add 3 m where permitted parking or loading would block through traffic.

### 2.1 Geometry Chapter 8 does not print

From TPDM Volume 2 and Volume 6 Chapter 10, August 2026. Summary: [TPDM schematic rules](../../../hk_s_reference/SS/TPDM%20Volumes%202%20and%206%20schematic%20rules_CS.md).

- Through Zone crossfall is between 2% and 3.3%.
- An at-grade crossing is generally 4 m to 6 m wide, and not narrower than 2.5 m or wider than 9 m. Dropped kerbs cover the full crossing width and do not continue around a corner radius.
- An at-grade crossing is not the general solution on a trunk road or a primary distributor.
- Junction types in the manual are priority, signals, roundabout, and grade-separated. Junction spacing stays in Chapter 8.

Check a suggested walking width against [human scale](../../references/hk-human-scale-dimensions.md). Two people pass comfortably at 1,500–1,800 mm. That passing width does not replace the 3 m Through Zone.

Active Design Guidelines (May 2023) ask for destinations and a walk that people will use. They print no width. Summary: [Active Design Guidelines](../../../hk_s_reference/SS/Active%20Design%20Guidelines_CS.md).

## 3. Chapter 11 principles (December 2025)

Chapter 11 is a design brief, not a code. It does not print a podium height, a setback, a separation, a footpath width, or a permeability percentage.

| Principle | What to lock | Figure the chapter prints |
|---|---|---|
| 1 Responding to context | Ridgelines, neighbourhood height, and permeability | A 20% to 30% building-free zone below the ridgelines, viewed from the strategic viewing points. Street and block axes within 30 degrees of the prevailing wind |
| 2 Pedestrian movement | A walk to public transport, weather protection, and direct ground-level links | A walk under 500 m to a station is the convenient catchment |
| 3 Public realm | Parks, waterfront, streetscape, landscape, and furniture | No area and no footpath width. Open space is Chapter 4. Footpath width is Chapter 8 |
| 4 People-centric buildings | A low zone that meets the street, heritage setting, and wind permeability | Block axis within 30 degrees of the prevailing wind. No podium height |

The eight strategic viewing points on the Planning Department page saved 15 November 2026 are: West Kowloon Cultural District; Cultural Complex, Tsim Sha Tsui; Waterfront Promenade at Kai Tak Development; Quarry Bay Park; Hong Kong Convention and Exhibition Centre; Sun Yat Sen Memorial Park, Sai Ying Pun; The Peak; Central Pier No. 7. Count rooftop structures other than an antenna. Summary: [Strategic Viewing Points](../../../hk_s_reference/SS/Strategic%20Viewing%20Points_CS.md).

## 4. Public-realm tests from Chapter 4

These are design tests, not the population standard. The area per person is in `hk-building-programming`.

| Test | Figure |
|---|---|
| Public-housing green coverage | 30% target, 20% floor |
| Soft landscaping on public open space | 20% of active space, 70% of passive space |

## 5. Air ventilation

Joint Technical Circular No. 1/06 (19 July 2006) compares design options by wind velocity ratio. It states no absolute pass/fail benchmark, no Lawson comfort criterion, and no gap equal to a percentage of the site frontage. A higher velocity ratio means less reduction of the wind. The local average takes precedence over the site average. Permeability dimensions are PNAP APP-152. Summary: [Technical Circular No. 1/06](../../../hk_s_reference/SS/Technical%20Circular%20No.%201-06%20Air%20Ventilation%20Assessments_CS.md).

Government categories that should be tested include a site over 2 hectares at plot ratio 5 or above, gross floor area over 100,000 m², a podium over one hectare, a waterfront frontage over 100 m, and a building over 15 m inside a designated breezeway or public open space. A private project is encouraged. A planning condition can still require the study.

## 6. Harbour edge

The Harbour Planning Principles (endorsed 27 April 2006) ask for pedestrian access to and along the harbour, preferably at grade, and for public enjoyment. The draft Harbour Planning Guidelines (14 June 2007 agenda) add a continuous promenade of adequate width, a setback where the use can give it, height descending toward the harbour, and active frontage without plant rooms or blank walls. Neither document prints the promenade width. Summaries: [principles](../../../hk_s_reference/SS/Harbour%20Planning%20Principles_CS.md), [guidelines](../../../hk_s_reference/SS/Harbour%20Planning%20Guidelines_CS.md). Reclamation is Cap. 531, in [coastal and wetland controls](../../references/hk-coastal-wetland-controls.md).

## 7. Public open space in a private development

The Development Bureau guidelines took effect on 14 February 2011. Design uses connectivity, appropriateness and quality, and five types: public green, plaza, courtyard, pocket space, and promenade. Management guidelines do not override the lease or a deed of dedication. A key pedestrian link or a waterfront promenade should be open 24 hours unless the lease grants an exemption. Otherwise public access should not be less than 13 hours, subject to the lease. A commercial use of a passageway has a printed 10% ceiling and must not block the route. Summary: [POSPD guidelines](../../../hk_s_reference/SS/Public%20Open%20Space%20in%20Private%20Developments%20Design%20and%20Management%20Guidelines_CS.md).

## 8. Visual impact (TPB PG-No. 41A, January 2026)

A visual impact assessment is not required for every application. Paragraph 2.3 expects one when the Notes or a condition require it, the Board asks, the site is under a Master Layout Plan or design brief, development parameters intensify the scale, a non-development zone is rezoned for development, or the proposal may affect a public view. If none of those apply and adverse impact is unlikely, do not assume a full assessment.

Judge layout, scale, form, massing and disposition. The conclusion is one of: beneficial, negligible, slight, moderate, substantial. A substantial impact means the mass has to change. Start the assessment area at a radius of three times the building height, then check it on the ground. Frame each view within about 60 degrees vertically and horizontally. The full summary is [TPB PG-No. 41A](../../../hk_s_reference/Planning%20Department%20(PlanD)/Town%20Planning%20Board%20Guidelines/summaries/TPB%20PG-No.%2041A%20Submission%20of%20Visual%20Impact%20Assessment_CS.md).

## 9. Human-scale check

When a street or promenade is proposed, state at least one dimension from [hk-human-scale-dimensions.md](../../references/hk-human-scale-dimensions.md) and the Chapter 8 or TPDM figure that governs the same edge. The human-scale millimetres do not replace the Through Zone.

## 10. Landscape and building-interface coordination

Use for planting, public realm and podium/ground-level external works in Hong Kong. The architect coordinates the building interface; landscape/tree specialists establish planting and root requirements; engineers establish structural/drainage performance. A planting sketch does not establish approval, soil depth or slab capacity.

**Inputs:** current survey/levels; boundaries and public/private access obligations; tree survey/status where relevant; approved/submitted landscape information and conditions; utilities/services; structure/load information; planting strategy; drainage/irrigation design; waterproofing system; occupation/maintenance requirements. Record missing evidence. Check lease/planning/tree conditions through the relevant existing topics, without treating design guidance as statutory permission.

### Coordination sequence and responsibilities

1. Define the intended use, accessible circulation, emergency/service access and management responsibilities. Identify affected public links, common parts and neighbouring premises.
2. Overlay planting, rooting zones, structure, services, drainage and access on one revision baseline. Assign the conflicts below before freezing levels or landscape layouts.
3. Compare feasible layouts with landscape, structural and MEP/drainage specialists. Record species/growth and maintenance assumptions, occupied-area disruption and replacement routes. Do not solve an unverified load problem by merely calling a planter “lightweight”.
4. Coordinate details through [building envelope](../hk-building-envelope/hk-building-envelope.md#8-landscape-over-structure-and-waterproofing-interfaces); take unresolved layout constraints back to [concept design](../hk-concept-design/hk-concept-design.md#7-landscape-interfaces-at-concept-stage).
5. Agree construction sequence, protected areas, inspections before concealment and project-specific testing. Establish who maintains outlets, irrigation and planting after handover.
6. Record the selected layout, restrictions and evidence. Hold affected construction information if loads, drainage, water resistance or access remain unresolved; enter issues in the existing documentation QA log.

| Interface | Decision to coordinate | Lead input / evidence |
|---|---|---|
| Trees/planting and services | Rooting space, growth, utility conflicts and repair access | Landscape/arboricultural input plus utility survey and coordinated section |
| Podium/roof loading | Growing medium, retained water, plants, furniture and maintenance loads | Structural engineer's assessment of the actual build-up and load cases |
| Drainage/irrigation | Outlets, overflow, water supply, leakage isolation and maintainable access | Drainage/MEP design coordinated with levels, structure and planting |
| Waterproofing | Root protection, membrane continuity, penetrations and movement | Envelope/system specialist detail and agreed inspection/test evidence |
| Circulation and boundaries | Accessible route, door thresholds, emergency/service access and public/private obligations | Architect with accessibility/fire/planning/lease reviewers as applicable |
| Maintenance | Safe access, debris clearance, pruning and replacement logistics | Landscape/FM agreement and operational responsibility record |

**Interface register:** location; drawing revisions; proposed planting/build-up; source of constraint; conflict; owner; required survey/calculation/detail; affected outputs; due date; status and closure evidence. Leave unavailable soil/load/drainage criteria unresolved rather than inventing dimensions.

**Hypothetical case:** new planters on an occupied podium obstruct the route to a drain and move a door threshold. Request surveyed levels, drainage access and a structural check of the proposed saturated build-up. Compare relocation/reconfiguration with the landscape designer and accessibility reviewer. Keep construction release pending those checks; a greenery target or management endorsement does not close the interfaces.

**HK source context:** [BD Guidelines on Greening in Buildings](https://www.bd.gov.hk/doc/en/resources/codes-and-references/code-and-design-manuals/IGG_e.pdf) address structural, drainage and waterproofing considerations for building greening. Consult the actual applicable project/authority requirements; this workflow adds no generic load, soil-depth or drainage threshold. Source checked 24 November 2026.

*Sources: HKPSG Chapters 4, 8 and 11 (December 2025); TPDM Volumes 2 and 6 (August 2026); TPB PG-No. 41A (January 2026); Harbour Planning Principles (27 April 2006); draft Harbour Planning Guidelines (14 June 2007); Technical Circular No. 1/06 (19 July 2006); POSPD guidelines (14 February 2011); Active Design Guidelines consultancy report (May 2023); Planning Department strategic viewing points page (saved 15 November 2026); PNAP APP-101 and APP-152.*

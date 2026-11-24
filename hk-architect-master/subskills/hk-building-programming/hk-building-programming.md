---
name: hk-building-programming
description: HK building programming — BO use classifications, HKPSG facility ratios, HA/HD unit schedules, Grade A office benchmarks, FEHD licensing constraints, and area schedule methodology.
disable-model-invocation: true
---

# HK Building Programming

Area benchmarks and facility ratios for HK building types. BO use classifications govern plot ratio calculations. HKPSG provides community facility provision standards.

Neufert, *Architect's Data* (Second International English Edition, 1980), may suggest which rooms adjoin. Do not import its areas, stairs, parking, fire, or services figures. Benchmarks in this file remain the area source. See `../../references/hk-foreign-design-handbooks.md`.

For **Schedule of accommodation / unit mix**, use `hk-building-programming`. For other topics, see the routing table below.

## When to Use This Skill

Use section 7 for user workshops, functional adjacencies, journey studies and requirement-to-design validation; keep interior-led or other specialist design with the named role skills.

**Role boundary:** Refer interior-led layouts, FF&E and detailed interior briefs to **Skills-Interior-Designer-HK**, and technical smart-system design to **Skills-MEP-Engineer-HK**. Retain the architectural accommodation and coordination brief. Apply the [master referral rule](../../SKILL.md#specialist-role-referrals); state the referral and do not supply the specialist answer from local background tables.

Use section 6 to define smart-building user outcomes, operating modes and space/interface needs before selecting technology.

Area schedules, HKPSG ratios, HA/HD unit mix, FEHD licensing constraints.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Schedule of accommodation / unit mix | `hk-building-programming` | `—` |
| OZP development parameters | `—` | `hk-spatial-planning` |
| Concept massing strategy | `—` | `hk-concept-design` |
---

## 1. BO Use Classifications

| Classification | Description | PR Basis |
|---|---|---|
| Domestic | Residential use | Domestic PR (per OZP) |
| Non-domestic | Commercial, office, retail, industrial | Non-domestic PR (per OZP) |
| Composite | Mixed domestic + non-domestic | Separate PR caps for each portion |

---

## 2. Area Benchmarks by Building Type

### 2.1 Residential

| Type | Net Internal Area | Net-to-Gross | Notes |
|---|---|---|---|
| HA public housing (1P/2P) | 14–21 m² | 70–75% | HA allocation schedule |
| HA public housing (3P/4R) | 35 m² | 70–75% | HA allocation schedule |
| Private residential (studio) | 20–35 m² saleable | 75–82% | SRPE saleable area definition |
| Private residential (2-bed) | 45–65 m² saleable | 75–82% | Market norm |
| Private residential (3-bed) | 65–90 m² saleable | 75–82% | Market norm |

### 2.2 Commercial

| Type | Benchmark | Net-to-Gross |
|---|---|---|
| Grade A office | 12–18 m²/person | 75–80% |
| Grade B office | 10–14 m²/person | 70–78% |
| Retail (shopping mall) | 15–25 m² GLA per 1,000 catchment pop. | 65–75% |
| Hotel (midscale) | 28–35 m²/key | 60–70% |
| Hotel (upscale) | 35–42 m²/key | 60–70% |

### 2.3 Institutional

| Type | Benchmark | Source |
|---|---|---|
| Government primary school | 56 m² per 30-pupil classroom | EDB schedule |
| Government secondary school | 65 m² per 30-pupil classroom | EDB schedule |
| Hospital (HA) | 50–80 m² GIA per bed | HA design standards |
| Elderly care (residential) | 6.5 m² per resident (min) | SWD standards |

---

## 3. HKPSG provision the architect locks

Catalogue: [hkpsg](../../references/catalogues/hkpsg.md). These are guidelines until the statutory plan, the lease, or a Town Planning Board permission writes them in.

| Subject | What to lock | Chapter |
|---|---|---|
| Open space | 3.5 m² per person for the territory; 1 m² per person inside public housing and private comprehensive residential development; 0.5 m² per worker in an employment node | 4 |
| Primary school | A 30-classroom reservation at 6,200 m² with a 65 m width, plus a 10% site reserve in a new development area | 3 |
| Secondary school | A 30-classroom reservation at 6,950 m² with a 65 m width | 3 |
| Kindergarten | Within a 0.4 km radius, without relying on an uncontrolled major-road crossing | 3 |
| Elderly care | 17.2 community-care places and 21.3 residential-care beds per 1,000 persons aged 65 or above | 3 |
| Rehabilitation | 23 pre-school places per 1,000 children aged 0–6; 23 vocational places per 10,000 persons aged 15 or above; 36 residential places per 10,000 persons aged 15 or above | 3 |
| Retail | Do not apply a retail gross-floor-area ratio from Chapter 6. Place district retail at a rail station or a bus terminal | 6 |
| Parking | Do not use a generic space-per-flat or space-per-office ratio. Chapter 8 and the lease set the provision | 8 |

Public-housing green coverage and soft-landscaping percentages are design tests in `hk-urban-space-statutory`, not population standards.

---

## 4. FEHD Licensing Constraints

| Use | FEHD Licence | Key Space Requirement |
|---|---|---|
| Restaurant / food factory | Food Business Licence | Kitchen:dining ≥ 1:3; grease trap; ventilation 15–30 ACH |
| Childcare centre | Child Care Centre Licence | Min 1.85 m²/child; outdoor play area |
| Elderly care centre | Residential Care Home Licence | Min 6.5 m²/resident; nursing station |
| Supermarket | Food Business Licence | Cold storage; loading dock |

---

## 5. Parent ordinances for licensed uses

Section 4 states space ratios used in practice. The parent ordinances below do not print those room sizes. Room, hygiene, and staffing figures sit in a code or in regulations made under the ordinance. Non-compliance with Cap. 123 design, fire, health, and sanitation is itself a ground to refuse several of these licences.

| Ordinance | When it applies | What the architect must lock |
|---|---|---|
| Cap. 132 Public Health and Municipal Services | Parent for public sewers, latrine notices, canopies, mosquito water on a site, offensive trades, ventilation of scheduled premises, and dangerous advertisement hoardings | Keep site wash and waste building materials out of the public sewer. A latrine notice that is building works needs the Building Authority’s written consent. A restaurant, cinema, theatre, dancing establishment, factory canteen, or funeral parlour without adequate natural ventilation is sized to the Second Schedule rate per person, and that system is not altered without written permission. A billiard establishment, public bowling alley, public skating rink, or undertaker cannot open without the licence named in the Ordinance. A cinema or restaurant is not licensed by those two sections |
| Cap. 172 Places of Public Entertainment | A place capable of accommodating the public at which a Schedule 1 entertainment is presented, including a lecture, an exhibition, a bazaar, or a dance party of over 200 persons or between 2 a.m. and 6 a.m., unless an exemption order covers that class | Stair, gangway, exit, seating, and temporary stage dimensions are in regulations under section 7, which are not in the Ordinance consolidation. The licence can cap the number of persons and the hours |
| Cap. 279 Education | A school must be registered. Where the premises were not designed and constructed as a school, certificates are required before registration | No-structural-timber-floors certificate, a Director of Fire Services certificate of no undue fire risk, a means-of-escape certificate for everyone in the building, and, where Cap. 123 applies, a Building Authority notice that he does not intend to prohibit the school use under section 25. A later wing that was not designed as a school repeats those certificates. Classroom sizes are not in this Ordinance |
| Cap. 349 Hotel and Guesthouse Accommodation | Premises held out as sleeping accommodation for a fee | Mandatory refusal where the deed of mutual covenant or Government lease limits the part to private residential use, prohibits commercial use, or prohibits hotel or guesthouse use. After licensing, do not alter the layout so that it substantially deviates from the plan deposited with the Authority. On a licence longer than 36 months an authorized person must certify each year. This Ordinance does not set room sizes |
| Cap. 459 Residential care homes (elderly persons) | More than 5 residents aged 60 or over habitually received for care, unless a Cap. 613 or Cap. 633 exemption already covers the home | Licence for not more than 36 months. Freeze ingress, egress, and the fire and health layout against Cap. 123 and the Director’s code of practice. A hazard direction can be followed by an order that the premises cease to be used as the home. Room sizes are in the section 22 code, not in the Ordinance |
| Cap. 613 Residential care homes (persons with disabilities) | More than 5 persons with disabilities aged 6 or over habitually received for residential accommodation with care, unless an exemption or a Cap. 459 licence already covers the home | A new home cannot use a certificate of exemption. That route is only for a home that existed immediately before 18 November 2011. Licence not longer than 36 months. Ingress, egress, and Cap. 123 compliance are grounds to refuse |

---

*Sources: HA Schedule of Accommodation, HKPSG Chapters 3, 4, 6 and 8 (Chapter 4 and Chapter 8 December 2025), Cap. 132 (10 July 2026), Cap. 172 (1 July 2022), Cap. 279 (1 August 2026), Cap. 349 (1 September 2023), Cap. 459 and Cap. 613 (26 July 2024), Buildings Ordinance Cap. 123.*

## 6. Smart-building user and operational brief

Define outcomes before devices. Request client/FM priorities, uses/users/hours, existing systems, operating responsibilities, access needs, budget, outages and data/privacy constraints. Refer technical systems design to **Skills-MEP-Engineer-HK**; retain the architect's spatial and user-interface brief here.

For each journey — arrival, after-hours access, room occupation, maintenance and fault response — record desired outcome, normal/exceptional modes, manual fallback and operating owner. Do not prescribe a vendor, sensor count or algorithm from a room name alone. Confirm monitoring need and access to data with client/ICT advisers.

| Use-case ID / space | Outcome/hours | Spatial/device interface | Operator / specialist owner | Failure/manual mode | Acceptance evidence / questions |
|---|---|---|---|---|---|
| SB-01 / meeting rooms | Comfortable use including late meetings | Reachable controls; coordinated sensors and services access | Client/FM + MEP/controls | Missing signal must not be assumed to mean vacant | Reviewed sequence and witnessed scenarios; occupancy/hours pending |

Send this to [services coordination](../hk-building-services/hk-building-services.md#12-smart-building-coordination-brief) for the architectural interface record and specialist referrals. Return plant/panel/cabling and access needs to the accommodation schedule. Freeze agreed outcomes and spatial allowances only; controls engineering, cybersecurity and systems integration remain specialist responsibilities.

## 7. User research and functional brief validation

Use for the architect's building-level brief, accommodation schedule, functional adjacencies and circulation. Apply the [role-referral rule](../../SKILL.md#specialist-role-referrals): refer interior-led layouts/FF&E/joinery to **Skills-Interior-Designer-HK**, landscape design to **Skills-Landscape-Architects-HK**, district/masterplanning to **Skills-Urban-Planner-HK**, and systems/capacity questions to the MEP/structural skills. Coordination requirements may be recorded here without answering those specialist questions.

### 7.1 Prepare the workshop

Obtain project purpose, client decisions to make, user/operator groups, existing-use evidence, site/building constraints, area/budget/programme assumptions and the stage of appointment. Include visitors, staff, people with differing access needs, cleaners/security and FM where relevant. Record missing representatives. Agree accessible formats/languages and proportionate handling of feedback; do not collect personal or medical details merely to describe an access requirement.

Ask:

- What activities occur, for whom, at what times, with what peak or exceptional demand? Which are observed and which are forecasts?
- What must happen together, nearby, separately or out of public view? Why?
- How do visitors, staff, goods, waste and maintenance personnel arrive, move and leave, including after-hours operation?
- Where do queues, conflicts, privacy problems or difficult access occur? What evidence supports the concern?
- What storage, cleaning, servicing and future changes must the building accommodate?
- Which needs are essential, desirable or optional, and who may decide a trade-off? What would demonstrate a successful outcome?

### 7.2 Convert activities into a testable brief

1. Record requirements in the users' terms, then identify architectural implications. Distinguish verified obligations, client objectives, assumptions and preferences; do not turn a requested area into an established statutory minimum.
2. Map user journeys and an adjacency table. Classify relationships as `Must connect`, `Prefer near`, `Separate`, or `Undecided`, with rationale, operating hours and relevant specialist dependencies.
3. Develop building-level options and test ordinary, peak and exceptional scenarios. Check circulation, servicing, access, usable area and flexibility against the supplied constraints; refer technical sizing/design rather than inventing it.
4. Show competing requirements and unresolved evidence. Ask QS/programme advisers for impacts and the appropriate role skill for specialist decisions. Do not silently remove a less-represented group's requirement to fit a target area.
5. Validate the option with users/FM and the authorised client decision-maker. Record accepted changes, dissent, exclusions and unanswered questions; approval does not itself establish statutory compliance.
6. Trace each requirement into the drawings/specification and handover checks. Revisit changes using [project decision governance](../hk-project-management/hk-project-management.md#13-brief-decisions-and-aftercare-governance); later compare outcomes through [POE](../hk-plan-of-work/hk-plan-of-work.md#9-post-occupancy-evaluation-and-aftercare-service).

| Requirement ID / source | Activity/user/hours | Priority and rationale | Space/adjacency or journey implication | Evidence / assumption | Owner / specialist referral | Validation and design reference | Status |
|---|---|---|---|---|---|---|---|
| BR-01 / user workshop | Visitors arrive while deliveries occur | Essential safe, usable arrival; peak timing unconfirmed | Test shared versus separated arrival/service paths | Survey and operating observations required | Architect + client/FM; specialist access/traffic input if needed | Option plan/revision and client decision pending | Open |

**Hypothetical case:** a Hong Kong community facility wants an open welcoming lobby, secure after-hours access and deliveries through the same entrance. Map visitor, staff and goods journeys at different times and test alternative layouts/operating arrangements. Refer security-system design to **Skills-MEP-Engineer-HK** and detailed interior-led reception design to **Skills-Interior-Designer-HK**. Do not solve the conflict by assuming an unverified corridor width or an automatic-lock sequence. Return options with unresolved constraints and named decision owners.

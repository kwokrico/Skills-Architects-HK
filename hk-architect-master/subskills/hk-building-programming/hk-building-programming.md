---
name: hk-building-programming
description: HK building programming — BO use classifications, HKPSG facility ratios, HA/HD unit schedules, Grade A office benchmarks, FEHD licensing constraints, and area schedule methodology.
disable-model-invocation: true
---

# HK Building Programming

Area benchmarks and facility ratios for HK building types. BO use classifications govern plot ratio calculations. HKPSG provides community facility provision standards.

For **Schedule of accommodation / unit mix**, use `hk-building-programming`. For other topics, see the routing table below.

## When to Use This Skill

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

## 3. HKPSG Facility Provision Ratios

| Facility | Provision Standard |
|---|---|
| Local open space | 1 m²/person (district); 2 m²/person (regional) |
| Car parking (residential) | 1 space per 3–5 units (varies by district; check OZP/TPB) |
| Car parking (office) | 1 space per 200–300 m² GFA |
| Kindergarten | 1 class per 1,000 children aged 3–5 |
| Primary school | 1 class per 1,000 children aged 6–11 |

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

*Sources: HA Schedule of Accommodation, HKPSG 2023, Cap. 132 (10 July 2026), Cap. 172 (1 July 2022), Cap. 279 (1 August 2026), Cap. 349 (1 September 2023), Cap. 459 and Cap. 613 (26 July 2024), Buildings Ordinance Cap. 123.*
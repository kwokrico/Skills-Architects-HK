---
name: hk-acoustic-design
description: HK acoustic design — EPD noise guidelines, MTR/KCR railway noise, road/aircraft noise (EIAO TM), BEAM Plus IEQ acoustic credits, and construction noise permits (Cap.400).
disable-model-invocation: true
---

# HK Acoustic Design

For **worker hearing loss or Cap. 469 Occupational Deafness (Compensation)**, route to `hk-construction-health-safety` and the [Cap. 469 workflow](../../references/hk-labour-safety-legislation.md#cap-469--occupational-deafness-compensation-ordinance). Community/building noise under Cap. 400, occupational noise prevention under Cap. 59 and compensation eligibility are separate assessments.

Primary references: EPD Technical Memorandum on Noise (TME), EIAO Technical Memorandum, Noise Control Ordinance Cap. 400. BEAM Plus NB IEQ acoustic credits.

For **Facade or room acoustic specification**, use `hk-acoustic-design`. For other topics, see the routing table below.

## When to Use This Skill

EPD noise, railway/MTR vibration, construction noise permits, and building acoustic design.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Facade or room acoustic specification | `hk-acoustic-design` | `—` |
| Fire-rated compartmentation | `—` | `hk-fire-life-safety` |
| Environmental planning EIA scoping | `—` | `hk-spatial-planning` |

## Halt criteria

- Noise assessment requires site-specific measurements for compliance claims.
---

## 1. Environmental Noise Criteria (EPD)

| Noise Source | Daytime Limit | Night-time Limit | Source |
|---|---|---|---|
| Road traffic (residential) | 70 dB(A) L10 | 60 dB(A) L10 | EPD TME |
| Railway (residential) | 65 dB(A) Leq | 55 dB(A) Leq | EPD Railway Noise IA |
| Aircraft (residential) | NEF 25 contour | NEF 25 contour | EIAO TM |
| Industrial (residential area) | 60 dB(A) L10 | 50 dB(A) L10 | EPD TME |

---

## 2. Railway Noise (MTR/KCR)

| Aspect | Requirement |
|---|---|
| Impact assessment | EPD Railway Noise Impact Assessment required for residential within 300 m of rail |
| Facade Rw target | ≥ 35 dB (moderate exposure); ≥ 45 dB (high exposure near elevated rail) |
| Mitigation | Acoustic glazing (laminated + air gap); solid spandrel panels; balcony as acoustic buffer |
| Vibration | Structure-borne vibration from underground MTR: floating slab or resilient mounts for residential above tunnels |

---

## 3. Aircraft Noise (Chek Lap Kok)

- NEF 25 contour: residential development discouraged; acoustic treatment required
- NEF 30 contour: residential development not permitted (EIAO TM)
- Check CAAS noise contour maps for Lantau, North Lantau, and Tung Chung sites

---

## 4. BEAM Plus IEQ Acoustic Credits

| Credit | Requirement |
|---|---|
| Airborne sound insulation | STC ≥ 50 (unit-to-unit walls/floors); STC ≥ 55 recommended |
| Background noise (office) | ≤ 40 dB(A) NC |
| Background noise (residential) | ≤ 35 dB(A) NC |
| Reverberation (open office) | RT60 0.5–0.8 s |

---

## 5. Construction Noise (Cap. 400)

| Aspect | Requirement |
|---|---|
| General construction using powered mechanical equipment | Check CNP requirements for 19:00–07:00 and general holidays, including Sundays; designated-area prescribed construction work has additional controls |
| Percussive piling | Separate permit regime; prohibited during restricted hours rather than made permissible by an ordinary night-work CNP |
| Noise assessment | Use the applicable Technical Memorandum, receiver/location, equipment, hours and actual permit conditions; no universal 75 dB(A) CNP limit |

TD lane-closure approval does not establish noise permission. Confirm the activity and conditions before advising that night work can proceed. [EPD construction-noise guidance](https://www.epd.gov.hk/epd/noise_education/web/ENG_EPD_HTML/m3/ordinance_7.html).

---

## 6. Internal Acoustic Separation

| Adjacency | Min STC | Recommended STC |
|---|---|---|
| Residential unit-to-unit (wall) | 50 | 55 |
| Residential unit-to-unit (floor) | 50 | 55 |
| Residential above commercial/F&B | 60 | 65 + floating slab |
| Classroom-to-classroom | 50 | 55 |
| Office-to-office (closed) | 45 | 50 |

---

*Sources: EPD Technical Memorandum on Noise (TME), EIAO Technical Memorandum, Noise Control Ordinance Cap. 400, BEAM Plus NB v2.0 IEQ, EPD Railway Noise Impact Assessment guidelines.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-acoustic-design.md`. The master router links these files directly.

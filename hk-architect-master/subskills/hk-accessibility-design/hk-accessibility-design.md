---
name: hk-accessibility-design
description: Hong Kong barrier-free access — Design Manual Barrier Free Access 2008 (DMBA), PNAP APP-41, BD compliance, accessible routes, ramps, lifts, tactile paving, and MTR interface.
disable-model-invocation: true
---

# HK Accessibility Design

Primary code: Design Manual: Barrier Free Access 2008 (DMBA 2008). BD enforces via BO Cap. 123 and PNAP APP-41. Compliance checked at Building Plan submission stage.

For **DMBA ramps**, use `hk-accessibility-design`. For other topics, see the routing table below.

## When to Use This Skill

Barrier-free access under DMBA 2008 and PNAP APP-41.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| DMBA ramps, lifts, tactile paving, accessible WC | `hk-accessibility-design` | `—` |
| GFA / plot ratio / MOE only | `—` | `hk-building-codes` |
| Site H&S on construction sites | `—` | `hk-construction-health-safety` |

## Halt criteria

- Do not certify BD barrier-free approval without AP submission.
---

## 1. Key Dimensional Requirements (DMBA 2008)

| Element | Requirement |
|---|---|
| Entrance threshold | ≤ 13 mm |
| Accessible route min width | 1200 mm clear |
| Passing space | 1800 × 1800 mm at intervals ≤ 30 m |
| Ramp gradient | 1:12 max; 1:20 preferred |
| Ramp max rise per flight | 500 mm |
| Ramp width | 1200 mm min clear |
| Ramp landing | ≥ 1200 mm at top, bottom, and intermediate landings |
| Lift car min dimensions | 1100 mm (W) × 1400 mm (D) |
| Lift door clear width | 900 mm min |
| Accessible WC turning circle | 1500 mm diameter |
| Accessible WC door clear width | 850 mm min |
| Grab rail height | 700–800 mm AFL (horizontal); 900 mm AFL (vertical) |
| Accessible parking stall width | 3300 mm |
| Accessible parking ratio | Min 1 per 50 spaces |

---

## 2. Tactile Paving (DMBA 2008 Appendix)

| Type | Application |
|---|---|
| Attention (dot pattern) | Hazard warning: top/bottom of ramps, kerb edges, platform edges |
| Directional (bar pattern) | Guide path along accessible routes in public areas |
| Colour contrast | Yellow preferred; min 30% LRV difference from surrounding surface |

Required at: all public entrances, lift lobbies, pedestrian crossings, MTR/public transport interfaces.

---

## 3. BD Submission Requirements

- PNAP APP-41: administrative reference for barrier-free access compliance (Design Manual: Barrier Free Access 2008)
- Barrier-free access plan required as part of General Building Plans submission
- Accessible route must connect: entrance → lift → all floors → accessible WC → all primary spaces
- Exemptions: village houses (NTEH); certain minor works under Cap. 123N

---

## 4. MTR / Public Transport Interface

- Covered accessible route from MTR exit to building entrance (where TOD development)
- Level change between MTR concourse and building podium: lift or ramp required
- Tactile guide path continuous from MTR exit to building lobby

---

## 5. Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| Accessible entrance separate from main entrance | Principal entrance IS the accessible entrance; no separate "accessible entrance" |
| Ramp added post-completion | Level access designed from concept; max 13 mm threshold at all primary entrances |
| Lift omitted in < 3-storey building | Install lift regardless of exemption; DMBA 2008 applies to all new buildings |
| Tactile paving discontinuous | Trace full route from street to all primary destinations; no gaps |

---

## 6. Design Manual on Universal Accessibility 2026

The 2026 manual revamps the Design Manual: Barrier Free Access 2008 (2025 Edition). Except for provisions already in regulations 72 and 73 and the Third and Fourth Schedules of the Building (Planning) Regulations, the manual states that its requirements are at present **advisory**. The Buildings Department intends to propose making obligatory provisions later. Until that change is in force, do not describe a 2026-only dimension as a current statutory minimum. The dimensions below are the manual’s own figures.

| Item | Figure in the 2026 manual |
|---|---|
| Domestic coverage | Full common-area package above four domestic storeys. Size every residential entrance door and every bathroom, kitchen, and toilet floor even in a building of four storeys or fewer |
| Tactile guide path | From the lot boundary for shopping, schools, hospitals, sports complexes, elderly homes, and transport buildings. Hotels and banks need an accessible counter and a visual fire alarm; Table 2 does not require a tactile guide path for them |
| Accessible car bay | At least one bay of 3,500 mm × 5,000 mm (or 4,000 mm × 6,000 mm if it has electric-vehicle charging) on an accessible route to an accessible lift, using the lot-wide ratio, and a higher ratio only when the premises exceed 10,000 occupants |
| Corridors | 1,200 mm clear, with 1,500 mm × 1,500 mm turn near every dead end. Every residential entrance door is 850 mm clear |
| Circulation ramp | 1,200 mm wide, not steeper than 1 in 12, with 1,500 mm square landings |
| Main circulation stair | 300 mm tread / 150 mm riser, rather than the required-stair 225 mm / 175 mm |
| Accessible lift | At least one of 1,200 mm × 1,400 mm with an 850 mm door on every floor. If there are more than three lifts, one of them is 1,500 mm × 1,400 mm to every floor |
| Auditorium | Four wheelchair spaces (800 mm × 1,300 mm) up to 800 seats, then two per 400 seats, on a 1,500 mm passage |
| Hotel | Two accessible guest rooms per 100 rooms, with bathrooms to paragraph 9.3 |
| Sanitary | On each non-domestic floor, one accessible cubicle of at least 1,500 mm × 1,750 mm when there are 20 or fewer water closets, and two when there are more, plus one accessible unisex toilet. The one-per-15 ratio is an advisory rule inside specified premises |

Access for external maintenance is a separate code (2021, 2024 edition) and PNAP ADV-14, not this manual.

---

*Sources: Design Manual: Barrier Free Access 2008 (2025 Edition), Design Manual on Universal Accessibility 2026, PNAP APP-41, Buildings Ordinance Cap. 123, Building (Planning) Regulations 72 and 73.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-accessibility-design.md`. The master router links these files directly.

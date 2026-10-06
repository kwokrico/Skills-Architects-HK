---
name: hk-structural-systems
description: HK structural systems — SUC 2013, SUS 2011, HKWC wind-governed lateral design, transfer slabs, HK residential grid norms, and foundation types for HK ground conditions.
disable-model-invocation: true
---

# HK Structural Systems

Primary codes: Code of Practice for Structural Use of Concrete 2013 (SUC 2013, with the February 2022, June 2023, and April 2024 amendments in the CS library), Code of Practice for the Structural Use of Steel 2011 (2023 edition, with the April 2026 amendment), Code of Practice on Wind Effects in Hong Kong 2019 (December 2023 amendments). Cap. 123Q is the operative construction regulation and replaced repealed Cap. 123B. It is performance-based; the hard numbers live in the codes accepted under PNAP APP-53. Seismic: low (PGA ~0.07g); wind governs lateral design. The 50 m/s gust figure in the table below is retained as the existing practice note in this skill; confirm it against the 2019 wind code for the site.

For **Structural system selection**, use `hk-structural-systems`. For other topics, see the routing table below.

## When to Use This Skill

SUC 2013, SUS, HKWC wind, transfer structures, foundations.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Structural system selection | `hk-structural-systems` | `—` |
| Facade panel fixing | `—` | `hk-building-envelope` |
| RSE certification / submission | `—` | `hk-construction-documentation` |

## Halt criteria

- Structural design certification is RSE-only.
---

## 1. Lateral Design

| Driver | HK Context |
|---|---|
| Primary lateral load | Wind (HKWC 2004); seismic secondary |
| Design wind speed | 50 m/s (3-sec gust, 50-yr return, most sites) |
| Seismic zone | Low; PGA ~0.07g; SUC 2013 Appendix D |
| Lateral system (residential) | RC shear walls (dominant); core + perimeter walls |
| Lateral system (office) | RC core + flat slab; or steel frame + RC core |

---

## 2. Structural Grid Norms

| Typology | Typical Bay Width | Basis |
|---|---|---|
| HA public housing (Harmony) | 3.3–3.6 m | Unit width module |
| Private residential tower | 3.6–4.5 m | Unit width + structural wall |
| Composite podium (parking below) | 8.1–9.0 m | 2 parking stalls + aisle |
| Grade A office (RC flat slab) | 8.4–9.0 m | Open-plan flexibility |
| Grade A office (post-tensioned) | 9.0–12.0 m | PT extends span |

---

## 3. Transfer Slab (Standard HK Element)

| Aspect | Guidance |
|---|---|
| Typical location | L3–L5; podium/tower interface |
| Depth | 1.5–3.0 m (RC); or post-tensioned transfer plate |
| Fix at concept | Transfer level must be fixed at concept; governs grid, M&E risers, unit module above |
| Coordination | Riser positions and unit module above must align with transfer beam/wall grid |
| Loading | Transfer slab carries full tower load; RSE input required at concept stage |

---

## 4. Floor Systems

| System | Span Range | Typical Use |
|---|---|---|
| RC flat slab | 7.5–9.0 m | Office, podium |
| Post-tensioned flat slab | 9.0–12.0 m | Office, transfer |
| RC one-way slab + beams | 4.5–7.5 m | Residential |
| Precast hollow-core | 5.0–8.0 m | HA public housing |

---

## 5. Foundations (HK Ground Conditions)

| Ground Type | Typical Foundation |
|---|---|
| Rock (granite, common in HK) | Rock socket piles or caissons to rock head |
| Fill / marine deposit | Driven precast piles or bored piles through fill to rock/dense sand |
| Reclaimed land (common in HK) | Driven piles; settlement monitoring required |
| Sloped sites | Retaining walls; slope stability assessment (GEO) required |

> GEO (Geotechnical Engineering Office) approval required for slopes and retaining walls.

---

## 6. Concrete Specification (SUC 2013)

| Element | Min Grade | Min Cover |
|---|---|---|
| Foundations (aggressive ground) | C35 | 75 mm |
| Columns / walls | C35–C50 | 40 mm |
| Slabs (internal) | C30 | 25 mm |
| External / exposed | C35 | 50 mm |
| Marine exposure | C40 + silane | 60 mm |

**Construction sequencing:** **Underground lane** (excavation, support, raft) and **standard floor cycle** (rebar → embed → formwork → pour → cure → strike) drive programme critical path for RC towers. Transfer slab level must be fixed before repeating typical cycles. Load `hk-construction-programme` for layered excavation and 7–10 day floor rhythm; confirm ELS type (pile wall vs diaphragm wall) per geotechnical design.

---

## 7. Coordination numbers from Cap. 123Q

Label every floor zone with its Table 1 class and its distributed imposed load before the registered structural engineer freezes the design. The figures below are kilopascals from that table, not class numbers. Offices for general use are 3 kPa; offices for storage and normal filing are 5 kPa. A domestic kitchen follows the domestic 2 kPa load; a kitchen not in domestic premises is 4 kPa. A refuge floor is 5 kPa. A plant room is 7.5 kPa. A utility platform is not less than 4 kPa even where the flat it serves is 2 kPa. Lock the heaviest vehicle (private car, light goods vehicle, or fire appliance on an emergency-vehicular-access ramp) before sizing car-park barriers. **600 mm** is the schematic threshold for barriers at steps, terraces, planter edges, sunken courts, and podium drops, including outdoor areas.

Flag the Mid-Levels Scheduled Area before assuming a deep basement. The Building Authority scrutinises cumulative hillside impact, not only the plot. Exotic materials need agreement in principle early under APP-53. Movement joints and corrosion protection for marine exposure are elevation issues from schematic design, not a late specification.

## 8. Slope maintenance (Geoguide 5, fourth edition, 2023)

Geoguide 5 is guidance. Its recommendations are not mandatory. At schematic design, mark every slope, wall, and natural-terrain measure the lot must maintain, including land outside the boundary where the lease, a natural-terrain clause, or the owner’s own works create that duty, and name the maintaining party.

Include a Maintenance Manual in the design-service scope, with as-built geometry, access, services layouts, the consequence-to-life category, and the monitoring schedule, and state who keeps duplicate records after handover. Routine maintenance inspections follow Table 3.1 and, where they are not more frequent than once a year, finish before the wet season in April. An engineer inspection for maintenance is at the Table 3.3 interval by a registered professional engineer (geotechnical). Provide safe access. If the scheme uses prestressed ground anchors or designed raking drains, put alert levels and contingency actions in the manual before handover. Plan chunam replacement around every ten years, and keep tree roots and cultivation off covers, joints, channels, and the slope crest.

---

*Sources: Code of Practice for Structural Use of Concrete 2013 and its amendments to April 2024, Code of Practice for the Structural Use of Steel 2011 (2023 edition) and the April 2026 amendment, Code of Practice on Wind Effects in Hong Kong 2019 and the December 2023 amendments, Code of Practice for Foundations 2017 (2024 edition, September 2025 amendments), Code of Practice for Dead and Imposed Loads 2011 (2021 edition), Code of Practice for Structural Use of Glass 2018, Code of Practice for Precast Concrete Construction 2016, Building (Construction) Regulation Cap. 123Q (24 June 2021), Geoguide 5 (fourth edition, 2023), GEO Publication No. 1/2006.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-structural-systems.md`. The master router links these files directly.

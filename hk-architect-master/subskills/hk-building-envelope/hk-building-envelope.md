---
name: hk-building-envelope
description: HK building envelope — OTTV/RTTV, BEAM Plus energy credits, HKWC typhoon wind loading, curtain wall for subtropical CZ 1A climate, cladding durability in marine environment.
disable-model-invocation: true
---

# HK Building Envelope

Climate: ASHRAE CZ 1A (hot-humid subtropical, 22.3°N). Primary energy code: EMSD Building Energy Code (BEC) 2021. Performance target: BEAM Plus NB Energy credits.

For **Facade system and typhoon performance**, use `hk-building-envelope`. For other topics, see the routing table below.

## When to Use This Skill

Use section 9 for architectural maintenance/replacement-route reviews from design to handover; refer engineering capacities and safe-work methods to competent specialists.

**Role boundary:** Refer structural capacity/anchors to **Skills-Structural-Engineer-HK**, engineered drainage/systems to **Skills-MEP-Engineer-HK**, and planting/root/soil design to **Skills-Landscape-Architects-HK**. Keep envelope geometry, junction coordination and evidence requests here. Apply the [master referral rule](../../SKILL.md#specialist-role-referrals); state the referral and do not supply the specialist answer from local background tables.

For planting over roofs/podiums and its waterproofing interfaces, use section 8 with the urban-space landscape workflow.

Curtain wall, cladding, typhoon wind, weatherproofing, facade OTTV optimisation, roof/threshold/slab-edge junction coordination and construction-detail review. Section 7 provides the coordinated junction workflow and hypothetical refurbishment example.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Facade system and typhoon performance | `hk-building-envelope` | `—` |
| BEAM Plus credit strategy (whole building) | `—` | `hk-building-sustainability` |
| Structural wind load / HKWC | `—` | `hk-structural-systems` |
---

## 1. OTTV & RTTV Targets

| Metric | BEAM Plus Target | BEC Baseline |
|---|---|---|
| OTTV (non-domestic walls) | ≤ 20 W/m² | ≤ 35 W/m² |
| RTTV (roof) | ≤ 25 W/m² | ≤ 35 W/m² |

Statutory OTTV under Cap. 123M / APP-67, for plans submitted on or after 31 December 2025, is tower ≤ 20 W/m² and podium ≤ 40 W/m². That is the Building Authority floor. The BEAM Plus and BEC columns above are separate targets. See `hk-building-sustainability`.

### 1.1 OTTV Formula

```
OTTV = Σ [Uw × (1-WWR) × TDeq] + Σ [Uf × WWR × ΔT] + Σ [SC × WWR × SF]
```

| Input | Typical HK Value |
|---|---|
| Solar factor (SF), E/W facade | 150–180 W/m² |
| Solar factor (SF), N/S facade | 80–110 W/m² |
| SC target (high-performance glass) | ≤ 0.25 |
| ΔT (indoor–outdoor) | 5–8°C (CZ 1A) |

---

## 2. Glazing Strategy (CZ 1A)

| Facade | WWR Target | SHGC Max | Notes |
|---|---|---|---|
| East / West | 15–25% | 0.25 | External shading essential |
| North / South | 25–35% | 0.35 | Lower solar gain than E/W |
| Residential (all) | 25–35% | 0.35 | BO Reg.30: min 1/10 floor area |

- Low-e double glazing standard for non-domestic; single low-e acceptable for residential
- External shading (horizontal fins, deep reveals, brise-soleil) prioritised over glass spec alone

---

## 3. Typhoon Wind Loading (HKWC 2004)

| Parameter | Value |
|---|---|
| Design wind speed (most HK sites) | 50 m/s (3-second gust, 50-yr return) |
| Exposure category | Varies by terrain; Category 1 (open sea) to Category 3 (urban) |
| BD requirement | Wind load test certificates required for curtain wall and cladding systems |
| Fixings | Stainless steel or aluminium alloy; mild steel not acceptable in exposed locations |

---

## 4. Curtain Wall (HK High-Rise Practice)

| Aspect | HK Norm |
|---|---|
| System type | Unitised curtain wall dominant above 15 storeys |
| Pressure equalisation | Required; drained-and-ventilated cavity |
| Air infiltration | ≤ 1.5 m³/h·m² at 600 Pa (AAMA 501) |
| Water penetration | No leakage at 720 Pa (AAMA 501) |
| Thermal movement | Accommodate ±25 mm inter-storey drift (typhoon) |
| Maintenance | BMU/cradle track required; load into structure from concept |

---

## 5. Roof

| Strategy | Target |
|---|---|
| Reflective coating | SRI ≥ 78 (BEAM Plus SA credit) |
| Green roof | Reduces RTTV; BEAM Plus SA greenery credit |
| Insulation | R ≥ 2.0 m²K/W (RTTV compliance) |
| Drainage falls | Min 1:60 (1:40 preferred); secondary overflow scupper at +50 mm |

---

## 6. Durability (Marine/Subtropical Exposure)

| Material | Recommendation |
|---|---|
| Facade framing | Aluminium alloy (6063-T5 or 6061-T6) |
| Fixings | Grade 316 stainless steel minimum |
| Sealants | Neutral-cure silicone; 10-yr replacement cycle |
| Concrete (exposed) | C35 min; 50 mm cover; silane impregnation for coastal sites |
| Steel (exposed) | Hot-dip galvanised + paint system; or weathering steel where aesthetically appropriate |

**Construction sequencing:** Facade works typically **follow-the-structure** — start when superstructure is ~5–7 floors below top (lane 5: frame, sealant, waterproofing, cladding, clean). Coordinate long-lead aluminium and curtain wall packages with procurement lane 9. Load `hk-construction-programme` for full facade swimlane steps.

---

*Sources: EMSD Building Energy Code 2021, BEAM Plus NB v2.0, Code of Practice on Wind Effects in Hong Kong 2004 (HKWC), ASHRAE 90.1-2022 (CZ 1A), AAMA 501.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-building-envelope.md`. The master router links these files directly.

## 7. Junction coordination and design review

Use for facade, roof, podium and wet-area interfaces in Hong Kong projects. Apply the shared [detail checklist](../hk-construction-documentation/hk-construction-documentation.md#61-architectural-detail-coordination).

**Inputs:** current architectural/structural/MEP details, performance brief, exposure/movement assumptions, facade/waterproofing system information, finished levels, access constraints and installation sequence. Distinguish design intent from reviewed specialist/shop details. Missing evidence remains an open action; generic tables do not establish project acceptance criteria.

| Interface | Architect coordinates | Specialist inputs and closure evidence |
|---|---|---|
| Roof/parapet | Coping/membrane/outlet continuity and inspection access | Support, system compatibility, drainage; coordinated section and test/inspection plan |
| Facade/slab edge | Control layers and internal finish/ceiling interfaces | Engineer's movement/anchors, facade system and fire stopping where applicable; matching assumptions/tolerances |
| External threshold | Finished levels, weather resistance, door operation and accessible route | Drainage, waterproofing, door system and accessibility review; coordinated details |
| Wet-area penetration | Membrane continuity and trade ownership | Services location, compatible seals and fire/acoustic review where applicable; inspection before concealment |
| Movement joint | Continuity through finishes and waterproofing; repair access | Engineer's movement range and compatible system; no generic joint width |

### Hypothetical example: occupied podium terrace refurbishment

**Given:** rain-related leakage occurs near a lobby door. The client wants a flush route; proposed paving changes finished levels, the outlet position is uncertain and slab-edge details are unavailable. These are illustrative facts, not a standard construction solution.

1. **Investigate:** survey door/slab/finish levels, photograph staining, map drainage and record leakage conditions. Keep membrane, door-perimeter, drainage and services failures as competing hypotheses; a stain does not identify the failed layer.
2. **Define the clash:** establish whether the accessible threshold, drainage and waterproofing termination can coexist within surveyed geometry. Do not solve it by adding a step or cutting the slab without the relevant reviews.
3. **Assign actions:** architect coordinates survey/door/route; drainage designer confirms outlets/overflow; facade/waterproofing specialists develop compatible terminations; structural engineer checks alterations; AP assesses submission implications; management coordinates access and occupied-area protection.
4. **Compare:** retaining the door with revised drainage/finishes versus replacing the threshold assembly. Record access, weather resistance, maintenance, disruption and cost consequences; neither option is accepted without interface evidence.
5. **Verify:** agree representative mock-up/sample where appropriate, inspection before concealment and project-specific water-test method/acceptance criteria. Agree test loads and occupied-area protection; do not prescribe arbitrary flooding. A successful sample supports only the tested assembly/conditions.
6. **Decide:** hold the affected construction detail pending survey and specialist review. A bounded investigation package may proceed within its agreed limits.

**Output:** junction/location; drawing revisions; requirements/sources; observations; unknowns; options; design/trade owners; inspection/test plan; residual risks; release status. Feed resolved changes into the documentation QA log.

## 8. Landscape over structure and waterproofing interfaces

Start with the [landscape interface register](../hk-urban-space-statutory/hk-urban-space-statutory.md#10-landscape-and-building-interface-coordination). Request the actual planting/build-up, structural assessment, surveyed levels, drainage/irrigation design, waterproofing/root-protection system and maintenance strategy.

Trace water from planting/irrigation to the designed drainage and overflow routes. Coordinate membrane termination, protection, penetrations, movement joints, thresholds and accessible outlets with the landscape/drainage/structural designers. Keep saturated build-up/load assumptions with the engineer and growing-medium/root requirements with landscape specialists; no generic depth or loading is prescribed here.

Define who inspects the substrate and waterproofing before covering, how test conditions protect occupied premises, and how later planting work avoids damage. Confirm access to find leaks, clear outlets and replace planting or membrane; warranty wording does not establish practical repairability. Refer the section 7 junction example for the shared review method.

**Return:** coordinated section/revisions; load/drainage/design assumptions; system compatibility evidence; trade interfaces; hold points and testing criteria to agree; maintenance access; open issue owners. Do not release covering-up or affected construction details on unresolved waterproofing, structural or drainage evidence.

## 9. Maintenance access and replacement review

Use from concept through handover to test whether architectural envelope elements can actually be inspected, cleaned, repaired and replaced. Apply the [role-referral rule](../../SKILL.md#specialist-role-referrals). Structural capacity, anchors and temporary support go to **Skills-Structural-Engineer-HK**; engineered access equipment/services to **Skills-MEP-Engineer-HK** or the appropriate competent specialist; planting access to **Skills-Landscape-Architects-HK**. Do not specify rope-access, lifting or other specialist safe-work methods here.

**Inputs:** element/asset list, geometry/levels, proposed systems, supplier maintenance/replacement information, access rights/common-part boundaries, FM capabilities, occupied-area constraints and specialist access proposals. Unavailable weights, dimensions or anchor evidence stay unresolved.

1. Walk each maintenance task from arrival/storage to work position and removal/disposal route. Check doors, lifts, corners, working space, public/tenant disruption and permissions without assuming structural or equipment capacity.
2. Review inspection/cleaning access, replaceable joints/panels, removable covers and access to outlets or concealed interfaces. Coordinate with landscape and services so later work need not damage adjoining systems.
3. Refer required clearances, loads, lifting/support and safe methods to the appropriate specialists. A drawn access route does not prove safe access or a capacity check.
4. Compare options before design freeze; record repairability, interruption, replacement availability and cost dependencies. Feed geometry changes into documentation QA.
5. At handover reconcile the as-built route/details with the reviewed strategy and FM instructions. Record blocked/unverified routes, restrictions and owners; use [operational readiness](../hk-practical-completion-snagging/hk-practical-completion-snagging.md#11-operational-readiness-and-aftercare-handoff).

**Access record:** element/location; task/frequency basis supplied by responsible specialist; route/drawing revision; required space/load evidence; access rights; occupied-area effects; specialist/owner; inspection or demonstration evidence; unresolved limitation; status.

**Boundary case:** replacement glazing fits the elevation but the proposed delivery route has an unverified lift limit. Refer load/lifting and equipment checks to the relevant specialists; coordinate alternative spatial routes without inventing allowable loads. A manufacturer's warranty does not prove replaceability.

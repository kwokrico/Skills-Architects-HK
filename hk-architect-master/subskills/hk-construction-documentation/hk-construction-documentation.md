---
name: hk-construction-documentation
description: HK construction documentation — BD statutory submissions, AP/RSE/RC appointments, OP process, PNAP references, GS specifications, and Minor Works regime (Cap.123N).
disable-model-invocation: true
---

# HK Construction Documentation

BD statutory workflow governs all documentation milestones. Authorized Person (AP) is the lead professional; Registered Structural Engineer (RSE) and Registered Contractor (RC) are statutory appointments.

For **General building plans / submission drawings**, use `hk-construction-documentation`. For other topics, see the routing table below.

## When to Use This Skill

**Role boundary:** Refer BIM production/configuration to **Skills-BIM Manager-HK**, detailed interiors to **Skills-Interior-Designer-HK**, and specialist engineering designs to the corresponding role skills. Retain architectural document QA and coordination. Apply the [master referral rule](../../SKILL.md#specialist-role-referrals); state the referral and do not supply the specialist answer from local background tables.

BD submission packages, AP/RSE drawings, GS, compliance documentation, pre-issue drawing/schedule/specification QA and architectural detail coordination. For technical review use section 6; release decisions hand off to deliverables/workstages.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| General building plans / submission drawings | `hk-construction-documentation` | `—` |
| Who receives which issue pack by stage | `—` | `hk-deliverables-workstages` |
| Site supervision during build | `—` | `hk-site-supervision` |
---

## 1. BD Statutory Submission Workflow

| Stage | Form / Submission | Purpose |
|---|---|---|
| AP/RSE appointment | Form BA1 | Notify BD of AP/RSE appointments |
| Building Plan submission | General Building Plans + drainage + structural | BD approval of design |
| Commencement | Form BA7 (Notice to Commence) | Notify BD before works start |
| Supervision | Supervision plan; site inspection records | AP/RSE statutory duties |
| Completion | BA13 new-building completion/OP application; BA12 temporary OP; BA14 for works not resulting in a new building or street works | Appropriate statutory professionals certify the applicable scope; application is not permit issuance |
| Occupation Permit | OP application + FSD/BD inspections | Legal occupation of building |

---

## 2. Drawing Set Requirements (BD Submission)

| Drawing Type | Submitted To | Key Content |
|---|---|---|
| General Building Plans | BD | Site plan, floor plans, sections, elevations, GFA schedule |
| Drainage Plans | BD | Stormwater and foul drainage; DSD compliance |
| Structural Plans | BD (RSE) | Foundation, structural framing, transfer slab |
| Fire Services Plans | FSD | Sprinkler, hose reel, alarm, smoke extraction |
| Barrier-Free Access Plan | BD | DMBA 2008 compliance; PNAP APP-41 |

---

## 3. PNAP Administrative References

| PNAP | Subject | When to Reference |
|---|---|---|
| APP-2 | GFA and non-accountable GFA | All submissions; GFA schedule |
| APP-40 | Hotel development | Hotel submissions |
| APP-41 | Barrier-free access (Design Manual: Barrier Free Access 2008) | Accessibility drawings |
| APP-130 | Means of escape | MOE drawings |
| APP-152 | Sustainable Building Design Guidelines | Concept and GBP when separation, setback, or greenery is in play |
| ADV-36 | Amenity features (balconies, utility platforms) | Residential projects |
| ADV-49 | Green and innovative buildings | BEAM Plus projects |

---

## 4. Specification Standards

| Project Type | Specification Reference |
|---|---|
| Government / public works | General Specification for Building (GS) — DEVB |
| HA public housing | HA Standard Specification |
| Private development | HKIA/consultant practice spec; NBS or bespoke |
| Minor works | Simplified spec per Cap. 123N requirements |

---

## 5. Minor Works Regime (Cap. 123N)

| Class | Scope | Requirement |
|---|---|---|
| Class I | Larger minor works (e.g. external wall repair, new partition) | Registered Minor Works Contractor (RMWC); supervision certificate |
| Class II | Medium minor works | RMWC; self-certification |
| Class III | Small minor works (e.g. internal partition ≤ 25 m²) | RMWC; notification only |

---

*Sources: Buildings Ordinance Cap. 123, Building (Minor Works) Regulation Cap. 123N, PNAP APP-2/APP-40/APP-130/APP-152/ADV-36/ADV-49, General Specification for Building (DEVB), HA Standard Specification.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-construction-documentation.md`. The master router links these files directly.

## 6. Pre-issue drawing, schedule and specification QA

Use for a Hong Kong statutory, tender or construction package, including refurbishment. This is architect-led coordination review, not BD/FSD approval or a replacement for specialist design checks.

**Inputs:** issue purpose and package boundary; drawing/specification register and revisions; coordinated consultant information; approved/submitted plans and authority comments where relevant; design brief; survey baseline for existing works; unresolved changes. Record missing inputs. The latest filename is not necessarily the approved or coordinated revision.

For each compliance-critical criterion, identify its applicable instrument/edition/clause or project requirement and reviewer. Summary tables are orientation, not automatic acceptance criteria: verify their applicability and currency before using figures. A supplier detail does not establish statutory acceptance.

### Review sequence

1. Freeze the dated document/revision list for review. Distinguish submission, tender and construction status.
2. Trace rooms, cores, facade bays, wet areas and typical/non-typical floors across plans, sections, elevations and details. Record sampling and exclusions; do not call an unchecked set reviewed.
3. Complete the matrix below. An inaccessible or missing item is `Not checked`, not a pass.
4. Assign discrepancies to design owners: structural loads/openings to the structural engineer; services capacity to MEP; fire/accessibility applicability to the appointed competent reviewers.
5. Identify affected drawings, calculations, schedules, specifications and quantities. Ask the AP to assess submission/approval implications; contractor or client agreement is not that assessment.
6. Inspect revised documents to close issues, rather than accepting a reply saying “done”. Hand the checked set to [package release](../hk-deliverables-workstages/hk-deliverables-workstages.md#7-package-release-after-technical-review).

| Check | Compare | Closure evidence |
|---|---|---|
| Geometry and levels | Grids, dimensions, datums, slab/finish/ceiling levels | Matching plans/sections; distinguish structural and finished levels |
| Rooms and circulation | Uses, occupancy assumptions, doors, escape/access routes | Matched IDs and applicable fire/accessibility review |
| Envelope | Elevation bays, opening schedules, sections, junctions | Matching geometry/performance, tolerances and specialist inputs |
| Wet areas | Build-ups, falls, outlets, thresholds, membranes | Coordinated levels/drainage; resolved penetrations |
| Structure/services | Openings, sleeves, plant zones, risers and access | Engineer agreement on the same revision; no assumed capacity |
| Specifications | Product/finish/hardware codes and performance | Consistent documents or contract-specific conflict resolution; no invented precedence |
| Issue status | Revisions, superseded sheets, authority comments | Correct register and affected-discipline review evidence |

### QA record

| ID / location | Documents + revisions | Conflict / missing input | Requirement/source | Owner / due date | Affected outputs | Closure evidence/checker | Status |
|---|---|---|---|---|---|---|---|
| QA-01 / lobby door | Plan Rev C; schedule Rev B | Swing/hardware disagree | Confirm design and applicable escape/accessibility requirements | Architect + relevant reviewers / before issue | Plan, schedule, detail, specification | Revised matching set pending | Open — hold affected construction information |

Statuses: `Open`, `Awaiting information`, `Resolved — pending recheck`, `Closed`, `Not checked`. Record severity separately: safety/statutory, functional/buildability or editorial. Open safety/statutory or critical interface issues block affected construction information. A bounded information-only issue needs explicit exclusions and dependency checks so it cannot be mistaken for construction instructions.

### 6.1 Architectural detail coordination

For roof/parapet, facade/slab edge, wet-area, threshold, movement-joint and penetration details, check:

- continuity of water, air, thermal, fire and acoustic control layers where applicable;
- support, movement, substrate, fixing zones and installation tolerances;
- finished levels, drainage/overflow, accessibility and door operation;
- material compatibility and continuity at corners, ends and penetrations;
- installation sequence, trade ownership, inspections before concealment and agreed testing;
- cleaning, repair and replacement access without damaging adjoining work.

Obtain unresolved dimensions/performance values from the applicable design, specialist or tested system. Do not substitute generic falls, joint widths, upstands, test pressures or fire ratings. Use the [envelope example](../hk-building-envelope/hk-building-envelope.md#7-junction-coordination-and-design-review) and return changes to the QA record.

## 7. Model and drawing consistency at the BIM interface

Use for architectural information QA, not BIM system administration or automated statutory certification. Refer model federation, export configuration, script execution and model health to **Skills-BIM Manager-HK**. See the [handoff workflow](../hk-deliverables-workstages/hk-deliverables-workstages.md#8-architect-to-bim-manager-handoff).

**Inputs:** agreed delivery requirements, source/exported model versions, drawing/schedule/specification revisions, authoring/export dates, coordinates/levels, view/phase settings and unresolved issues. If a model is unavailable, limit conclusions to the supplied documents and request the missing evidence.

Compare room/door IDs and uses, levels/dimensions, openings, facade types and schedules across the actual deliverables. Check whether annotations/manual overrides, hidden/phased elements or export filtering explain a discrepancy; ask the BIM manager to investigate technical causes. A model area calculation does not decide GFA exemption eligibility or statutory compliance.

Record the conflicting values and revisions without assuming model or drawing precedence. Obtain the relevant design decision and contract/information requirements; recheck the revised model export and sheets, including dependent schedules and consultant interfaces. Preserve issue lineage and do not silently modify source models to match one document.

**Return:** issue ID; element/location; model/export and document revisions; discrepancy; architectural decision required; BIM/specialist referral; affected outputs; reviewer; closure evidence; status. Apply the existing technical QA and release gates.

**Hypothetical case:** the clash report is clear, but an exported door schedule disagrees with the latest architectural plan and equipment maintenance clearance was excluded from clash rules. Keep both questions open. Refer export/rule-set investigation to BIM management and clearance criteria to **Skills-MEP-Engineer-HK**. The architect coordinates the door/layout decision; release waits for revised deliverables and relevant evidence, not the green clash count.

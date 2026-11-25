---
name: hk-site-supervision
description: Activate for AP/RSE site supervision during construction, site supervision plans, regular site meetings, deviation handling, completion certification workflows (Form BA14/BA12/BA13), audit and compliance checks, and handover preparation toward occupation permit stage.
disable-model-invocation: true
---

# HK Site Supervision
Covers the AP/RSE supervisory role during construction, including supervision planning, site governance, deviation control, statutory completion forms, and transition to Occupation Permit stage.

---

For **Site supervision and BA forms**, use `hk-site-supervision`. For other topics, see the routing table below.

## When to Use This Skill

For product submittals, substitution evidence and checks of delivered/installed products, use section 8. Keep technical recommendation, contractual authorisation and physical inspection separate.

AP/RSE site supervision, deviations, BA12/13/14, construction-phase AP duties.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Site supervision and BA forms | `hk-site-supervision` | `—` |
| Contract CA certificates | `—` | `hk-tender-contract-administration` |
| Site H&S incidents | `—` | `hk-construction-health-safety` |
## 1. Role of AP / RSE During Construction
- **AP (Authorized Person):** Overall statutory coordinator for compliance with approved plans, Buildings Ordinance requirements, and inter-disciplinary integration.
- **RSE (Registered Structural Engineer):** Responsible for structural compliance, site inspections for structural elements, and certification of structural works.
- **RGE / RC (where applicable):** Provide geotechnical and contractor-side statutory duties; AP/RSE remain accountable for their own certifications.

### Statutory split (Cap. 123)

From the Cap. 123 summary (1 March 2026). The summary does not print subsections 9(5) and 9(6) as separate tests, so those subsection numbers are not restated here.

| Who | Section | Duty as summarised |
|---|---|---|
| AP, RSE, RGE | s.4(3) | Supervise in accordance with the supervision plan. Notify the Building Authority of any regulation contravention that would result from carrying out works shown on the approved plan. Comply with the Ordinance generally |
| RGBC, RSC | s.9 | Continuously supervise under their supervision plan. Notify the Building Authority of an approved-plan regulatory contravention. Comply generally. Specialized works need the RSC registered in the matching category |

The s.4(3) duty and the contractor’s continuous duty under s.9 are separate. One does not discharge the other.

Core principle: supervision is not only quality control; it is legal risk control tied directly to consent, completion acknowledgment, and OP readiness.

---

## 2. Site Supervision Plan (SSP) Framework
Typical SSP components should define:
1. **Inspection levels and frequency** (critical hold points vs routine checks).
2. **Responsible parties** (AP/RSE/inspectors/contractor representatives).
3. **Records and evidence** (site photos, test reports, checklists, marked-up drawings).
4. **Escalation paths** for non-conforming works.
5. **Submission linkage** to BA forms and record plans.

Practical baseline:
- Increase inspection frequency for foundations, transfer structures, fire compartment interfaces, and major facade anchorage works.
- Ensure SSP aligns with BD acceptance conditions under current consent.

**Construction sequencing:** Contract **hold points** (lane 10 — rebar, formwork, concrete, waterproofing, doors, fire) should mirror the SSP and contractor ITP. Load `hk-construction-programme` for the full swimlane map and HK substitutions (e.g. 連續壁 → pile wall/ELS where applicable).

---

## 3. Site Meeting and Reporting Protocol
Maintain a structured cadence:
- **Weekly site meeting:** progress, safety interfaces, quality deviations, pending inspections.
- **Technical coordination meeting:** AP/RSE/consultants for unresolved design-construction conflicts.
- **Regulatory tracker:** open comments, BD/FSD/LandsD-related actions, and deadlines.

Minimum meeting outputs:
- Clear action owner and due date.
- Classification of issues: informational, minor deviation, major deviation, safety-critical.
- Updated risk log tied to statutory submissions and program milestones.

---

## 4. Deviation Handling (As-built vs Approved)
Use a triage approach:
1. **Identify deviation** from approved plan.
2. **Assess impact** on GFA, MOE, structure, fire safety, BFA/access, and lease constraints.
3. **Classify** as potentially minor (recorded in record plan) or major (amendment approval first).
4. **Implement corrective action** or submit amendment before completion certification.

High-risk triggers that usually need prior formal action:
- Changes reducing exit width or increasing travel distance.
- Structural member size/detail changes affecting load path.
- Changes increasing GFA/site coverage/encroachment.
- Material substitutions affecting FRR or code compliance.

---

## 5. Completion Forms and Certification Path
Key completion instruments:
- **Form BA14:** Completion certificate for works not resulting in a new building, or street works; check applicable variants.
- **Form BA12:** Certificate and application for a temporary occupation permit.
- **Form BA13:** New-building completion certificate and OP application, not the issued permit. See [OP form guidance](../hk-op-submission-strategy/hk-op-submission-strategy.md#2-select-the-form-for-the-actual-works).

Typical sequence logic:
1. Complete works and close non-conformities.
2. Finalize as-built and supporting records.
3. File completion package (including relevant BA form pathway).
4. Resolve BD comments/audit picks.
5. Proceed to OP application and issuance workflow.

Always verify the latest BD circulars/PNAP updates for exact form usage and documentary requirements by work type.

---

## 6. Audit and Compliance Checks
Before filing completion/OP submissions, run a pre-audit pack:
- Approved vs as-built drawing reconciliation.
- Test certificates and inspection logs completeness.
- Fire safety installations and means of escape consistency.
- Accessibility and statutory dimensional checks.
- Outstanding RFI/defect and concession status.

Recommended output:
- A signed compliance matrix linking each statutory requirement to objective evidence.

---

## 7. Handover to OP Stage
Handover package from supervision to OP closing should include:
- Final record drawings and revision control log.
- Completion certifications and test report index.
- Outstanding punch list with responsible party and closeout date.
- Operational constraints to be reflected in building management handover.

Program tip: include explicit float between practical completion and BA12/BA13 milestones for audit comments and documentation reconciliation.

---

*Sources to check on live projects: Buildings Ordinance Cap. 123 (1 March 2026) ss.4(3) and 9, current PNAP series, accepted SSP guidance, approved plans and consent conditions, and latest BD form instructions. Summary: `hk_s_reference/Building Department (BD)/Cap 123 Building Ordience/Cap 123 (01-03-2026)_Buildings Ordinance_CS.md`.*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-site-supervision.md`, `references/catalogues/pnrc-hk-site-supervision.md`, `references/catalogues/pnrc-index.md`. The master router links these files directly.

## 8. Product submittal and installation verification

Start with [technical comparison](../hk-material-selection/hk-material-selection.md#7-product-evidence-and-substitution-review) and [contract decision](../hk-tender-contract-administration/hk-tender-contract-administration.md#13-product-substitution-and-contract-change-control). Neither alone proves the delivered or installed product matches the reviewed system.

**Inputs:** reviewed submittal/revision and conditions, authorisation, product/batch identity, samples, delivery records, test reports, method and inspection/test plan. Identify competent specialist reviewers and the person with contractual authority to instruct corrective action.

1. Match product/model/batch and accessories to the reviewed selection; record discrepancies before incorporation. Appearance is not identity evidence.
2. Check storage, substrate, preparation, fixings, joints and installation against reviewed information. Refer structural, MEP or specialist landscape/interior questions to the corresponding role skill rather than supplying technical designs here.
3. Observe agreed hold points before concealment; record location, date, witnesses, photos, test scope/results and unchecked areas. Sampling does not establish all work.
4. Raise non-conformances, notify designer/contract administrator and obtain the appropriate hold/remedial instruction. Do not invent inspector authority or retrospectively approve a changed assembly.
5. Reinspect corrected work and collect evidence; update as-built/product and warranty/O&M records after resolution.

**Record:** system/product ID; location/batch; reviewed baseline; authorisation; observation/test; limitation; discrepancy; owner/action/date; reinspection evidence; status. Use `Not inspected` or `Awaiting evidence` where appropriate.

**Boundary case:** facade panels arrive with different fixings. Return the unresolved deviation for specialist and contractual review even if the supplier claims equivalence. Neither an appearance check nor a delivery note closes assembly performance.

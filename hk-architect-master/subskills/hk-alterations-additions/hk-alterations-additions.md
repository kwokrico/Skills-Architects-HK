---
name: hk-alterations-additions
description: >
  Dedicated to Alterations & Additions (A&A) works in existing buildings. Covers the distinction between 
  formal BD plan submissions and Minor Works (MWCS), structural implications, fire safety upgrades 
  (FS Code 2011/2012), UBW rectification, and coordination with Incorporated Owners (IO).
disable-model-invocation: true
---

# HK Alterations & Additions (A&A)
Expert guidance on modifying existing building stock in Hong Kong, focusing on regulatory pathways (Full A&A vs. Minor Works), structural stability, and fire safety compliance under the Buildings Ordinance.

---

For **A&A scope and approval pathway**, use `hk-alterations-additions`. For other topics, see the routing table below.

## When to Use This Skill

A&A in existing buildings, major alterations, interface with MWCS, acquisition/refurbishment due diligence and diagnostic survey briefs. Use section 7 for general investigation; prescribed MBIS/MWIS and suspected UBW retain their specialist routes.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| A&A scope and approval pathway | `hk-alterations-additions` | `—` |
| Small-scale MWCS items | `—` | `hk-minor-works` |
| UBW on existing building | `—` | `hk-unauthorised-building-works` |
## 1. Regulatory Pathways: A&A vs. Minor Works
Determining the submission route is the first critical step in any Hong Kong refurbishment project.

| Route | Scope of Work | Authority Process |
|---|---|---|
| **Major A&A** | Structural changes, change of use (e.g., Office to Hotel), major GFA increases, or new mezzanine floors. | Full submission to BD via AP/RSE/RGE; requires "Approval" and "Consent" (Form BD24). |
| **Minor Works (MWCS)** | Standardized works (Class I, II, III) such as internal staircases, cladding, or signboards per PNAP APP-147. | Simplified "Notification" (Form MW01/03/05); no prior approval required for Class II/III. |
| **Exempted Works** | Internal non-structural works that do not affect the drainage or structural integrity (Section 41 of BO). | No submission required, but must still comply with Building Regulations. |

---

## 2. Structural & GFA Considerations
A&A works must not overstress existing foundations or exceed the Permissible Plot Ratio/GFA allowed under the prevailing OZP.

### 2.1 Structural Justification
* **Loading Verification:** Any increase in live loads (e.g., converting a godown to an office) requires an RSE to certify the existing slab capacity.
* **Structural Strengthening:** Carbon fiber wrapping (FRP) or steel plate bonding must be detailed and submitted for BD approval if modifying structural elements.
* **Unauthorized Building Works (UBW):** BD generally requires the rectification of existing UBWs within the "affected area" of the A&A before granting approval.

### 2.2 GFA and Site Coverage
* **PNAP APP-2:** Check if new A&A features (like glass canopies or plant rooms) can be exempted from GFA.
* **Validation:** New mezzanine floors count towards GFA and must meet Reg. 30 (L&V) and Reg. 31 (Headroom).

---

## 3. Fire Safety Upgrades (Code of Practice 2011)
A&A works often trigger a "Change of Use" or "Material Alteration" which necessitates upgrading existing fire safety provisions.

### 3.1 Means of Escape (MOE)
* **Travel Distance:** New partitions must not create dead-ends exceeding 6m (unsprinklered) or 15m (sprinklered).
* **Exit Capacity:** Changes in occupancy (e.g., retail to F&B) require re-calculation of the discharge value for existing staircases.

### 3.2 Fire Resisting Construction (FRC)
* **Compartmentation:** New openings in floors or fire walls must be protected by FD60/FD120 fire shutters or doors.
* **External Walls:** A&A involving curtain wall replacement must maintain the 900mm non-combustible spandrel (protected zone) between floors.

---

## 4. Coordination & Management
### 4.1 Deed of Mutual Covenant (DMC) & IO
* A&A works involving common parts (e.g., external walls, rooftops) require consent from the **Incorporated Owners (IO)** or Management Office.
* Architects must review the DMC to ensure proposed works do not encroach on "Common Areas" or "Non-Exclusivity" zones.

### 4.2 Occupation Permit (OP) & Acknowledgement
* Upon completion of major A&A, a **Form BA14** (Completion Certificate) is submitted.
* For major changes of use, a new **Occupation Permit (OP)** or a "Temporary Occupation Permit" may be required.

---

## 5. Key PNAP Reference Index for A&A
| PNAP | Subject |
|---|---|
| **APP-147** | Minor Works Control System (MWCS) - Classes and Requirements |
| **APP-117** | Alterations and Additions Works in Existing Buildings (Submission Guidelines) |
| **APP-98** | Structural Requirements for A&A Works |
| **APP-47** | Fire Safety (Buildings) Ordinance Cap. 572 (Upgrading existing buildings) |
| **ADV-33** | Essential Services and Facilities for A&A Works |

---
## 6. Multi-owned buildings (Cap. 344)

The Building Management Ordinance is not a design code. It locks flat versus common parts, deed-of-mutual-covenant overrides, and owners’ corporation powers. From 13 July 2025 it also sets procurement gates for high-value or large-scale maintenance.

Enclosing a corridor, roof, external wall, light well, or podium garden into a flat, shop, or exclusive terrace needs the statutory and deed approval path before the general arrangement is frozen. An exclusive roof, balcony, garden, or shopfront still carries a duty to maintain. Design common risers, stacks, and fire service installations inside flats knowing the corporation will need access rights. Once a management committee is appointed, it is the owners’ committee for deed purposes.

Prescribed inspection and repair under MBIS/MWIS is `hk-mandatory-inspection`, not a substitute for this alteration path. Fire-safety directions on pre-1987 stock are `hk-fire-life-safety`.

---

*Sources: Buildings Ordinance Cap. 123, PNAP APP-117, PNAP APP-147, Fire Safety Code 2011, Building Management Ordinance Cap. 344 (13 July 2025), Practice Notes for Mandatory Building Inspection (route to `hk-mandatory-inspection`).*

Catalogue detail for this topic is in `references/catalogues/pnap-hk-alterations-additions.md`. The master router links these files directly.

## 7. Existing-building due diligence and diagnostic survey

Use for acquisition, lease/fit-out feasibility, refurbishment or change-of-use investigation. This architect-led workflow is not a structural certificate, valuation, legal title opinion or automatic MBIS/MWIS inspection. Route prescribed inspections to [mandatory inspection](../hk-mandatory-inspection/hk-mandatory-inspection.md#7-interface-with-general-due-diligence).

### 7.1 Survey brief and required inputs

Record purpose/intended reliance, site/lot and premises, proposed use/works, ownership/common-part boundaries, occupied areas, access permissions, survey date, records, exclusions and specialist appointments. Separate visual/measured/non-intrusive inspection from proposed opening-up/testing. Obtain authorisation and competent safety planning before intrusive work; a survey appointment does not automatically authorise disturbance.

Request approved plans/amendments, applicable OP/completion records, measured/as-built drawings, structural/MEP records, repair/test history, orders/notices/directions and closure evidence, lease/DMC information and management/occupant reports. Obtain relevant OZP/lease records when assessing use or redevelopment feasibility. Record unavailable information; a missing drawing or unanswered search is not proof of legality or illegality.

### 7.2 Investigation sequence

1. **Reconcile records:** list date, source, status and coverage. Distinguish approved plans from as-built drawings, marketing plans and sketches. Identify contradictions before selecting survey priorities.
2. **Plan access:** agree arrangements for occupied units, common areas, roofs, facades and concealed services with owners/management. Assess hazardous-material and service-isolation needs with specialists before disturbance.
3. **Observe:** record element/location ID, photos, safely measured extent, inspection conditions and exclusions. Separate observation, reported history and hypotheses. Visual review cannot establish hidden reinforcement, structural capacity or membrane continuity.
4. **Triage:** distinguish urgent safety, possible statutory/record discrepancies, performance defects and maintenance issues. For apparent instability, falling components or compromised escape, stop unsafe inspection, promptly alert the owner/manager and seek competent assistance; use emergency services for immediate danger. Do not wait for the final report to communicate urgent concerns.
5. **Investigate selectively:** structural engineer for capacity/cracking; MEP for services/drainage; facade/waterproofing specialists for envelope defects; appropriate hazardous-material specialist before suspect materials are disturbed. Define the question, scope, permissions and output of each investigation.
6. **Assess conditionally:** compare repair, retention, alteration or further investigation against evidence and the brief. Separate building, planning, lease, management and licensing questions; refer each to the relevant AP/specialist/legal adviser. Verify applicable criteria rather than applying generic numerical shortcuts.
7. **Report and follow through:** assign each finding an owner and decision date. Close risks only when new records, tests or reviewed design evidence address the original question.

### 7.3 Deliverables and example risk register

**Survey brief:** purpose/reliance; areas/elements; records supplied/missing; access/exclusions; methods; specialist investigations; occupation/safety constraints; reporting format; programme; limitations and follow-up triggers.

| ID / element | Observation/evidence | Hypothesis / unresolved question | Decision affected | Follow-up owner | Status / closure evidence |
|---|---|---|---|---|---|
| DD-01 / soffit below terrace | Staining photographed; outlet inaccessible | Membrane, drainage or service source unconfirmed | Repair scope and occupied-space protection | Architect arranges access; drainage/envelope specialists investigate | Open; diagnosis and remedy not established |
| DD-02 / partition opening | On site, absent from available drawing | Later approval/exemption/minor-works evidence missing | Alteration feasibility and records position | AP checks records/works; structural/fire reviewers as needed | Awaiting information; mismatch alone is not a legal conclusion |
| DD-03 / roof | No safe access | Condition unknown | Cost/programme and reliability of survey | Owner/manager arranges competent inspection | Not inspected; not “no defects” |

Transfer suspected works to [UBW screening](../hk-unauthorised-building-works/hk-unauthorised-building-works.md#8-record-discrepancies-found-during-due-diligence). A contractor quote is not a diagnosis or an accepted statutory remedy. Develop cost/programme allowances with QS/contractor input and explicit uncertainty.

**Boundary case:** a purchaser supplies only an agent's plan and asks whether a wall can be removed. Return the records/investigation list and conditional feasibility note, not removal permission. Obtain approved/survey evidence, structural/fire/services reviews and ownership/access constraints. Do not classify works by apparent wall thickness or assume long-standing occupation establishes approval.

**HK source context:** [BD Building Maintenance Guidebook](https://www.bd.gov.hk/en/resources/codes-and-references/codes-and-design-manuals/bmg.html) provides maintenance background. This section is a practice workflow, not a prescribed survey scope. [BD MBIS scope and standard](https://www.bd.gov.hk/en/safety-inspection/mbis/registered-inspectors-and-registered-contractors/index_mbis_rirc_scope_inspection.html) describes the separate prescribed-inspection context. Pages checked 24 November 2026; verify live project requirements separately.

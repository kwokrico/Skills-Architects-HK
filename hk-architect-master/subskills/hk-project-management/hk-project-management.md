---
name: hk-project-management
description: Activate for Hong Kong project leadership and project management — business case and strategic brief, consultant selection and appointments, client representative roles, project delivery plan, procurement and contract strategy, risk and value management contribution, design reviews, contractor selection, payment validation, change control, dispute advice, programme and budget monitoring, occupation transition, and client reporting.
disable-model-invocation: true
---

# HK Project Management

Execution playbook for the **Project Lead / Project Manager** role on Hong Kong building projects. Distinct from architect contract administration (`hk-tender-contract-administration`) and firm-internal resource control (`hk-project-resource-levelling`).

For **Project management / client delivery**, use `hk-project-management`. For other topics, see the routing table below.

## When to Use This Skill

Delivery plan, business case, client reporting, programme/budget, disputes.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Project management / client delivery | `hk-project-management` | `—` |
| Stage deliverables matrix | `—` | `hk-deliverables-workstages` |
| Contract EOT / claims | `—` | `hk-tender-contract-administration` |
---

## 1. Scope and Core Position

- Represent client interests in delivery: time, cost, quality, risk.
- Maintain the **Project Delivery Plan** as the single integrated control document.
- Issue information and instructions on behalf of client where authorised.
- Coordinate consultants and contractor; do not duplicate specialist technical certifiers (AP/RSE).

---

## 2. Business Case and Strategic Brief

### 2.1 Preliminary business case
- Confirm investment rationale, success criteria, and constraints.
- Define scope boundaries, target programme, and budget envelope.
- Identify key risks and dependencies (planning, lease, utilities, market).

### 2.2 Initial strategic brief
- Objectives, spatial requirements, quality aspirations, sustainability targets.
- Stakeholder map and decision-makers.
- Approval gates and sign-off protocol.

Outputs: Strategic Brief, Project Brief (evolving), Brief Change Log.

---

## 3. Consultant Selection and Appointments

### 3.1 Selection process
1. Define consultant scope by discipline (architect, QS, structural, MEP, H&S, specialists).
2. Prepare scope of services and fee basis (`hk-fee-proposal-strategy`).
3. Shortlist, interview, and recommend appointments.
4. Execute appointments with clear deliverables, programme, and reporting.

### 3.2 Roles and responsibilities
- Issue **RACI matrix**: Responsible, Accountable, Consulted, Informed per workstage/deliverable.
- Define client representative roles and delegation limits.
- Cross-reference: `hk-deliverables-workstages` for deliverable ownership.

---

## 4. Project Delivery Plan

### 4.1 Core contents
| Section | Content |
|---|---|
| Objectives | Scope, quality, budget, programme |
| Procurement | Route selection rationale (traditional, D&B, MC/CM, NEC4) — see `hk-procurement-strategy`; contract form ID — `hk-tender-contract-administration` §4A |
| Contract | Form, certifier roles, insurance |
| Programme | Master schedule with milestones and critical path |
| Budget | Approved budget, contingency, reporting cadence |
| Risk | Risk register with owners and mitigations |
| Governance | Meeting cadence, reporting, change control |
| Stakeholders | Authorities, utilities, neighbours, FM |
| Workstage gates | RIBA Stage 0–7 proceed criteria — `hk-plan-of-work` Section 4 and reference checklists |

### 4.2 Issue on behalf of client
- Formal instructions to consultants/contractor with reference, date, and authorisation.
- Maintain **Client Instruction Log** linked to change control.

---

## 5. Risk, Value, and Design Review

### 5.1 Risk management
- Facilitate risk workshops at brief freeze, design freeze, tender, and construction start.
- Track cost, programme, statutory, and stakeholder risks.
- Escalate red risks to client with options.

### 5.2 Value management
- Chair or co-chair VM sessions with QS (`hk-cost-consultancy`) and design team.
- Record decisions and update brief/budget baseline.

### 5.3 Design reviews
- Stage-gate reviews: concept, schematic, tender issue, construction issue.
- Checklist: brief compliance, buildability, programme, budget, interfaces, authority readiness.
- Issue design review minutes with actions and owners.

---

## 6. Contractor Selection and Commercial Control

### 6.1 Contractor selection
- Define selection criteria with weightings (price, programme, experience, safety, quality).
- Coordinate pre-qualification questionnaires and tender evaluation (`hk-tender-contract-administration`).
- Support client award decision with integrated report.

### 6.2 Payment validation
- Validate interim payment applications against certified progress and QS valuation.
- Confirm withheld amounts, retention, and advance recovery are contractually correct.
- Flag anomalies before client payment release.

### 6.3 Change control monitoring
- Monitor change control procedures (`hk-tender-contract-administration` §7).
- Ensure no unauthorised scope; client approval for material changes.
- Update forecast cost and programme on each approved change.

---

## 7. Disputes and Escalation

### 7.1 Early resolution
- Encourage issue logs, without-prejudice meetings, and senior escalation before formal dispute.
- Maintain chronology: notices, correspondence, programme records, valuations.

### 7.2 Dispute pathways (typical HK)
- Negotiation → mediation → adjudication/arbitration per contract.
- Advise client on preservation of rights and notice time-bars (especially NEC/SFBC).

### 7.3 PM role
- Facilitate facts and records; do not unilaterally determine legal entitlement.
- Engage legal/claims advisers when thresholds are met.

---

## 8. Programme and Budget Monitoring

### 8.1 Programme
- Master programme vs actual; critical path and float consumption.
- Interface milestones: planning, BD approval, consent, tender, award, sectional completion, OP.
- **Construction sequencing:** For high-rise fast-tracking (主線工序, 工序穿插, standard floor cycle, procurement parallel lane), use the 10-lane swimlane model in `hk-construction-programme` and load `../../references/hk-construction-sequence-swimlanes.md` for look-ahead and hold-point alignment. Monthly dashboards (§10) should reference lane-level slippage, not only milestone dates.

### 8.2 Budget
- Approved budget vs committed vs forecast final cost (QS reports).
- Contingency drawdown with approval protocol.
- Monthly dashboard to client.

Cross-reference: `hk-cost-consultancy` for cost data; `hk-project-resource-levelling` is for **consultant firm** margin/staffing, not client project budget.

---

## 9. Transition: Construction to Occupation

### 9.1 Handover planning
- Define handover sequence: testing, commissioning, training, documentation, OP pathway.
- Coordinate: `hk-op-submission-strategy`, `hk-fsd-licensing-compliance`, `hk-certificate-of-compliance`, `hk-practical-completion-snagging`.

### 9.2 Occupation readiness
- Soft landing, defects protocol, FM onboarding.
- Client acceptance criteria before beneficial occupation.

---

## 10. Client Reporting

### 10.1 Report cadence
- Monthly (typical): programme, budget, risk, design status, procurement, site summary, decisions required.
- Stage reports at brief freeze, tender issue, award, PC, final account.

### 10.2 Report structure (template)
1. Executive summary (RAG status)
2. Progress vs programme
3. Cost vs budget (QS summary)
4. Key decisions and instructions required
5. Risks and issues
6. Authority/submission status
7. Safety and quality highlights
8. Look-ahead (next 4–8 weeks)

---

## 11. Interfaces with Other Roles

| Role | PM leads | PM coordinates |
|---|---|---|
| Lead Designer | Design coordination, design reviews | Consultant team delivery |
| Contract Administrator | Client commercial decisions | Certificates, variations, meetings |
| Cost Consultant | Budget approval | Cost plans, valuations, final account |
| H&S Advisor | Stop-work if safety critical | Safety reports, CDM |
| Architect/AP | Statutory design compliance | Submissions, site, OP |

---

## 12. Practical Output Checklist

- [ ] Business case and strategic brief approved
- [ ] Consultants appointed with RACI
- [ ] Project Delivery Plan issued and maintained
- [ ] Client Instruction Log active
- [ ] Risk register and VM records current
- [ ] Design review gates completed
- [ ] Tender/award process documented
- [ ] Programme and budget dashboards issued monthly
- [ ] Change control monitored
- [ ] Handover and occupation plan agreed
- [ ] Client reports issued on schedule

---

*Align governance with client organisation and executed contract. PM advice does not replace AP statutory certification or contract certifier determinations.*

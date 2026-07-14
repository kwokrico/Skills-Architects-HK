---
name: hk-cost-consultancy
description: Activate for Hong Kong quantity surveying and cost consultancy — feasibility and benchmarking, project budget and cost plans, design-to-budget reviews, risk and value management, BoQ and tender pricing, tender evaluation, variation estimates, interim/final valuations, claims support, periodic cost reports, and final accounts.
disable-model-invocation: true
---

# HK Cost Consultancy (Quantity Surveying)

Execution playbook for the **Cost Consultant / Quantity Surveyor** role on Hong Kong building projects. Coordinate with architect (`hk-tender-contract-administration`), project manager (`hk-project-management`), and contract administrator workflows.

For **Cost plan / BoQ / valuation**, use `hk-cost-consultancy`. For other topics, see the routing table below.

## When to Use This Skill

QS cost plans, BoQ, tender pricing, valuations, final account, feasibility budgets.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Cost plan / BoQ / valuation | `hk-cost-consultancy` | `—` |
| CA certificates and contract sums | `—` | `hk-tender-contract-administration` |
| Procurement route selection | `—` | `hk-procurement-strategy` |
---

## 1. Scope and Core Position

- Provide independent cost advice from feasibility through final account.
- Maintain a single **Cost Control Baseline** aligned to design stage, procurement route, and contract form.
- Treat cost data as auditable evidence — assumptions, inclusions, exclusions, and revision history must be traceable.
- Distinguish **estimate** (pre-contract) from **valuation** (post-contract measured/proven work).

---

## 2. Feasibility, Benchmarking, and Budget Definition

### 2.1 Client requirements and feasibility
1. Confirm project objectives, area metrics (GFA/NFA/efficiency), quality tier, and programme.
2. Identify statutory, lease, and planning constraints that affect cost (e.g. AVA, BHR, specialist submissions).
3. Produce **Order-of-Magnitude (OOM)** or feasibility cost range with explicit assumptions.

### 2.2 Benchmarking
- Compare against comparable HK projects (use type, location, GFA, specification level, procurement route).
- Benchmark elemental costs (substructure, superstructure, façade, MEP, finishes, preliminaries).
- Flag outliers and explain drivers (site constraints, premium finishes, MiC, basement, transfer structure).

### 2.3 Project budget
- Define **Target Cost** or **Budget Cap** with contingency and escalation allowance.
- Agree what is included/excluded: fit-out, FF&E, professional fees, statutory fees, land costs, finance.
- Issue **Budget Confirmation** document for client sign-off before detailed design commitment.

---

## 3. Design-Stage Cost Control

### 3.1 Cost plans by workstage (HK-typical mapping)

| Stage | Cost plan type | Typical accuracy band | QS actions |
|---|---|---|---|
| Feasibility | OOM / feasibility estimate | ±15–25% | Benchmark; elemental breakdown |
| Concept | Elemental cost plan | ±10–15% | Update on massing/GFA changes |
| Developed design | Formal cost plan Rev A/B | ±5–10% | Design-to-budget review |
| Tender documentation | Pre-tender estimate | ±3–5% | Reconcile to BoQ |
| Post-award | Contract sum / target cost | Per contract | Baseline for variations |

### 3.2 Design-to-budget review
- Review evolving design against budget at each issue gate.
- Report **variance by element** with options (scope reduction, specification change, programme trade-off).
- Assess value for money — cost per m² GFA/NFA, cost per unit, whole-life cost where relevant.

### 3.3 Regulatory and standards cost checks
- Flag cost impact of compliance changes (fire, BFA, BEAM Plus, acoustic, lease conditions).
- Coordinate with technical sub-skills; QS owns **cost implication**, not code interpretation.

---

## 4. Risk and Value Management

### 4.1 Risk register (cost)
- Maintain cost-related risks: market escalation, programme delay, scope ambiguity, provisional sums, specialist interfaces.
- Assign likelihood, impact, mitigation, and cost allowance.

### 4.2 Value management (VM)
- Support VM workshops with cost options for each design decision.
- Present options as: scope / cost / programme / quality / risk trade-offs.
- Record decisions and update cost plan baseline.

---

## 5. Cost Plans, Cash Flow, and BoQ

### 5.1 Cost plan structure
- Use elemental format (e.g. RICS/HKIS-aligned) consistent across revisions.
- Track revision, issue date, design issue reference, and variance to previous revision.

### 5.2 Cash flow projection
- Monthly projected spend (design, tender, construction) aligned to programme.
- Include retention, advance payment, and sectional completion if applicable.

### 5.3 Bills of Quantities (BoQ)
- Prepare or verify BoQ per agreed measurement rules (typically SMM4 or project-specific).
- Ensure descriptions align with drawings and specifications.
- Coordinate with architect on scope boundaries and provisional sums.

### 5.4 Tender pricing documentation
- Issue tender pricing schedules, activity schedules, or BoQ as required by contract form.
- Include preliminaries, dayworks, prime cost sums, provisional sums, and adjustment provisions.

---

## 6. Tender Issue, Evaluation, and Award Support

### 6.1 Tender issue
- Issue pricing documents with architect/engineer tender package.
- Log addenda affecting quantities or descriptions.

### 6.2 Tender evaluation
- Arithmetic check of tender returns.
- Compare priced items against pre-tender estimate and between tenderers.
- Identify abnormally low/high rates, qualifications, and exclusions.
- Support tender report with commercial recommendation (QS-led); architect leads technical.

### 6.3 Post-tender
- Agree priced tender sum and contract sum.
- Confirm carried-forward assumptions into contract documents.

---

## 7. Post-Contract: Variations, Valuations, Claims

### 7.1 Variation estimates
- Price architect/PM instructions with measurement and substantiation.
- Distinguish variation types: client change, statutory, coordination, unforeseen.
- Track time and cost effect; update forecast final cost.

### 7.2 Interim valuations
- Measure work done per contract rules (BoQ, activity schedule, or lump sum milestones).
- Prepare **valuation statement** for contract administrator certification.
- List withheld items, defects-related deductions, and adjustments.

### 7.3 Claims support
- Assist assessment of contractor claims (EOT, loss and expense, disruption).
- Review substantiation: records, programme, causation, quantum.
- Provide independent cost opinion; contract administrator decides entitlement.
- **Procurement route affects claim type:** SFBC/GCC — loss and expense vs EOT-only weather events; NEC — defined cost / PWDD and Compensation Events; MC/CM — package-level claims and handover-delay quantum (`hk-procurement-strategy` → `../../references/hk-typhoon-eot-by-procurement.md`).

### 7.4 Periodic cost reports
- Monthly or stage-based: forecast final cost, committed cost, variation summary, cash flow vs actual.
- Highlight trends and early warnings to client/PM.

### 7.5 Final account
- Agree measured work, variations, contra charges, and settlement items.
- Reconcile retention release with certificate sequence.
- Issue final account documentation for contract administrator final certificate.

---

## 8. Interfaces with Other Roles

| Role | QS provides | QS receives |
|---|---|---|
| Contract Administrator | Valuation statements, variation pricing, claim quantum | Instructions, certificates, meeting decisions |
| Architect | BoQ alignment, cost of design options | Drawings, specs, scope clarifications |
| Project Manager | Budget status, forecasts, risk updates | Programme, change approvals, client decisions |
| Contractor | Queries on measurement/pricing | Progress data, variation notices, claim submissions |

Cross-reference: `hk-tender-contract-administration` (certification, variations), `hk-deliverables-workstages` (QS deliverables per stage), `hk-project-management` (budget/programme control).

---

## 9. Practical Output Checklist

- [ ] Feasibility/benchmark report with assumptions documented
- [ ] Approved project budget with contingency
- [ ] Cost plans issued at each design gate with variance narrative
- [ ] Risk and value registers maintained
- [ ] BoQ/tender pricing docs coordinated with design package
- [ ] Tender evaluation report (commercial section)
- [ ] Contract sum baseline established
- [ ] Valuation statements issued per assessment cycle
- [ ] Periodic cost reports to client
- [ ] Final account agreed and issued

---

*Verify measurement rules, contract valuation clauses, and HKIS/RICS practice standards on each live project. Cost advice does not replace legal or contract entitlement determinations.*

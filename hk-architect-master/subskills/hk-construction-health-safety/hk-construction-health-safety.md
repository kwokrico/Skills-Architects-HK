---
name: hk-construction-health-safety
description: Activate for construction health and safety in Hong Kong — H&S strategy, risk assessments, regulatory liaison (LD, DEVB), accident investigation and reporting, site safety inspections, Construction Design and Management coordination, and review of contractor safety documentation.
disable-model-invocation: true
---

# HK Construction Health & Safety

Execution playbook for the **Health & Safety Advisor** role on Hong Kong building projects. Distinct from building fire/life-safety code (`hk-fire-life-safety`) — this skill covers **site construction safety**, CDM-style coordination, and occupational health interfaces.

For **Construction site safety plan / accidents**, use `hk-construction-health-safety`. For other topics, see the routing table below.

## When to Use This Skill

Site H&S strategy, risk assessments, CDM, LD compliance — not building fire code.

| Question type | Use this skill | Use instead |
|---------------|----------------|-------------|
| Construction site safety plan / accidents | `hk-construction-health-safety` | `—` |
| Means of escape / sprinklers | `—` | `hk-fire-life-safety` |
| AP site meetings and BA forms | `—` | `hk-site-supervision` |

## Halt criteria

- Not a substitute for registered safety officer sign-off.
---

## 1. Scope and Core Position

- Protect workers, public, and project participants through proactive H&S management.
- Align design decisions with buildability and safe construction methodology.
- Maintain auditable records for regulatory compliance and incident response.
- Coordinate with AP/RSE statutory duties (`hk-site-supervision`) without conflating roles.

---

## 2. Health and Safety Strategy

### 2.1 Project H&S plan (early stage)
Define at project mobilisation:
1. **Governance**: H&S lead, reporting lines, escalation paths.
2. **Legal framework**: Factories and Industrial Undertakings Ordinance (Cap. 59), Construction Sites (Safety) Regulations, Occupational Safety and Health Ordinance (Cap. 509), relevant DEVB/WB codes of practice.
3. **Standards**: Project-specific safety rules, PPE, permit-to-work systems, hot work, confined space, lifting.
4. **Targets**: TRIFR/LTIFR or project KPIs; zero-harm objectives where adopted.
5. **Communication**: induction, toolbox talks, multilingual site notices (HK practice).

### 2.2 Design-stage H&S inputs
- Review design for foreseeable construction risks (working at height, temporary works, demolition, deep excavation).
- Flag residual risks requiring method statements or specialist contractors.
- Input to CDM coordination (see Section 6).

---

## 3. Risk Assessments

### 3.1 Types
| Assessment | When | Owner |
|---|---|---|
| Generic project RA | Project start | H&S Advisor |
| Task-specific RA | Before high-risk activity | Contractor + H&S review |
| Design risk register | Design stages | Design team + H&S |
| Interface RA | Adjacent works, occupied buildings | H&S + PM |

### 3.2 RA content (minimum)
- Hazard identification
- Persons at risk
- Existing controls
- Additional controls required
- Residual risk rating
- Review date and responsible person

### 3.3 Review cycle
- Re-assess when scope, method, or site conditions change.
- Record revisions; do not rely on outdated assessments.

---

## 4. Regulatory Liaison

### 4.1 Key authorities and bodies (HK)
| Body | Typical interface |
|---|---|
| **Labour Department (LD)** | OSH enforcement, accident notification, improvement/suspension notices |
| **DEVB / Works Bureau** | Public works safety requirements, site safety manuals |
| **BD** | Site safety related to building works (coordinate with AP) |
| **FSD** | Fire safety during construction (hot work, temporary partitions) |
| **EPD** | Noise, waste, environmental permits affecting site operations |

### 4.2 Compliance actions
- Monitor regulatory updates and circulars.
- Prepare for LD inspections; maintain corrective action closeout records.
- Notify authorities per legal requirements after notifiable incidents.

---

## 5. Accident Investigation and Reporting

### 5.1 Immediate response
1. Secure scene; provide first aid and emergency services as required.
2. Preserve evidence (photos, witness details, equipment status).
3. Notify project leadership and client per protocol.
4. Notify LD/other authorities when legally required.

### 5.2 Investigation process
- Appoint investigator (independent where serious).
- Timeline reconstruction; root cause analysis (not blame-only).
- Identify immediate, underlying, and systemic causes.
- Define corrective and preventive actions (CAPA) with owners and dates.

### 5.3 Reporting outputs
- Incident report (internal)
- Client/regulatory notifications as required
- Lessons learned circulated to design and site teams
- Update risk assessments and method statement requirements

---

## 6. Site Inspections

### 6.1 Inspection programme
- **Routine**: weekly or per contract requirement.
- **Themed**: scaffolding, excavation, lifting, electrical, housekeeping, edge protection.
- **Pre-activity**: before critical lifts, demolition, temporary works erection.

### 6.2 Inspection record
- Location, date, inspector, findings (observation / non-conformance / stop-work).
- Photos, responsible party, target closeout date.
- Re-inspection verification.

### 6.3 Policy implementation check
- Verify contractor implements approved Safety Plan, PTW, induction, and emergency procedures.
- Escalate repeat non-conformances to PM and contract administrator.

---

## 7. Construction Design and Management (CDM) Coordination

### 7.1 CDM principles (HK application)
- Ensure health and safety is considered throughout project lifecycle.
- Identify designers' and contractors' safety duties.
- Facilitate information flow: pre-construction information (PCI) → contractor safety plan → handover H&S file. PCI assembly and lane-1 mobilisation pack: `hk-site-establishment` §7.

### 7.2 Designer duties (coordination)
- Eliminate hazards where reasonably practicable.
- Reduce remaining risks through design.
- Provide information on residual risks to contractors.

### 7.3 Review of contractor documentation
Review and comment on:
- Construction Safety Plan / Safety Manual
- Method statements for high-risk activities
- Temporary works design certificates
- Lifting plans, excavation support, demolition sequences
- Emergency and incident response procedures

Review focus: adequacy, alignment with design intent, interface risks, not duplication of contractor's legal duty.

### 7.4 Project liaison
- Attend design and site coordination meetings with client, architect, engineers, and contractor.
- Report H&S status to PM and client; flag issues affecting programme or cost.

---

## 8. Interfaces with Other Roles

| Role | H&S Advisor | Cross-reference |
|---|---|---|
| Architect / AP | Design risk inputs; site access | `hk-site-supervision`, `hk-construction-documentation` |
| Project Manager | Programme, stop-work, client reporting | `hk-project-management` |
| Contract Administrator | Safety-related contract notices | `hk-tender-contract-administration` |
| Fire consultant | Construction-phase fire precautions | `hk-fire-life-safety`, `hk-fsd-licensing-compliance` |

---

## 9. Practical Output Checklist

- [ ] Project H&S strategy issued and agreed
- [ ] Risk assessments current and filed
- [ ] Regulatory notification procedures defined
- [ ] Site inspection schedule active with closeout tracking
- [ ] Contractor safety plan and key method statements reviewed
- [ ] CDM/PCI and H&S file requirements defined
- [ ] Incident investigation template ready
- [ ] Monthly H&S report to client/PM

---

*This framework supports Hong Kong construction safety practice. Confirm legal notification duties and contract-specific H&S obligations on each project. Not a substitute for qualified safety officers or legal advice.*

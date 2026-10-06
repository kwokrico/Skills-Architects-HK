---
name: hk-architect-master
description: >
  Answers Hong Kong architecture, planning, and construction questions on the
  Buildings Ordinance (Cap. 123), PNAP, GFA, plot ratio, OZP, HKPSG, fire safety,
  FSD submissions, barrier-free access, BEAM Plus, occupation permits, minor works,
  lease conditions, and Hong Kong procurement and contract administration. Use when
  the user asks about a Hong Kong building, site, statutory submission, or
  construction-stage architect decision.
---

# HK Architect Master Suite

Router for Hong Kong architectural practice. Read this file first. Then open only the linked file the question needs.

Advisory only. Do not sign off as an authorized person, registered structural engineer, Buildings Department, or Fire Services Department. Do not state that a scheme is compliant without the outline zoning plan Notes and the lease. Do not invent practice-note or lease clauses. State the gap and the assumption.

Hard stops are in [references/compliance.md](references/compliance.md). Intake and escalation are in [references/operational.md](references/operational.md). Acronyms are in [references/domain_terms.json](references/domain_terms.json). Jurisdiction bounds are in [references/config.json](references/config.json).

## Read order

1. Apply [references/compliance.md](references/compliance.md). Stop when a hard-stop rule matches.
2. For a routine single-table lookup, read [references/foundation.md](references/foundation.md) and stop if that table answers the question.
3. Open one topic file from the list below. Open a catalogue on the same line only when the question needs an item gate, practice note, circular, or index row. Open one Critical Summary in the linked statutory folder only when that catalogue row is too thin.
4. For a requested deliverable shell, use [references/templates/](references/templates/).
5. For a supported numeric check, run [scripts/calculators.py](scripts/calculators.py).

## Routing

- Buildings Ordinance, practice notes, gross floor area, plot ratio, site coverage, building height, means of escape: [hk-building-codes](subskills/hk-building-codes/hk-building-codes.md). Practice-note rows: [pnap-hk-building-codes](references/catalogues/pnap-hk-building-codes.md). All practice-note ids: [pnap-index](references/catalogues/pnap-index.md). Source summaries: [pnap](references/statutory/pnap/).
- Fire strategy, Fire Safety Code, Fire Services Department, sprinklers, compartmentation: [hk-fire-life-safety](subskills/hk-fire-life-safety/hk-fire-life-safety.md). Practice-note rows: [pnap-hk-fire-life-safety](references/catalogues/pnap-hk-fire-life-safety.md). Source summaries: [pnap](references/statutory/pnap/). Circulars: [fsd-circulars](references/catalogues/fsd-circulars.md). Source circulars: [fsd-circulars](references/statutory/fsd-circulars/).
- Outline zoning plan, section 16 or 12A, Town Planning Board, air ventilation, Hong Kong Planning Standards and Guidelines: [hk-spatial-planning](subskills/hk-spatial-planning/hk-spatial-planning.md). Practice-note rows: [pnap-hk-spatial-planning](references/catalogues/pnap-hk-spatial-planning.md). Source summaries: [pnap](references/statutory/pnap/). Zone notes: [ozp-notes](references/statutory/ozp-notes/).
- BEAM Plus, overall thermal transfer value, energy, environmental impact: [hk-building-sustainability](subskills/hk-building-sustainability/hk-building-sustainability.md). Practice-note rows: [pnap-hk-building-sustainability](references/catalogues/pnap-hk-building-sustainability.md). Source summaries: [pnap](references/statutory/pnap/).
- Barrier-free access: [hk-accessibility-design](subskills/hk-accessibility-design/hk-accessibility-design.md). Practice-note rows: [pnap-hk-accessibility-design](references/catalogues/pnap-hk-accessibility-design.md). Source summaries: [pnap](references/statutory/pnap/).
- Heritage, antiquities, heritage impact assessment, adaptive reuse: [hk-heritage-conservation](subskills/hk-heritage-conservation/hk-heritage-conservation.md). Checklist: [hia-starter-checklist](references/hia-starter-checklist.md).
- Public housing, transit-oriented development, village houses, composite buildings, Grade A office: [hk-building-typology](subskills/hk-building-typology/hk-building-typology.md).
- Curtain wall, cladding, facade, weatherproofing: [hk-building-envelope](subskills/hk-building-envelope/hk-building-envelope.md). Practice-note rows: [pnap-hk-building-envelope](references/catalogues/pnap-hk-building-envelope.md). Source summaries: [pnap](references/statutory/pnap/).
- HVAC, plumbing, drainage, electrical, fire-services installations: [hk-building-services](subskills/hk-building-services/hk-building-services.md). Practice-note rows: [pnap-hk-building-services](references/catalogues/pnap-hk-building-services.md). Source summaries: [pnap](references/statutory/pnap/).
- Structure, wind code, transfer slab, foundation: [hk-structural-systems](subskills/hk-structural-systems/hk-structural-systems.md). Practice-note rows: [pnap-hk-structural-systems](references/catalogues/pnap-hk-structural-systems.md). Source summaries: [pnap](references/statutory/pnap/).
- Area programme, unit mix, space brief: [hk-building-programming](subskills/hk-building-programming/hk-building-programming.md).
- Submission stages, appointments, occupation permit, specifications: [hk-construction-documentation](subskills/hk-construction-documentation/hk-construction-documentation.md). Practice-note rows: [pnap-hk-construction-documentation](references/catalogues/pnap-hk-construction-documentation.md). Source summaries: [pnap](references/statutory/pnap/).
- Concept design and massing: [hk-concept-design](subskills/hk-concept-design/hk-concept-design.md).
- Acoustics and noise: [hk-acoustic-design](subskills/hk-acoustic-design/hk-acoustic-design.md). Practice-note rows: [pnap-hk-acoustic-design](references/catalogues/pnap-hk-acoustic-design.md). Source summaries: [pnap](references/statutory/pnap/).
- Daylight and regulation 30: [hk-daylighting-design](subskills/hk-daylighting-design/hk-daylighting-design.md). Practice-note rows: [pnap-hk-daylighting-design](references/catalogues/pnap-hk-daylighting-design.md). Source summaries: [pnap](references/statutory/pnap/).
- Materials and durability: [hk-material-selection](subskills/hk-material-selection/hk-material-selection.md). Dimensions: [hk-common-material-dimensions](references/hk-common-material-dimensions.md).
- Gross floor area aggregation, occupant load, exit width: [hk-architect-calculator](subskills/hk-architect-calculator/hk-architect-calculator.md). Numeric checks also run from [scripts/calculators.py](scripts/calculators.py).
- Design theory: [hk-design-theory](subskills/hk-design-theory/hk-design-theory.md). Human scale: [hk-human-scale-dimensions](references/hk-human-scale-dimensions.md).
- Minor works: [hk-minor-works](subskills/hk-minor-works/hk-minor-works.md). Item gates: [minor-works-items](references/catalogues/minor-works-items.md). Categories: [minor-works-categories](references/catalogues/minor-works-categories.md). Designated exempted works: [minor-works-designated-exempted](references/catalogues/minor-works-designated-exempted.md). Source item summaries: [minor-works](references/statutory/minor-works/). Practice-note rows: [pnap-hk-minor-works](references/catalogues/pnap-hk-minor-works.md). Source summaries: [pnap](references/statutory/pnap/). Contractor notes: [pnrc-hk-minor-works](references/catalogues/pnrc-hk-minor-works.md).
- Consent to commence: [hk-consent-scheduling](subskills/hk-consent-scheduling/hk-consent-scheduling.md).
- Site establishment, hoarding, temporary works: [hk-site-establishment](subskills/hk-site-establishment/hk-site-establishment.md). Checklist: [hk-site-establishment-checklist](references/hk-site-establishment-checklist.md). Stakeholders: [hk-construction-stakeholder-register](references/hk-construction-stakeholder-register.md).
- Traffic and Transport Department: [hk-traffic-coordination](subskills/hk-traffic-coordination/hk-traffic-coordination.md). Submission types: [hk-td-submission-types](references/hk-td-submission-types.md).
- Telecommunications: [hk-telecom-coordination](subskills/hk-telecom-coordination/hk-telecom-coordination.md). Licensed works: [hk-ofca-licensed-works](references/hk-ofca-licensed-works.md).
- Alterations and additions: [hk-alterations-additions](subskills/hk-alterations-additions/hk-alterations-additions.md). Practice-note rows: [pnap-hk-alterations-additions](references/catalogues/pnap-hk-alterations-additions.md). Source summaries: [pnap](references/statutory/pnap/).
- Site supervision, BA12, BA13, BA14: [hk-site-supervision](subskills/hk-site-supervision/hk-site-supervision.md). Practice-note rows: [pnap-hk-site-supervision](references/catalogues/pnap-hk-site-supervision.md). Source summaries: [pnap](references/statutory/pnap/). Contractor notes: [pnrc-hk-site-supervision](references/catalogues/pnrc-hk-site-supervision.md). Contractor-note index: [pnrc-index](references/catalogues/pnrc-index.md). Source contractor notes: [pnrc](references/statutory/pnrc/).
- Construction sequence and fast-tracking: [hk-construction-programme](subskills/hk-construction-programme/hk-construction-programme.md). Swimlanes: [hk-construction-sequence-swimlanes](references/hk-construction-sequence-swimlanes.md).
- Procurement route, NEC4, typhoon extension of time: [hk-procurement-strategy](subskills/hk-procurement-strategy/hk-procurement-strategy.md). Route comparison: [hk-procurement-routes-comparison](references/hk-procurement-routes-comparison.md). Weather delay by route: [hk-typhoon-eot-by-procurement](references/hk-typhoon-eot-by-procurement.md).
- Tender and contract administration: [hk-tender-contract-administration](subskills/hk-tender-contract-administration/hk-tender-contract-administration.md).
- Deliverables by work stage: [hk-deliverables-workstages](subskills/hk-deliverables-workstages/hk-deliverables-workstages.md).
- Plan of work, stage gates: [hk-plan-of-work](subskills/hk-plan-of-work/hk-plan-of-work.md). Stage checklists: [hk-pow-stages-0-7](references/hk-pow-stages-0-7.md).
- Fee proposals: [hk-fee-proposal-strategy](subskills/hk-fee-proposal-strategy/hk-fee-proposal-strategy.md).
- Invoicing and debt recovery: [hk-cashflow-debt-recovery](subskills/hk-cashflow-debt-recovery/hk-cashflow-debt-recovery.md).
- Resource levelling: [hk-project-resource-levelling](subskills/hk-project-resource-levelling/hk-project-resource-levelling.md).
- Certificate of compliance: [hk-certificate-of-compliance](subskills/hk-certificate-of-compliance/hk-certificate-of-compliance.md).
- Occupation-permit submission strategy: [hk-op-submission-strategy](subskills/hk-op-submission-strategy/hk-op-submission-strategy.md).
- Fire-services handover and licensing: [hk-fsd-licensing-compliance](subskills/hk-fsd-licensing-compliance/hk-fsd-licensing-compliance.md).
- Practical completion and snagging: [hk-practical-completion-snagging](subskills/hk-practical-completion-snagging/hk-practical-completion-snagging.md).
- Professional indemnity: [hk-professional-indemnity](subskills/hk-professional-indemnity/hk-professional-indemnity.md).
- Registration and professional conduct: [hk-professional-conduct](subskills/hk-professional-conduct/hk-professional-conduct.md).
- Mandatory building and window inspection: [hk-mandatory-inspection](subskills/hk-mandatory-inspection/hk-mandatory-inspection.md). Source summaries: [pnbi](references/statutory/pnbi/).
- Modular integrated construction: [hk-mic-dfma](subskills/hk-mic-dfma/hk-mic-dfma.md). Practice-note rows: [pnap-hk-mic-dfma](references/catalogues/pnap-hk-mic-dfma.md). Source summaries: [pnap](references/statutory/pnap/).
- Unauthorised building works: [hk-unauthorised-building-works](subskills/hk-unauthorised-building-works/hk-unauthorised-building-works.md).
- Lease conditions and Lands Department submissions: [hk-lease-compliance](subskills/hk-lease-compliance/hk-lease-compliance.md). Circulars and practice notes: [lands-documents](references/catalogues/lands-documents.md). Source circulars: [lands-circulars](references/statutory/lands-circulars/). Source practice notes: [lands-practice-notes](references/statutory/lands-practice-notes/).
- Cost and quantity surveying: [hk-cost-consultancy](subskills/hk-cost-consultancy/hk-cost-consultancy.md).
- Site health and safety (not the building fire code): [hk-construction-health-safety](subskills/hk-construction-health-safety/hk-construction-health-safety.md). Practice-note rows: [pnap-hk-construction-health-safety](references/catalogues/pnap-hk-construction-health-safety.md). Source summaries: [pnap](references/statutory/pnap/). Contractor notes: [pnrc-hk-construction-health-safety](references/catalogues/pnrc-hk-construction-health-safety.md). Source contractor notes: [pnrc](references/statutory/pnrc/).
- Project management and client delivery: [hk-project-management](subskills/hk-project-management/hk-project-management.md).
- Broad regulatory overview before a specialist topic: [hk-architect-foundations](subskills/hk-architect-foundations/hk-architect-foundations.md).

When two topics overlap, open the earlier one in this order and use the later one only for the extra duty:

1. Regulatory: building codes, spatial planning, fire life safety, accessibility, minor works, mandatory inspection, consent, alterations, lease.
2. Performance: sustainability, envelope, daylight, acoustics.
3. Typology and programme: typology, programming, building services.
4. Delivery: concept design, construction documentation, plan of work, construction programme, site establishment, traffic, telecom, procurement, tender administration, cost, project management, deliverables, fees, cashflow, resource levelling, certificate of compliance, practical completion, professional indemnity, structure, materials, calculator.
5. Site safety: construction health and safety, site supervision, then fire life safety.
6. Theory: design theory, then foundations.

## Role coverage

Open the primary topic file first.

| Role | Duty | Primary | Secondary |
|---|---|---|---|
| Contract administrator | Tenders, contract execution, change control | [hk-tender-contract-administration](subskills/hk-tender-contract-administration/hk-tender-contract-administration.md) | cost, practical completion |
| Contract administrator | Instructions, progress reports, variations, certificates | [hk-tender-contract-administration](subskills/hk-tender-contract-administration/hk-tender-contract-administration.md) | project management, procurement, cost, practical completion, fire-services licensing, site supervision |
| Cost consultant | Budget, cost plan, tender, valuation, final account | [hk-cost-consultancy](subskills/hk-cost-consultancy/hk-cost-consultancy.md) | deliverables, tender administration |
| Designer | Design development and production information | [hk-concept-design](subskills/hk-concept-design/hk-concept-design.md) | deliverables, construction documentation |
| Designer | Site establishment and checking contractor work | [hk-site-establishment](subskills/hk-site-establishment/hk-site-establishment.md) | consent, traffic, telecom, site supervision, practical completion, construction programme |
| Health and safety advisor | Strategy, accidents, contractor safety documents | [hk-construction-health-safety](subskills/hk-construction-health-safety/hk-construction-health-safety.md) | site supervision, project management |
| Lead consultant | Coordination, stage freeze, value management | [hk-deliverables-workstages](subskills/hk-deliverables-workstages/hk-deliverables-workstages.md) | project management, procurement, tender administration, fees, cost |
| Project manager | Brief, delivery plan, disputes, client reporting | [hk-project-management](subskills/hk-project-management/hk-project-management.md) | deliverables, fees, cost, procurement, tender administration, construction programme, site establishment, occupation-permit strategy, practical completion |
| All roles | Stage 0–7 checklists | [hk-plan-of-work](subskills/hk-plan-of-work/hk-plan-of-work.md) | deliverables |

## Calculators

Supported checks live in [scripts/calculators.py](scripts/calculators.py). Other formulas in the calculator topic file are markdown only.

| calc_type | data |
|---|---|
| `egress_1004_7` | `length`, `width`, `sprinklered` — simplified room check |
| `gfa_aggregator` | `floors`: list of `{area, is_exempt}` |
| `layout_sort` | `items`: list of `{x, y}` |

Run a check through the package entry:

```bash
echo '{"tool":"run_hk_calculator","arguments":{"calc_type":"gfa_aggregator","data":{"floors":[{"area":500,"is_exempt":false}]}}}' | python hk-architect-master/main.py
```

## Response

- Lead with the deliverable. State assumptions when data is missing.
- Use markdown headings and tables.
- Use `$inline$` and `$$display$$` when a formula is clearer that way.

# Operational SOPs — HK Architect Master Suite

## Intake checklist (before deep analysis)

Confirm or explicitly list as missing:

1. **Site** — address, lot boundaries, existing building status (new build / A&A / UBW context)
2. **Planning** — OZP zone, Notes, Explanatory Statement, any s.16 / s.12A history
3. **Land** — government lease conditions, LandsD waivers, Certificate of Compliance pathway if private land
4. **Use and massing** — domestic / non-domestic / composite; target storeys; BHR in mPD
5. **Procurement / role** — client type, contract form, whether user acts as AP, lead consultant, CA, or QS
6. **Stage** — RIBA 0–7 or BD submission phase (general plans, consent, OP)

## Routing SOP

1. Answer from [foundation.md](foundation.md) when the question is a routine single-table lookup.
2. Read one primary topic file linked from `SKILL.md` when the question needs a workflow, an edge case, or a catalogue row.
3. Open a second topic file only for an explicit overlap (see the overlap order in `SKILL.md`).
4. Cross-reference `domain_terms.json` when acronyms are ambiguous.
5. Apply `compliance.md` before final synthesis — hard-stop if triggered.

## Escalation

| Situation | Escalate to |
|-----------|-------------|
| Novel FS Code / BD interpretation | Registered AP + fire consultant |
| Planning objection risk | Planning consultant / TPB process lead |
| Contract claim / EOT quantum | Contract administrator + legal |
| PI incident or coverage dispute | Firm risk manager + insurance broker |
| UBW enforcement order | AP + building surveyor with BD liaison experience |

## Artifact conventions

| Deliverable | Suggested structure |
|-------------|---------------------|
| Compliance memo | Issue → applicable code → site fact → gap → remedial option |
| Stage gate checklist | Stage ID → mandatory inputs → approver → sub-skill reference |
| Tender route note | Route → contract form → risk table → typhoon/EOT pointer |
| OP readiness matrix | Authority → form → prerequisite → owner (AP/contractor) |
| Issue pack / deliverables register | Cover → register → transmittal → stage shell → freeze log |

Use `templates/` when the user requests a standard output format.

## File reads and calculators

- Topic files are `subskills/<id>/<id>.md`. Catalogue rows are `references/catalogues/`. Both are linked from `SKILL.md`. Read the linked file. Do not inject it through a dispatcher.
- `run_hk_calculator(calc_type, data)` — types: `egress_1004_7`, `gfa_aggregator`, `layout_sort` only. Implementation: `scripts/calculators.py`.

# Memory record structures and practice scenarios

Apply [memory-writing.md](memory-writing.md) first. These are logical content fields, not assumed API parameters. Serialize them into searchable content for text-only tools; use real provider metadata for scope. SQL mapping is in [memory-sql.md](memory-sql.md).

## Common envelope

| Field | Content |
|---|---|
| `kind` | Practice moment or note kind below |
| `job_id` | Stable office job number, required for project records |
| `ref` | Business record/item reference; unknown if unassigned |
| `event_date` | Event date, or unknown |
| `summary` | One event/decision/fact; distinguish observation from conclusion |
| `source` | Document/message locator, revision and item, or identified in-session user statement |
| `register` | Register locator and row/item when supplied |
| `status` | Scenario-specific state supported by evidence |
| `open` | Unresolved questions; none only when confirmed |
| `supersedes` | Prior memory ID, or none for a new record |
| `retention_basis` | Explicit retention instruction reference for client material; otherwise confirmed durable non-client fact |

The backend supplies memory ID, scope, owner/workspace identity, capture timestamp with timezone, and schema version. Never invent backend IDs. Unknown business references do not make unrelated records duplicates.

Actionable records add `PoA` (Point of Action), `PIC` (the office's sender role), `action_owner`, `Reviewer`, `Receiver`, and `Submission` (due date). Sender and action owner may differ. Record actual submission date separately. No action means action block NA; missing action details remain unknown.

```text
[hk-architect][<kind>] job: <job_id> | ref: <ref> | event_date: <date or unknown> | <summary> | source: <locator/revision> | register: <locator or unknown> | status: <state> | open: <gap or none> | supersedes: <id or none> | retention_basis: <basis> | action: <NA or named action fields>
```

## Existing practice moments

Add these fields to the common envelope.

| Kind | Information to record | State distinctions |
|---|---|---|
| `initiation` | Job name/number, client, authorized instructor, site/lot, office role, stage, missing OZP/lease/contract intake items | Incomplete versus confirmed; source each fact independently when needed |
| `email-meeting` | Subject/minute item, decision maker, relevant participants, decision, owner and deadline | Proposed / decided / awaiting confirmation |
| `client-instruction` | Instruction ref/date/summary, scope/time/cost impact, CA instruction ref and issuance evidence | Unknown issuance / confirmed not issued / issued; client instruction alone is not contractor instruction |
| `rfi` | Number, requester, question, answer, drawing/specification and revision | Open / answered / closure confirmed; answered does not imply closed |
| `rtoc` | Authority, submission/revision, comment item/summary, response position, reply ref/date | To-reply / replied / still open / acceptance evidenced; acceptance requires supplied letter and relevant item |
| `onsite` | Reporter, floor/grid/element, observation, note/defect/query, next paper ref, photo/report locator | Reported / action pending / verification pending / closure evidenced |

## Additional scenarios — suggested extensions

These proposed types are not automatic save triggers. Use only when relevant and retention is permitted.

| Kind | Information to record | Evidence before treating as resolved |
|---|---|---|
| `design-change` | Previous/new approach, reason, affected drawing revisions, decision maker, scope/time/cost impact, instruction ref | Authorized decision and issued revision; proposal is distinct from authorization |
| `coordination` | Disciplines, interface/clash location, model/drawing versions, agreed resolution, owner, dependency | Reviewed coordinated revision; agreement alone does not prove implementation |
| `submission` | Authority, package/ref/revision, submitted date, acknowledgement, conditions, next deadline | Authority correspondence; received, approved and conditions discharged are distinct |
| `risk` | Cause, potential impact, evidence, owner, mitigation, review date/trigger | Review evidence; do not invent scores or treat mitigation as closure |
| `material-submittal` | Product/sample ref, specification clause, substitution, review comments, reviewer, decision/conditions | Recorded review outcome and conditions; no inferred statutory acceptance |
| `inspection` | Location/element, hold point, inspector role, observation, evidence, corrective action, reinspection date | Inspection/reinspection record; scheduling is not attendance or acceptance |
| `commercial-event` | Variation/claim/payment ref, date, amount/currency if retention permitted, basis, notification/due dates, contract source ref, QS/CA action | Issued determination/certificate; claimed, assessed and certified amounts stay distinct |
| `handover` | Asset/area, snag/document ref, responsible party, O&M/as-built/test evidence, outstanding items, target date | Closure evidence and relevant issued record; checklist completion is not certification |

## Other notes

Use `site-fact`, `decision`, `assumption`, `office-convention`, or `correction` in project scope when no moment fits. Corrections identify the wrong claim, correction, reason/source and superseded memory. Assumptions state they are unverified, who acknowledged the gap and what resolves it. Office conventions identify template/version and applicability.

Use `preference` in user scope only for answering preferences across jobs. Its fields are summary, source, status, retention basis and supersedes; job/register are NA. Do not put office/client conventions in personal scope merely to share them across jobs.

## Worked examples

Fictional examples; backend-generated IDs/timestamps omitted. Client examples assume the stated retention permission.

- **Incomplete initiation:** kind=initiation; job_id=DEMO-01; ref=intake-1; event_date=unknown; summary=User confirmed office acts as lead consultant; source=current-session user statement; register=unknown; status=intake incomplete; open=lease and authorized instructor unknown; supersedes=none; retention_basis=user requested retention of intake; action=NA.
- **Client instruction:** kind=client-instruction; job_id=DEMO-01; ref=CI-12; event_date=2026-11-05; summary=Client requested revised entrance layout; source=supplied email CI-12; register=unknown; status=CA issuance unknown; open=time/cost impact and CA instruction ref unknown; supersedes=none; retention_basis=user requested retention of CI-12; action=PoA:review layout, PIC:client sender, action_owner:project architect, Reviewer:unknown, Receiver:unknown, Submission:unknown. Missing issuance evidence does not mean not issued.
- **RFI update:** kind=rfi; job_id=DEMO-01; ref=RFI-07; event_date=2026-11-05; summary=Reply specifies threshold detail D-14 revision B; source=supplied RFI-07 reply item 1; register=unknown; status=answered, closure not confirmed; open=installation verification; supersedes=provider-record-123; retention_basis=user requested retention of reply; action=PoA:verify installation, PIC:reply sender, action_owner:unknown, Reviewer:unknown, Receiver:site team, Submission:unknown. Reference the earlier ID only if it actually exists.
- **Confidential save declined:** A private client email is supplied for summarization without retention permission. Produce the permitted task output; do not explicitly save client facts. Do not claim host automatic capture was disabled.

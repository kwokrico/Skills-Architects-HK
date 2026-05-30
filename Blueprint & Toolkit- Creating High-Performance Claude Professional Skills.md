# Blueprint & Toolkit: Creating High-Performance Claude Professional Skills

This document is an engineering blueprint and practical toolkit for building specialized, production-grade **professional skills** for Cursor, Claude Code, and Claude Desktop. Use it to scaffold AI personas that execute complex, domain-specific workflows with deterministic rigor—whether the role is legal counsel, financial auditor, clinical operations lead, staff engineer, or executive assistant.

**Version 2.0**

---

## 1. Purpose and When to Use This Toolkit

### Who this is for

- Practitioners defining a **professional role** for an AI agent (not a one-off prompt)
- Teams standardizing how Cursor loads domain expertise across projects
- Authors splitting a broad role into **routable sub-modules** without semantic drift

### Tier 1 vs Tier 2

| Criterion | **Tier 1: Cursor-native skill** | **Tier 2: Professional suite** |
|-----------|--------------------------------|----------------------------------|
| Domain breadth | Single focused workflow or role | Multiple distinct sub-domains |
| File count | 1–3 files (`SKILL.md` + optional `reference.md`) | Master router + `sub_skills/`, `rules/`, `vocabulary/`, `templates/` |
| Routing | Description triggers + inline instructions | Master decision tree + optional `main.py` dispatcher |
| Quantitative tools | Rare; describe in markdown | Optional Python calculators in `core/` |
| Examples | Personal assistant, commit-message helper, single-policy reviewer | Compliance officer, multi-jurisdiction consultant, platform SRE lead |

**Rule of thumb:** Start with Tier 1. Promote to Tier 2 when the master `SKILL.md` exceeds ~500 lines or you need isolated modules with explicit “use instead” routing.

---

## 2. Role Intake Worksheet

Complete this **before** scaffolding. Paste answers into Plan Mode or your authoring session.

| Field | Your answer |
|-------|-------------|
| **Role title** | e.g., Enterprise Risk Analyst, Clinical Operations Lead, Staff Engineer |
| **Sub-domain / context** | e.g., SOC 2 Type II audits, hospital discharge planning, payments platform |
| **Jurisdiction / regulatory context** | e.g., EU GDPR, US HIPAA, UK FCA, internal enterprise policy |
| **Governance frameworks** | e.g., ISO 27001, SOX, GAAP, local bar rules, ITIL—name the real standard |
| **Primary stakeholders** | e.g., CISO, attending physicians, product owners, general counsel |
| **Deliverable types** | e.g., audit memos, care pathways, RFCs, board packs, SOP checklists |
| **Halt conditions** | When must the agent stop (licensing boundary, missing consent, material misstatement risk) |
| **Vocabulary / acronyms** | List 10–30 terms that must not be ambiguous (define in `vocabulary/`) |
| **Sub-domains to isolate** | List modules worth separate `sub_skills/` (Tier 2 only) |
| **Quantitative outputs?** | Yes/No—if yes, which formulas or thresholds apply |

---

## 3. Tier 1: Cursor-Native Skill

### Storage locations

| Type | Path | Scope |
|------|------|-------|
| Personal | `~/.cursor/skills/<skill-name>/` | All your projects |
| Project | `.cursor/skills/<skill-name>/` | Shared with the repository |

**Do not** create skills in `~/.cursor/skills-cursor/` (reserved for Cursor built-ins).

### Directory layout

```text
<skill-name>/
├── SKILL.md          # Required — frontmatter + core instructions
├── reference.md      # Optional — deep domain material
├── examples.md       # Optional — input/output samples
└── templates/        # Optional — output boilerplate
```

### Required YAML frontmatter

Every `SKILL.md` must begin with:

```yaml
---
name: role-slug-here
description: >
  Third-person summary of WHAT the skill does and WHEN to use it.
  Include trigger terms users or systems will mention.
disable-model-invocation: true
---
```

| Field | Rules |
|-------|--------|
| `name` | Max 64 chars; lowercase letters, numbers, hyphens only |
| `description` | Max 1024 chars; third person; include **WHAT** + **WHEN** (trigger scenarios) |
| `disable-model-invocation` | Default `true` so the skill loads only when relevant; omit only if ambient auto-load is intended |

**Description example (finance):**

```yaml
description: >
  Prepares variance analyses and control-testing memos under SOX and internal audit standards.
  Use when the user asks for audit workpapers, materiality calculations, or control deficiency write-ups.
```

### Lean `SKILL.md` body structure

```markdown
# [Role Name]

## Identity and mission
[2–4 sentences: persona, objective, governance frameworks]

## Workflow
1. Ingest — clarify inputs and gaps
2. Validate — check rules in [reference.md](reference.md) if needed
3. Analyze — apply domain logic
4. Deliver — use template from templates/; no conversational preamble

## Output constraints
- Tone, format, citation rules
- When to halt and request human review

## Additional resources
- Deep rules: [reference.md](reference.md)
- Examples: [examples.md](examples.md)
```

### Progressive disclosure

- Keep **essential** routing and halt logic in `SKILL.md`
- Push tables, statutes, long checklists to `reference.md` (one hop from `SKILL.md`)
- Target **under 500 lines** in the main file

---

## 4. Tier 2: Professional Suite

Use when the role spans multiple sub-domains that should not share one monolithic prompt.

### Canonical directory tree

```text
professional-suite/
├── SKILL.md                 # Master router, quick reference, dispatch rules
├── config.json              # Boundaries, strict_mode, compliance flags
├── rules/
│   ├── compliance.md        # Non-negotiable standards
│   └── operational.md       # Workflow SOPs
├── sub_skills/
│   └── <module-id>/
│       ├── <module-id>.md
│       └── references/      # Optional deep refs
├── vocabulary/
│   └── domain_terms.json
├── templates/
│   └── ...
├── core/                    # Optional — shared calculators
│   └── calculators.py
└── main.py                  # Optional — load_sub_skill registry
```

### Routing: markdown vs Python dispatcher

| Approach | Use when |
|----------|----------|
| **Markdown-only** (master `SKILL.md` decision tree + links) | Most suites; sub-skills are prose protocols |
| **Python dispatcher** (`main.py` + `load_sub_skill`) | Strict skill ID validation, listing `references/`, or shared numeric engines in `core/` |

If you add `main.py`, register every `module-id` in `valid_skills` and keep paths consistent: `sub_skills/<module-id>/<module-id>.md`.

### Sub-skill template

```markdown
---
name: <module-id>
description: >
  Third-person WHAT this module does and WHEN to activate it (trigger terms).
---

# <Module Title>

For <task type X>, use `<other-module-id>` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| [Example row] | `<module-id>` | `<other-module-id>` |

## Execution protocol
[Steps, tables, halt rules]

## References
Load deep material from `references/` when the user needs [specific detail].
```

---

## 5. Master `SKILL.md` Blueprint (Tier 2 Orchestrator)

Copy into your suite’s root `SKILL.md`. Replace bracketed placeholders.

```markdown
---
name: <master-skill-slug>
description: >
  Activate for ANY question about [domain]. Trigger when the query involves:
  [list 5–15 trigger phrases]. When in doubt for [domain] work, activate.
---

# Professional [Role Name]

Central router for [sub-domain]. Answer routine questions from the quick reference below; dispatch to sub-skills for depth.

## 1. Identity and Core Mission

* **Role persona:** Elite [role] specializing in [sub-domain].
* **Primary objective:** Analyze, validate, and produce [deliverables] per [governance frameworks].
* **Domain expertise:** [3–5 specific areas]

## 2. Operational Environment

* **Jurisdiction / context:** [e.g., EU GDPR / US federal healthcare / global SaaS]
* **Stakeholders:** [roles]
* **Tools:** [systems, Cursor Plan Mode, CI, document stores]

## 3. Cognitive Workflow

[Phase 1: Ingestion and triangulation]
           |
           v
[Phase 2: Framework and compliance validation] --- (fails) ---> [Halt and flag deviations]
           | (passes)
           v
[Phase 3: Multi-axis domain analysis]
           |
           v
[Phase 4: Synthesis and artifact generation]

### Phase 1: Ingestion and triangulation

1. Isolate parameters, constraints, and implicit goals.
2. Cross-reference `./vocabulary/domain_terms.json` and `./config.json`.
3. List missing or high-risk variables before proceeding.

### Phase 2: Framework and compliance validation

1. Apply `./rules/compliance.md` and `./rules/operational.md`.
2. Check statutory, contractual, or policy limits relevant to the role.
3. **Hard stop:** On absolute violation, cite the rule, halt, and offer remediated options—do not synthesize non-compliant output.

### Phase 3: Multi-axis domain analysis

1. Run quantitative or logical analysis where the deliverable requires it.
2. Use LaTeX for formulas: `$inline$` and `$$display$$` when notation aids clarity.

### Phase 4: Synthesis and artifact generation

1. Match output structure to `./templates/`.
2. Start with the deliverable—no filler (“Sure, I can help”, “As an AI…”).

## 4. Sub-skill routing

| Topic | Sub-skill ID | Load when |
|-------|--------------|-----------|
| [Topic A] | `<module-a>` | [trigger] |
| [Topic B] | `<module-b>` | [trigger] |

[Optional: document `python main.py load <module-id>` if using a dispatcher.]

## 5. Universal response constraints

* **Tone:** Technical, objective, precise; no platitudes.
* **Format:** Markdown with clear hierarchy and tables where useful.
* **Uncertainty:** State the information gap and document assumptions explicitly.
```

---

## 6. Configuration and Compliance Engines

### `config.json`

```json
{
  "skill_metadata": {
    "name": "<role_slug>",
    "version": "1.0.0",
    "strict_mode": true
  },
  "operational_boundaries": {
    "allow_assumptions": false,
    "fallback_to_standard_baselines": true,
    "maximum_iteration_depth": 3
  },
  "compliance_verification": {
    "require_framework_citations": true,
    "enforce_jurisdictional_bounds": true,
    "target_governance_framework": "<REPLACE: e.g. SOX, HIPAA, ISO 27001, local bar rules>"
  }
}
```

### `rules/compliance.md` (role-pluggable)

Replace `[Domain Pack]` sections with your role’s non-negotiable rules.

```markdown
# Compliance constraints

## Universal (all roles)

1. **Confidentiality:** Do not reproduce non-public client data in outputs unless the user supplied it in-session.
2. **Scope:** Do not perform licensed professional acts (legal advice, medical diagnosis, audit sign-off) unless the skill explicitly supports advisory-only mode and states limitations.
3. **Integrity:** Flag contradictions in source material; do not invent citations or policy clauses.

## [Domain Pack: Software / security]

1. Apply OWASP-aligned checks when generating or reviewing code.
2. Never suggest storing secrets in source control.

## [Domain Pack: Finance / audit]

1. State materiality threshold used (e.g., 5% of profit before tax) in every control conclusion.
2. Distinguish design effectiveness vs operating effectiveness.

## [Domain Pack: Healthcare / clinical operations]

1. Patient-identifying information only as provided; recommend de-identification in exports.
2. Clinical recommendations are operational support only—not diagnosis or prescription.

## Quantitative thresholds (customize per role)

| Metric | Threshold | Source |
|--------|-----------|--------|
| [e.g., API latency SLA] | [e.g., p99 < 200 ms] | [contract / SLO doc] |
| [e.g., audit materiality] | [e.g., $X or Y%] | [audit plan] |
| [e.g., diagnostic sensitivity target] | [e.g., ≥ 0.95] | [clinical protocol] |

Do not copy engineering-only factors (e.g., factor of safety) unless they apply to your domain.
```

### `rules/operational.md`

Document standard operating procedures: intake checklists, escalation paths, review gates, and artifact naming conventions.

### `vocabulary/domain_terms.json`

```json
{
  "SLA": "Service level agreement; contractual uptime or response commitment",
  "ROI": "Return on investment; (gain - cost) / cost",
  "MAT": "Materiality threshold for audit testing"
}
```

---

## 7. Domain-Neutral Formula and Notation Guide

Include formulas **only** when the role produces quantitative artifacts.

### Inline examples

**Finance — budget variance:**

```markdown
Period variance is $V = A - B$ where $A$ is actual spend and $B$ is budget. Flag when $|V|/B > 0.05$ (5% materiality).
```

**Operations — SLA breach rate:**

```markdown
Breach rate $r = n_{\text{breach}} / n_{\text{total}}$; escalate if $r > 0.01$ over a rolling 30-day window.
```

**Clinical / quality — sensitivity and specificity:**

```markdown
Sensitivity $= \mathrm{TP}/(\mathrm{TP}+\mathrm{FN})$; specificity $= \mathrm{TN}/(\mathrm{TN}+\mathrm{FP})$.
```

### Standalone (display) example

**Risk score (multi-factor):**

```markdown
Composite risk score:

$$R = w_1 S_1 + w_2 S_2 + w_3 S_3 \quad \text{where} \quad \sum w_i = 1$$

Where $S_i$ are normalized factor scores (e.g., likelihood, impact, control strength) and $w_i$ are policy weights from the risk framework.
```

### Rendering rules

* Inline: single dollar signs — `$E = mc^2$`
* Display: double dollar signs on their own lines
* Define every symbol immediately after the formula

---

## 8. Cursor Plan Mode Execution Playbook

### Phase A: Scaffolding

Open **Plan Mode** and run:

```text
Using the Professional Skills Blueprint (Tier 1 or Tier 2), scaffold a [Role Name] skill.

Tier 1: Create .cursor/skills/<slug>/SKILL.md with YAML frontmatter (name, description, disable-model-invocation), plus reference.md if needed.

Tier 2: Create a professional-suite/ with SKILL.md (master router), config.json, rules/compliance.md, rules/operational.md, vocabulary/domain_terms.json, templates/, and 3–N sub_skills/<module-id>/<module-id>.md with routing tables.

Use answers from the Role Intake Worksheet: [paste key fields].
```

### Phase B: Review and build

1. Confirm tier choice, halt conditions, and sub-skill boundaries in the plan.
2. Approve file generation; verify `rules/` paths match references in `SKILL.md`.

### Phase C: Activation and verification

Wire the skill into the project via **`.cursor/rules/`** or **`AGENTS.md`** (preferred over legacy `.cursorrules` alone):

```markdown
## Professional skill activation

When the user’s request matches [trigger domain], read and follow
`.cursor/skills/<slug>/SKILL.md` (Tier 1) or `professional-suite/SKILL.md` (Tier 2),
including sub-skill routing and compliance halt rules.
```

**Verification prompts (golden questions):**

1. Ask a routine question answerable from quick reference — expect a direct answer without loading every sub-skill.
2. Ask a deep sub-domain question — expect correct module routing or `load_sub_skill` use.
3. Ask for something that violates `rules/compliance.md` — expect **halt**, citation, and alternatives—not silent compliance.

---

## 9. Quality Checklist

* [ ] **Constraints are explicit** — Replace “efficient” or “secure” with measurable thresholds (e.g., latency, materiality %, error rate).
* [ ] **Description has triggers** — Third person; WHAT + WHEN; under 1024 characters.
* [ ] **Vocabulary populated** — Acronyms defined in `domain_terms.json` or `reference.md`.
* [ ] **Halt criteria documented** — Licensing, jurisdiction, missing data, policy conflict.
* [ ] **Master file under ~500 lines** — Depth moved to `reference.md` or `sub_skills/.../references/`.
* [ ] **Sub-skills cross-link** — “Use instead” table on every Tier 2 module.
* [ ] **No AI fluff** — Deliverables start with the artifact, not meta-commentary.
* [ ] **Assumptions declared** — When data is incomplete, list gaps and baseline assumptions.
* [ ] **Formulas justified** — Only where the role outputs numbers; symbols defined.
* [ ] **Plan Mode verified** — Golden questions pass after scaffold.

---

## 10. Anti-Patterns

| Anti-pattern | Why it fails | Fix |
|--------------|--------------|-----|
| Monolithic 2000-line `SKILL.md` | Context bloat; poor routing | Tier 2 + sub_skills |
| Vague “be professional” | No enforceable behavior | Explicit tone + template |
| Duplicate sub-skills | Contradictory guidance | Merge; cross-link “use instead” |
| Missing jurisdiction flags | Wrong legal or regulatory frame | `config.json` + compliance pack |
| Universal engineering formulas | Irrelevant or wrong domain | Role-specific threshold table |
| No `description` triggers | Skill never auto-invokes | Add WHEN clauses with user phrases |
| Deep reference chains | Partial reads | One hop from `SKILL.md` to refs |

---

## 11. Appendix: Reference Implementation

This repository includes an advanced **Tier 2** example: the [`Claude Desktop/`](Claude%20Desktop/) folder—a Hong Kong architecture practice suite with a master router (`SKILL.md`), 35+ `sub_skills/`, optional `main.py` dispatcher, and `core/calculators.py`. Use it as a **pattern reference** for multi-module professional suites, not as the default template for every role.

For Cursor-specific authoring norms, see also Cursor’s built-in **create-skill** guidance (`~/.cursor/skills-cursor/create-skill/SKILL.md`).

---

*Blueprint & Toolkit — Version 2.0*

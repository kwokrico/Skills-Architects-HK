# HK Architect Skills

### A Tier 2 professional skill suite for Hong Kong architectural practice

`Skills-Architects-HK` is a localized architecture skill built around one master router (`hk-architect-master`) and **47** specialist topic files. It follows the [FUNC_Skills_Guideline](FUNC_Skills_Guideline/GUIDELINE.md) canonical layout: `SKILL.md`, `subskills/`, `references/`, `scripts/`, and `evals/`.

---

- `hk-architect-master/`: Skill content root (`SKILL.md`, subskills, references, scripts, evals)
- `hk_architect_skills/`: Installable Python dispatcher (`HKSkillsDispatcher`, calculators)
- `hk-architect-master-workspace/`: Sibling eval run outputs (gitignored)

- [Quick Start](#quick-start)
- [What You Get](#what-you-get)
- [How It Works](#how-it-works)
- [Skill Map](#skill-map)
- [Calculators](#calculators)
- [Folder Structure](#folder-structure)
- [Verification](#verification)
- [Example Prompts](#example-prompts)
- [Standards and Frameworks](#standards-and-frameworks)
- [Credits](#credits)

---

## Quick Start

### Option 1: Claude Code or Cursor skill

The entrance is `hk-architect-master/SKILL.md`. The agent reads a linked topic or catalogue file. It does not load topic text through `load_sub_skill`.

Claude Code discovers a skill only when `SKILL.md` sits in `.claude/skills/<name>/` or `~/.claude/skills/<name>/`. This repo links the skill folder rather than copying it:

```powershell
New-Item -ItemType Directory -Force -Path .claude/skills
New-Item -ItemType Junction -Path .claude/skills/hk-architect-master -Target (Resolve-Path ./hk-architect-master)
```

For a user-wide install, point the junction at the same folder from `~/.claude/skills/hk-architect-master`. Recreate the junction on a machine where it is missing. Do not copy the folder.

### Option 2: Calculator package

From the repo root:

```bash
pip install -e .
echo '{"tool":"run_hk_calculator","arguments":{"calc_type":"gfa_aggregator","data":{"floors":[{"area":500,"is_exempt":false}]}}}' | python hk-architect-master/main.py
```

Override the content root with `HK_ARCHITECT_SKILLS_ROOT` if needed. An older `load_sub_skill` call still returns a topic file for existing scripts. The skill instructions do not use that call.

### Option 3: Use directly in Claude Desktop

1. Install the module: `pip install -e .`
2. Point Claude at the plugin folder:

```bash
claude --plugin-dir "./hk-architect-master"
```

3. Plugin `main.py` delegates to `hk_architect_skills`.

### Option 4: Full HK Architect Desk (vault + RAG)

Use the separate **Architect Desk-HK** application repo, which installs this package as a dependency:

```bash
pip install -e /path/to/Skills-Architects-HK
pip install -e /path/to/Architect-Desk-HK
```

---

## What You Get

- **1 master router skill**: `hk-architect-master` in `hk-architect-master/SKILL.md`
- **47 subskills** across compliance, design, engineering, and delivery
- **Built-in quick-reference layer** in `hk-architect-master/references/foundation.md`
- **Calculation support** via `hk-architect-master/scripts/calculators.py`
- **Routing by file link** from `SKILL.md` to one topic file and, when needed, one catalogue file

---

## How It Works

The system follows a progressive flow:

1. **Quick answer first**  
   The master skill reads `references/foundation.md` for a routine table (travel distances, baseline zoning, envelope rules).

2. **Open one topic file**  
   For a workflow or an edge case, it reads the `subskills/<slug>/<slug>.md` file linked from `SKILL.md`. Catalogue rows (minor-works items, practice notes, Lands documents, Fire Services Department circulars) stay in `references/catalogues/` and are opened only when a row is needed. `references/statutory/` is a copy of those Critical Summaries, and `hk_s_reference` remains the archive. These copies are not updated automatically.

3. **Run computations for numeric checks**  
   For calculation tasks, it calls `run_hk_calculator`, implemented in `scripts/calculators.py`.

This keeps routine queries fast while preserving deep, domain-specific responses for complex work.

---

## Skill Map

### 1) Regulatory and Statutory

- `hk-building-codes`
- `hk-spatial-planning`
- `hk-fire-life-safety`
- `hk-accessibility-design`
- `hk-minor-works`
- `hk-mandatory-inspection`
- `hk-consent-scheduling`
- `hk-alterations-additions`
- `hk-lease-compliance`
- `hk-unauthorised-building-works`
- `hk-fsd-licensing-compliance`
- `hk-certificate-of-compliance`

### 2) Technical and Performance Design

- `hk-building-sustainability`
- `hk-building-envelope`
- `hk-building-services`
- `hk-structural-systems`
- `hk-acoustic-design`
- `hk-daylighting-design`
- `hk-material-selection`
- `hk-building-programming`
- `hk-building-typology`
- `hk-mic-dfma`

### 3) Design and Documentation

- `hk-concept-design`
- `hk-construction-documentation`
- `hk-design-theory`
- `hk-architect-calculator`

### 4) Delivery, Contract, and Practice Operations

- `hk-site-supervision`
- `hk-procurement-strategy`
- `hk-tender-contract-administration`
- `hk-fee-proposal-strategy`
- `hk-cashflow-debt-recovery`
- `hk-project-resource-levelling`
- `hk-professional-indemnity`
- `hk-professional-conduct`
- `hk-op-submission-strategy`
- `hk-practical-completion-snagging`
- `hk-heritage-conservation`
- `hk-cost-consultancy`
- `hk-construction-health-safety`
- `hk-construction-programme`
- `hk-project-management`
- `hk-deliverables-workstages`
- `hk-plan-of-work`
- `hk-architect-foundations`

---

## Verification

See [hk-architect-master/VERIFICATION.md](hk-architect-master/VERIFICATION.md) for golden prompts. Formal eval cases: [hk-architect-master/evals/evals.json](hk-architect-master/evals/evals.json).

---

## Calculators

The calculator module supports (via `run_hk_calculator`):

- **Egress check** (`egress_1004_7`): simplified rectangular-room check vs FS Code travel limits (not full remotest-point path)
- **GFA aggregation** (`gfa_aggregator`): accountable vs exempt GFA roll-up (`floors` array in JSON)
- **Layout sorting** (`layout_sort`): OCR/layout ordering helper by X/Y coordinates

OTTV, MOE exit width, and occupant load formulas live in `hk-architect-calculator` markdown only.

---

## Folder Structure

```text
Skills-Architects-HK/
├── hk-architect-master/           # Tier 2 skill (GUIDELINE.md layout)
│   ├── SKILL.md                   # Master router: hk-architect-master
│   ├── main.py                    # Claude plugin stdin entry
│   ├── subskills/                 # specialist modules
│   ├── references/
│   │   ├── foundation.md          # Routine lookup tables
│   │   ├── compliance.md
│   │   ├── operational.md
│   │   ├── domain_terms.json
│   │   ├── config.json
│   │   ├── catalogues/            # Item, practice-note, and circular rows
│   │   ├── templates/
│   │   └── hk-*.md                # Module deep-dives
│   ├── scripts/
│   │   ├── calculators.py
│   │   └── dispatcher.py
│   ├── evals/
│   │   └── evals.json
│   └── VERIFICATION.md
├── hk_architect_skills/           # pip install -e .
│   ├── dispatcher.py
│   ├── paths.py
│   └── core/calculators.py        # Re-export shim → scripts/
└── hk-architect-master-workspace/ # Eval outputs (gitignored)
```

`.claude/skills/hk-architect-master` is a directory junction to `hk-architect-master/` so Claude Code can discover `SKILL.md`. Recreate it with the Quick Start command if it is missing.

For **Cursor**, optional activation rule: [`.cursor/rules/hk-architect-skills.mdc`](.cursor/rules/hk-architect-skills.mdc).

### Breaking change (v2.1 layout)

The skill folder was renamed from `Claude Desktop/` to `hk-architect-master/` to match `references/config.json` → `skill_metadata.name`. Update install paths:

- `pip install -e .` (repo root)
- `claude --plugin-dir "./hk-architect-master"`

---

## Example Prompts

- "Classify this mixed-use tower under BO/PNAP and flag key compliance risks."
- "Check egress strategy for a 28-storey composite building with two scissor stairs."
- "What OZP and lease constraints should I validate before concept massing?"
- "Compare OTTV/RTTV reduction options for a west-facing facade in Hong Kong."
- "Draft a submission sequence from general building plans to OP."
- "Evaluate whether this A&A scope falls under MWCS or full approval."
- "Build a consultant fee proposal with scope boundaries and additional-services triggers."
- "Use the calculator to aggregate GFA with exempt features and report accountable GFA."

---

## Standards and Frameworks

This suite is designed around Hong Kong practice and frequently references:

- Buildings Ordinance (Cap. 123) and related regulations
- PNAP series (including APP-2, APP-40, APP-130, APP-152, ADV-36, ADV-49)
- Code of Practice for Fire Safety in Buildings
- Design Manual: Barrier Free Access
- Town Planning Ordinance and OZP-driven planning controls
- BEAM Plus workflows and environmental performance expectations

Always verify project-specific conditions (OZP notes, lease clauses, and authority comments), since those can override rule-of-thumb guidance.

---

## Credits

This project is a Hong Kong localization and expansion of the original [Skills-Architects](https://github.com/Amanbh997/Skills-Architects) framework by Abhinav Bhardwaj, adapted for local regulations, workflow realities, and delivery practice.

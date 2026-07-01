# HK Architect Skills

### A Tier 2 professional skill suite for Hong Kong architectural practice

`Skills-Architects-HK` is a localized architecture plugin built around one master router (`hk-architect-master`) and **42** specialist subskills. It follows the [FUNC_Skills_Guideline](FUNC_Skills_Guideline/GUIDELINE.md) canonical layout: `subskills/`, `references/`, `scripts/`, and `evals/`.

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

### Option 1: Install as Python module (recommended)

From the repo root:

```bash
pip install -e .
```

Dispatch skills tools from any host (Claude Desktop plugin, Architect Desk, scripts):

```bash
echo '{"tool":"load_sub_skill","arguments":{"skill_id":"hk-building-codes"}}' | python hk-architect-master/main.py
```

Or programmatically:

```python
from hk_architect_skills.dispatcher import HKSkillsDispatcher
HKSkillsDispatcher().dispatch("load_sub_skill", {"skill_id": "hk-building-codes"})
```

Override the content root with `HK_ARCHITECT_SKILLS_ROOT` if needed.

### Option 2: Use directly in Claude Desktop

1. Install the module: `pip install -e .`
2. Point Claude at the plugin folder:

```bash
claude --plugin-dir "./hk-architect-master"
```

3. Plugin `main.py` delegates to `hk_architect_skills`.

### Option 3: Full HK Architect Desk (vault + RAG)

Use the separate **Architect Desk-HK** application repo, which installs this package as a dependency:

```bash
pip install -e /path/to/Skills-Architects-HK
pip install -e /path/to/Architect-Desk-HK
```

---

## What You Get

- **1 master router skill**: `hk-architect-master` in `hk-architect-master/SKILL.md`
- **42 subskills** across compliance, design, engineering, and delivery
- **Built-in quick-reference layer** for common HK metrics and code checks
- **Calculation support** via `hk-architect-master/scripts/calculators.py`
- **Structured routing** through `load_sub_skill` and calculator dispatch via `HKSkillsDispatcher`

---

## How It Works

The system follows a progressive flow:

1. **Quick answer first**  
   The master skill checks if your question can be answered from built-in HK quick references (e.g., PNAP snapshots, travel distances, baseline zoning and envelope rules).

2. **Route to a specialist when needed**  
   For deeper queries, it dispatches to `subskills/<slug>/<slug>.md` via `load_sub_skill`.

3. **Run computations for numeric checks**  
   For calculation tasks, it calls calculator workflows through `run_hk_calculator`.

This keeps routine queries fast while preserving deep, domain-specific responses for complex work.

---

## Skill Map

### 1) Regulatory and Statutory

- `hk-building-codes`
- `hk-spatial-planning`
- `hk-fire-life-safety`
- `hk-accessibility-design`
- `hk-minor-works`
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
│   ├── subskills/                 # 42 specialist modules
│   ├── references/
│   │   ├── compliance.md
│   │   ├── operational.md
│   │   ├── domain_terms.json
│   │   ├── config.json
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

# HK Architect Skills

### A Claude Desktop skill suite for Hong Kong architectural practice

`Skills-Architects-HK` is a localized architecture plugin built around one master router (`hk-architect-master`) and 34 specialist sub-skills. It is tuned for Hong Kong statutory, technical, and delivery workflows: BO/PNAP compliance, OZP planning logic, fire and accessibility checks, BEAM Plus strategy, MiC/DfMA coordination, submissions, OP handover, and post-contract administration.

---

- `SKILL.md`: Main entry skill (`hk-architect-master`) with routing logic and quick-reference tables.
- `sub_skills/*.md`: Domain sub-skills for focused expertise (codes, planning, fire, sustainability, delivery, contract, handover, etc.).
- `core/calculators.py`: Calculation helpers used by calculator workflows.
- `main.py`: Runtime entry point for loading sub-skills and tool dispatch.

- [Quick Start](#quick-start)
- [What You Get](#what-you-get)
- [How It Works](#how-it-works)
- [Skill Map](#skill-map)
- [Calculators](#calculators)
- [Folder Structure](#folder-structure)
- [Example Prompts](#example-prompts)
- [Standards and Frameworks](#standards-and-frameworks)
- [Credits](#credits)

---

## Quick Start

### Option 1: Use directly in Claude Desktop

1. Copy or clone this folder into your Claude Desktop skills workspace.
2. Keep the package structure unchanged:
   - `SKILL.md`
   - `sub_skills/`
   - `core/`
   - `main.py`
3. Load the skill package from this directory.
4. Start a new chat and ask a Hong Kong architecture question.

### Option 2: Plugin directory launch

```bash
claude --plugin-dir "/path/to/Skills-Architects-HK/Claude Desktop"
```

---

## What You Get

- **1 master router skill**: `hk-architect-master` in `SKILL.md`
- **34 sub-skills** across compliance, design, engineering, and delivery
- **Built-in quick-reference layer** for common HK metrics and code checks
- **Calculation support** via `core/calculators.py`
- **Structured routing** through `load_sub_skill` and calculator dispatch

---

## How It Works

The system follows a progressive flow:

1. **Quick answer first**  
   The master skill checks if your question can be answered from built-in HK quick references (e.g., PNAP snapshots, travel distances, baseline zoning and envelope rules).

2. **Route to a specialist when needed**  
   For deeper queries, it dispatches to the best-matching sub-skill using `load_sub_skill`.

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
- `hk-tender-contract-administration`
- `hk-fee-proposal-strategy`
- `hk-cashflow-debt-recovery`
- `hk-project-resource-levelling`
- `hk-professional-indemnity`
- `hk-op-submission-strategy`
- `hk-practical-completion-snagging`
- `hk-heritage-conservation`

---

## Calculators

The calculator module currently supports:

- **Egress check** (`egress_1004_7`): travel-distance style compliance logic from room geometry
- **GFA aggregation** (`gfa_aggregator`): accountable vs exempt GFA roll-up logic
- **Layout sorting utility** (`layout_sort`): OCR/layout ordering helper by X/Y coordinates

---

## Folder Structure

```text
Claude Desktop/
├── SKILL.md                      # Master router: hk-architect-master
├── main.py                       # Runtime entry and dispatch
├── core/
│   └── calculators.py            # Calculator workflows
└── sub_skills/
    ├── hk-building-codes/
    ├── hk-fire-life-safety/
    ├── hk-spatial-planning/
    ├── ... (34 specialist skills total)
    └── hk-heritage-conservation/
```

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
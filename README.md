# Skills-Architects-HK (Claude Desktop)

Hong Kong architecture skill suite for Claude Desktop.

This package uses a **master router skill** (`SKILL.md`) plus modular `sub_skills` that cover statutory compliance, technical design, and project delivery workflows specific to Hong Kong practice.

## What This Installs

- `SKILL.md`: Main entry skill (`hk-architect-master`) with routing logic and quick-reference tables.
- `sub_skills/*.md`: Domain sub-skills for focused expertise (codes, planning, fire, sustainability, delivery, contract, handover, etc.).
- `core/calculators.py`: Calculation helpers used by calculator workflows.
- `main.py`: Runtime entry point for loading sub-skills and tool dispatch.

## Installation (Claude Desktop)

1. Copy or clone this folder into your local Claude Desktop skills/workspace location.
2. Ensure this folder keeps the current structure:
   - `SKILL.md`
   - `sub_skills/`
   - `core/`
   - `main.py`
3. In Claude Desktop, load the skill package from this directory.
4. Start a new chat and trigger with HK architecture prompts (for example: BO/PNAP compliance, OZP planning, BEAM Plus, OP workflow, MiC, or tender admin).

If you are distributing this as a plugin package, keep the directory names unchanged so `load_sub_skill` can resolve the sub-skill files correctly.

## Skill Capability

The current structure is built around **34 specialized sub-skills** routed by the master skill.

### 1) Regulatory and Statutory

- `hk-building-codes`, `hk-spatial-planning`, `hk-fire-life-safety`, `hk-accessibility-design`
- `hk-minor-works`, `hk-consent-scheduling`, `hk-alterations-additions`, `hk-lease-compliance`
- `hk-unauthorised-building-works`, `hk-fsd-licensing-compliance`, `hk-certificate-of-compliance`

### 2) Technical and Performance Design

- `hk-building-sustainability`, `hk-building-envelope`, `hk-building-services`, `hk-structural-systems`
- `hk-acoustic-design`, `hk-daylighting-design`, `hk-material-selection`
- `hk-building-programming`, `hk-building-typology`, `hk-mic-dfma`

### 3) Design and Documentation

- `hk-concept-design`, `hk-construction-documentation`, `hk-design-theory`
- `hk-architect-calculator`

### 4) Delivery, Contract, and Commercial Practice

- `hk-site-supervision`, `hk-tender-contract-administration`, `hk-fee-proposal-strategy`
- `hk-cashflow-debt-recovery`, `hk-project-resource-levelling`, `hk-professional-indemnity`
- `hk-op-submission-strategy`, `hk-practical-completion-snagging`, `hk-heritage-conservation`

## How Routing Works

- The master skill first answers straightforward queries using built-in quick references.
- For deeper questions, it routes to the most relevant sub-skill through `load_sub_skill`.
- Multi-topic questions are handled by primary-skill routing with cross-reference to secondary skills when needed.

## Credits

This project is a localized expansion of the original [Skills-Architects](https://github.com/Amanbh997/Skills-Architects) framework by Abhinav Bhardwaj, adapted for Hong Kong regulations, workflows, and delivery conditions.
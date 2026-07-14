"""Shared dispatcher — subskills loader and calculators."""

import os

from calculators import run_calculation


SKILL_REFERENCES = {
    "hk-construction-programme": ["hk-construction-sequence-swimlanes.md"],
    "hk-design-theory": ["hk-human-scale-dimensions.md"],
    "hk-heritage-conservation": ["hia-starter-checklist.md"],
    "hk-material-selection": ["hk-common-material-dimensions.md"],
    "hk-plan-of-work": ["hk-pow-stages-0-7.md"],
    "hk-procurement-strategy": [
        "hk-procurement-routes-comparison.md",
        "hk-typhoon-eot-by-procurement.md",
    ],
    "hk-site-establishment": [
        "hk-site-establishment-checklist.md",
        "hk-construction-stakeholder-register.md",
    ],
    "hk-traffic-coordination": ["hk-td-submission-types.md"],
    "hk-telecom-coordination": ["hk-ofca-licensed-works.md"],
}


class HKSkillsDispatcher:
    VALID_SKILLS = [
        "hk-accessibility-design", "hk-acoustic-design", "hk-architect-calculator",
        "hk-architect-foundations",
        "hk-building-codes", "hk-building-envelope", "hk-building-programming",
        "hk-building-services", "hk-building-sustainability", "hk-building-typology",
        "hk-concept-design", "hk-construction-documentation", "hk-construction-health-safety",
        "hk-construction-programme",
        "hk-site-establishment", "hk-traffic-coordination", "hk-telecom-coordination",
        "hk-cost-consultancy", "hk-daylighting-design",
        "hk-design-theory", "hk-fire-life-safety", "hk-material-selection",
        "hk-spatial-planning", "hk-structural-systems", "hk-minor-works",
        "hk-consent-scheduling", "hk-alterations-additions", "hk-lease-compliance",
        "hk-heritage-conservation",
        "hk-deliverables-workstages",
        "hk-site-supervision", "hk-unauthorised-building-works",
        "hk-tender-contract-administration", "hk-fee-proposal-strategy", "hk-mic-dfma",
        "hk-professional-indemnity", "hk-cashflow-debt-recovery", "hk-certificate-of-compliance",
        "hk-project-management", "hk-project-resource-levelling",
        "hk-op-submission-strategy", "hk-plan-of-work", "hk-practical-completion-snagging",
        "hk-procurement-strategy",
        "hk-fsd-licensing-compliance",
    ]

    def __init__(self, skills_root=None):
        if skills_root is None:
            from hk_architect_skills.paths import get_skills_root
            skills_root = get_skills_root()
        self.base_path = str(skills_root)
        self.subskills_base = os.path.join(self.base_path, "subskills")
        self.references_base = os.path.join(self.base_path, "references")

    def _skill_file_path(self, skill_id):
        primary = os.path.join(self.subskills_base, skill_id, f"{skill_id}.md")
        if os.path.isfile(primary):
            return primary
        legacy = os.path.join(
            self.subskills_base, skill_id, f"{skill_id.replace('-works', '-work')}.md"
        )
        if os.path.isfile(legacy):
            return legacy
        return primary

    def _references_available(self, skill_id):
        refs = SKILL_REFERENCES.get(skill_id, [])
        return [name for name in refs if os.path.isfile(os.path.join(self.references_base, name))]

    def load_sub_skill(self, skill_id):
        if skill_id not in self.VALID_SKILLS:
            return {"error": f"Skill ID '{skill_id}' not recognized."}

        file_path = self._skill_file_path(skill_id)

        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
            return {
                "status": "success",
                "skill_id": skill_id,
                "instructions": content,
                "references_available": self._references_available(skill_id),
            }
        except FileNotFoundError:
            return {"error": f"Expected file at {file_path} not found."}
        except OSError as e:
            return {"error": str(e)}

    def run_hk_calculator(self, calc_type, data=None):
        data = data or {}
        valid_types = ("egress_1004_7", "gfa_aggregator", "layout_sort")
        if calc_type not in valid_types:
            return {"error": f"Calculator '{calc_type}' not recognized."}

        if calc_type == "gfa_aggregator":
            floor_data = data if isinstance(data, list) else data.get("floors", data)
            result = run_calculation(calc_type, floor_data)
        else:
            result = run_calculation(calc_type, data)

        if isinstance(result, dict) and result.get("error"):
            return result
        return {"status": "success", "calc_type": calc_type, "result": result}

    def dispatch(self, tool_name, arguments=None):
        arguments = arguments or {}
        if tool_name == "load_sub_skill":
            return self.load_sub_skill(arguments.get("skill_id"))
        if tool_name == "run_hk_calculator":
            return self.run_hk_calculator(arguments.get("calc_type"), arguments.get("data"))
        return {"error": f"Unknown skills tool: {tool_name}"}

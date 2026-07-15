"""Re-export calculators from hk-architect-master/scripts."""

import importlib.util
import sys

from hk_architect_skills.paths import get_skills_root


def _load_calculators_module():
    scripts_dir = get_skills_root() / "scripts"
    path = scripts_dir / "calculators.py"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    spec = importlib.util.spec_from_file_location("hk_skill_scripts_calculators", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_mod = _load_calculators_module()
EgressCalculator = _mod.EgressCalculator
GFACalculator = _mod.GFACalculator
DataSorter = _mod.DataSorter
run_calculation = _mod.run_calculation

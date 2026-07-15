"""Skills-only dispatcher — re-exports from hk-architect-master/scripts."""

import importlib.util
import sys
from pathlib import Path

from hk_architect_skills.paths import get_skills_root


def _load_dispatcher_class():
    scripts_dir = get_skills_root() / "scripts"
    path = scripts_dir / "dispatcher.py"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    spec = importlib.util.spec_from_file_location("hk_skill_scripts_dispatcher", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.HKSkillsDispatcher


HKSkillsDispatcher = _load_dispatcher_class()

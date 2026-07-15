"""Resolve the hk-architect-master skills content root."""

import os
from pathlib import Path


def get_skills_root() -> Path:
    """
    Return the directory containing SKILL.md, subskills/, references/, etc.

    Override with HK_ARCHITECT_SKILLS_ROOT for custom installs.
    Default: sibling ``hk-architect-master/`` next to this package.
    """
    override = os.environ.get("HK_ARCHITECT_SKILLS_ROOT")
    if override:
        return Path(override).resolve()
    return (Path(__file__).resolve().parent.parent / "hk-architect-master").resolve()

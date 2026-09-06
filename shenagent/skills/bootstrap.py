from __future__ import annotations

from skills import SkillRegistry


def load_builtin_skills() -> list[str]:
    SkillRegistry.load_module("skills.builtin")
    return [s.name for s in SkillRegistry.all_skills()]

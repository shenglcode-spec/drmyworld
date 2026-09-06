from __future__ import annotations

import importlib
import inspect
import json
import re
from typing import Callable, get_type_hints

_TYPE_MAP = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
}

_REGISTRY: dict[str, "Skill"] = {}


class Skill:
    def __init__(self, func: Callable):
        self.func = func
        self.name = func.__name__
        self.description, self.param_docs = self._parse_docstring(func.__doc__ or "")
        self.schema = self._build_schema(func)

    def _parse_docstring(self, doc: str) -> tuple[str, dict]:
        desc_lines, params = [], {}
        in_args = False
        for line in doc.strip().splitlines():
            stripped = line.strip()
            lowered = stripped.lower()
            if lowered in ("args:", "arguments:", "parameters:"):
                in_args = True
                continue
            if lowered in ("returns:", "raises:", "examples:"):
                in_args = False
                continue
            if in_args:
                m = re.match(r"([\w_]+)\s*(?:\([\w\[\], |]+\))?\s*:\s*(.+)", stripped)
                if m:
                    params[m.group(1)] = m.group(2)
            elif stripped:
                desc_lines.append(stripped)
        return "\n".join(desc_lines), params

    def _build_schema(self, func: Callable) -> dict:
        hints = get_type_hints(func)
        properties, required = {}, []
        for pname, param in inspect.signature(func).parameters.items():
            ptype = _TYPE_MAP.get(hints.get(pname, str), "string")
            prop = {"type": ptype, "description": self.param_docs.get(pname, pname)}
            if param.default is inspect.Parameter.empty:
                required.append(pname)
            else:
                prop["default"] = param.default
            properties[pname] = prop
        return {"type": "object", "properties": properties, "required": required}

    def to_openai_tool(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.schema,
            },
        }

    def execute(self, arguments: dict) -> str:
        try:
            result = self.func(**arguments)
        except Exception as e:
            return json.dumps({"error": f"{type(e).__name__}: {e}"}, ensure_ascii=False)
        if not isinstance(result, str):
            result = json.dumps(result, ensure_ascii=False, default=str)
        return result


def skill(func: Callable) -> Callable:
    _REGISTRY[func.__name__] = Skill(func)
    return func


class SkillRegistry:
    @staticmethod
    def get(name: str) -> Skill:
        return _REGISTRY[name]

    @staticmethod
    def all_skills() -> list[Skill]:
        return list(_REGISTRY.values())

    @staticmethod
    def to_openai_tools() -> list[dict]:
        return [s.to_openai_tool() for s in _REGISTRY.values()]

    @staticmethod
    def execute(name: str, arguments: dict) -> str:
        if name not in _REGISTRY:
            return json.dumps({"error": f"未注册的 skill: {name}"}, ensure_ascii=False)
        return _REGISTRY[name].execute(arguments)

    @staticmethod
    def load_module(module_name: str) -> None:
        importlib.import_module(module_name)

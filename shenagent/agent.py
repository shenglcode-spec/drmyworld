from __future__ import annotations

import json

from providers import get_client
from skills import SkillRegistry

MAX_ITERATIONS = 10

SYSTEM_PROMPT = (
    "你是一个能调用工具的智能助手。"
    "遇到精确计算请调用 calculate，需要当前时间或日期请调用 get_current_time，"
    "需要访问网络资源请调用 http_get；不需要工具时直接回答。回答使用中文。"
)


class Agent:
    def __init__(self, provider_name: str):
        self.client, self.cfg = get_client(provider_name)
        self.tools = SkillRegistry.to_openai_tools()
        self.messages: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]

    def switch_provider(self, provider_name: str) -> None:
        self.client, self.cfg = get_client(provider_name)

    def reset(self) -> None:
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    def chat(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})
        for _ in range(MAX_ITERATIONS):
            resp = self.client.chat.completions.create(
                model=self.cfg.model,
                messages=self.messages,
                tools=self.tools or None,
            )
            msg = resp.choices[0].message
            if not msg.tool_calls:
                self.messages.append({"role": "assistant", "content": msg.content or ""})
                return msg.content or ""
            self.messages.append({
                "role": "assistant",
                "content": msg.content or "",
                "tool_calls": [tc.model_dump() for tc in msg.tool_calls],
            })
            for tc in msg.tool_calls:
                args = json.loads(tc.function.arguments or "{}")
                print(f"  [skill] {tc.function.name} <- {args}")
                result = SkillRegistry.execute(tc.function.name, args)
                print(f"  [result] {result[:200]}")
                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result,
                })
        return "已达最大工具调用轮数，任务中止。"

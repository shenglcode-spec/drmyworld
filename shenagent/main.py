from __future__ import annotations

from agent import Agent
from config import DEFAULT_PROVIDER, PROVIDERS
from skills import SkillRegistry
from skills.bootstrap import load_builtin_skills


def print_banner() -> None:
    print("=" * 60)
    print("ShenAgent | 国内大模型 + 自定义 Skills 的命令行 Agent")
    print(f"提供方: {', '.join(PROVIDERS)} | 默认: {DEFAULT_PROVIDER}")
    print("命令: /model <deepseek|doubao|qwen>  /skills  /reset  /quit")
    print("=" * 60)


def handle_command(cmd: str, agent: Agent) -> bool:
    parts = cmd.split(maxsplit=1)
    name = parts[0].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""
    if name in ("/quit", "/exit"):
        print("再见!")
        return False
    if name == "/model":
        if arg not in PROVIDERS:
            print(f"可选提供方: {', '.join(PROVIDERS)}")
        else:
            agent.switch_provider(arg)
            print(f"已切换到 {arg} (模型: {agent.cfg.model})")
        return True
    if name == "/skills":
        for s in SkillRegistry.all_skills():
            first_line = s.description.splitlines()[0] if s.description else ""
            print(f"- {s.name}: {first_line}")
        return True
    if name == "/reset":
        agent.reset()
        print("对话上下文已重置")
        return True
    print("未知命令，可用: /model /skills /reset /quit")
    return True


def main() -> None:
    skills = load_builtin_skills()
    agent = Agent(DEFAULT_PROVIDER)
    print_banner()
    print(f"已加载 {len(skills)} 个 skills: {', '.join(skills)}")
    while True:
        try:
            user_input = input("\n你> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见!")
            break
        if not user_input:
            continue
        if user_input.startswith("/"):
            if not handle_command(user_input, agent):
                break
            continue
        try:
            print(f"\n助手> {agent.chat(user_input)}")
        except Exception as e:
            print(f"[错误] {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

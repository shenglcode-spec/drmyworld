from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class ProviderConfig:
    name: str
    base_url: str
    api_key: str
    model: str


PROVIDERS: dict[str, ProviderConfig] = {
    "deepseek": ProviderConfig(
        name="deepseek",
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        api_key=os.getenv("DEEPSEEK_API_KEY", ""),
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
    ),
    "doubao": ProviderConfig(
        name="doubao",
        base_url=os.getenv("DOUBAO_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"),
        api_key=os.getenv("DOUBAO_API_KEY", ""),
        model=os.getenv("DOUBAO_MODEL", "doubao-seed-1-6-250615"),
    ),
    "qwen": ProviderConfig(
        name="qwen",
        base_url=os.getenv("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"),
        api_key=os.getenv("QWEN_API_KEY", ""),
        model=os.getenv("QWEN_MODEL", "qwen-plus"),
    ),
}

DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "deepseek")


def get_provider_config(name: str) -> ProviderConfig:
    if name not in PROVIDERS:
        raise KeyError(f"未知的模型提供方: {name}，可选: {', '.join(PROVIDERS)}")
    cfg = PROVIDERS[name]
    if not cfg.api_key:
        raise ValueError(f"请在 .env 中配置 {name.upper()}_API_KEY")
    return cfg

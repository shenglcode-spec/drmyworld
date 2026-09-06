from __future__ import annotations

from openai import OpenAI

from config import ProviderConfig, get_provider_config

_clients: dict[tuple[str, str], OpenAI] = {}


def get_client(name: str) -> tuple[OpenAI, ProviderConfig]:
    cfg = get_provider_config(name)
    cache_key = (cfg.base_url, cfg.api_key)
    if cache_key not in _clients:
        _clients[cache_key] = OpenAI(api_key=cfg.api_key, base_url=cfg.base_url)
    return _clients[cache_key], cfg

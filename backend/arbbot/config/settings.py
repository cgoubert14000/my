"""Runtime settings (environment / .env). Secrets never live in the repository.

Two kinds of configuration exist and are deliberately separated:
  * Settings (this file)  — operational knobs the operator sets (RPC URLs, chain, ports, paths).
  * AuthorizationPolicy   — financial limits & allowlists; read-only for the engine (see policy.py).
  * TunableParams         — non-critical strategy parameters the self-correction loop MAY change (see tunables.py).
"""
from __future__ import annotations

import pathlib
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="ARB_", env_file=str(REPO_ROOT / ".env"), extra="ignore")

    # --- chain / data ---
    chain: Literal["local", "base", "arbitrum"] = "local"
    rpc_http_url: str = "http://127.0.0.1:8545"
    rpc_ws_url: str = ""  # optional; falls back to HTTP polling when empty
    rpc_fallback_http_urls: str = ""  # comma separated
    rpc_timeout_s: float = 10.0
    rpc_max_rps: float = 20.0  # client-side rate limit (free tiers are typically 10-25 req/s)
    poll_interval_s: float = 1.0
    data_dir: pathlib.Path = REPO_ROOT / "data"
    db_path: pathlib.Path = REPO_ROOT / "data" / "arbbot.sqlite"
    log_level: str = "INFO"

    # --- API ---
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_cors_origins: str = "*"

    # --- executor contract & simulation ---
    executor_address: str = ""  # deployed FlashArbExecutor; empty => simulation via state override only
    executor_artifact: pathlib.Path = REPO_ROOT / "contracts" / "out" / "FlashArbExecutor.sol" / "FlashArbExecutor.json"
    simulate_with_state_override: bool = True
    # --- universe discovery (mainnet): hub tokens come from the verified chain config; the long tail comes from
    # bundled public token lists and from DEX factory enumeration, then every pool is measured on-chain
    discovery_tokenlists: bool = True  # use data/tokenlists/<chain>.json (documented sources)
    discovery_factory_enum: bool = True  # enumerate Aerodrome / Slipstream factories (allPools) for pools with a hub side
    discovery_factory_enum_max: int = 60_000  # safety cap on enumerated pools per factory
    discovery_min_pool_usd: float = 10_000.0  # pools shallower than this are not watched (re-measured at each start)
    discovery_max_pools: int = 1_500  # deepest pools kept (RPC budget on public endpoints)
    discovery_max_routes: int = 1_500_000
    discovery_max_tokens: int = 1_200  # candidate tokens (lists first, then factory-enumerated) — RPC budget
    discovery_cache_max_age_s: float = 3600.0  # data/universe_<chain>.json written by verify-chain, reused by ghost/serve
    # ghost observations (reliability model inputs) exported/imported across sessions — the CI runner is ephemeral,
    # the maturity decision must not restart from zero at every session. Empty ⇒ docs/reports/real/observations_<chain>.jsonl
    observations_file: str = ""

    # --- authorization / signer (read-only from the engine's perspective) ---
    policy_path: pathlib.Path = REPO_ROOT / "authorization.json"
    tunables_path: pathlib.Path = REPO_ROOT / "data" / "tunables.json"
    signer_url: str = "http://127.0.0.1:8787"
    signer_token: str = ""  # shared secret between engine and signer process (not the private key)

    # --- economics ---
    eur_per_usd: float = 0.92  # used only for display; refreshed manually by the operator
    native_usd_fallback: float = 0.0  # 0 => price derived from pools; set to override for display

    # --- devnet convenience ---
    devnet_deployments: pathlib.Path = REPO_ROOT / "devnet" / "deployments.local.json"

    @property
    def fallback_urls(self) -> list[str]:
        return [u.strip() for u in self.rpc_fallback_http_urls.split(",") if u.strip()]

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip() for o in self.api_cors_origins.split(",") if o.strip()]


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
        _settings.data_dir.mkdir(parents=True, exist_ok=True)
    return _settings


def reset_settings() -> None:
    global _settings
    _settings = None

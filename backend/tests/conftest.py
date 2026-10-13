from __future__ import annotations

import json
import os
import pathlib

import pytest

REPO = pathlib.Path(__file__).resolve().parents[2]
DEVNET = REPO / "devnet" / "deployments.local.json"


def devnet_available() -> bool:
    if not DEVNET.exists():
        return False
    try:
        import urllib.request

        url = json.loads(DEVNET.read_text()).get("rpc", "http://127.0.0.1:8545")
        req = urllib.request.Request(url, data=b'{"jsonrpc":"2.0","id":1,"method":"eth_chainId","params":[]}',
                                     headers={"content-type": "application/json"})
        with urllib.request.urlopen(req, timeout=3) as r:
            return r.status == 200
    except Exception:
        return False


requires_devnet = pytest.mark.skipif(not devnet_available(), reason="local anvil devnet not running")


@pytest.fixture(scope="session")
def devnet_cfg() -> dict:
    return json.loads(DEVNET.read_text())


@pytest.fixture(autouse=True)
def _isolated_env(tmp_path, monkeypatch):
    monkeypatch.setenv("ARB_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("ARB_DB_PATH", str(tmp_path / "data" / "test.sqlite"))
    monkeypatch.setenv("ARB_TUNABLES_PATH", str(tmp_path / "data" / "tunables.json"))
    monkeypatch.setenv("ARB_POLICY_PATH", str(tmp_path / "authorization.json"))
    from arbbot.config.settings import reset_settings

    reset_settings()
    yield
    reset_settings()

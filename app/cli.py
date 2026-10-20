"""Lanceur : ``python main.py`` (voir README pour les options)."""

from __future__ import annotations

import argparse
import socket
import sys
import threading
import webbrowser
from pathlib import Path

from . import __version__
from .state import AppState
from .web import create_app

BANNER = r"""
 __     ___       _            _     ____        _
 \ \   / (_)_ __ | |_ ___  ___| |_  / ___| _ __ (_)_ __   ___ _ __
  \ \ / /| | '_ \| __/ _ \/ __| __| \___ \| '_ \| | '_ \ / _ \ '__|
   \ V / | | | | | ||  __/ (__| |_   ___) | | | | | | | | |  __/ |
    \_/  |_|_| |_|\__\___|\___|\__| |____/|_| |_|_|_| |_|\___|_|
"""


def _free_port(host: str, port: int) -> int:
    """Si le port est occupé, propose le suivant (évite un crash au démarrage)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind((host if host != "0.0.0.0" else "", port))
            return port
        except OSError:
            pass
    for candidate in range(port + 1, port + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host if host != "0.0.0.0" else "", candidate))
                return candidate
            except OSError:
                continue
    return port


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vinted-sniper",
        description="Veille Vinted multi-profils, alertes Discord, dashboard local.",
    )
    parser.add_argument(
        "--host",
        default=None,
        help="Adresse d'écoute (défaut : config.json → 127.0.0.1).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port du dashboard (défaut : config.json → 8000).",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Mode démonstration : annonces fictives, aucun envoi réel.",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="N'ouvre pas automatiquement le navigateur.",
    )
    parser.add_argument(
        "--config", default="config.json", help="Chemin du fichier de config."
    )
    parser.add_argument(
        "--db",
        default=None,
        help="Chemin de la base SQLite (défaut : data/vinted_sniper.db, "
        "ou data/demo.db en mode démo).",
    )
    parser.add_argument(
        "--version", action="version", version=f"Vinted Sniper {__version__}"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config_path = Path(args.config)
    if not config_path.exists() and config_path == Path("config.json"):
        # Premier lancement hors du dépôt : on crée une config par défaut.
        print("ℹ️  config.json absent, création avec les valeurs par défaut.")
    # En démo, on utilise une base séparée pour ne jamais polluer les vraies données.
    db_path = args.db or ("data/demo.db" if args.demo else "data/vinted_sniper.db")
    state = AppState(config_path=config_path, db_path=db_path, demo=args.demo)
    host = args.host or str(state.config.get("app.host", "127.0.0.1"))
    requested_port = int(args.port or state.config.get("app.port", 8000))
    port = _free_port(host, requested_port)
    if port != requested_port:
        print(f"⚠️  Port {requested_port} occupé → utilisation du port {port}.")
    open_browser = (not args.no_browser) and bool(
        state.config.get("app.open_browser", True)
    )
    url_host = "127.0.0.1" if host in {"0.0.0.0", "::"} else host

    app = create_app(state)

    print(BANNER, flush=True)
    print(
        f"  Vinted Sniper v{__version__} — {'MODE DÉMO' if args.demo else 'mode réel'}",
        flush=True,
    )
    print(f"  Dashboard : http://{url_host}:{port}", flush=True)
    print(f"  Base      : {Path(db_path).resolve()}", flush=True)
    print(f"  Config    : {config_path.resolve()}", flush=True)
    print("  Arrêt : Ctrl+C\n", flush=True)

    if open_browser:
        threading.Timer(
            1.2, lambda: webbrowser.open(f"http://{url_host}:{port}")
        ).start()

    import uvicorn

    try:
        uvicorn.run(app, host=host, port=port, log_level="warning", access_log=False)
    except KeyboardInterrupt:
        pass
    print("\n👋 Vinted Sniper arrêté. À bientôt !")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())

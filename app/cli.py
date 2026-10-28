"""Lanceur : ``python main.py`` (voir README pour les options)."""

from __future__ import annotations

import argparse
import asyncio
import os
import socket
import sys
import threading
import webbrowser
from pathlib import Path

from . import __version__
from .brands import parse_brand_reference, popular as popular_brands
from .categories import build_profile_url
from .database import brand_search_key
from .diagnostics import run_diagnostics
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
        help="Chemin de la base SQLite (défaut : data/vinted_sniper.db).",
    )
    parser.add_argument(
        "--check",
        nargs="?",
        const="nike",
        metavar="RECHERCHE",
        help="Diagnostic réel (session, catalogue, fiche article, vendeur) puis sortie, "
        'sans lancer le dashboard. Exemple : python main.py --check "air max 97"',
    )
    parser.add_argument(
        "--brand",
        default="",
        metavar="MARQUE",
        help="Avec --check : teste la recherche filtrée sur une marque "
        '(« nike », « Nike » ou son identifiant Vinted « 53 »).',
    )
    parser.add_argument(
        "--webhook",
        default="",
        help="Webhook Discord à tester avec --check.",
    )
    parser.add_argument(
        "--domain",
        default="www.vinted.fr",
        help="Domaine Vinted pour --check (défaut : www.vinted.fr).",
    )
    parser.add_argument(
        "--turbo",
        action="store_true",
        help="Vitesse maximale : sonde chaque profil en continu à l'intervalle minimal "
        "(1,5 s par défaut). Détection la plus rapide, risque de blocage plus élevé.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=None,
        metavar="SECONDES",
        help="Force l'intervalle minimal du mode temps réel (ex. --interval 2.5).",
    )
    parser.add_argument(
        "--export-brands",
        nargs="?",
        const="marques-vinted",
        metavar="FICHIER",
        help="Exporte TOUTES les marques de l'index local (CSV + JSON) puis sortie. "
        "Exemple : vinted-sniper.exe --export-brands marques-vinted",
    )
    parser.add_argument(
        "--import-brands",
        default="",
        metavar="FICHIER",
        help="Importe un fichier de marques (.csv ou .json) dans la base locale, "
        "puis sortie.",
    )
    parser.add_argument(
        "--version", action="version", version=f"Vinted Sniper {__version__}"
    )
    return parser


def _apply_speed_options(state: AppState, args) -> None:
    """``--turbo`` / ``--interval`` : réglages de vitesse appliqués à la config."""
    patch: dict[str, dict] = {}
    if args.turbo:
        patch["engine"] = {"realtime_turbo": True}
    if args.interval:
        patch.setdefault("engine", {})["realtime_min_interval"] = max(
            0.5, min(60.0, float(args.interval))
        )
    if not patch:
        return
    try:
        state.config.apply_patch(patch)
    except Exception as exc:  # pragma: no cover - config en lecture seule
        print(f"⚠️  Réglage de vitesse ignoré : {exc}")
        return
    label = "TURBO" if args.turbo else f"intervalle mini {args.interval} s"
    print(f"⚡ Mode vitesse : {label} (enregistré dans config.json)")


def _resolve_check_brand(state: AppState, value: str) -> tuple[str, str] | None:
    """Identifiant + nom d'une marque, sans réseau (index local, puis listes connues)."""
    raw = (value or "").strip()
    if not raw:
        return None
    reference = parse_brand_reference(raw)
    if reference:
        known = state.db.get_brand(reference["id"])
        return reference["id"], (known or reference)["name"]
    matches = state.db.search_brands(raw, limit=5)
    if matches:
        return matches[0]["id"], matches[0]["name"]
    needle = brand_search_key(raw)
    for row in popular_brands():
        if brand_search_key(row["name"]) == needle:
            return row["id"], row["name"]
    return None


def _checked_query(state: AppState, args) -> tuple[str, str]:
    """Recherche à tester, enrichie du filtre de marque si ``--brand`` est fourni."""
    query = (args.check or "nike").strip()
    if not args.brand:
        return query, ""
    resolved = _resolve_check_brand(state, args.brand)
    if not resolved:
        print(
            f"⚠️  Marque « {args.brand} » inconnue localement : le test se fait sans "
            "filtre de marque.\n"
            "   Utilisez son identifiant Vinted (ex. --brand 53) ou importez l'index "
            "des marques depuis le dashboard.\n",
            flush=True,
        )
        return query, ""
    brand_id, name = resolved
    url = build_profile_url(query, None, [brand_id], args.domain or "www.vinted.fr")
    return url, f"{name} (#{brand_id})"


#: Durée maximale du diagnostic : au-delà, on explique au lieu de laisser
#: le terminal muet (réseau bloqué, pare-feu, proxy d'entreprise…).
CHECK_TIMEOUT_SECONDS = 90


def _print_step(step: dict) -> None:
    icon = "⏭️" if step.get("skipped") else ("✅" if step["ok"] else "❌")
    print(f"{icon} {step['label']} — {step['detail']}", flush=True)
    if step["key"] == "sample":
        for sample in step["data"].get("items", [])[:3]:
            print(
                f"     • {sample['title'][:60]} · {sample['price']} · "
                f"{sample['brand']} {sample['size']}",
                flush=True,
            )
            print(f"       {sample['url']}", flush=True)


def _print_progress(key: str, label: str, hint: str = "") -> None:
    print(f"⏳ {label} — {hint}", flush=True)


async def _diagnose(state: AppState, args) -> dict:
    try:
        return await asyncio.wait_for(
            run_diagnostics(
                state,
                query=_checked_query(state, args)[0],
                webhook=args.webhook,
                domain=args.domain,
                on_step=_print_step,
                on_progress=_print_progress,
            ),
            timeout=CHECK_TIMEOUT_SECONDS,
        )
    finally:
        await state.client.close()
        await state.notifier.close()
        state.db.close()


def run_check(state: AppState, args) -> int:
    """Affiche un rapport lisible et renvoie un code de sortie exploitable."""
    print(BANNER, flush=True)
    print(f"  Diagnostic Vinted Sniper v{__version__} — mode réel", flush=True)
    query, brand_label = _checked_query(state, args)
    print(f"  Recherche : {args.check} · domaine : {args.domain}", flush=True)
    if brand_label:
        print(f"  Marque    : {brand_label}", flush=True)
        print(f"  URL testée: {query}", flush=True)
    print(
        f"  Chaque ligne s'affiche dès qu'elle est prête (max {CHECK_TIMEOUT_SECONDS} s).\n",
        flush=True,
    )
    try:
        report = asyncio.run(_diagnose(state, args))
    except asyncio.TimeoutError:
        print(
            f"\n⏱️  Diagnostic interrompu après {CHECK_TIMEOUT_SECONDS} s : Vinted ne répond pas "
            "depuis cette machine.\n"
            "   Vérifiez : connexion Internet, pare-feu/antivirus, VPN ou proxy d'entreprise.\n"
            "   Test rapide dans un terminal : curl -I https://www.vinted.fr\n",
            flush=True,
        )
        return 1
    except KeyboardInterrupt:
        print("\n⏹️  Diagnostic annulé.", flush=True)
        return 130

    print("", flush=True)
    print("💡 Conseils :")
    for line in report["advice"]:
        print(f"   - {line}")
    print(f"\nTerminé en {report['duration_ms']} ms.")
    if report["ok"]:
        print(
            "\n✅ Vinted répond et le parseur extrait de vraies annonces : "
            "vous pouvez lancer `python main.py`."
        )
        return 0
    print(
        "\n❌ Le scan réel n'a pas abouti. Corrigez les points ci-dessus, "
        "puis relancez `python main.py --check`."
    )
    return 1


def run_export_brands(state: AppState, destination: str) -> int:
    """Écrit le catalogue complet des marques dans un CSV et un JSON."""
    from .brand_pack import export_rows, write_brand_files

    rows = export_rows(state.db)
    total = state.db.brand_stats().get("total", 0)
    if not rows:
        print(
            "\n❌ Aucune marque en base : lancez d'abord l'import depuis le dashboard\n"
            "   (Modale Marques → bouton ⬇) ou depuis un fichier :\n"
            "   vinted-sniper.exe --import-brands mes-marques.csv\n",
            flush=True,
        )
        state.db.close()
        return 1
    report = write_brand_files(rows, destination)
    print("", flush=True)
    print(f"✅ {report['rows']} marque(s) exportée(s) (index local : {total}).", flush=True)
    print(
        f"   CSV  : {report['csv']}  ({report['csv_bytes'] / 1024:.0f} Ko)",
        flush=True,
    )
    print(
        f"   JSON : {report['json']}  ({report['json_bytes'] / 1024:.0f} Ko)",
        flush=True,
    )
    print(
        "\n   Pour l'embarquer dans le bot : placez le CSV dans app/data/brands.csv\n"
        "   (ou à côté de l'exécutable, sous le nom brands.csv) : il sera chargé\n"
        "   automatiquement au premier démarrage, sans réseau.",
        flush=True,
    )
    state.db.close()
    return 0


def run_import_brands(state: AppState, source: str) -> int:
    """Charge un fichier de marques dans la base (idempotent)."""
    from .brand_pack import read_brand_file

    path = Path(source)
    if not path.is_file():
        print(f"\n❌ Fichier introuvable : {path}\n", flush=True)
        state.db.close()
        return 1
    try:
        rows = read_brand_file(path)
    except (ValueError, OSError) as error:
        print(f"\n❌ Fichier illisible : {error}\n", flush=True)
        state.db.close()
        return 1
    imported = state.db.upsert_brands(rows) if rows else 0
    total = state.db.brand_stats().get("total", 0)
    print("", flush=True)
    print(f"✅ {imported} marque(s) importée(s) depuis {path.name}.", flush=True)
    print(f"   Index local : {total} marque(s).", flush=True)
    if not imported:
        print(
            "   (Fichier vide, ou colonnes attendues : id,slug,name.)",
            flush=True,
        )
    state.db.close()
    return 0 if imported else 1


def _prepare_frozen_runtime() -> None:
    """Exécutable autonome : tout se passe à côté du binaire.

    Sans cela, un double-clic depuis un autre dossier créerait ``data/`` et
    ``config.json`` n'importe où, et la console Windows pourrait planter sur les
    emojis (cp1252).
    """
    if not getattr(sys, "frozen", False):
        return
    try:
        os.chdir(Path(sys.executable).resolve().parent)
    except OSError:
        pass
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
        except (AttributeError, OSError, ValueError):
            pass


def main(argv: list[str] | None = None) -> int:
    _prepare_frozen_runtime()
    args = build_parser().parse_args(argv)
    config_path = Path(args.config)
    if not config_path.exists() and config_path == Path("config.json"):
        # Premier lancement hors du dépôt : on crée une config par défaut.
        print("ℹ️  config.json absent, création avec les valeurs par défaut.")
    db_path = args.db or "data/vinted_sniper.db"
    state = AppState(config_path=config_path, db_path=db_path)
    _apply_speed_options(state, args)
    if args.export_brands:
        return run_export_brands(state, args.export_brands)
    if args.import_brands:
        return run_import_brands(state, args.import_brands)
    if args.check:
        return run_check(state, args)
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
        f"  Vinted Sniper v{__version__} — mode réel",
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

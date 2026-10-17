from __future__ import annotations

import argparse
import getpass
import logging
import shutil
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import set_key

from facebook_bot import __version__
from facebook_bot.config import (
    DEFAULT_API_VERSION,
    DEFAULT_PAGE_ID,
    DEFAULT_PAGE_NAME,
    Config,
    ConfigError,
)
from facebook_bot.facebook import FacebookError, FacebookPublisher
from facebook_bot.images import ImageQueue
from facebook_bot.runner import BotRunner
from facebook_bot.state import StateStore

LOGGER = logging.getLogger(__name__)
STATUS_LABELS = {
    "pending": "prévu",
    "running": "en cours",
    "completed": "publié",
    "simulated": "simulé",
    "empty": "sans image",
    "missed": "manqué",
    "failed": "échec",
    "uncertain": "à vérifier",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="facebook-image-bot",
        description=(
            "Publie les images d'un dossier sur une Page Facebook, à une heure aléatoire "
            "dans chacune de trois plages quotidiennes."
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "--env-file",
        type=Path,
        help="Fichier .env à utiliser (par défaut : .env dans le dossier courant).",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Logs plus détaillés.")

    commands = parser.add_subparsers(dest="command", required=True)

    run_parser = commands.add_parser("run", help="Lancer le bot en continu.")
    run_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simuler les créneaux sans contacter Facebook ni déplacer les images.",
    )

    post_parser = commands.add_parser(
        "post-now", help="Publier immédiatement la prochaine image de la file."
    )
    post_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Afficher ce qui serait publié, sans contacter Facebook.",
    )

    schedule_parser = commands.add_parser(
        "schedule", help="Créer puis afficher les heures aléatoires du planning."
    )
    schedule_parser.add_argument(
        "--days", type=int, default=2, help="Nombre de jours à afficher (1 à 31, défaut : 2)."
    )

    setup_parser = commands.add_parser(
        "setup",
        help="Enregistrer un nouveau jeton de façon masquée puis vérifier la Page.",
    )
    setup_parser.add_argument(
        "--clipboard",
        action="store_true",
        help="Lire le jeton depuis le presse-papiers Windows, puis vider celui-ci.",
    )
    commands.add_parser("doctor", help="Vérifier les dossiers, le jeton et la Page Facebook.")
    commands.add_parser("queue", help="Compter les images encore à publier.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _configure_logging(args.verbose)

    require_facebook = args.command == "doctor" or (
        args.command in {"run", "post-now"} and not args.dry_run
    )
    try:
        if args.command == "setup":
            env_path = args.env_file or Path.cwd() / ".env"
            return _setup(env_path, from_clipboard=args.clipboard)

        config = Config.from_env(args.env_file, require_facebook=require_facebook)
        if args.command == "run":
            BotRunner(config, dry_run=args.dry_run).run_forever()
            return 0
        if args.command == "post-now":
            result = BotRunner(config, dry_run=args.dry_run).post_now()
            return 0 if result is not None else 2
        if args.command == "schedule":
            return _show_schedule(config, args.days)
        if args.command == "doctor":
            return _doctor(config)
        if args.command == "queue":
            return _show_queue(config)
    except ConfigError as exc:
        LOGGER.error("Configuration invalide : %s", exc)
    except FacebookError as exc:
        LOGGER.error("Erreur Facebook : %s", exc)
    except sqlite3.Error as exc:
        LOGGER.error("Erreur de base de données locale : %s", exc)
    except OSError as exc:
        LOGGER.error("Erreur de fichier : %s", exc)
    return 1


def _setup(env_path: Path, *, from_clipboard: bool = False) -> int:
    """Vérifie puis enregistre un jeton sans jamais l'afficher dans le terminal."""
    env_path = env_path.expanduser().resolve()
    if env_path.name == ".env.example":
        raise ConfigError("Le jeton ne doit jamais être enregistré dans .env.example.")

    print("Configuration sécurisée de la Page Madame Portugais")
    if from_clipboard:
        print("Lecture du nouveau jeton depuis le presse-papiers…")
        token = _read_clipboard_token()
        _clear_clipboard()
        print("✓ Presse-papiers vidé par sécurité.")
    else:
        print("Le jeton saisi sera masqué et ne sera jamais affiché dans les logs.")
        try:
            prompt = "Collez le NOUVEAU jeton de Page puis appuyez sur Entrée : "
            token = getpass.getpass(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nConfiguration annulée.")
            return 1

    if len(token) < 40 or any(character.isspace() for character in token):
        raise ConfigError("Le jeton saisi paraît incomplet ou contient un espace.")

    print("Vérification auprès de Facebook…")
    publisher = FacebookPublisher(
        page_id=DEFAULT_PAGE_ID,
        access_token=token,
        api_version=DEFAULT_API_VERSION,
    )
    page = publisher.verify_destination(DEFAULT_PAGE_NAME)

    if not env_path.exists():
        template = Path.cwd() / ".env.example"
        if template.is_file():
            env_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(template, env_path)
        else:
            env_path.parent.mkdir(parents=True, exist_ok=True)
            env_path.touch()

    set_key(str(env_path), "FACEBOOK_EXPECTED_PAGE_NAME", DEFAULT_PAGE_NAME, quote_mode="always")
    set_key(str(env_path), "FACEBOOK_PAGE_ID", DEFAULT_PAGE_ID, quote_mode="never")
    set_key(str(env_path), "FACEBOOK_PAGE_ACCESS_TOKEN", token, quote_mode="always")
    set_key(str(env_path), "FACEBOOK_API_VERSION", DEFAULT_API_VERSION, quote_mode="never")
    try:
        env_path.chmod(0o600)
    except OSError:
        # Les ACL Windows ne suivent pas toujours les bits POSIX ; le fichier reste ignoré par Git.
        pass

    print(f"✓ Jeton vérifié pour {page.name} (ID {page.id}).")
    print(f"✓ Configuration enregistrée localement dans {env_path}")
    print("Vous pouvez maintenant lancer : python -m facebook_bot doctor")
    return 0


def _read_clipboard_token() -> str:
    if sys.platform != "win32":
        raise ConfigError("La lecture automatique du presse-papiers est réservée à Windows.")
    powershell = shutil.which("powershell.exe") or shutil.which("powershell")
    if powershell is None:
        raise ConfigError("PowerShell est introuvable ; impossible de lire le presse-papiers.")
    try:
        result = subprocess.run(
            [powershell, "-NoProfile", "-NonInteractive", "-Command", "Get-Clipboard -Raw"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ConfigError("Impossible de lire le presse-papiers Windows.") from exc
    if result.returncode != 0:
        raise ConfigError("Impossible de lire le presse-papiers Windows.")
    token = result.stdout.strip()
    if not token:
        raise ConfigError(
            "Le presse-papiers est vide. Cliquez d'abord sur l'icône Copier de Meta."
        )
    return token


def _clear_clipboard() -> None:
    if sys.platform != "win32":
        return
    powershell = shutil.which("powershell.exe") or shutil.which("powershell")
    if powershell is None:
        return
    try:
        subprocess.run(
            [powershell, "-NoProfile", "-NonInteractive", "-Command", "Set-Clipboard -Value ''"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        pass


def _show_schedule(config: Config, days: int) -> int:
    if not 1 <= days <= 31:
        raise ConfigError("--days doit être compris entre 1 et 31.")
    config.prepare_directories()
    state = StateStore(config.state_db)
    state.initialize()
    now = datetime.now(config.timezone)

    print(f"Planning ({config.timezone_name})")
    for offset in range(days):
        day = now.date() + timedelta(days=offset)
        slots = state.ensure_day(
            day,
            config.posting_windows,
            config.timezone,
            now=now,
        )
        print(f"\n{day.strftime('%d/%m/%Y')} :")
        for slot in slots:
            status = STATUS_LABELS.get(slot.status, slot.status)
            print(
                f"  {slot.index}. {slot.scheduled_at:%H:%S} "
                f"(plage {slot.window_start:%H:%M}-{slot.window_end:%H:%M}) — {status}"
            )
    return 0


def _show_queue(config: Config) -> int:
    config.prepare_directories()
    state = StateStore(config.state_db)
    state.initialize()
    queue = ImageQueue(
        image_dir=config.image_dir,
        archive_dir=config.archive_dir,
        queue_order=config.queue_order,
        default_caption=config.default_caption,
    )
    count = queue.count_available(state.was_posted)
    print(f"{count} nouvelle(s) image(s) dans {config.image_dir}")
    return 0


def _doctor(config: Config) -> int:
    print("Diagnostic du bot Facebook\n")
    config.prepare_directories()
    state = StateStore(config.state_db)
    state.initialize()
    print(f"✓ Dossier d'entrée : {config.image_dir}")
    print(f"✓ Dossier d'archive : {config.archive_dir}")
    print(f"✓ Base locale : {config.state_db}")
    print(f"✓ Fuseau : {config.timezone_name}")
    print(f"✓ Plages : {', '.join(str(window) for window in config.posting_windows)}")

    publisher = FacebookPublisher(
        page_id=config.page_id,
        access_token=config.page_access_token,
        api_version=config.api_version,
        timeout_seconds=config.http_timeout_seconds,
    )
    print(f"… Vérification de la Page via l'API Graph {config.api_version}")
    page = publisher.verify_destination(config.expected_page_name)
    print(f"✓ Destination verrouillée : {page.name} (ID {page.id})")
    print("\nLe bot est prêt. Ce test n'a rien publié.")
    return 0


def _configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    if not verbose:
        logging.getLogger("urllib3").setLevel(logging.WARNING)


if __name__ == "__main__":
    sys.exit(main())

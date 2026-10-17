from __future__ import annotations

import argparse
import csv
import getpass
import logging
import shutil
import sqlite3
import subprocess
import sys
from datetime import date, datetime, timedelta
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
from facebook_bot.planner import (
    SCHEDULE_MINUTES,
    SCHEDULE_START_HOUR,
    PlannedPost,
    build_plan,
)
from facebook_bot.runner import BotRunner
from facebook_bot.state import StateError, StateStore

LOGGER = logging.getLogger(__name__)
TOKEN_FILE_TEMPLATE = """COLLEZ_VOTRE_NOUVEAU_JETON_ICI

Après avoir collé le jeton, enregistrez et fermez ce document.
CONFIGURER.bat le vérifiera, le transférera dans .env puis effacera cette valeur.
"""

STATUS_LABELS = {
    "pending": "prévu",
    "running": "en cours",
    "completed": "publié",
    "simulated": "simulé",
    "empty": "sans image",
    "missed": "manqué",
    "failed": "échec",
    "skipped": "ignoré",
    "uncertain": "à vérifier",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="facebook-image-bot",
        description=(
            "Planifie les images d'un dossier sur trois horaires entrelacés et les publie "
            "sur la Page Facebook Madame Portugais."
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

    commands.add_parser("run", help="Lancer le bot en continu.")

    post_parser = commands.add_parser(
        "post-now", help="Publier immédiatement la prochaine image de la file."
    )
    post_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Afficher ce qui serait publié, sans contacter Facebook.",
    )

    plan_parser = commands.add_parser(
        "plan",
        help="Demander une date, compter les images et proposer les horaires.",
    )
    plan_parser.add_argument(
        "--date",
        help="Date au format JJ/MM/AAAA (sinon elle est demandée).",
    )
    plan_parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Enregistrer le planning sans demander de confirmation.",
    )

    schedule_parser = commands.add_parser(
        "schedule", help="Afficher les publications déjà planifiées."
    )
    schedule_parser.add_argument(
        "--days", type=int, default=7, help="Nombre de jours à afficher (1 à 31, défaut : 7)."
    )

    setup_parser = commands.add_parser(
        "setup",
        help="Enregistrer un nouveau jeton de façon masquée puis vérifier la Page.",
    )
    setup_source = setup_parser.add_mutually_exclusive_group()
    setup_source.add_argument(
        "--clipboard",
        action="store_true",
        help="Lire le jeton depuis le presse-papiers Windows, puis vider celui-ci.",
    )
    setup_source.add_argument(
        "--token-file",
        type=Path,
        help="Lire le jeton depuis un fichier texte local, puis effacer sa valeur.",
    )
    commands.add_parser("doctor", help="Vérifier les dossiers, le jeton et la Page Facebook.")
    commands.add_parser("queue", help="Compter les images encore à publier.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _configure_logging(args.verbose)

    require_facebook = args.command in {"doctor", "run"} or (
        args.command == "post-now" and not args.dry_run
    )
    try:
        if args.command == "setup":
            env_path = args.env_file or Path.cwd() / ".env"
            return _setup(
                env_path,
                from_clipboard=args.clipboard,
                token_file=args.token_file,
            )

        config = Config.from_env(args.env_file, require_facebook=require_facebook)
        if args.command == "run":
            BotRunner(config).run_forever()
            return 0
        if args.command == "post-now":
            result = BotRunner(config, dry_run=args.dry_run).post_now()
            return 0 if result is not None else 2
        if args.command == "plan":
            return _plan_publications(config, args.date, assume_yes=args.yes)
        if args.command == "schedule":
            return _show_schedule(config, args.days)
        if args.command == "doctor":
            return _doctor(config)
        if args.command == "queue":
            return _show_queue(config)
    except ConfigError as exc:
        LOGGER.error("Configuration invalide : %s", exc)
    except StateError as exc:
        LOGGER.error("Planning impossible : %s", exc)
    except FacebookError as exc:
        LOGGER.error("Erreur Facebook : %s", exc)
    except sqlite3.Error as exc:
        LOGGER.error("Erreur de base de données locale : %s", exc)
    except OSError as exc:
        LOGGER.error("Erreur de fichier : %s", exc)
    return 1


def _setup(
    env_path: Path,
    *,
    from_clipboard: bool = False,
    token_file: Path | None = None,
) -> int:
    """Vérifie puis enregistre un jeton sans jamais l'afficher dans le terminal."""
    env_path = env_path.expanduser().resolve()
    if env_path.name == ".env.example":
        raise ConfigError("Le jeton ne doit jamais être enregistré dans .env.example.")

    print("Configuration sécurisée de la Page Madame Portugais")
    if token_file is not None:
        token_path = token_file.expanduser().resolve()
        print(f"Lecture du nouveau jeton depuis {token_path.name}…")
        token = _read_token_file(token_path)
        _reset_token_file(token_path)
        print("✓ Jeton retiré du document texte après lecture.")
    elif from_clipboard:
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


def _read_token_file(path: Path) -> str:
    if not path.is_file():
        raise ConfigError(f"Document de jeton introuvable : {path}")
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as exc:
        raise ConfigError(f"Impossible de lire le document {path.name}.") from exc

    for raw_line in lines:
        candidate = raw_line.strip()
        if candidate.startswith("FACEBOOK_PAGE_ACCESS_TOKEN="):
            candidate = candidate.split("=", 1)[1].strip().strip("'\"")
        if (
            len(candidate) >= 40
            and not any(character.isspace() for character in candidate)
            and candidate != "COLLEZ_VOTRE_NOUVEAU_JETON_ICI"
        ):
            return candidate
    raise ConfigError(
        f"Aucun jeton valide trouvé dans {path.name}. Remplacez la première ligne."
    )


def _reset_token_file(path: Path) -> None:
    try:
        path.write_text(TOKEN_FILE_TEMPLATE, encoding="utf-8")
    except OSError as exc:
        raise ConfigError(
            "Le jeton a été lu, mais le document texte n'a pas pu être nettoyé."
        ) from exc


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


def _plan_publications(
    config: Config,
    date_text: str | None,
    *,
    assume_yes: bool = False,
) -> int:
    config.prepare_directories()
    state = StateStore(config.state_db)
    state.initialize()
    day = _get_plan_date(date_text)
    now = datetime.now(config.timezone)
    first_publication = datetime(
        day.year,
        day.month,
        day.day,
        SCHEDULE_START_HOUR,
        min(SCHEDULE_MINUTES),
        tzinfo=config.timezone,
    )
    if day < now.date():
        raise ConfigError("La date de publication ne peut pas être dans le passé.")
    if first_publication <= now + timedelta(minutes=2):
        raise ConfigError(
            "Pour conserver les 3 horaires complets, choisissez une date future "
            "(généralement demain ou plus tard)."
        )
    if state.scheduled_for_day(day):
        raise StateError(
            f"Un planning existe déjà pour le {day.strftime('%d/%m/%Y')}."
        )

    queue = _make_image_queue(config)
    items = queue.available_items(state.is_unavailable)
    if not items:
        raise StateError(f"Aucune nouvelle image trouvée dans {config.image_dir}.")

    capacity = config.max_posts_per_schedule * 3
    selected_items = items[:capacity]
    plan = build_plan(
        day=day,
        items=selected_items,
        timezone=config.timezone,
        max_per_schedule=config.max_posts_per_schedule,
    )

    print(f"\nDate choisie : {day.strftime('%d/%m/%Y')}")
    print(f"Images détectées et disponibles : {len(items)}")
    print(f"Images placées sur cette date : {len(plan)} (maximum {capacity})")
    if len(items) > capacity:
        print(
            f"Il restera {len(items) - capacity} image(s) à planifier sur une autre date."
        )
    print(f"Hashtags automatiques : {config.fixed_hashtags}")
    print("Répartition automatique égale ; aucune publication à la même minute.\n")

    for schedule_index, minute in enumerate(SCHEDULE_MINUTES, start=1):
        entries = [entry for entry in plan if entry.window_index == schedule_index]
        example = f"07:{minute:02d}, 08:{minute:02d}, 09:{minute:02d}…"
        print(
            f"Horaire {schedule_index} ({example}) — {len(entries)} publication(s)"
        )
        for entry in entries:
            print(f"  {entry.scheduled_at:%H:%M}  {entry.item.path.name}")
        print()

    if len(plan) > 30:
        print(
            "Attention : un grand nombre de publications peut fatiguer votre audience. "
            "Vérifiez le planning avant de confirmer.\n"
        )

    if not assume_yes:
        try:
            answer = input("Enregistrer ce planning ? [o/N] : ").strip().casefold()
        except (EOFError, KeyboardInterrupt):
            print("\nPlanification annulée.")
            return 1
        if answer not in {"o", "oui", "y", "yes"}:
            print("Planification annulée ; aucune donnée n'a été enregistrée.")
            return 0

    state.create_plan(day, plan)
    csv_path = _write_plan_csv(config, day, plan)
    print(f"\n✓ {len(plan)} publication(s) planifiée(s) pour le {day:%d/%m/%Y}.")
    print(f"✓ Copie lisible du planning : {csv_path}")
    print("Laissez maintenant LANCER_BOT.bat ouvert aux heures prévues.")
    return 0


def _get_plan_date(value: str | None) -> date:
    raw_value = value
    while raw_value is None:
        try:
            raw_value = input("Date de publication (JJ/MM/AAAA) : ").strip()
        except (EOFError, KeyboardInterrupt) as exc:
            raise ConfigError("Saisie de la date annulée.") from exc
        if not raw_value:
            print("Veuillez saisir une date, par exemple 20/10/2026.")
            raw_value = None

    for date_format in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(raw_value, date_format).date()
        except ValueError:
            continue
    raise ConfigError("Date invalide. Utilisez le format JJ/MM/AAAA.")


def _write_plan_csv(config: Config, day: date, plan: list[PlannedPost]) -> Path:
    path = config.state_db.parent / f"planning-{day.isoformat()}.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["date", "heure", "horaire", "image", "légende"])
        for entry in plan:
            writer.writerow(
                [
                    day.strftime("%d/%m/%Y"),
                    entry.scheduled_at.strftime("%H:%M"),
                    entry.window_index,
                    entry.item.path.name,
                    entry.item.caption,
                ]
            )
    return path


def _make_image_queue(config: Config) -> ImageQueue:
    return ImageQueue(
        image_dir=config.image_dir,
        archive_dir=config.archive_dir,
        queue_order=config.queue_order,
        default_caption=config.default_caption,
        fixed_hashtags=config.fixed_hashtags,
    )


def _show_schedule(config: Config, days: int) -> int:
    if not 1 <= days <= 31:
        raise ConfigError("--days doit être compris entre 1 et 31.")
    config.prepare_directories()
    state = StateStore(config.state_db)
    state.initialize()
    now = datetime.now(config.timezone)

    print(f"Planning enregistré ({config.timezone_name})")
    total = 0
    for offset in range(days):
        day = now.date() + timedelta(days=offset)
        publications = state.scheduled_for_day(day)
        if not publications:
            continue
        print(f"\n{day.strftime('%d/%m/%Y')} :")
        for publication in publications:
            status = STATUS_LABELS.get(publication.status, publication.status)
            print(
                f"  {publication.scheduled_at:%H:%M} — horaire {publication.window_index} — "
                f"{publication.item.path.name} — {status}"
            )
        total += len(publications)
    if total == 0:
        print("Aucune publication planifiée. Lancez PLANIFIER.bat.")
    else:
        print(f"\nTotal affiché : {total} publication(s).")
    return 0


def _show_queue(config: Config) -> int:
    config.prepare_directories()
    state = StateStore(config.state_db)
    state.initialize()
    queue = _make_image_queue(config)
    count = queue.count_available(state.is_unavailable)
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
    print("✓ Horaire 1 : 07:30, 08:30, 09:30…")
    print("✓ Horaire 2 : 07:15, 08:15, 09:15…")
    print("✓ Horaire 3 : 07:45, 08:45, 09:45…")
    print(f"✓ Maximum par horaire : {config.max_posts_per_schedule}")
    print(f"✓ Hashtags automatiques : {config.fixed_hashtags}")

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

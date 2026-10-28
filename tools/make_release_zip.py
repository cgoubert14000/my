"""Assemble le zip de distribution (exe Windows + sources + lanceurs).

Usage :
    python tools/make_release_zip.py

Le binaire Windows n'est pas versionné (19 Mo) : il est récupéré depuis le
dernier commit de la branche qui le contenait, ou depuis ``dist/`` s'il vient
d'être construit localement. Le zip est écrit à la racine du dépôt.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from app import __version__  # noqa: E402

FOLDER = f"VintedSniper-{__version__}"
EXE_NAME = "vinted-sniper.exe"
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules", "data",
             "dist", "build", ".ruff_cache", "_delivery"}
#: ``app/data`` est livré exprès : il contient l'index des marques.
KEEP_DIRS = {("app", "data")}
SKIP_SUFFIX = {".pyc", ".db", ".db-wal", ".db-shm", ".log"}


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()


def find_exe(tmp: Path) -> Path:
    """Binaire Windows : dist/ local d'abord, puis historique Git."""
    local = ROOT / "dist" / EXE_NAME
    if local.exists():
        return local
    try:
        commits = _git("log", "--all", "--format=%H", "--", f"_delivery/{EXE_NAME}")
    except subprocess.CalledProcessError:
        commits = ""
    for sha in [line for line in commits.splitlines() if line]:
        target = tmp / EXE_NAME
        with target.open("wb") as handle:
            result = subprocess.run(
                ["git", "show", f"{sha}:_delivery/{EXE_NAME}"],
                cwd=ROOT,
                stdout=handle,
                stderr=subprocess.DEVNULL,
            )
        if result.returncode == 0 and target.stat().st_size > 1_000_000:
            return target
    raise SystemExit(
        "Binaire Windows introuvable.\n"
        "Construisez-le (tools/build_executable.py sous Windows) ou lancez le "
        "workflow GitHub « Build executables »."
    )


def file_list() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        try:
            parts = path.relative_to(ROOT).parts
        except ValueError:  # pragma: no cover - hors dépôt
            continue
        # « data » est ignoré partout… sauf dans app/data (pack de marques).
        keep = any(parts[: len(prefix)] == prefix for prefix in KEEP_DIRS)
        if not keep and any(part in SKIP_DIRS for part in parts):
            continue
        if path.is_file() and path.suffix not in SKIP_SUFFIX:
            if path.name in {f"{FOLDER}.zip", "LISEZ-MOI.txt"}:
                continue  # LISEZ-MOI est ajouté en premier, exprès
            if path.suffix == ".zip":
                continue  # jamais d'archive de version dans l'archive (36 Mo pour rien)
            files.append(path)
    return files


def main() -> int:
    target = ROOT / f"{FOLDER}.zip"
    with tempfile.TemporaryDirectory() as raw_tmp:
        tmp = Path(raw_tmp)
        exe = find_exe(tmp)
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            archive.write(exe, f"{FOLDER}/{EXE_NAME}")
            for path in file_list():
                arcname = f"{FOLDER}/{path.relative_to(ROOT).as_posix()}"
                archive.write(path, arcname)
            # LISEZ-MOI en tête de liste pour être vu en premier.
            readme = ROOT / "LISEZ-MOI.txt"
            if readme.exists():
                archive.write(readme, f"{FOLDER}/LISEZ-MOI.txt")
    size = target.stat().st_size / (1024 * 1024)
    print(f"[OK] {target}  ({size:.1f} Mo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

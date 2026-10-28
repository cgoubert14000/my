#!/usr/bin/env python3
"""Construit un exécutable autonome (Windows, Linux ou macOS).

Usage :
    python tools/build_executable.py

Résultat :
    dist/vinted-sniper        (Linux / macOS)
    dist/vinted-sniper.exe    (Windows)

Le binaire embarque Python, FastAPI, uvicorn, curl_cffi et tout le dashboard :
aucune installation n'est nécessaire sur la machine cible. Il suffit de le
poser dans un dossier et de le lancer ; il crée à côté de lui ``config.json``
et ``data/``.

Prérequis de *build* uniquement : ``pip install pyinstaller`` (le script le
propose s'il manque). Côté utilisateur final, rien à installer.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

# La console Windows est en cp1252 : sans cela, les emojis font planter le build.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
    except (AttributeError, OSError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
NAME = "vinted-sniper" if sys.platform != "win32" else "vinted-sniper"

SEP = ";" if sys.platform == "win32" else ":"

# Modules chargés dynamiquement par uvicorn et les parseurs optionnels.
HIDDEN_IMPORTS = [
    "uvicorn.logging",
    "uvicorn.loops.auto",
    "uvicorn.loops.asyncio",
    "uvicorn.protocols.http.auto",
    "uvicorn.protocols.http.h11_impl",
    "uvicorn.protocols.websockets.auto",
    "uvicorn.lifespan.on",
    "uvicorn.lifespan.off",
    "app.cli",
    "app.web",
    "app.api",
    "app.browser_session",
    "app.brand_pack",
]


def _has(module: str) -> bool:
    try:
        __import__(module)
    except Exception:
        return False
    return True


def main() -> int:
    if not _has("PyInstaller"):
        print("PyInstaller est requis pour construire l'exécutable.")
        print(f"Interpréteur utilisé : {sys.executable}")
        print("Installez-le avec :  pip install pyinstaller")
        return 2

    args = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--name",
        NAME,
        "--add-data",
        f"{ROOT / 'app' / 'static'}{SEP}app/static",
        "--add-data",
        f"{ROOT / 'app' / 'data'}{SEP}app/data",
        "--collect-all",
        "curl_cffi",
        "--distpath",
        str(ROOT / "dist"),
        "--workpath",
        str(ROOT / "build" / "pyinstaller"),
        "--specpath",
        str(ROOT / "build"),
    ]
    if _has("lxml"):
        args += ["--collect-all", "lxml"]
    for module in HIDDEN_IMPORTS:
        args += ["--hidden-import", module]
    if sys.platform == "win32":
        args += ["--console"]
    args.append(str(ROOT / "main.py"))

    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "dist").mkdir(exist_ok=True)

    import PyInstaller

    print(f"Python {sys.version.split()[0]} · PyInstaller {PyInstaller.__version__}")
    print("Construction de l'exécutable... (1 a 3 minutes)", flush=True)
    result = subprocess.run(args, cwd=ROOT)
    if result.returncode != 0:
        print("Échec de la construction.")
        return result.returncode

    binary = ROOT / "dist" / (NAME + (".exe" if sys.platform == "win32" else ""))
    if not binary.exists():
        print(f"Binaire introuvable : {binary}")
        return 1

    size_mb = binary.stat().st_size / (1024 * 1024)
    print(f"\n[OK] Exécutable prêt : {binary}  ({size_mb:.1f} Mo)")
    print("     Double-cliquez dessus (ou lancez-le dans un terminal) :")
    print("     le dashboard s'ouvre sur http://127.0.0.1:8000")
    return 0


if __name__ == "__main__":
    if "--help" in sys.argv:
        print(__doc__)
        raise SystemExit(0)
    raise SystemExit(main())


# Utilisé par les tests : le dossier doit rester propre après un build.
def clean_build_artifacts() -> None:
    for path in (ROOT / "build" / "pyinstaller", ROOT / "dist"):
        shutil.rmtree(path, ignore_errors=True)

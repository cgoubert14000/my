#!/usr/bin/env python3
"""Lance la suite de tests avec un garde-fou anti-blocage.

Un test qui attend un événement jamais publié (flux SSE, tâche asyncio,
attente réseau simulée) ne doit pas bloquer la CI pendant quinze minutes :
après ``TESTS_STALL_TIMEOUT`` secondes (240 par défaut), la pile de **tous**
les threads est écrite sur la sortie d'erreur, puis le processus s'arrête en
erreur. On sait immédiatement quel test était en cause.

Usage :
    python tools/run_tests.py            # suite complète
    TESTS_STALL_TIMEOUT=60 python tools/run_tests.py
    python tools/run_tests.py tests.test_realtime   # un module
"""

from __future__ import annotations

import faulthandler
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main(argv: list[str]) -> int:
    try:
        stall = int(os.environ.get("TESTS_STALL_TIMEOUT", "240"))
    except ValueError:
        stall = 240
    # Trace des piles si la suite se fige, puis code de sortie non nul.
    faulthandler.enable()
    faulthandler.dump_traceback_later(stall, exit=True)

    loader = unittest.TestLoader()
    if argv:
        suite = loader.loadTestsFromNames(argv)
    else:
        tests_dir = ROOT / "tests"
        # ``tests/`` n'est pas un paquet : on découvre depuis ce dossier et on
        # garde la racine du projet dans ``sys.path`` pour ``import app``.
        suite = loader.discover(
            str(tests_dir), pattern="test_*.py", top_level_dir=str(tests_dir)
        )

    result = unittest.TextTestRunner(verbosity=2, buffer=False).run(suite)
    faulthandler.cancel_dump_traceback_later()
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

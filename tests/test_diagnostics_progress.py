"""Diagnostic : progression en direct et garde-fou de durée.

Le terminal ne doit jamais rester muet : chaque étape est signalée avant et
après, et un blocage réseau se termine par un message explicite.
"""

from __future__ import annotations

import asyncio
import json
import tempfile
import unittest
from pathlib import Path

from app.cli import CHECK_TIMEOUT_SECONDS, _print_step
from app.diagnostics import run_diagnostics
from app.state import AppState
from tests.fake_vinted import FakeVintedAPI


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(
            json.dumps({"engine": {"start_paused": True}}), encoding="utf-8"
        )
        self.state = AppState(
            config_path=config_path, db_path=root / "test.db", api_class=FakeVintedAPI
        )
        self.state.notifier.dry_run = True

    def tearDown(self):
        self.state.db.close()
        self.tmp.cleanup()

    def test_steps_are_emitted_as_they_finish(self):
        seen: list[dict] = []
        started: list[tuple[str, str]] = []

        report = asyncio.run(
            run_diagnostics(
                self.state,
                query="nike",
                on_step=seen.append,
                on_progress=lambda key, label, hint="": started.append((key, label)),
            )
        )

        self.assertTrue(seen, "au moins une étape doit être remontée")
        self.assertEqual([step["key"] for step in seen], [step["key"] for step in report["steps"]])
        keys = [key for key, _ in started]
        self.assertIn("session", keys)
        self.assertIn("catalog", keys)
        # La première étape est locale : elle arrive avant toute requête réseau.
        self.assertEqual(seen[0]["key"], "setup")
        self.assertEqual(keys[0], "session")

    def test_callbacks_are_optional(self):
        report = asyncio.run(run_diagnostics(self.state, query="nike"))
        self.assertIn("steps", report)
        self.assertTrue(report["steps"])

    def test_broken_callback_does_not_break_diagnostic(self):
        def boom(*_args, **_kwargs):
            raise RuntimeError("affichage cassé")

        report = asyncio.run(
            run_diagnostics(
                self.state, query="nike", on_step=boom, on_progress=boom
            )
        )
        self.assertTrue(report["steps"])

    def test_print_step_handles_sample_and_errors(self):
        import io
        from contextlib import redirect_stdout

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            _print_step(
                {
                    "key": "sample",
                    "label": "Échantillon",
                    "ok": True,
                    "skipped": False,
                    "detail": "1 annonce",
                    "data": {
                        "items": [
                            {
                                "title": "Nike Air Max",
                                "price": "89 €",
                                "brand": "Nike",
                                "size": "42",
                                "url": "https://www.vinted.fr/items/1",
                            }
                        ]
                    },
                }
            )
            _print_step(
                {
                    "key": "catalog",
                    "label": "Catalogue",
                    "ok": False,
                    "skipped": False,
                    "detail": "bloqué",
                    "data": {},
                }
            )
        text = buffer.getvalue()
        self.assertIn("✅ Échantillon", text)
        self.assertIn("Nike Air Max", text)
        self.assertIn("https://www.vinted.fr/items/1", text)
        self.assertIn("❌ Catalogue", text)


class TimeoutTests(unittest.TestCase):
    def test_timeout_is_bounded(self):
        # Un blocage réseau ne doit jamais laisser le terminal muet indéfiniment.
        self.assertLessEqual(CHECK_TIMEOUT_SECONDS, 120)
        self.assertGreaterEqual(CHECK_TIMEOUT_SECONDS, 30)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

"""Anti-bruit : recherche de marques compacte et journal non répétitif."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import Database  # noqa: E402
from app.notify import DiscordNotifier  # noqa: E402


def _db_with(tmp: Path, rows: list[tuple[str, str]]) -> Database:
    db = Database(tmp / "brands.db")
    db.upsert_brands(
        [{"id": i, "slug": name.lower().replace(" ", "-"), "name": name} for i, name in rows]
    )
    return db


class BrandCompactSearchTests(unittest.TestCase):
    """« cp » doit trouver « C.P. Company » (ponctuation transformée en espaces)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.db = _db_with(Path(self._tmp.name), 
            [
                ("101", "C.P. Company"),
                ("102", "CP Company"),
                ("103", "Nike"),
                ("104", "Nike SB"),
                ("105", "H&M"),
                ("106", "Le Coq Sportif"),
                ("107", "Capacité"),
            ]
        )

    def tearDown(self):
        self.db.close()

    def names(self, query: str) -> list[str]:
        return [row["name"] for row in self.db.search_brands(query, limit=20, prefix=True)]

    def test_cp_finds_punctuated_brand(self):
        self.assertEqual(sorted(self.names("cp")), ["C.P. Company", "CP Company"])

    def test_exact_prefix_ranked_first(self):
        self.assertEqual(self.names("cp")[0], "CP Company")

    def test_multi_word_query(self):
        self.assertEqual(sorted(self.names("cp comp")), ["C.P. Company", "CP Company"])

    def test_ampersand(self):
        self.assertEqual(self.names("hm"), ["H&M"])
        self.assertEqual(self.names("h&m"), ["H&M"])

    def test_word_prefix(self):
        self.assertEqual(self.names("coq"), ["Le Coq Sportif"])

    def test_count_matches_search(self):
        self.assertEqual(self.db.count_brands("cp"), 2)

    def test_plain_prefix_still_works(self):
        self.assertEqual(self.names("nike"), ["Nike", "Nike SB"])

    def test_unknown_brand_returns_empty(self):
        self.assertEqual(self.names("zzzz"), [])


class NotifyLogThrottleTests(unittest.IsolatedAsyncioTestCase):
    """Sans webhook, 70 échecs identiques ne doivent pas écrire 70 lignes."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        from app.config import ConfigStore

        (root / "config.json").write_text("{}", encoding="utf-8")
        self.db = Database(root / "log.db")
        self.notifier = DiscordNotifier(ConfigStore(root / "config.json"), self.db)

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    async def test_repeated_error_logged_once(self):
        profile = {"id": 1, "name": "cp compagny"}
        item = {"id": "1", "title": "Veste", "price": 10}
        for _ in range(10):
            ok, error = await self.notifier.notify(profile, item)
            self.assertFalse(ok)
            self.assertIn("webhook", str(error))
        errors = [row for row in self.db.recent_logs(limit=50) if row["level"] == "ERROR"]
        self.assertEqual(len(errors), 1, [row["message"] for row in errors])

    async def test_distinct_profiles_still_logged(self):
        for profile_id, name in ((1, "cp compagny"), (2, "sneakers")):
            await self.notifier.notify({"id": profile_id, "name": name}, {"id": "1", "title": "x"})
        errors = [row for row in self.db.recent_logs(limit=50) if row["level"] == "ERROR"]
        self.assertEqual(len(errors), 2)

    def test_first_error_is_never_swallowed_at_boot(self):
        """Machine fraîchement démarrée : ``monotonic()`` peut être < 60 s.

        Bug observé en CI : la valeur par défaut 0.0 faisait croire que
        l'erreur venait d'être journalisée, d'où zéro ligne au lieu d'une.
        """
        notifier = DiscordNotifier.__new__(DiscordNotifier)
        notifier._log_throttle = {}
        self.assertTrue(notifier._should_log("p", "erreur"))
        self.assertFalse(notifier._should_log("p", "erreur"))

    async def test_throttle_window(self):
        self.assertTrue(self.notifier._should_log("p", "erreur"))
        self.assertFalse(self.notifier._should_log("p", "erreur"))
        self.assertTrue(self.notifier._should_log("p", "autre erreur"))


if __name__ == "__main__":
    unittest.main()

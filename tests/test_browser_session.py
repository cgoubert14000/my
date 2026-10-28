"""Tests du déblocage d'une vérification Cloudflare (gratuit, sans dépendance).

Trois niveaux :

* le client WebSocket minimal (encodage/masquage des trames, ping/pong) ;
* le parcours complet bout en bout avec un **faux serveur CDP** local : il
  simule Edge/Chrome (``/json/list``, ``DevToolsActivePort``, ``Runtime.evaluate``,
  ``Network.getAllCookies``) pour prouver que la récupération des cookies
  fonctionne réellement, sans navigateur dans la CI ;
* l'API : ``/api/session/unblock`` importe la session, lève le refroidissement
  et relance les profils.
"""

from __future__ import annotations

import base64
import json
import socket
import struct
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from app.browser_session import (
    Harvest,
    _cookie_records,
    _WebSocket,
    find_browser,
    harvest_with_solver,
)


class CookieFilterTests(unittest.TestCase):
    def test_keeps_only_the_target_domain(self):
        raw = [
            {"name": "cf_clearance", "value": "abc", "domain": ".vinted.fr"},
            {"name": "datadome", "value": "dd", "domain": "www.vinted.fr"},
            {"name": "autre", "value": "x", "domain": ".example.com"},
            {"name": "sans_domaine", "value": "y"},
        ]
        jar = _cookie_records(raw, "www.vinted.fr")
        self.assertIn("cf_clearance", jar)
        self.assertIn("datadome", jar)
        self.assertIn("sans_domaine", jar)  # cookie d'hôte, conservé
        self.assertNotIn("autre", jar)

    def test_a_parent_domain_cookie_is_not_confused_with_a_lookalike(self):
        raw = [{"name": "x", "value": "1", "domain": "notvinted.fr"}]
        self.assertEqual(_cookie_records(raw, "www.vinted.fr"), {})


class WebSocketTests(unittest.TestCase):
    """Vérifie le client WebSocket maison contre un serveur minimal."""

    def setUp(self):
        self.received = []
        self.ready = threading.Event()
        self.port = self._free_port()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(("127.0.0.1", self.port))
        self.server.listen(1)
        self.thread = threading.Thread(target=self._serve, daemon=True)
        self.thread.start()

    def _free_port(self):
        probe = socket.socket()
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
        probe.close()
        return port

    def _serve(self):
        client, _ = self.server.accept()
        request = b""
        while b"\r\n\r\n" not in request:
            request += client.recv(4096)
        key = ""
        for line in request.decode("latin-1").splitlines():
            if line.lower().startswith("sec-websocket-key:"):
                key = line.split(":", 1)[1].strip()
        import hashlib

        accept = base64.b64encode(
            hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()
        ).decode()
        client.sendall(
            (
                "HTTP/1.1 101 Switching Protocols\r\n"
                "Upgrade: websocket\r\nConnection: Upgrade\r\n"
                f"Sec-WebSocket-Accept: {accept}\r\n\r\n"
            ).encode()
        )
        self.ready.set()
        # Envoie un texte non masqué puis un ping, comme le ferait un serveur.
        self._send_text(client, '{"hello": true}')
        self._send_frame(client, 0x9, b"ping!")
        # Lit la réponse (pong éventuel, puis le message du client).
        for _ in range(2):
            data = self._read_frame(client)
            if data is not None:
                self.received.append(data)
        try:
            self._send_frame(client, 0x8, b"")
        except OSError:
            pass  # le client a déjà fermé : c'est le comportement attendu
        client.close()

    def _send_text(self, client, text):
        self._send_frame(client, 0x1, text.encode())

    def _send_frame(self, client, opcode, payload):
        header = bytearray([0x80 | opcode])
        size = len(payload)
        if size < 126:
            header.append(size)
        else:
            header.append(126)
            header += struct.pack("!H", size)
        client.sendall(bytes(header) + payload)

    def _read_frame(self, client):
        head = client.recv(2)
        if len(head) < 2:
            return None
        length = head[1] & 0x7F
        masked = bool(head[1] & 0x80)
        if length == 126:
            length = struct.unpack("!H", client.recv(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", client.recv(8))[0]
        mask = client.recv(4) if masked else b""
        data = b""
        while len(data) < length:
            data += client.recv(length - len(data))
        if mask:
            data = bytes(b ^ mask[i % 4] for i, b in enumerate(data))
        if (head[0] & 0x0F) == 0xA:
            return None  # pong : ignoré comme le ferait un client
        return data

    def tearDown(self):
        try:
            self.server.close()
        except OSError:
            pass
        self.thread.join(timeout=3)

    def test_handshake_masking_and_pong(self):
        ws = _WebSocket(f"ws://127.0.0.1:{self.port}/devtools/page/1", timeout=5)
        try:
            self.assertEqual(json.loads(ws.recv(timeout=5)), {"hello": True})
            ws.send('{"id": 1, "method": "ping"}')  # masqué côté client
            deadline = time.monotonic() + 5
            while time.monotonic() < deadline and not self.received:
                time.sleep(0.05)
            self.assertTrue(self.received, "le serveur n'a rien reçu")
            self.assertEqual(
                json.loads(self.received[-1]), {"id": 1, "method": "ping"}
            )
        finally:
            ws.close()


class FakeCDP:
    """Sert /json/list et une page DevTools qui répond comme un vrai Chrome."""

    def __init__(self):
        self.port = self._free_port()
        self.cookies = [
            {"name": "cf_clearance", "value": "clear123", "domain": ".vinted.fr"},
            {"name": "datadome", "value": "dd", "domain": "www.vinted.fr"},
            {"name": "hors_sujet", "value": "nope", "domain": ".example.com"},
        ]
        self.requests = []
        #: État de page renvoyé par Runtime.evaluate (modifiable par les tests).
        self.page = {
            "ready": "complete",
            "title": "Vinted",
            "url": "https://www.vinted.fr/catalog?search_text=nike",
            "blocked": False,
            "app": True,
            "cards": 24,
        }
        outer = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):  # silence
                pass

            def do_GET(self):
                if self.path.startswith("/json/list"):
                    body = json.dumps(
                        [
                            {
                                "type": "page",
                                "url": "https://www.vinted.fr/catalog?search_text=nike",
                                "webSocketDebuggerUrl": f"ws://127.0.0.1:{outer.port}/devtools/page/A",
                            }
                        ]
                    ).encode()
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                    return
                self.send_error(404)

        self.http = ThreadingHTTPServer(("127.0.0.1", self.port), Handler)
        threading.Thread(target=self.http.serve_forever, daemon=True).start()

        self.ws_port = self._free_port()
        self.ws_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ws_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ws_server.bind(("127.0.0.1", self.ws_port))
        self.ws_server.listen(1)
        threading.Thread(target=self._serve_ws, daemon=True).start()

    def _free_port(self):
        probe = socket.socket()
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
        probe.close()
        return port

    def _serve_ws(self):
        client, _ = self.ws_server.accept()
        request = b""
        while b"\r\n\r\n" not in request:
            chunk = client.recv(4096)
            if not chunk:
                return
            request += chunk
        import hashlib

        key = ""
        for line in request.decode("latin-1").splitlines():
            if line.lower().startswith("sec-websocket-key:"):
                key = line.split(":", 1)[1].strip()
        accept = base64.b64encode(
            hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()
        ).decode()
        client.sendall(
            (
                "HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\n"
                f"Connection: Upgrade\r\nSec-WebSocket-Accept: {accept}\r\n\r\n"
            ).encode()
        )
        while True:
            try:
                message = self._read(client)
            except OSError:
                return
            if message is None:
                return
            try:
                payload = json.loads(message)
            except json.JSONDecodeError:
                return  # trame incomplète (client fermé) : on s'arrête proprement
            self.requests.append(payload.get("method"))
            method = payload.get("method")
            if method == "Runtime.evaluate":
                expression = (payload.get("params") or {}).get("expression", "")
                if "navigator.userAgent" in expression:
                    value = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0.0.0"
                else:
                    value = json.dumps(self.page)
                result = {"result": {"result": {"type": "string", "value": value}}}
            elif method == "Network.getAllCookies":
                result = {"result": {"cookies": self.cookies}}
            else:
                result = {"result": {}}
            result["id"] = payload.get("id")
            self._send(client, json.dumps(result))

    def _read(self, client):
        head = client.recv(2)
        if len(head) < 2:
            return None
        length = head[1] & 0x7F
        masked = bool(head[1] & 0x80)
        if length == 126:
            length = struct.unpack("!H", client.recv(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", client.recv(8))[0]
        mask = client.recv(4) if masked else b""
        data = b""
        while len(data) < length:
            data += client.recv(length - len(data))
        if mask:
            data = bytes(b ^ mask[i % 4] for i, b in enumerate(data))
        return data.decode("utf-8", "replace")

    def _send(self, client, text):
        payload = text.encode()
        header = bytearray([0x81])
        if len(payload) < 126:
            header.append(len(payload))
        else:
            header.append(126)
            header += struct.pack("!H", len(payload))
        client.sendall(bytes(header) + payload)

    def close(self):
        self.http.shutdown()
        self.http.server_close()
        try:
            self.ws_server.close()
        except OSError:
            pass


class HarvestTests(unittest.TestCase):
    """Parcours complet : navigateur piloté par CDP (ici, un faux serveur)."""

    def setUp(self):
        import tempfile
        from pathlib import Path as _Path

        self.fake = FakeCDP()
        self.addCleanup(self.fake.close)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.profile = _Path(self.tmp.name)
        self.profile.joinpath("DevToolsActivePort").write_text(
            f"{self.fake.port}\n/devtools/browser/xyz\n", encoding="utf-8"
        )
        self.launched: list[tuple[str, list[str]]] = []

    def _patch(self, module, *, exit_code=None, port_ok=True, fail_first=0):
        """Prépare un faux lancement : aucun vrai processus n'est créé."""
        state = {"calls": 0}
        originals = {
            name: getattr(module, name)
            for name in (
                "find_browser",
                "_installed_browsers",
                "subprocess",
                "_await_devtools",
                "_page_ws_url",
                "_free_port",
            )
        }

        class FakeProc:
            def __init__(self, code):
                self.pid = 4242
                self.returncode = code

            def poll(self):
                return self.returncode

            def wait(self, timeout=None):
                return self.returncode

            def terminate(self):
                pass

            def kill(self):
                pass

        class FakeSubprocess:
            Popen = staticmethod(lambda args, **kwargs: self.launched.append((args[0], args)) or FakeProc(exit_code))
            DEVNULL = -3
            CREATE_NO_WINDOW = 0

        module.subprocess = FakeSubprocess
        module.find_browser = lambda explicit="": "/opt/faux-chrome"
        module._installed_browsers = lambda: ["/opt/faux-chrome", "/opt/autre-edge"]
        module._free_port = lambda: 9500

        def fake_await(profile_dir, port, process, stderr_path, deadline):
            state["calls"] += 1
            if state["calls"] <= fail_first:
                raise module.BrowserError("Le navigateur s'est arrêté aussitôt (code 21).")
            if not port_ok:
                raise module.BrowserError("Le navigateur n'a pas ouvert son port de débogage.")
            return self.fake.port

        module._await_devtools = fake_await
        module._page_ws_url = lambda port, deadline: (
            f"ws://127.0.0.1:{self.fake.ws_port}/devtools/page/A"
        )
        self.addCleanup(lambda: [setattr(module, k, v) for k, v in originals.items()])
        return module

    def _harvest(self, **kwargs):
        import app.browser_session as module

        options = {"profile_dir": self.tmp.name, "timeout": 8}
        options.update(kwargs)
        self._patch(module, **{k: options.pop(k) for k in list(options) if k in
                               {"exit_code", "port_ok", "fail_first"}})
        return module.harvest_with_browser(
            "https://www.vinted.fr/catalog?search_text=nike", **options
        )

    def test_harvest_imports_clearance_cookie_and_user_agent(self):
        result = self._harvest()
        self.assertTrue(result.ok, result.message)
        self.assertIn("cf_clearance", result.cookies)
        self.assertEqual(result.cookies["cf_clearance"], "clear123")
        self.assertNotIn("hors_sujet", result.cookies)
        self.assertIn("Mozilla/5.0", result.user_agent)
        self.assertEqual(result.cards, 24)
        self.assertIn("Runtime.evaluate", self.fake.requests)
        self.assertIn("Network.getAllCookies", self.fake.requests)
        self.assertTrue(result.cleared)

    def test_launch_uses_an_absolute_profile_and_an_explicit_port(self):
        self._harvest()
        self.assertTrue(self.launched, "aucun navigateur lancé")
        args = self.launched[0][1]
        profile_arg = next(a for a in args if a.startswith("--user-data-dir="))
        # Chemin absolu : Edge ne doit pas résoudre « data\… » à sa façon.
        self.assertTrue(profile_arg.split("=", 1)[1].startswith(("/", "C:", "c:")))
        self.assertTrue(any(a.startswith("--remote-debugging-port=") for a in args))

    def test_an_empty_result_page_still_counts_as_solved(self):
        import app.browser_session as module

        self.fake.page.update({"cards": 0, "app": True, "blocked": False})
        originals = dict(self.fake.page)
        try:
            result = self._harvest()
        finally:
            self.fake.page.update(originals)
        self.assertTrue(result.ok, "une page vide ne doit pas être vue comme un blocage")
        self.assertTrue(result.cookies)
        _ = module

    def test_a_challenge_page_is_not_reported_as_solved(self):
        """Défi encore affiché : on ne prétend pas avoir débloqué."""
        self.fake.page.update({"cards": 0, "app": False, "blocked": True})
        originals = dict(self.fake.page)
        try:
            result = self._harvest()
        finally:
            self.fake.page.update(originals)
        self.assertFalse(result.ok)
        self.assertIn("vérification", result.message.lower())
        self.assertTrue(result.cookies)  # remontés pour diagnostic, jamais importés

    def test_retries_with_a_fresh_profile_when_the_first_launch_fails(self):
        """Panne constatée en 1.3.7 : profil verrouillé → on réessaie ailleurs."""
        import app.browser_session as module

        options = {"profile_dir": self.tmp.name, "timeout": 8, "fail_first": 1}
        self._patch(module, fail_first=1)
        result = module.harvest_with_browser(
            "https://www.vinted.fr/catalog", profile_dir=self.tmp.name, timeout=8
        )
        _ = options
        self.assertTrue(result.ok)
        profiles = [
            next(a for a in args if a.startswith("--user-data-dir="))
            for _, args in self.launched
        ]
        self.assertEqual(len(profiles), 2, "deux tentatives attendues")
        self.assertNotEqual(profiles[0], profiles[1], "le second essai doit changer de profil")

    def test_switches_to_another_browser_after_two_failures(self):
        import app.browser_session as module

        self._patch(module, fail_first=2)
        result = module.harvest_with_browser(
            "https://www.vinted.fr/catalog", profile_dir=self.tmp.name, timeout=8
        )
        self.assertTrue(result.ok)
        executables = {path for path, _ in self.launched}
        self.assertEqual(len(executables), 2, "un autre navigateur doit être essayé")

    def test_reports_every_failure_with_actionable_text(self):
        import app.browser_session as module

        self._patch(module, port_ok=False)
        with self.assertRaises(module.BrowserError) as caught:
            module.harvest_with_browser(
                "https://www.vinted.fr/catalog", profile_dir=self.tmp.name, timeout=2
            )
        message = str(caught.exception)
        self.assertIn("Déblocage impossible", message)
        self.assertIn("port de débogage", message)
        self.assertIn("Réglages", message)


class CurlImportTests(unittest.TestCase):
    """Secours : une commande cURL copiée du navigateur."""

    CHROME = (
        "curl 'https://www.vinted.fr/catalog?brand_ids[]=53' \\\n"
        "  -H 'accept: text/html' \\\n"
        "  -H 'Cookie: cf_clearance=abc123; datadome=xyz; _vinted_fr_session=t' \\\n"
        "  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/141' \\\n"
        "  --compressed"
    )

    def test_parses_cookies_and_user_agent(self):
        from app.browser_session import session_from_curl

        session = session_from_curl(self.CHROME)
        self.assertEqual(session["cookies"]["cf_clearance"], "abc123")
        self.assertEqual(session["cookies"]["datadome"], "xyz")
        self.assertIn("Chrome/141", session["user_agent"])
        self.assertTrue(session["clearance"])
        self.assertEqual(session["url"], "https://www.vinted.fr/catalog?brand_ids[]=53")

    def test_accepts_windows_cmd_continuations_and_cookie_flag(self):
        from app.browser_session import session_from_curl

        command = (
            'curl.exe "https://www.vinted.fr/catalog" ^\n'
            ' -b "cf_clearance=zzz; datadome=dd" ^\n'
            ' -H "User-Agent: Mozilla/5.0 (Linux) Chrome/140"'
        )
        session = session_from_curl(command)
        self.assertEqual(session["cookies"]["cf_clearance"], "zzz")
        self.assertIn("Linux", session["user_agent"])

    def test_refuses_non_curl_and_missing_cookies(self):
        from app.browser_session import session_from_curl

        with self.assertRaises(ValueError):
            session_from_curl("wget https://www.vinted.fr")
        with self.assertRaises(ValueError):
            session_from_curl("curl 'https://www.vinted.fr/catalog' -H 'accept: */*'")

    def test_without_clearance_the_import_is_flagged(self):
        from app.browser_session import session_from_curl

        session = session_from_curl(
            "curl 'https://www.vinted.fr/catalog' -H 'Cookie: _vinted_fr_session=t'"
        )
        self.assertFalse(session["clearance"])
        self.assertEqual(session["cookies"], {"_vinted_fr_session": "t"})


class SolverTests(unittest.TestCase):
    """FlareSolverr / Byparr : même API, réponse ``solution.cookies``."""

    def setUp(self):
        payload = json.dumps(
            {
                "status": "ok",
                "message": "Challenge solved!",
                "solution": {
                    "url": "https://www.vinted.fr/catalog",
                    "userAgent": "Mozilla/5.0 Chrome/131",
                    "cookies": [
                        {"name": "cf_clearance", "value": "via-solver", "domain": ".vinted.fr"},
                        {"name": "bruit", "value": "1", "domain": ".autre.fr"},
                    ],
                },
            }
        ).encode()

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                length = int(self.headers.get("Content-Length", 0))
                self.rfile.read(length)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

        probe = socket.socket()
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
        probe.close()
        self.http = ThreadingHTTPServer(("127.0.0.1", port), Handler)
        threading.Thread(target=self.http.serve_forever, daemon=True).start()
        self.endpoint = f"http://127.0.0.1:{port}"

    def tearDown(self):
        self.http.shutdown()
        self.http.server_close()

    def test_solution_cookies_are_used(self):
        result = harvest_with_solver("https://www.vinted.fr/catalog", self.endpoint, timeout=10)
        self.assertTrue(result.ok)
        self.assertEqual(result.cookies["cf_clearance"], "via-solver")
        self.assertNotIn("bruit", result.cookies)
        self.assertEqual(result.user_agent, "Mozilla/5.0 Chrome/131")
        self.assertEqual(result.source, "solver")


class BrowserDetectionTests(unittest.TestCase):
    def test_explicit_path_is_used_or_refused(self):
        self.assertIsNone(find_browser("C:/chemin/inexistant/chrome.exe"))

    def test_detection_never_raises(self):
        # Sur la CI Linux, soit un Chromium est présent, soit None : jamais d'erreur.
        self.assertTrue(find_browser() is None or isinstance(find_browser(), str))


class HarvestSummaryTests(unittest.TestCase):
    def test_summary_is_json_safe(self):
        harvest = Harvest(ok=True, cookies={"cf_clearance": "x"}, user_agent="UA")
        summary = harvest.summary()
        json.dumps(summary)  # ne doit pas lever
        self.assertEqual(summary["cookies"], ["cf_clearance"])
        self.assertNotIn("x", json.dumps(summary))  # jamais la valeur du cookie


if __name__ == "__main__":
    unittest.main()

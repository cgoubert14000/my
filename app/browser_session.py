"""Déblocage d'une vérification Cloudflare **gratuitement**, avec le navigateur
déjà installé sur la machine.

Pourquoi ce module existe
-------------------------
Quand Vinted renvoie ``page « challenge-platform »``, la réponse ne contient
pas le catalogue : elle contient le script de vérification Cloudflare, que le
bot (curl_cffi) ne peut pas exécuter. Insister ne sert à rien, et un défi
interactif ne peut **pas** être résolu sans navigateur.

Il existe pourtant une solution gratuite, celle qu'utilisent FlareSolverr,
Byparr ou CloudflareBypassForScraping : **ouvrir une vraie page dans un vrai
navigateur**, laisser la vérification se terminer (automatiquement, ou en
cochant la case à la main), puis **récupérer les cookies** — dont
``cf_clearance``, qui est ``HttpOnly`` et donc invisible depuis
``document.cookie``. Ces cookies sont liés à l'adresse IP **et** au User-Agent :
on réinjecte donc les deux ensemble dans le client HTTP, qui garde ensuite son
identité stable (``curl_cffi`` imite déjà l'empreinte TLS de Chrome).

Aucune dépendance : ce module pilote Microsoft Edge ou Google Chrome via le
**Chrome DevTools Protocol** (CDP), en WebSocket, avec la bibliothèque standard.
Edge est installé d'office sur Windows : rien à télécharger, rien à installer.

Deux sources possibles, choisies dans cet ordre :

1. ``challenge.solver_url`` — un FlareSolverr / Byparr local (Docker), pratique
   si l'utilisateur en a déjà un ;
2. sinon, le navigateur local (``challenge.browser_path`` ou détection auto).

Le module est volontairement **synchrone** : il est appelé depuis un thread
(``asyncio.to_thread``) pour ne jamais bloquer la boucle du moteur.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

#: Fichiers à interroger, dans l'ordre, selon le système.
_WINDOWS_CANDIDATES = (
    r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe",
    r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe",
    r"%ProgramFiles%\Google\Chrome\Application\chrome.exe",
    r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe",
    r"%LocalAppData%\Google\Chrome\Application\chrome.exe",
    r"%LocalAppData%\Chromium\Application\chrome.exe",
    r"%ProgramFiles%\BraveSoftware\Brave-Browser\Application\brave.exe",
)

_MAC_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
)

_LINUX_CANDIDATES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "microsoft-edge",
    "brave-browser",
)

#: Motifs d'une page de vérification encore affichée.
CHALLENGE_HTML_MARKERS = (
    "challenge-platform",
    "just a moment",
    "captcha-delivery",
    "cf-chl",
    "cf-browser-verification",
    "unusual traffic",
    "access to this page has been denied",
)

#: Sonde exécutée dans la page : la vérification est-elle passée ?
#:
#: ⚠️ Même leçon que pour la 1.3.4 : la chaîne « challenge-platform » apparaît
#: aussi sur une page Vinted normale (Cloudflare injecte son script sur tout le
#: site). On ne conclut donc **jamais** sur un marqueur seul : on regarde
#: d'abord si l'application Vinted est là (``#__nuxt``, en-tête, grille).
_PROBE_JS = """
(() => {
  const title = document.title || "";
  const html = document.documentElement ? document.documentElement.outerHTML : "";
  const sample = html.slice(0, 300000).toLowerCase();
  const appRoot = document.querySelector('#__nuxt, #app, [data-testid="header"], header');
  const challengeNode = document.querySelector(
    '#challenge-form, #challenge-stage, #cf-challenge-running, .cf-turnstile, iframe[src*="challenges.cloudflare.com"]'
  );
  const markers = ["just a moment", "attention required", "captcha-delivery",
                   "cf-chl", "checking your browser", "unusual traffic",
                   "access to this page has been denied"];
  const titledBlock = /just a moment|attention required|un instant|vérification de sécurité/i.test(title);
  const textBlock = markers.some((m) => sample.includes(m));
  const blocked = Boolean(challengeNode) || titledBlock || (textBlock && !appRoot);
  const cards = document.querySelectorAll(
    '[data-testid^="product-item"], [data-testid="grid-item"], .new-item-box__container'
  ).length;
  return JSON.stringify({
    ready: document.readyState,
    title: title,
    url: location.href,
    blocked: blocked,
    app: Boolean(appRoot),
    cards: cards,
    cookies: /(?:^|;\s*)cf_clearance=/.test(document.cookie) ? 1 : 0,
  });
})()
"""


class BrowserError(RuntimeError):
    """Le navigateur n'a pas pu être lancé ou piloté."""


class SolverError(RuntimeError):
    """Le solutionneur externe (FlareSolverr / Byparr) a échoué."""


@dataclass
class Harvest:
    """Résultat d'une tentative de déblocage."""

    ok: bool
    cookies: dict[str, str] = field(default_factory=dict)
    user_agent: str = ""
    url: str = ""
    title: str = ""
    source: str = "browser"
    solved: bool = False
    cards: int = 0
    elapsed_ms: int = 0
    message: str = ""
    cleared: list[str] = field(default_factory=list)

    def summary(self) -> dict:
        return {
            "ok": self.ok,
            "source": self.source,
            "solved": self.solved,
            "cards": self.cards,
            "title": self.title,
            "url": self.url,
            "cookies": sorted(self.cookies),
            "cleared": self.cleared,
            "user_agent": self.user_agent,
            "elapsed_ms": self.elapsed_ms,
            "message": self.message,
        }


# ── Détection du navigateur ──────────────────────────────────────────────────


def find_browser(explicit: str = "") -> str | None:
    """Chemin du premier navigateur Chromium disponible (``None`` sinon).

    ``explicit`` (``challenge.browser_path``) est prioritaire : utile quand le
    navigateur est installé ailleurs (portable, autre lecteur…).
    """
    if explicit:
        candidate = Path(os.path.expandvars(os.path.expanduser(str(explicit))))
        if candidate.is_file():
            return str(candidate)
        return None
    if sys.platform.startswith("win"):
        for raw in _WINDOWS_CANDIDATES:
            candidate = Path(os.path.expandvars(raw))
            if candidate.is_file():
                return str(candidate)
        return None
    if sys.platform == "darwin":
        for raw in _MAC_CANDIDATES:
            if Path(raw).is_file():
                return raw
        return None
    for name in _LINUX_CANDIDATES:
        found = shutil.which(name)
        if found:
            return found
    return None


# ── WebSocket minimal (RFC 6455) ─────────────────────────────────────────────


class _WebSocket:
    """Client WebSocket texte, suffisant pour parler à CDP.

    Volontairement réduit : trames non fragmentées en écriture, fragmentation
    assemblée en lecture, ``ping``/``pong`` honorés. Aucune dépendance externe.
    """

    def __init__(self, url: str, timeout: float = 20.0):
        parsed = urlparse(url)
        if parsed.scheme != "ws":
            raise BrowserError(f"WebSocket refusé : {url}")
        host = parsed.hostname or "127.0.0.1"
        port = parsed.port or 80
        path = parsed.path or "/"
        if parsed.query:
            path += f"?{parsed.query}"
        self._sock = socket.create_connection((host, port), timeout=timeout)
        self._sock.settimeout(timeout)
        self._buffer = b""
        key = base64.b64encode(os.urandom(16)).decode()
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            "Origin: http://127.0.0.1\r\n"
            "\r\n"
        )
        self._sock.sendall(request.encode())
        response = self._read_until(b"\r\n\r\n").decode("latin-1")
        if " 101 " not in response.split("\r\n", 1)[0]:
            raise BrowserError(f"Poignée de main WebSocket refusée : {response.splitlines()[:1]}")
        expected = base64.b64encode(
            hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()
        ).decode()
        if expected.lower() not in response.lower():
            raise BrowserError("Poignée de main WebSocket invalide (clé d'acceptation).")

    # ── Lecture brute ────────────────────────────────────────────────────
    def _read_until(self, marker: bytes) -> bytes:
        while marker not in self._buffer:
            chunk = self._sock.recv(65536)
            if not chunk:
                raise BrowserError("Connexion DevTools fermée par le navigateur.")
            self._buffer += chunk
        head, _, rest = self._buffer.partition(marker)
        self._buffer = rest
        return head + marker

    def _read_exact(self, size: int) -> bytes:
        while len(self._buffer) < size:
            chunk = self._sock.recv(max(65536, size - len(self._buffer)))
            if not chunk:
                raise BrowserError("Connexion DevTools fermée par le navigateur.")
            self._buffer += chunk
        data, self._buffer = self._buffer[:size], self._buffer[size:]
        return data

    # ── Trames ───────────────────────────────────────────────────────────
    def send(self, text: str) -> None:
        payload = text.encode("utf-8")
        header = bytearray()
        header.append(0x81)  # FIN + texte
        length = len(payload)
        mask_bit = 0x80
        if length < 126:
            header.append(mask_bit | length)
        elif length < 65536:
            header.append(mask_bit | 126)
            header += struct.pack("!H", length)
        else:
            header.append(mask_bit | 127)
            header += struct.pack("!Q", length)
        mask = os.urandom(4)
        header += mask
        masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        self._sock.sendall(bytes(header) + masked)

    def recv(self, timeout: float | None = None) -> str:
        if timeout is not None:
            self._sock.settimeout(timeout)
        while True:
            head = self._read_exact(2)
            fin = bool(head[0] & 0x80)
            opcode = head[0] & 0x0F
            masked = bool(head[1] & 0x80)
            length = head[1] & 0x7F
            if length == 126:
                length = struct.unpack("!H", self._read_exact(2))[0]
            elif length == 127:
                length = struct.unpack("!Q", self._read_exact(8))[0]
            mask = self._read_exact(4) if masked else b""
            data = self._read_exact(length) if length else b""
            if mask:
                data = bytes(byte ^ mask[index % 4] for index, byte in enumerate(data))
            if opcode == 0x9:  # ping → pong
                self._send_control(0xA, data)
                continue
            if opcode == 0xA:  # pong
                continue
            if opcode == 0x8:  # close
                raise BrowserError("Le navigateur a fermé la session DevTools.")
            chunk = data.decode("utf-8", "replace")
            if fin:
                return chunk
            parts = [chunk]
            while True:  # trame fragmentée
                head = self._read_exact(2)
                fin = bool(head[0] & 0x80)
                length = head[1] & 0x7F
                if length == 126:
                    length = struct.unpack("!H", self._read_exact(2))[0]
                elif length == 127:
                    length = struct.unpack("!Q", self._read_exact(8))[0]
                parts.append(self._read_exact(length).decode("utf-8", "replace"))
                if fin:
                    return "".join(parts)

    def _send_control(self, opcode: int, payload: bytes = b"") -> None:
        header = bytearray([0x80 | opcode])
        header.append(0x80 | len(payload))
        mask = os.urandom(4)
        header += mask
        masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        self._sock.sendall(bytes(header) + masked)

    def close(self) -> None:
        try:
            self._send_control(0x8)
        except Exception:  # pragma: no cover - déjà fermé
            pass
        try:
            self._sock.close()
        except Exception:  # pragma: no cover
            pass


# ── Client CDP ───────────────────────────────────────────────────────────────


class _CDP:
    """Petit client DevTools : ``call("Network.getAllCookies")``."""

    def __init__(self, ws: _WebSocket):
        self.ws = ws
        self._id = 0

    def call(self, method: str, params: dict | None = None, timeout: float = 20.0):
        self._id += 1
        message = {"id": self._id, "method": method}
        if params:
            message["params"] = params
        self.ws.send(json.dumps(message))
        deadline = time.monotonic() + timeout
        while True:
            remaining = max(0.1, deadline - time.monotonic())
            raw = self.ws.recv(timeout=remaining)
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:  # pragma: no cover - trame inattendue
                continue
            if payload.get("id") != self._id:
                continue  # événement (Network.responseReceived…)
            if "error" in payload:
                raise BrowserError(f"{method} : {payload['error'].get('message', payload['error'])}")
            return payload.get("result", {})


def _devtools_endpoint(profile_dir: Path, deadline: float) -> tuple[int, str]:
    """Attend que le navigateur écrive ``DevToolsActivePort`` et le lit."""
    port_file = profile_dir / "DevToolsActivePort"
    while time.monotonic() < deadline:
        if port_file.is_file():
            content = port_file.read_text(encoding="utf-8", errors="replace").splitlines()
            if content and content[0].strip().isdigit():
                return int(content[0].strip()), (content[1].strip() if len(content) > 1 else "")
        time.sleep(0.15)
    raise BrowserError(
        "Le navigateur n'a pas ouvert son port de débogage "
        "(profil déjà utilisé par une autre fenêtre ?)."
    )


def _page_ws_url(port: int, deadline: float) -> str:
    """URL WebSocket de la page ouverte (via ``/json/list``)."""
    last_error = ""
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=3) as response:
                targets = json.loads(response.read().decode("utf-8"))
            pages = [t for t in targets if t.get("type") == "page"]
            if pages:
                chosen = next((t for t in pages if t.get("url", "").startswith("http")), pages[0])
                return chosen["webSocketDebuggerUrl"]
        except (urllib.error.URLError, json.JSONDecodeError, KeyError) as error:
            last_error = str(error)
        time.sleep(0.2)
    raise BrowserError(f"Aucune page DevTools disponible ({last_error or 'délai dépassé'}).")


def _cookie_records(raw: list, domain: str) -> dict[str, str]:
    """Ne garde que les cookies du domaine visé (Vinted + sous-domaines)."""
    suffix = domain.lower().lstrip(".")
    jar: dict[str, str] = {}
    for cookie in raw or []:
        name = cookie.get("name")
        if not name:
            continue
        host = str(cookie.get("domain", "")).lower().lstrip(".")
        if host and suffix and not (host == suffix or host.endswith("." + suffix) or suffix.endswith("." + host)):
            continue
        jar[name] = str(cookie.get("value", ""))
    return jar


def harvest_with_browser(
    url: str,
    *,
    browser_path: str = "",
    profile_dir: str | Path | None = None,
    timeout: float = 60.0,
    headless: bool = False,
    on_log=None,
) -> Harvest:
    """Ouvre ``url`` dans le navigateur local et récupère cookies + User-Agent.

    Le navigateur reste **visible** par défaut : si Cloudflare demande une
    action (case à cocher, « maintenir le bouton »), l'utilisateur la fait et
    la session est récupérée dès que la page réelle apparaît. Aucun cookie
    n'est deviné : ils viennent de la session que Vinted vient d'accepter.
    """
    started = time.monotonic()
    log = on_log or (lambda message: None)
    executable = find_browser(browser_path)
    if not executable:
        raise BrowserError(
            "Aucun navigateur Chromium trouvé. Installez Microsoft Edge ou Google "
            "Chrome, ou indiquez son chemin (challenge.browser_path)."
        )
    if not url.startswith(("http://", "https://")):
        url = "https://" + url.lstrip("/")
    domain = urlparse(url).netloc
    profile = Path(profile_dir or Path(tempfile.gettempdir()) / "vinted-sniper-browser")
    profile.mkdir(parents=True, exist_ok=True)

    # Un ancien DevToolsActivePort ferait croire à un port valide : on l'efface.
    stale = profile / "DevToolsActivePort"
    if stale.exists():
        stale.unlink()

    args = [
        executable,
        "--remote-debugging-port=0",
        f"--user-data-dir={profile}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-blink-features=AutomationControlled",
        "--disable-features=Translate,MediaRouter,OptimizationHints",
        "--window-size=1280,900",
    ]
    if headless:
        args.append("--headless=new")
    args.append(url)

    log(f"Ouverture de {domain} dans {Path(executable).name}…")
    try:
        process = subprocess.Popen(  # noqa: S603 - chemin contrôlé, arguments fixes
            args,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )
    except OSError as error:
        raise BrowserError(f"Lancement impossible : {error}") from error

    deadline = time.monotonic() + timeout
    ws: _WebSocket | None = None
    try:
        port, _ = _devtools_endpoint(profile, min(deadline, time.monotonic() + 25))
        ws = _WebSocket(_page_ws_url(port, min(deadline, time.monotonic() + 15)))
        cdp = _CDP(ws)
        try:
            cdp.call("Network.enable", timeout=10)
        except BrowserError:
            pass  # certaines versions l'exposent au niveau navigateur seulement

        probe: dict = {}
        while time.monotonic() < deadline:
            try:
                result = cdp.call(
                    "Runtime.evaluate",
                    {"expression": _PROBE_JS, "returnByValue": True},
                    timeout=10,
                )
                value = (result.get("result") or {}).get("value")
                probe = json.loads(value) if value else {}
            except (BrowserError, json.JSONDecodeError):
                probe = {}
            if probe.get("cards", 0) > 0:
                break  # grille d'annonces : c'est gagné
            if (
                probe.get("ready") == "complete"
                and not probe.get("blocked")
                and probe.get("app")
            ):
                break  # page réelle, simplement sans résultat
            time.sleep(0.7)

        cookies = cdp.call("Network.getAllCookies", timeout=15).get("cookies", [])
        jar = _cookie_records(cookies, domain)
        user_agent = ""
        try:
            ua = cdp.call(
                "Runtime.evaluate",
                {"expression": "navigator.userAgent", "returnByValue": True},
                timeout=10,
            )
            user_agent = str((ua.get("result") or {}).get("value") or "")
        except BrowserError:
            user_agent = ""
        # Réussi si Vinted a réellement répondu (grille ou application) et
        # qu'aucun défi n'est encore affiché.
        page_ok = bool(probe.get("cards", 0) > 0) or bool(
            probe.get("app") and not probe.get("blocked")
        )
        solved = bool(jar) and page_ok
        elapsed = int((time.monotonic() - started) * 1000)
        cleared = sorted(name for name in jar if name.startswith(("cf_", "__cf", "datadome")))
        message = (
            f"Session récupérée ({len(jar)} cookie(s), {probe.get('cards', 0)} annonce(s) visible(s))."
            if solved
            else "La vérification n'est pas terminée : terminez-la dans la fenêtre ouverte, "
            "puis relancez."
        )
        return Harvest(
            ok=solved,
            cookies=jar,
            user_agent=user_agent,
            url=str(probe.get("url") or url),
            title=str(probe.get("title") or ""),
            source="browser",
            solved=solved,
            cards=int(probe.get("cards") or 0),
            elapsed_ms=elapsed,
            message=message,
            cleared=cleared,
        )
    finally:
        if ws is not None:
            ws.close()
        try:
            process.terminate()
            process.wait(timeout=8)
        except Exception:  # pragma: no cover - processus déjà arrêté
            try:
                process.kill()
            except Exception:
                pass


# ── FlareSolverr / Byparr (Docker, même API) ─────────────────────────────────


def harvest_with_solver(url: str, endpoint: str, timeout: float = 70.0) -> Harvest:
    """Demande la page à un FlareSolverr/Byparr local et récupère sa session.

    Ces deux projets sont gratuits et open source ; ils font exactement la même
    chose que :func:`harvest_with_browser`, mais dans un conteneur. Utile si
    l'utilisateur en fait déjà tourner un (Prowlarr, Jackett, *arr…).
    """
    started = time.monotonic()
    base = endpoint.rstrip("/")
    if not base.endswith("/v1"):
        base += "/v1"
    payload = json.dumps(
        {"cmd": "request.get", "url": url, "maxTimeout": int(max(10, timeout) * 1000)}
    ).encode()
    request = urllib.request.Request(
        base,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        raise SolverError(f"Solutionneur injoignable ({base}) : {error}") from error
    if str(data.get("status", "")).lower() != "ok":
        raise SolverError(str(data.get("message") or "Le solutionneur a échoué."))
    solution = data.get("solution") or {}
    domain = urlparse(url).netloc
    jar = _cookie_records(solution.get("cookies") or [], domain)
    return Harvest(
        ok=bool(jar),
        cookies=jar,
        user_agent=str(solution.get("userAgent") or ""),
        url=str(solution.get("url") or url),
        source="solver",
        solved=bool(jar),
        elapsed_ms=int((time.monotonic() - started) * 1000),
        message=f"Session récupérée via {base} ({len(jar)} cookie(s))."
        if jar
        else "Le solutionneur n'a renvoyé aucun cookie.",
        cleared=sorted(n for n in jar if n.startswith(("cf_", "__cf", "datadome"))),
    )


# ── Point d'entrée ───────────────────────────────────────────────────────────


def harvest(
    url: str,
    *,
    solver_url: str = "",
    browser_path: str = "",
    profile_dir: str | Path | None = None,
    timeout: float = 60.0,
    headless: bool = False,
    on_log=None,
) -> Harvest:
    """Récupère une session valide, par le solutionneur ou le navigateur local."""
    if solver_url:
        try:
            return harvest_with_solver(url, solver_url, timeout=timeout + 10)
        except SolverError as error:
            if on_log:
                on_log(f"Solutionneur indisponible ({error}) : bascule sur le navigateur local.")
    return harvest_with_browser(
        url,
        browser_path=browser_path,
        profile_dir=profile_dir,
        timeout=timeout,
        headless=headless,
        on_log=on_log,
    )

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
import re
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


def _free_port() -> int:
    """Port TCP libre choisi par l'OS."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


def _http_ok(url: str, timeout: float = 1.5) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:  # noqa: S310
            response.read(512)
        return True
    except Exception:
        return False


def _active_port(profile_dir: Path) -> int | None:
    """Port inscrit par le navigateur dans ``DevToolsActivePort`` (source sûre)."""
    port_file = profile_dir / "DevToolsActivePort"
    try:
        content = port_file.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None
    if content and content[0].strip().isdigit():
        return int(content[0].strip())
    return None


def _stderr_tail(path: Path, limit: int = 400) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace").strip()
    except OSError:
        return ""
    return text[-limit:].replace("\n", " ")


def _await_devtools(
    profile_dir: Path,
    port: int,
    process: subprocess.Popen,
    stderr_path: Path,
    deadline: float,
) -> int:
    """Attend que DevTools réponde, puis renvoie le port réellement ouvert.

    Deux sources, dans cet ordre :

    1. ``DevToolsActivePort`` écrit par le navigateur (valeur exacte) ;
    2. le port demandé, sondé en HTTP — utile si Edge/Chrome ignore le fichier.

    Si le processus meurt avant, on remonte son code de sortie et sa sortie
    d'erreur : c'est ce qui distingue « profil verrouillé » d'un simple
    ralentissement.
    """
    while time.monotonic() < deadline:
        candidate = _active_port(profile_dir)
        if candidate and _http_ok(f"http://127.0.0.1:{candidate}/json/version"):
            return candidate
        if _http_ok(f"http://127.0.0.1:{port}/json/version"):
            return port
        code = process.poll()
        if code is not None:
            detail = _stderr_tail(stderr_path)
            raise BrowserError(
                f"Le navigateur s'est arrêté aussitôt (code {code}). "
                + (f"Détail : {detail}" if detail else
                   "Le profil de débogage est probablement déjà ouvert ailleurs.")
            )
        time.sleep(0.25)
    detail = _stderr_tail(stderr_path)
    raise BrowserError(
        "Le navigateur n'a pas ouvert son port de débogage"
        + (f" ({detail})" if detail else "")
        + ". Une stratégie Windows (« Allow remote debugging ») ou un antivirus "
        "peut le bloquer."
    )


def _page_ws_url(port: int, deadline: float) -> str:
    """URL WebSocket de la page ouverte (via ``/json/list``)."""
    last_error = ""
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(  # noqa: S310
                f"http://127.0.0.1:{port}/json/list", timeout=3
            ) as response:
                targets = json.loads(response.read().decode("utf-8"))
            pages = [t for t in targets if t.get("type") == "page"]
            if pages:
                chosen = next((t for t in pages if t.get("url", "").startswith("http")), pages[0])
                return chosen["webSocketDebuggerUrl"]
        except (urllib.error.URLError, json.JSONDecodeError, KeyError) as error:
            last_error = str(error)
        time.sleep(0.2)
    raise BrowserError(f"Aucune page DevTools disponible ({last_error or 'délai dépassé'}).")


def _stop_process(process: subprocess.Popen) -> None:
    """Ferme le navigateur et ses enfants (Windows : ``taskkill /T``)."""
    if process.poll() is not None:
        return
    try:
        if sys.platform.startswith("win"):
            subprocess.run(  # noqa: S603,S607 - commande système fixe
                ["taskkill", "/F", "/T", "/PID", str(process.pid)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
        else:
            process.terminate()
        process.wait(timeout=8)
    except Exception:  # pragma: no cover - déjà terminé
        try:
            process.kill()
        except Exception:
            pass


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


def _installed_browsers() -> list[str]:
    """Tous les navigateurs Chromium présents, dans l'ordre de préférence."""
    found: list[str] = []
    if sys.platform.startswith("win"):
        for raw in _WINDOWS_CANDIDATES:
            candidate = Path(os.path.expandvars(raw))
            if candidate.is_file():
                found.append(str(candidate))
    elif sys.platform == "darwin":
        found = [raw for raw in _MAC_CANDIDATES if Path(raw).is_file()]
    else:
        for name in _LINUX_CANDIDATES:
            path = shutil.which(name)
            if path:
                found.append(path)
    return found


def _browser_candidates(explicit: str) -> list[str]:
    """Navigateurs à essayer, sans doublon : le chemin demandé, puis les autres."""
    ordered: list[str] = []
    if explicit:
        chosen = find_browser(explicit)
        if chosen:
            ordered.append(chosen)
    for path in _installed_browsers():
        if path not in ordered:
            ordered.append(path)
    return ordered


def _launch_once(
    executable: str,
    url: str,
    profile_dir: Path,
    *,
    headless: bool,
    timeout: float,
    log,
) -> Harvest:
    """Une tentative : lance UN navigateur, attend DevTools, lit la session."""
    started = time.monotonic()
    port = _free_port()
    profile_dir = profile_dir.resolve()
    profile_dir.mkdir(parents=True, exist_ok=True)
    stale = profile_dir / "DevToolsActivePort"
    if stale.exists():
        stale.unlink()

    args = [
        executable,
        f"--remote-debugging-port={port}",
        f"--user-data-dir={profile_dir}",
        "--remote-allow-origins=*",
        "--no-first-run",
        "--no-default-browser-check",
        "--no-service-autorun",
        "--disable-sync",
        "--disable-blink-features=AutomationControlled",
        "--disable-features=Translate,MediaRouter,OptimizationHints",
        "--window-size=1280,900",
    ]
    if headless:
        args.append("--headless=new")
    args.append(url)

    stderr_path = profile_dir / "browser-stderr.log"
    log(f"Lancement de {Path(executable).name} (port DevTools {port}, profil {profile_dir})…")
    with stderr_path.open("wb") as stderr_handle:
        try:
            process = subprocess.Popen(  # noqa: S603 - chemin contrôlé, arguments fixes
                args,
                stdout=subprocess.DEVNULL,
                stderr=stderr_handle,
                stdin=subprocess.DEVNULL,
                close_fds=True,
            )
        except OSError as error:
            raise BrowserError(f"Lancement impossible ({Path(executable).name}) : {error}") from error

        ws: _WebSocket | None = None
        try:
            active = _await_devtools(
                profile_dir,
                port,
                process,
                stderr_path,
                min(time.monotonic() + 25, started + timeout),
            )
            ws = _WebSocket(_page_ws_url(active, min(time.monotonic() + 15, started + timeout)))
            cdp = _CDP(ws)
            try:
                cdp.call("Network.enable", timeout=10)
            except BrowserError:
                pass  # certaines versions l'exposent au niveau navigateur seulement

            probe: dict = {}
            deadline = started + timeout
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
                time.sleep(0.6)

            cookies = cdp.call("Network.getAllCookies", timeout=15).get("cookies", [])
            jar = _cookie_records(cookies, urlparse(url).netloc)
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
            page_ok = bool(probe.get("cards", 0) > 0) or bool(
                probe.get("app") and not probe.get("blocked")
            )
            solved = bool(jar) and page_ok
            return Harvest(
                ok=solved,
                cookies=jar,
                user_agent=user_agent,
                url=str(probe.get("url") or url),
                title=str(probe.get("title") or ""),
                source="browser",
                solved=solved,
                cards=int(probe.get("cards") or 0),
                elapsed_ms=int((time.monotonic() - started) * 1000),
                message=(
                    f"Session récupérée ({len(jar)} cookie(s), "
                    f"{probe.get('cards', 0)} annonce(s) visible(s))."
                    if solved
                    else "La vérification n'est pas terminée : terminez-la dans la fenêtre "
                    "ouverte, puis relancez le déblocage."
                ),
                cleared=sorted(n for n in jar if n.startswith(("cf_", "__cf", "datadome"))),
            )
        finally:
            if ws is not None:
                ws.close()
            _stop_process(process)


def harvest_with_browser(
    url: str,
    *,
    browser_path: str = "",
    profile_dir: str | Path | None = None,
    timeout: float = 60.0,
    headless: bool = False,
    on_log=None,
) -> Harvest:
    """Ouvre ``url`` dans un navigateur local et récupère cookies + User-Agent.

    Le navigateur reste **visible** par défaut : si Cloudflare demande une
    action (case à cocher, « maintenir le bouton »), l'utilisateur la fait et
    la session est récupérée dès que la page réelle apparaît.

    Trois tentatives au maximum, dans cet ordre :

    1. le navigateur détecté, avec le profil persistant (session réutilisable) ;
    2. le même, avec un profil **neuf** — cas d'un profil déjà verrouillé par
       une fenêtre restée ouverte : c'était la panne constatée en 1.3.7 ;
    3. les autres navigateurs installés (Chrome si Edge échoue, et inversement).
    """
    if not url.startswith(("http://", "https://")):
        url = "https://" + url.lstrip("/")
    log = on_log or (lambda message: None)
    base_profile = Path(
        profile_dir or Path(tempfile.gettempdir()) / "vinted-sniper-browser"
    )

    candidates = _browser_candidates(browser_path)
    if not candidates:
        raise BrowserError(
            "Aucun navigateur Chromium trouvé. Microsoft Edge (installé d'office "
            "sur Windows 10/11) ou Google Chrome suffit : installez-en un, ou "
            "indiquez son chemin exact dans Réglages → Déblocage Cloudflare."
        )

    #: Profil persistant (session réutilisée) puis profil système : le second
    #: passe même si le dossier de données est verrouillé (fenêtre restée
    #: ouverte) ou protégé par un antivirus.
    temp_profile = Path(tempfile.gettempdir()) / "vinted-sniper-browser"
    attempts: list[tuple[str, Path]] = []
    for executable in candidates[:2]:
        for profile in (base_profile, temp_profile):
            if (executable, profile) not in attempts:
                attempts.append((executable, profile))
    # Les échecs sont tous conservés : le message final doit dire quoi faire.
    failures: list[str] = []
    for index, (executable, profile) in enumerate(attempts, start=1):
        try:
            return _launch_once(
                executable, url, profile, headless=headless, timeout=timeout, log=log
            )
        except BrowserError as error:
            failures.append(f"{Path(executable).name} (essai {index}) : {error}")
            log(f"Essai {index} avec {Path(executable).name} : {error}")
            continue
    raise BrowserError(
        "Déblocage impossible.\n" + "\n".join(failures) + "\n"
        "À essayer : fermer toutes les fenêtres Edge/Chrome, puis relancer ; "
        "sinon indiquer un autre navigateur dans Réglages → Déblocage Cloudflare."
    )


# ── Secours : importer une session copiée du navigateur (cURL) ───────────────


_CURL_SPLIT = re.compile(r"""(?:"([^"]*)"|'([^']*)'|(\S+))""")


def _tokens(command: str) -> list[str]:
    """Découpe une commande cURL en respectant les guillemets et les ``^``."""
    flattened = re.sub(r"\\\r?\n", " ", command)   # continuation POSIX « \ »
    flattened = re.sub(r"\^\r?\n", " ", flattened)  # continuation cmd.exe « ^ »
    return [double or single or bare for double, single, bare in _CURL_SPLIT.findall(flattened)]


def session_from_curl(command: str) -> dict:
    """Extrait URL, cookies et User-Agent d'une commande cURL du navigateur.

    Secours universel quand le pilotage automatique est bloqué par une
    stratégie Windows : dans Edge ou Chrome, F12 → onglet Réseau → clic droit
    sur la requête ``catalog`` → **Copier → Copier en tant que cURL**. Cette
    commande contient déjà tout ce que Cloudflare a validé (cookies
    ``HttpOnly`` compris) et le User-Agent exact, qu'il faut réutiliser
    ensemble — sinon la clearance est refusée.

    Aucun réseau ici : uniquement de l'analyse de texte, donc testable.
    """
    tokens = _tokens(command or "")
    if not tokens or tokens[0].lower() not in {"curl", "curl.exe"}:
        raise ValueError(
            "Ce n'est pas une commande cURL : copiez la requête depuis l'onglet "
            "Réseau du navigateur (« Copier en tant que cURL »)."
        )
    url = ""
    headers: dict[str, str] = {}
    cookie_raw = ""
    index = 1
    while index < len(tokens):
        token = tokens[index]
        lowered = token.lower()
        if token.startswith(("http://", "https://")):
            url = token
        elif lowered in {"-h", "--header"} and index + 1 < len(tokens):
            index += 1
            name, _, value = tokens[index].partition(":")
            if name.strip() and value.strip():
                headers[name.strip().lower()] = value.strip()
        elif lowered in {"-b", "--cookie", "--cookie-jar"} and index + 1 < len(tokens):
            index += 1
            cookie_raw = tokens[index]
        elif lowered in {"-a", "--user-agent"} and index + 1 < len(tokens):
            index += 1
            headers["user-agent"] = tokens[index]
        elif lowered in {"-e", "--referer"} and index + 1 < len(tokens):
            index += 1
        index += 1

    if not url:
        raise ValueError("Aucune URL https://www.vinted.fr/… trouvée dans la commande.")
    raw = cookie_raw or headers.get("cookie", "")
    cookies: dict[str, str] = {}
    for part in raw.split(";"):
        name, _, value = part.strip().partition("=")
        if name.strip() and value:
            cookies[name.strip()] = value
    if not cookies:
        raise ValueError(
            "Aucun cookie dans la commande : recopiez-la depuis une requête du "
            "catalogue Vinted (les cookies y figurent)."
        )
    return {
        "url": url,
        "cookies": cookies,
        "user_agent": headers.get("user-agent", ""),
        "clearance": bool(cookies.get("cf_clearance") or cookies.get("cf_clearance_legacy")),
    }


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

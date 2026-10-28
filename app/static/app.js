/* ──────────────────────────────────────────────────────────────────────────
   Vinted Sniper — dashboard (vanilla JS, aucune dépendance, aucun build)
   ────────────────────────────────────────────────────────────────────────── */
(() => {
  "use strict";

  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));

  const state = {
    status: null,
    config: null,
    profiles: [],
    feed: [],
    logs: [],
    feedProfile: "all",
    feedSignature: "",
    feedFilterSignature: "",
    logSignature: "",
    offline: false,
    editingId: null,
    confirmHandler: null,
    busy: false,
    stream: null,
    streamState: "loading", // loading | live | offline
    streamItems: 0,
    lastEventAt: 0,
    streamRetry: 0,
    streamTimer: null,
    statusFailures: 0,
    blockBannerHiddenAt: 0,
    catTrail: [],      // [{path, name}]
    catChildren: [],
    catLoading: false,
    formCategory: { path: "/catalog", label: "Toutes les catégories" },
    formBrands: [],    // [{id, name}]
    formFilters: { size_ids: [], status_ids: [], color_ids: [], price_from: "", price_to: "", order: "" },
    filterCatalogue: null,
    brandRows: [],
    brandDraft: [],
    brandLetter: "A",
    brandLoading: false,
    brandIndex: { total: 0, updated_at: null },
    brandImporting: false,
    brandAutoImportFailed: false,
    brandAutoImportFailedAt: 0,
  };

  const LEVEL_LABELS = { INFO: "INFO", DEBUG: "DBG", WARNING: "WARN", ERROR: "ERR", SUCCESS: "OK" };

  /* ── Utilitaires ─────────────────────────────────────────────────────── */

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = String(text);
    return node;
  }

  function svgIcon(path) {
    const ns = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(ns, "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("width", "15");
    svg.setAttribute("height", "15");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    const p = document.createElementNS(ns, "path");
    p.setAttribute("d", path);
    svg.appendChild(p);
    return svg;
  }

  function iconButton(label, title, path, onClick, extraClass = "") {
    const button = el("button", `icon-btn ${extraClass}`.trim());
    button.type = "button";
    button.title = title;
    button.setAttribute("aria-label", title);
    button.appendChild(svgIcon(path));
    button.addEventListener("click", onClick);
    return button;
  }

  const PENCIL = "M12 20h9M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z";
  const COPY = "M8 8h11v11H8zM5 16H4V4h11v1";
  const TRASH = "M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14";
  const PLAY = "M7 4l13 8-13 8V4z";
  const EYE = "M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7Zm10 3a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z";
  const REFRESH = "M21 12a9 9 0 1 1-3-6.7M21 3v6h-6";
  const BOLT = "M13 2 4 14h7l-1 8 9-12h-7l1-8z";

  function relativeTime(iso) {
    if (!iso) return "jamais";
    const then = new Date(iso).getTime();
    if (Number.isNaN(then)) return "—";
    const seconds = Math.max(0, Math.round((Date.now() - then) / 1000));
    if (seconds < 10) return "à l'instant";
    if (seconds < 60) return `il y a ${seconds} s`;
    const minutes = Math.floor(seconds / 60);
    if (minutes < 60) return `il y a ${minutes} min`;
    const hours = Math.floor(minutes / 60);
    if (hours < 24) return `il y a ${hours} h`;
    const days = Math.floor(hours / 24);
    if (days < 7) return `il y a ${days} j`;
    return new Date(iso).toLocaleDateString("fr-FR", { day: "2-digit", month: "short" });
  }

  function humanDuration(seconds) {
    if (seconds === null || seconds === undefined) return "—";
    seconds = Math.max(0, Math.floor(seconds));
    if (seconds < 60) return `${seconds} s`;
    const minutes = Math.floor(seconds / 60);
    if (minutes < 60) return `${minutes} min`;
    const hours = Math.floor(minutes / 60);
    if (hours < 24) return `${hours} h ${String(minutes % 60).padStart(2, "0")}`;
    return `${Math.floor(hours / 24)} j ${hours % 24} h`;
  }

  function formatInterval(seconds) {
    const value = Number(seconds);
    if (!Number.isFinite(value) || value <= 0) return "—";
    if (value < 10) return `${value.toFixed(1)} s`;
    return `${Math.round(value)} s`;
  }

  function startCountdownTicker() {
    if (state.countdownTimer) return;
    state.countdownTimer = setInterval(() => {
      const now = Date.now();
      for (const node of $$("[data-countdown]")) {
        const base = Number(node.dataset.base || 0);
        const synced = Number(node.dataset.synced || 0);
        const left = base - (now - synced) / 1000;
        node.textContent = left > 0.05
          ? `prochain passage ${formatInterval(left)}`
          : "prochain passage · imminent";
      }
    }, 250);
  }

  function formatMoney(amount, currency) {
    if (amount === null || amount === undefined || Number.isNaN(Number(amount))) return "—";
    const value = Number(amount);
    const text = Number.isInteger(value)
      ? value.toLocaleString("fr-FR")
      : value.toLocaleString("fr-FR", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    const symbols = { EUR: "€", GBP: "£", USD: "$", CHF: "CHF", PLN: "zł", CZK: "Kč", SEK: "kr", DKK: "kr" };
    const symbol = symbols[(currency || "EUR").toUpperCase()];
    return symbol ? `${text} ${symbol}` : `${text} ${currency || ""}`.trim();
  }

  function stars(rating) {
    if (rating === null || rating === undefined) return "—";
    const value = Number(rating);
    const full = Math.floor(value);
    const half = value - full >= 0.5;
    return `${"★".repeat(full)}${half ? "½" : ""}${"☆".repeat(Math.max(0, 5 - full - (half ? 1 : 0)))} ${value.toFixed(1)}`;
  }

  function setStreamState(value) {
    if (state.streamState === value) return;
    state.streamState = value;
    const pill = $("#livePill");
    if (!pill) return;
    pill.classList.remove("is-loading", "is-live", "is-down");
    pill.classList.add(value === "live" ? "is-live" : value === "offline" ? "is-down" : "is-loading");
    $("#liveLabel").textContent = value === "live"
      ? "Temps réel"
      : value === "offline"
        ? "Flux interrompu"
        : "Connexion…";
  }

  function feedAccepts(profileId) {
    return state.feedProfile === "all" || String(profileId) === String(state.feedProfile);
  }

  function insertLiveItem(item, { silent = false } = {}) {
    if (!item || !item.item_id) return;
    state.streamItems += 1;
    state.lastEventAt = Date.now();
    if (!feedAccepts(item.profile_id)) return;
    const id = item.item_id;
    const index = state.feed.findIndex((row) => row.item_id === id);
    if (index >= 0) state.feed[index] = { ...state.feed[index], ...item };
    else state.feed.unshift(item);
    const limit = Math.max(12, Number((state.config && state.config.dashboard && state.config.dashboard.feed_size) || 60));
    state.feed = state.feed.slice(0, limit);
    state.feedSignature = "";           // force un nouveau rendu
    renderFeed();
    const card = document.querySelector(`.item-card[data-item="${id}"]`);
    if (card) {
      card.classList.add("is-fresh");
      setTimeout(() => card.classList.remove("is-fresh"), 2400);
    }
    if (silent) return;
    const price = formatMoney(item.price, item.currency);
    toast(`⚡ ${item.title || "Nouvelle annonce"} — ${price} · ${profileName(item.profile_id)}`, "success");
  }

  function pushLog(log) {
    if (!log || !log.id) return;
    if (state.logs.some((row) => row.id === log.id)) return;
    state.logs.unshift(log);
    if (state.logs.length > 120) state.logs.length = 120;
    renderLogs();
  }

  function updateLiveItem(item) {
    if (!item || !item.item_id) return;
    const index = state.feed.findIndex((row) => row.item_id === item.item_id);
    if (index < 0) return;
    state.feed[index] = { ...state.feed[index], ...item };
    state.feedSignature = "";
    renderFeed();
  }

  function scheduleReconnect() {
    if (state.streamTimer) return;
    const delay = Math.min(30000, 1500 * Math.pow(2, Math.min(state.streamRetry, 4)));
    state.streamRetry += 1;
    state.streamTimer = setTimeout(() => {
      state.streamTimer = null;
      connectStream();
    }, delay);
  }

  function connectStream() {
    if (typeof window.EventSource !== "function") {
      setStreamState("offline");
      return;
    }
    try {
      if (state.stream) {
        try { state.stream.close(); } catch (_) { /* déjà fermé */ }
      }
      const source = new window.EventSource("/api/stream");
      state.stream = source;
      source.addEventListener("hello", () => {
        state.streamRetry = 0;
        state.lastEventAt = Date.now();
        setStreamState("live");
      });
      /* Chien de garde : sans nouvelles du serveur, on relance le flux.
         Un onglet laissé ouvert après un redémarrage du bot restait sinon
         bloqué sur « Flux interrompu » alors que le serveur tournait. */
      source.addEventListener("ping", () => { state.lastEventAt = Date.now(); });
      source.addEventListener("item", (event) => {
        try {
          const payload = JSON.parse(event.data);
          insertLiveItem(payload.item, { silent: Boolean(payload.baseline) });
        } catch (_) { /* ignore */ }
        refreshStatus();
      });
      source.addEventListener("item_update", (event) => {
        try { updateLiveItem(JSON.parse(event.data).item); } catch (_) { /* ignore */ }
      });
      source.addEventListener("scan", () => { state.lastEventAt = Date.now(); });
      /* Journaux poussés par le serveur (aucune attente de poll). */
      source.addEventListener("log", (event) => {
        try { pushLog(JSON.parse(event.data)); } catch (_) { /* ignore */ }
      });
      source.addEventListener("blocked", (event) => {
        try {
          const data = JSON.parse(event.data);
          const reason = String(data.error || "");
          const interactive = /challenge-platform|captcha-delivery|just a moment|cf-chl/i.test(reason);
          const advice = interactive
            ? "vérification navigateur : le bot laisse l'IP respirer (1 à 5 min). Si ça dure, changez d'IP."
            : "nouvelle tentative automatique dans quelques secondes.";
          toast(`⚠ Blocage Vinted (profil ${data.profile_id}) — ${advice}`, "error");
        } catch (_) { /* ignore */ }
      });
      source.onerror = () => {
        setStreamState("offline");
        if (state.stream) {
          try { state.stream.close(); } catch (_) { /* ignoré */ }
          state.stream = null;
        }
        scheduleReconnect();
      };
    } catch (_) {
      setStreamState("offline");
    }
  }

  function toast(message, type = "info") {
    const node = el("div", `toast ${type}`, message);
    $("#toasts").appendChild(node);
    setTimeout(() => {
      node.style.opacity = "0";
      node.style.transition = "opacity .25s";
      setTimeout(() => node.remove(), 260);
    }, 4600);
  }

  async function api(path, options = {}) {
    const { timeoutMs, ...init } = options;
    let timer = null;
    let timedOut = false;
    if (timeoutMs && typeof window.AbortController === "function") {
      const controller = new window.AbortController();
      init.signal = controller.signal;
      timer = setTimeout(() => {
        timedOut = true;
        controller.abort();
      }, timeoutMs);
    }
    let response;
    try {
      response = await fetch(`/api${path}`, {
        headers: { "Content-Type": "application/json", ...(options.headers || {}) },
        ...init,
      });
    } catch (error) {
      if (timedOut) {
        throw new Error("Délai dépassé : la fenêtre du navigateur n'a pas répondu à temps.");
      }
      throw error;
    } finally {
      if (timer) clearTimeout(timer);
    }
    let data = null;
    try { data = await response.json(); } catch (_) { /* réponse vide */ }
    if (!response.ok) {
      let detail = data && (data.detail || data.error);
      if (Array.isArray(detail)) {
        detail = detail.map((item) => item.msg || JSON.stringify(item)).join(" · ");
      }
      throw new Error(detail || `Erreur HTTP ${response.status}`);
    }
    return data;
  }

  function openDialog(id) {
    const dialog = document.getElementById(id);
    if (dialog && !dialog.open) dialog.showModal();
  }
  function closeDialog(id) {
    const dialog = document.getElementById(id);
    if (dialog && dialog.open) dialog.close();
  }

  function nullableNumber(input) {
    const raw = input.value.trim().replace(",", ".");
    if (!raw) return null;
    const value = Number(raw);
    return Number.isFinite(value) ? value : null;
  }

  function splitTerms(value) {
    return value.split(/[\n,;]/).map((term) => term.trim()).filter(Boolean).slice(0, 60);
  }

  function profileName(profileId) {
    const profile = state.profiles.find((item) => item.id === profileId);
    return profile ? profile.name : `Profil #${profileId}`;
  }

  /* ── Rendu : barre supérieure & statistiques ─────────────────────────── */

  const CHALLENGE_RE = /challenge-platform|captcha-delivery|just a moment|cf-chl/i;

  /* Un blocage Cloudflare vient de l'IP : on l'affiche comme tel, avec la
     marche à suivre, au lieu de laisser croire que le bot est hors ligne. */
  function blockState(status) {
    const stats = (status && status.stats) || {};
    const reason = String(stats.last_error || "");
    /* L'âge vient du serveur : aucun décalage de fuseau horaire possible. */
    const age = typeof stats.block_age_seconds === "number"
      ? stats.block_age_seconds
      : Infinity;
    return {
      active: CHALLENGE_RE.test(reason) && age < 900,
      age,
      reason,
    };
  }

  function renderBlockBanner(status) {
    const banner = $("#blockBanner");
    if (!banner) return;
    const block = blockState(status);
    const hidden = Date.now() - state.blockBannerHiddenAt < 600000;
    banner.classList.toggle("hidden", !block.active || hidden);
    if (!block.active) return;
    const age = $("#blockBannerAge");
    if (age) {
      age.textContent = block.age < 120
        ? `Blocage détecté il y a ${Math.round(block.age)} s.`
        : `Blocage détecté il y a ${Math.round(block.age / 60)} min.`;
    }
  }

  function renderStatus(status) {
    state.status = status;
    const engine = $("#enginePill");
    const block = blockState(status);
    engine.classList.remove("is-loading", "is-paused", "is-down");
    if (block.active) {
      /* Le moteur tourne toujours : il attend simplement que l'IP revienne. */
      engine.classList.add("is-paused");
      $("#engineLabel").textContent = "Vérification Vinted";
    } else if (status.paused) {
      engine.classList.add("is-paused");
      $("#engineLabel").textContent = "En pause";
    } else {
      const realtime = status.realtime || {};
      $("#engineLabel").textContent = realtime.enabled
        ? `En veille · ${(realtime.live_profiles || []).length}⚡`
        : "En veille";
    }
    $("#pauseLabel").textContent = status.paused ? "Reprendre" : "Pause";
    $("#pauseIcon").textContent = status.paused ? "▶" : "❚❚";
    $("#versionLabel").textContent = `v${status.version || ""}`.trim();

    const stats = status.stats || {};
    const counts = status.counts || {};
    const pool = (status.http && status.http.proxy_pool) || {};

    $("#statProfiles").textContent = status.profiles_active ?? "—";
    $("#statProfilesSub").textContent = `${status.profiles_total ?? 0} profils · ${(status.inflight || []).length} en cours`;
    $("#statToday").textContent = counts.today ?? 0;
    $("#statTodaySub").textContent = `${counts.total ?? 0} annonces suivies`;
    $("#statAlerts").textContent = counts.notified ?? 0;
    $("#statAlertsSub").textContent = `${stats.alerts_sent ?? 0} cette session`;
    $("#statLastScan").textContent = relativeTime(stats.last_scan_at);
    const latency = stats.last_detection_ms;
    $("#statLastScanSub").textContent = latency
      ? `⚡ ${(latency / 1000).toFixed(2)} s de détection · ${stats.scans ?? 0} scans`
      : `${stats.scans ?? 0} scans · ${stats.scans_failed ?? 0} échecs`;
    $("#statBlocks").textContent = stats.blocked ?? 0;
    $("#statBlocksSub").textContent = pool.enabled
      ? `${pool.available ?? 0}/${pool.total ?? 0} proxys disponibles`
      : "rotation de proxys désactivée";

    $("#uptimeChip").textContent = status.uptime_human || "—";
    $("#ctlScans").textContent = stats.scans ?? 0;
    $("#ctlNew").textContent = stats.new_items ?? 0;
    $("#ctlFailed").textContent = stats.alerts_failed ?? 0;
    $("#ctlTransport").textContent = status.transport || "—";
    $("#ctlDb").textContent = `${Math.max(1, Math.round((status.db_size || 0) / 1024))} Ko`;

    const cookies = Object.entries((status.http && status.http.cookies) || {});
    const cookieCount = cookies.reduce((sum, [, list]) => sum + list.length, 0);
    $("#cookieState").textContent = cookieCount
      ? `${cookieCount} cookie(s) sur ${cookies.length} domaine(s)`
      : "aucune session";

    $("#proxyChip").textContent = pool.enabled ? "Activés" : "Désactivés";
    $("#proxyChip").className = `chip ${pool.enabled ? "chip-green" : "chip-muted"}`;
    $("#proxyAvailable").textContent = `${pool.available ?? 0} / ${pool.total ?? 0}`;
    $("#proxyQuarantined").textContent = pool.quarantined ?? 0;

    const banner = $("#alertBanner");
    if (banner) banner.classList.toggle("hidden", status.webhook_configured !== false);
    const quick = $("#quickStart");
    if (quick) quick.classList.toggle("hidden", (status.profiles_total || 0) > 0);
    renderBlockBanner(status);

    const nextHint = Object.values(status.next_runs || {});
    const soonest = nextHint.length ? Math.min(...nextHint) : null;
    $("#ctlScans").title = soonest !== null ? `Prochain scan dans ${humanDuration(soonest)}` : "";
  }

  function renderOffline() {
    const engine = $("#enginePill");
    engine.classList.remove("is-loading", "is-paused");
    engine.classList.add("is-down");
    $("#engineLabel").textContent = "Hors ligne";
    if (!state.offline) {
      state.offline = true;
      toast("Connexion au serveur perdue — nouvelle tentative…", "error");
    }
  }

  /* ── Rendu incrémental ───────────────────────────────────────────────── */

  /* Ne recrée que les cartes qui ont réellement changé.
     Avant, chaque rafraîchissement (3 à 4 s) vidait la grille et la
     reconstruisait : les animations rejouaient et le scroll sautait. */
  function patchKeyed(container, items, keyOf, signatureOf, render) {
    const existing = new Map();
    for (const node of [...container.children]) {
      const key = node.dataset ? node.dataset.key : "";
      if (key) existing.set(key, node);
      else node.remove();
    }
    const seen = new Set();
    items.forEach((item, index) => {
      const key = String(keyOf(item));
      const signature = String(signatureOf(item));
      seen.add(key);
      let node = existing.get(key);
      if (!node || node.dataset.sig !== signature) {
        const fresh = render(item);
        fresh.dataset.key = key;
        fresh.dataset.sig = signature;
        if (node) {
          node.replaceWith(fresh);
        } else {
          fresh.classList.add("is-new");
          container.insertBefore(fresh, container.children[index] || null);
        }
        node = fresh;
      }
      const anchor = container.children[index] || null;
      if (node !== anchor) container.insertBefore(node, anchor);
    });
    for (const node of [...container.children]) {
      if (node.dataset && node.dataset.key && !seen.has(node.dataset.key)) node.remove();
    }
  }

  /* Champs visibles d'un profil : le compte à rebours (seconds_to_next) est
     volontairement exclu, sinon la carte serait recréée à chaque seconde. */
  function profileSignature(profile) {
    return JSON.stringify([
      profile.name, profile.active, profile.url, profile.category, profile.brands,
      profile.interval_seconds, profile.live_mode, profile.min_price, profile.max_price,
      profile.pages, profile.whitelist, profile.blacklist, profile.keyword_mode,
      profile.min_seller_rating, profile.min_seller_feedback, profile.webhook_masked,
      profile.last_run_at, profile.last_error, profile.scan_count, profile.found_count,
      profile.running,
    ]);
  }

  function feedItemSignature(item) {
    return JSON.stringify([
      item.title, item.price, item.currency, item.image_url, item.brand, item.size,
      item.condition, item.seller_name, item.seller_rating, item.seller_feedback,
      item.favourites, item.url, item.found_at,
    ]);
  }

  /* ── Rendu : profils ─────────────────────────────────────────────────── */

  function searchSummary(rawUrl) {
    if (!rawUrl) return { host: "vinted.fr", query: "Recherche vide" };
    try {
      const url = new URL(rawUrl.startsWith("http") ? rawUrl : `https://${rawUrl}`);
      const text = url.searchParams.get("search_text");
      const query = text
        || (url.pathname && url.pathname !== "/catalog" ? decodeURIComponent(url.pathname) : "Catalogue complet");
      return { host: url.hostname, query };
    } catch (_) {
      return { host: "vinted.fr", query: rawUrl };
    }
  }

  function profileCard(profile) {
    const card = el("article", "profile-card");
    card.classList.toggle("is-off", !profile.active);
    card.classList.toggle("is-scanning", Boolean(profile.running));
    card.dataset.id = profile.id;

    /* En-tête */
    const top = el("div", "profile-top");
    const title = el("div", "profile-title");
    title.appendChild(el("span", "dot"));
    title.appendChild(el("h3", "", profile.name));
    top.appendChild(title);

    const actions = el("div", "profile-actions");
    const toggle = el("input", "switch");
    toggle.type = "checkbox";
    toggle.checked = Boolean(profile.active);
    toggle.title = profile.active ? "Désactiver le profil" : "Activer le profil";
    toggle.setAttribute("aria-label", toggle.title);
    toggle.addEventListener("change", async () => {
      toggle.disabled = true;
      try {
        const result = await api(`/profiles/${profile.id}/toggle`, {
          method: "POST",
          body: JSON.stringify({ active: toggle.checked }),
        });
        toast(`Profil « ${result.profile.name} » ${toggle.checked ? "activé" : "désactivé"}.`, "success");
        await refreshProfiles();
      } catch (error) {
        toggle.checked = !toggle.checked;
        toast(error.message, "error");
      } finally {
        toggle.disabled = false;
      }
    });
    actions.appendChild(toggle);
    actions.appendChild(iconButton("Modifier", "Modifier le profil", PENCIL, () => openProfileModal(profile)));
    top.appendChild(actions);
    card.appendChild(top);

    /* URL */
    const summary = searchSummary(profile.url);
    const urlRow = el("div", "profile-url");
    urlRow.appendChild(el("span", "host", summary.host.replace(/^www\./, "")));
    urlRow.appendChild(el("span", "", summary.query));
    urlRow.title = profile.url || "Aucune URL configurée";
    card.appendChild(urlRow);
    if (profile.category) {
      const categoryRow = el("div", "profile-category");
      const chip = el("span", "meta-tag", `📂 ${profile.category}`);
      chip.title = "Catégorie surveillée";
      categoryRow.appendChild(chip);
      if (profile.url && profile.url.startsWith("http")) {
        const open = el("a", "meta-tag open-link", "Ouvrir sur Vinted ↗");
        open.href = profile.url;
        open.target = "_blank";
        open.rel = "noopener noreferrer";
        categoryRow.appendChild(open);
      }
      card.appendChild(categoryRow);
    }
    if (profile.brands) {
      const brandRow = el("div", "profile-category");
      const chip = el("span", "meta-tag", `🏷️ ${profile.brands}`);
      chip.title = "Marques filtrées";
      brandRow.appendChild(chip);
      card.appendChild(brandRow);
    }

    /* Métadonnées */
    const meta = el("div", "profile-meta");
    const priceText = profile.min_price !== null || profile.max_price !== null
      ? `${profile.min_price !== null ? formatMoney(profile.min_price, "EUR") : "0 €"} – ${profile.max_price !== null ? formatMoney(profile.max_price, "EUR") : "∞"}`
      : "Tous les prix";
    meta.appendChild(el("span", "meta-tag", `💰 ${priceText}`));
    if (profile.live_mode) {
      const live = el("span", "meta-tag live", `⚡ ${formatInterval(profile.poll_interval)}`);
      live.title = "Suivi continu : une annonce publiée est détectée en quelques secondes";
      meta.appendChild(live);
      const countdown = el("span", "meta-tag countdown");
      countdown.dataset.countdown = String(profile.id);
      countdown.dataset.base = String(profile.seconds_to_next ?? 0);
      countdown.dataset.synced = String(Date.now());
      countdown.textContent = `prochain passage ${formatInterval(profile.seconds_to_next)}`;
      meta.appendChild(countdown);
    } else {
      meta.appendChild(el("span", "meta-tag", `⏱ ${profile.interval_seconds}s · ${profile.pages} page${profile.pages > 1 ? "s" : ""}`));
    }
    if (profile.pages > 1) meta.appendChild(el("span", "meta-tag", `📄 ${profile.pages} pages`));
    if (profile.throttle && profile.throttle > 1.05) {
      const slow = el("span", "meta-tag warn", `🐢 ralenti ×${profile.throttle.toFixed(1)}`);
      slow.title = "Vinted a bloqué des requêtes : le moteur espace automatiquement les passages, puis revient à la vitesse normale.";
      meta.appendChild(slow);
    }
    if ((profile.whitelist || []).length) meta.appendChild(el("span", "meta-tag", `✅ ${profile.whitelist.length} mot(s) requis`));
    if ((profile.blacklist || []).length) meta.appendChild(el("span", "meta-tag", `🚫 ${profile.blacklist.length} mot(s) bannis`));
    if (profile.min_seller_rating !== null || profile.min_seller_feedback !== null) {
      const bits = [];
      if (profile.min_seller_rating !== null) bits.push(`★ ≥ ${profile.min_seller_rating}`);
      if (profile.min_seller_feedback !== null) bits.push(`≥ ${profile.min_seller_feedback} avis`);
      meta.appendChild(el("span", "meta-tag", `👤 ${bits.join(" · ")}`));
    }
    meta.appendChild(el("span", "meta-tag", profile.webhook_masked ? "🔔 webhook dédié" : (profile.effective_webhook ? "🔔 webhook global" : "🔕 sans webhook")));
    if (profile.last_error) {
      const warning = el("span", "meta-tag warn", `⚠ ${profile.last_error.slice(0, 46)}`);
      warning.title = profile.last_error;
      meta.appendChild(warning);
    }
    card.appendChild(meta);

    /* Pied */
    const foot = el("div", "profile-foot");
    const times = el("div", "profile-times");
    const last = el("span");
    last.append("Dernier scan : ");
    last.append(el("b", "", relativeTime(profile.last_run_at)));
    times.appendChild(last);
    const stats = el("span");
    stats.append(`${profile.scan_count} scan(s) · `);
    stats.append(el("b", "", `${profile.found_count} trouvée(s)`));
    times.appendChild(stats);
    foot.appendChild(times);

    const buttons = el("div", "btn-row");
    const scanButton = el("button", "btn btn-sm btn-ghost");
    scanButton.type = "button";
    scanButton.disabled = Boolean(profile.running) || !profile.url;
    scanButton.appendChild(svgIcon(PLAY));
    scanButton.append(profile.running ? " Scan…" : " Scanner");
    scanButton.addEventListener("click", () => scanNow(profile, scanButton));
    buttons.appendChild(scanButton);

    const previewButton = el("button", "btn btn-sm btn-ghost");
    previewButton.type = "button";
    previewButton.title = "Tester les filtres sur les annonces en ligne";
    previewButton.appendChild(svgIcon(EYE));
    previewButton.append(" Aperçu");
    previewButton.disabled = !profile.url;
    previewButton.addEventListener("click", () => openPreview(profile));
    buttons.appendChild(previewButton);

    buttons.appendChild(iconButton("Dupliquer", "Dupliquer le profil", COPY, () => duplicateProfile(profile)));
    buttons.appendChild(iconButton("Supprimer", "Supprimer le profil", TRASH,
      () => deleteProfile(profile), "danger"));
    foot.appendChild(buttons);
    card.appendChild(foot);
    return card;
  }

  function renderProfiles() {
    const grid = $("#profilesGrid");
    patchKeyed(grid, state.profiles, (profile) => profile.id, profileSignature, profileCard);
    // Le compte à rebours évolue en continu : on le recale sans toucher au DOM.
    for (const profile of state.profiles) {
      const node = grid.querySelector(`[data-countdown="${profile.id}"]`);
      if (!node) continue;
      const base = Number(profile.seconds_to_next ?? 0);
      const synced = Number(node.dataset.synced || 0);
      const left = Number(node.dataset.base || 0) - (Date.now() - synced) / 1000;
      if (Math.abs(left - base) > 1.2) {
        node.dataset.base = String(base);
        node.dataset.synced = String(Date.now());
      }
    }
    $("#profilesEmpty").classList.toggle("hidden", state.profiles.length > 0);
    $("#profilesCount").textContent = `${state.profiles.filter((p) => p.active).length} actif(s) / ${state.profiles.length}`;
    renderFeedFilter();
  }

  function renderFeedFilter() {
    const select = $("#feedFilter");
    const signature = state.profiles.map((p) => `${p.id}:${p.name}`).join("|");
    if (signature === state.feedFilterSignature) return;
    state.feedFilterSignature = signature;
    const current = state.feedProfile;
    select.replaceChildren();
    const all = new Option("Tous les profils", "all");
    select.appendChild(all);
    for (const profile of state.profiles) {
      select.appendChild(new Option(profile.name, String(profile.id)));
    }
    select.value = current;
    if (select.value !== current) {
      select.value = "all";
      state.feedProfile = "all";
    }
  }

  /* ── Rendu : flux ────────────────────────────────────────────────────── */

  function sellerLink(item, className = "seller-name") {
    const name = item.seller_name ? `@${item.seller_name}` : "Vendeur inconnu";
    if (!item.seller_url) return el("span", className, name);
    const link = el("a", className, name);
    link.href = item.seller_url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.title = "Ouvrir le profil du vendeur sur Vinted";
    return link;
  }

  function itemCard(item) {
    const card = el("article", "item-card");
    card.dataset.item = item.item_id || item.id || "";
    const href = item.url || "#";
    const label = item.title || "Annonce Vinted";

    /* Photo cliquable → annonce */
    const media = el("a", "item-media");
    media.href = href;
    media.target = "_blank";
    media.rel = "noopener noreferrer";
    media.title = item.description ? `${label}\n\n${item.description}` : label;
    const fallback = el("div", "fallback", (item.brand || "V").slice(0, 2).toUpperCase());
    media.appendChild(fallback);
    if (item.image_url) {
      const img = new Image();
      img.alt = label;
      img.loading = "lazy";
      img.referrerPolicy = "no-referrer";
      img.addEventListener("load", () => fallback.remove());
      img.addEventListener("error", () => img.remove());
      img.src = item.image_url;
      media.appendChild(img);
    }
    if (item.found_at && (Date.now() - new Date(item.found_at).getTime()) < 10 * 60 * 1000) {
      media.appendChild(el("span", "new-tag", "NOUVEAU"));
    }
    media.appendChild(el("span", "price-tag", formatMoney(item.price, item.currency)));
    card.appendChild(media);

    /* Corps */
    const body = el("div", "item-body");
    const title = el("a", "item-title", label);
    title.href = href;
    title.target = "_blank";
    title.rel = "noopener noreferrer";
    body.appendChild(title);

    const tags = el("div", "item-tags");
    if (item.brand) tags.appendChild(el("span", "item-tag", item.brand));
    if (item.size) tags.appendChild(el("span", "item-tag", `T. ${item.size}`));
    if (item.condition) tags.appendChild(el("span", "item-tag", item.condition));
    body.appendChild(tags);

    const seller = el("div", "item-seller");
    seller.appendChild(sellerLink(item));
    const rating = el("span", "seller-rating");
    if (item.seller_rating !== null && item.seller_rating !== undefined) {
      rating.append(`★ ${Number(item.seller_rating).toFixed(1)}`);
      if (item.seller_feedback !== null && item.seller_feedback !== undefined) {
        rating.appendChild(el("small", "", ` · ${item.seller_feedback} avis`));
      }
    } else {
      rating.append("—");
    }
    rating.title = `${stars(item.seller_rating)} — ${item.seller_feedback ?? "?"} avis`;
    seller.appendChild(rating);
    body.appendChild(seller);

    const foot = el("div", "item-foot");
    foot.appendChild(el("span", "profile-chip", item.profile_name || profileName(item.profile_id)));
    const open = el("a", "item-open", "Voir l'annonce ↗");
    open.href = href;
    open.target = "_blank";
    open.rel = "noopener noreferrer";
    open.title = href;
    foot.appendChild(open);
    const time = el("time", "", relativeTime(item.found_at));
    time.dataset.found = item.found_at || "";
    if (item.notified === 0 && item.notify_error) {
      time.classList.add("unnotified");
      time.title = `Notification : ${item.notify_error}`;
    }
    foot.appendChild(time);
    body.appendChild(foot);
    card.appendChild(body);
    return card;
  }

  function renderFeed() {
    const grid = $("#feedGrid");
    patchKeyed(
      grid,
      state.feed,
      (item) => item.item_id || item.id,
      feedItemSignature,
      itemCard,
    );
    for (const time of $$("time[data-found]", grid)) {
      time.textContent = relativeTime(time.dataset.found);
    }
    $("#feedEmpty").classList.toggle("hidden", state.feed.length > 0);
    $("#feedCount").textContent = `${state.feed.length} annonce(s)`;
  }

  /* ── Rendu : journal ─────────────────────────────────────────────────── */

  function logLine(log) {
    const line = el("div", `log-line ${log.level}`);
    const date = new Date(log.ts);
    line.appendChild(el("span", "log-time",
      Number.isNaN(date.getTime()) ? "--:--:--" : date.toLocaleTimeString("fr-FR")));
    line.appendChild(el("span", "log-level", LEVEL_LABELS[log.level] || log.level));
    line.appendChild(el("span", "log-msg", log.message));
    line.title = `${log.source || "engine"}${log.profile_id ? ` · profil #${log.profile_id}` : ""} — ${log.ts}`;
    return line;
  }

  function renderLogs() {
    const signature = state.logs.map((log) => log.id).join(",");
    if (signature === state.logSignature) return;
    state.logSignature = signature;
    const list = $("#logList");
    if (!state.logs.length) {
      list.replaceChildren();
      list.appendChild(el("div", "hint", "Aucun événement pour le moment."));
      return;
    }
    // Une seule ligne insérée par nouvel événement (au lieu de 120 reconstruites).
    patchKeyed(
      list,
      state.logs,
      (log) => log.id,
      (log) => `${log.level}|${log.ts}|${log.message}`,
      logLine,
    );
  }

  /* ── Rendu : réglages ────────────────────────────────────────────────── */

  function fillSettings(config) {
    const engine = config.engine || {};
    const http = config.http || {};
    const proxies = config.proxies || {};
    const discord = config.discord || {};
    const notifications = config.notifications || {};
    $("#cfgInterval").value = engine.default_interval_seconds ?? 60;
    $("#cfgLive").checked = engine.live_mode !== false;
    $("#cfgTurbo").checked = Boolean(engine.realtime_turbo);
    $("#cfgRealtimeMin").value = engine.realtime_min_interval ?? 1.5;
    $("#cfgRealtimeMax").value = engine.realtime_max_interval ?? 10;
    $("#cfgDelay").value = engine.min_request_delay ?? 2;
    $("#cfgConcurrency").value = engine.max_concurrent_profiles ?? 2;
    $("#cfgPerPage").value = engine.max_items_per_page ?? 96;
    $("#cfgWebhook").value = discord.default_webhook || "";
    $("#cfgMention").value = discord.mention || "";
    $("#cfgNotifications").checked = notifications.enabled !== false;
    $("#cfgProxies").checked = Boolean(proxies.enabled);
    $("#cfgPreferProxies").checked = Boolean(proxies.prefer_proxies);
    $("#cfgAutoDiscover").checked = proxies.auto_discover !== false;
    $("#cfgBaseline").checked = engine.baseline_first_scan !== false;
    $("#cfgProxyList").value = (proxies.list || []).join("\n");
    const challenge = config.challenge || {};
    if ($("#cfgBrowserPath")) $("#cfgBrowserPath").value = challenge.browser_path || "";
    if ($("#cfgSolverUrl")) $("#cfgSolverUrl").value = challenge.solver_url || "";
    if ($("#cfgHeadless")) $("#cfgHeadless").checked = Boolean(challenge.headless);
    void http;
  }

  async function saveSettings(event) {
    event.preventDefault();
    const button = $("#settingsForm button[type=submit]");
    button.disabled = true;
    try {
      await api("/config", {
        method: "PUT",
        body: JSON.stringify({
          patch: {
            engine: {
              default_interval_seconds: Math.max(1, Number($("#cfgInterval").value) || 60),
              live_mode: $("#cfgLive").checked,
              realtime_turbo: $("#cfgTurbo").checked,
              realtime_min_interval: Number($("#cfgRealtimeMin").value) || 1.5,
              realtime_max_interval: Number($("#cfgRealtimeMax").value) || 10,
              min_request_delay: Number($("#cfgDelay").value),
              max_concurrent_profiles: Number($("#cfgConcurrency").value),
              max_items_per_page: Number($("#cfgPerPage").value),
              baseline_first_scan: $("#cfgBaseline").checked,
            },
            notifications: { enabled: $("#cfgNotifications").checked },
            discord: {
              default_webhook: $("#cfgWebhook").value.trim(),
              mention: $("#cfgMention").value.trim(),
            },
            challenge: {
              browser_path: $("#cfgBrowserPath") ? $("#cfgBrowserPath").value.trim() : "",
              solver_url: $("#cfgSolverUrl") ? $("#cfgSolverUrl").value.trim() : "",
              headless: $("#cfgHeadless") ? $("#cfgHeadless").checked : false,
            },
            proxies: {
              enabled: $("#cfgProxies").checked,
              prefer_proxies: $("#cfgPreferProxies").checked,
              auto_discover: $("#cfgAutoDiscover").checked,
              list: $("#cfgProxyList").value.split(/\n|,/).map((v) => v.trim()).filter(Boolean),
            },
          },
        }),
      });
      toast("Réglages enregistrés.", "success");
      await refreshConfig();
    } catch (error) {
      toast(error.message, "error");
    } finally {
      button.disabled = false;
    }
  }

  /* ── Modale profil ───────────────────────────────────────────────────── */

  function toggleIntervalField() {
    const live = $("#pLiveMode").checked;
    const field = $("#pIntervalField");
    if (field) field.classList.toggle("is-muted", live);
    const input = $("#pInterval");
    if (input) input.disabled = false;
  }

  function openProfileModal(profile = null) {
    state.editingId = profile ? profile.id : null;
    $("#profileModalTitle").textContent = profile ? `Modifier « ${profile.name} »` : "Nouveau profil";
    $("#profileError").textContent = "";
    $("#pName").value = profile ? profile.name : "";
    $("#pActive").checked = profile ? Boolean(profile.active) : true;
    $("#pUrl").value = profile ? profile.url : "";
    $("#pInterval").value = profile ? profile.interval_seconds : 60;
    $("#pLiveMode").checked = profile ? Boolean(profile.live_mode) : true;
    toggleIntervalField();
    const category = profile
      ? categoryFromUrl(profile.url, profile.category || "")
      : { path: "/catalog", label: "Toutes les catégories" };
    state.formCategory = category;
    syncCategoryPill(category);
    const brandRows = profile ? brandsFromUrl(profile.url, profile.brands || "") : [];
    state.formBrands = brandRows;
    syncBrandsPill();
    state.formFilters = filtersFromUrl(profile ? profile.url : "");
    renderFilterPanel();
    ensureFilterCatalogue().then(() => renderFilterPanel());
    $("#pPages").value = profile ? profile.pages : 1;
    $("#pMinPrice").value = profile && profile.min_price !== null ? profile.min_price : "";
    $("#pMaxPrice").value = profile && profile.max_price !== null ? profile.max_price : "";
    $("#pWhitelist").value = profile ? (profile.whitelist || []).join("\n") : "";
    $("#pBlacklist").value = profile ? (profile.blacklist || []).join("\n") : "";
    $("#pKeywordMode").value = profile ? profile.keyword_mode : "any";
    $("#pCheckDescription").checked = profile ? Boolean(profile.check_description) : true;
    $("#pMinRating").value = profile && profile.min_seller_rating !== null ? profile.min_seller_rating : "";
    $("#pMinFeedback").value = profile && profile.min_seller_feedback !== null ? profile.min_seller_feedback : "";
    $("#pWebhook").value = profile ? profile.webhook || "" : "";
    $("#pNotes").value = profile ? profile.notes || "" : "";
    const clearButton = $("#pClearSeen");
    clearButton.classList.toggle("hidden", !profile);
    clearButton.onclick = profile ? () => clearSeen(profile) : null;
    openDialog("profileModal");
    setTimeout(() => $("#pName").focus(), 60);
  }

  /* Démarrage express : un mot-clé suffit pour créer un profil complet
     (temps réel activé, une page, prix max optionnel, webhook optionnel). */
  async function submitQuickStart(event) {
    event.preventDefault();
    const query = ($("#qsQuery").value || "").trim();
    const errorBox = $("#qsError");
    if (errorBox) errorBox.textContent = "";
    if (!query) {
      if (errorBox) errorBox.textContent = "Indiquez au moins un mot-clé (ex. « nike tech »).";
      return;
    }
    const maxPrice = nullableNumber($("#qsMaxPrice"));
    const webhook = ($("#qsWebhook").value || "").trim();
    const button = $("#qsSubmit");
    button.disabled = true;
    button.textContent = "Création…";
    try {
      await api("/profiles", {
        method: "POST",
        body: JSON.stringify({
          name: query.slice(0, 60),
          active: true,
          url: query,
          live_mode: true,
          interval_seconds: 1,
          pages: 1,
          max_price: maxPrice,
          webhook,
          check_description: true,
        }),
      });
      if (errorBox) errorBox.textContent = "";
      $("#qsQuery").value = "";
      $("#qsMaxPrice").value = "";
      $("#qsWebhook").value = "";
      toast("C'est parti : première détection dans quelques secondes.", "success");
      await Promise.all([refreshProfiles(), refreshStatus(), refreshFeed(), refreshLogs()]);
    } catch (error) {
      if (errorBox) errorBox.textContent = error.message;
    } finally {
      button.disabled = false;
      button.textContent = "🚀 Démarrer le snipe";
    }
  }

  async function submitProfile(event) {
    event.preventDefault();
    const category = state.formCategory || { path: "/catalog", label: "" };
    const hasCategory = category.path && category.path !== "/catalog";
    const brands = state.formBrands || [];
    if (hasCategory || brands.length || filterCount(state.formFilters)) rebuildFormUrl();
    const payload = {
      name: $("#pName").value.trim(),
      active: $("#pActive").checked,
      url: $("#pUrl").value.trim(),
      category: hasCategory ? category.label : "",
      brands: brands.length ? brands.map((row) => row.name).join(", ") : "",
      interval_seconds: Math.max(1, Number($("#pInterval").value) || 60),
      live_mode: $("#pLiveMode").checked,
      pages: Number($("#pPages").value) || 1,
      min_price: nullableNumber($("#pMinPrice")),
      max_price: nullableNumber($("#pMaxPrice")),
      whitelist: splitTerms($("#pWhitelist").value),
      blacklist: splitTerms($("#pBlacklist").value),
      keyword_mode: $("#pKeywordMode").value,
      check_description: $("#pCheckDescription").checked,
      min_seller_rating: nullableNumber($("#pMinRating")),
      min_seller_feedback: nullableNumber($("#pMinFeedback")),
      webhook: $("#pWebhook").value.trim(),
      notes: $("#pNotes").value.trim(),
    };
    const errorBox = $("#profileError");
    errorBox.textContent = "";
    if (!payload.name) { errorBox.textContent = "Le nom du profil est obligatoire."; return; }
    if (payload.min_price !== null && payload.max_price !== null && payload.min_price > payload.max_price) {
      errorBox.textContent = "Le prix minimum doit être inférieur au prix maximum.";
      return;
    }
    const button = $("#profileSubmit");
    button.disabled = true;
    button.textContent = "Enregistrement…";
    try {
      if (state.editingId) {
        await api(`/profiles/${state.editingId}`, { method: "PUT", body: JSON.stringify(payload) });
        toast("Profil mis à jour.", "success");
      } else {
        await api("/profiles", { method: "POST", body: JSON.stringify(payload) });
        toast("Profil créé. Il sera scanné sous quelques secondes.", "success");
      }
      closeDialog("profileModal");
      await refreshProfiles();
      await refreshStatus();
    } catch (error) {
      errorBox.textContent = error.message;
    } finally {
      button.disabled = false;
      button.textContent = "Enregistrer";
    }
  }

  /* ── Catégories Vinted ──────────────────────────────────────────────── */

  function profileDomainFromForm() {
    const raw = ($("#pUrl").value || "").trim();
    const match = raw.match(/^https?:\/\/([^/]+)/i);
    return match ? match[1].toLowerCase() : "www.vinted.fr";
  }

  function currentCategoryPath() {
    const trail = state.catTrail;
    return trail.length ? trail[trail.length - 1].path : "/catalog";
  }

  function currentCategoryName() {
    const trail = state.catTrail;
    return trail.length ? trail[trail.length - 1].name : "Toutes les catégories";
  }

  function renderCategoryTrail() {
    const box = $("#catBreadcrumb");
    box.replaceChildren();
    const root = el("button", "", "Toutes les catégories");
    root.type = "button";
    root.addEventListener("click", () => goCategory("/catalog"));
    box.appendChild(root);
    state.catTrail.forEach((node, index) => {
      box.appendChild(el("span", "sep", "›"));
      if (index === state.catTrail.length - 1) {
        box.appendChild(el("span", "", node.name));
        return;
      }
      const link = el("button", "", node.name);
      link.type = "button";
      link.addEventListener("click", () => {
        state.catTrail = state.catTrail.slice(0, index + 1);
        loadCategories(node.path, node.name);
      });
      box.appendChild(link);
    });
    $("#catSelected").textContent = state.catTrail.length
      ? `Sélection : ${currentCategoryName()}`
      : "Aucune catégorie choisie (toutes les annonces)";
    $("#catChoose").textContent = state.catTrail.length
      ? `Choisir « ${currentCategoryName()} »`
      : "Chercher dans toutes les catégories";
  }

  function renderCategoryList() {
    const list = $("#catList");
    const filter = ($("#catFilter").value || "").trim().toLowerCase();
    list.replaceChildren();
    if (state.catLoading) {
      list.appendChild(el("p", "cat-empty", "Lecture des catégories sur Vinted…"));
      return;
    }
    const rows = state.catChildren.filter((row) => !filter || row.name.toLowerCase().includes(filter));
    if (!rows.length) {
      list.appendChild(el("p", "cat-empty", filter
        ? "Aucune catégorie ne correspond au filtre."
        : "Cette catégorie n'a pas de sous-catégorie : vous pouvez la choisir telle quelle."));
      return;
    }
    for (const row of rows) {
      const button = el("button", "cat-item");
      button.type = "button";
      button.dataset.path = row.path;
      button.appendChild(el("span", "", row.name));
      button.appendChild(el("span", "chev", "›"));
      button.addEventListener("click", () => enterCategory(row));
      list.appendChild(button);
    }
  }

  function enterCategory(row) {
    state.formCategory = { path: row.path, label: row.name };
    state.catTrail.push({ path: row.path, name: row.name });
    renderCategoryTrail();
    loadCategories(row.path, row.name);
  }

  function goCategory(path, name = "Toutes les catégories") {
    state.formCategory = { path, label: name };
    state.catTrail = path === "/catalog" ? [] : [{ path, name }];
    renderCategoryTrail();
    loadCategories(path, name);
  }

  async function loadCategories(path, name = "") {
    state.catLoading = true;
    renderCategoryList();
    const domain = profileDomainFromForm();
    try {
      const data = await api(`/categories?path=${encodeURIComponent(path)}&domain=${encodeURIComponent(domain)}`);
      state.catChildren = data.children || [];
      $("#catSub").textContent = data.source === "vinted"
        ? `Sous-catégories de « ${data.title || name} » lues sur ${domain}`
        : "Grandes catégories Vinted — cliquez pour explorer";
      $("#catNote").textContent = data.source === "vinted" && !state.catChildren.length
        ? "Dernier niveau : les annonces de cette catégorie seront surveillées."
        : "";
    } catch (error) {
      state.catChildren = [];
      $("#catNote").textContent = `Impossible de lire les sous-catégories : ${error.message}`;
    } finally {
      state.catLoading = false;
      renderCategoryList();
      renderCategoryTrail();
    }
  }

  function openCategoryBrowser() {
    state.catChildren = [];
    const current = categoryFromUrl($("#pUrl").value, state.formCategory.label);
    selectCategory(current, { updateUrl: false });
    if (current.path && current.path !== "/catalog") {
      state.catTrail = [{ path: current.path, name: current.label }];
    }
    $("#catFilter").value = "";
    $("#catSub").textContent = "Grandes catégories Vinted — cliquez pour explorer";
    renderCategoryTrail();
    openDialog("categoryModal");
    loadCategories(current.path || "/catalog", current.label || "");
  }

  function syncCategoryPill(category) {
    const pill = $("#pCategoryLabel");
    const isAll = !category.path || category.path === "/catalog";
    pill.textContent = isAll ? "Toutes les catégories" : category.label;
    pill.classList.toggle("is-all", isAll);
    pill.title = isAll ? "Aucun filtre de catégorie" : category.path;
  }

  const MANAGED_PARAMS = new Set([
    "catalog[]", "catalog", "brand_ids[]", "brand_ids", "page", "time",
    "size_ids[]", "status_ids[]", "color_ids[]", "material_ids[]",
    "price_from", "price_to", "order",
  ]);

  /* ── Filtres Vinted (tailles, état, couleurs, prix, tri) ───────────────── */

  function emptyFilters() {
    return { size_ids: [], status_ids: [], color_ids: [], price_from: "", price_to: "", order: "" };
  }

  function filtersFromUrl(rawUrl) {
    const filters = emptyFilters();
    for (const [key, value] of searchParams(rawUrl)) {
      const id = String(value || "").trim();
      if (key === "size_ids[]" || key === "size_ids") filters.size_ids.push(id);
      else if (key === "status_ids[]" || key === "status_ids") filters.status_ids.push(id);
      else if (key === "color_ids[]" || key === "color_ids") filters.color_ids.push(id);
      else if (key === "price_from") filters.price_from = id;
      else if (key === "price_to") filters.price_to = id;
      else if (key === "order") filters.order = id;
    }
    filters.size_ids = [...new Set(filters.size_ids.filter((id) => /^\d+$/.test(id)))];
    filters.status_ids = [...new Set(filters.status_ids.filter((id) => /^\d+$/.test(id)))];
    filters.color_ids = [...new Set(filters.color_ids.filter((id) => /^\d+$/.test(id)))];
    return filters;
  }

  /* Paires « clé=valeur » des filtres, dans l'ordre où Vinted les écrit. */
  function filterPairs(filters) {
    const pairs = [];
    (filters.size_ids || []).forEach((id) => pairs.push(["size_ids[]", id]));
    (filters.status_ids || []).forEach((id) => pairs.push(["status_ids[]", id]));
    (filters.color_ids || []).forEach((id) => pairs.push(["color_ids[]", id]));
    if (filters.price_from !== "" && filters.price_from !== null && filters.price_from !== undefined) {
      pairs.push(["price_from", filters.price_from]);
    }
    if (filters.price_to !== "" && filters.price_to !== null && filters.price_to !== undefined) {
      pairs.push(["price_to", filters.price_to]);
    }
    if (filters.order) pairs.push(["order", filters.order]);
    return pairs;
  }

  function filterCount(filters) {
    if (!filters) return 0;
    return (filters.size_ids || []).length + (filters.status_ids || []).length
      + (filters.color_ids || []).length
      + (filters.price_from !== "" ? 1 : 0) + (filters.price_to !== "" ? 1 : 0)
      + (filters.order ? 1 : 0);
  }

  function filterSummary(filters) {
    if (!filterCount(filters)) return "Aucun filtre Vinted";
    const parts = [];
    if ((filters.size_ids || []).length) parts.push(`${filters.size_ids.length} taille(s)`);
    if ((filters.status_ids || []).length) parts.push(`${filters.status_ids.length} état(s)`);
    if ((filters.color_ids || []).length) parts.push(`${filters.color_ids.length} couleur(s)`);
    if (filters.price_from !== "" || filters.price_to !== "") {
      parts.push(`prix ${filters.price_from || "0"}–${filters.price_to || "∞"} €`);
    }
    if (filters.order) parts.push("tri personnalisé");
    return parts.join(" · ");
  }

  async function ensureFilterCatalogue() {
    if (state.filterCatalogue) return state.filterCatalogue;
    try {
      const data = await api("/filters");
      state.filterCatalogue = data && Array.isArray(data.size_groups) && data.size_groups.length ? data : null;
    } catch (_) {
      state.filterCatalogue = null;
    }
    return state.filterCatalogue;
  }

  const COLOR_HEX = {
    "1": "#1b1b1f", "2": "#7a4b2a", "3": "#8d8f96", "4": "#e0d3b8",
    "5": "#e0219a", "6": "#8b5cf6", "7": "#e23b3b", "8": "#f2cf3a",
    "9": "#2f6fed", "10": "#2fae62", "11": "#f08a2c", "12": "#f4f6f8",
  };

  function renderFilterPanel() {
    const panel = $("#filterPanel");
    if (!panel) return;
    const catalogue = state.filterCatalogue;
    const filters = state.formFilters || emptyFilters();
    panel.replaceChildren();

    if (!catalogue || !Array.isArray(catalogue.size_groups) || !catalogue.size_groups.length) {
      panel.appendChild(el("p", "hint", "Catalogue de filtres indisponible — vous pouvez toujours coller une URL Vinted filtrée ci-dessous."));
      return;
    }

    const chipsGroup = (title, hint, items, key, { color = false } = {}) => {
      if (!Array.isArray(items) || !items.length) return null;
      const section = el("div", "filter-group");
      const head = el("div", "filter-group-head");
      head.appendChild(el("strong", "", title));
      if (hint) head.appendChild(el("small", "", hint));
      section.appendChild(head);
      const box = el("div", "filter-chips");
      for (const item of items) {
        const chip = el("button", "filter-chip", item.label);
        chip.type = "button";
        chip.dataset.filterKey = key;
        chip.dataset.filterId = String(item.id);
        const on = (filters[key] || []).includes(String(item.id));
        chip.classList.toggle("is-on", on);
        chip.setAttribute("aria-pressed", on ? "true" : "false");
        if (color) {
          const dot = el("span", "filter-dot");
          dot.style.background = COLOR_HEX[item.id] || "#888";
          chip.prepend(dot);
        }
        box.appendChild(chip);
      }
      section.appendChild(box);
      return section;
    };

    for (const group of catalogue.size_groups) {
      const section = chipsGroup(group.label, group.hint, group.sizes, "size_ids");
      if (!section) continue;
      section.classList.add("filter-group-sizes");
      panel.appendChild(section);
    }
    const statusSection = chipsGroup("État", "Neuf, très bon état, satisfaisant…", catalogue.statuses, "status_ids");
    if (statusSection) panel.appendChild(statusSection);
    const colorSection = chipsGroup("Couleurs", "Filtre exact du site", catalogue.colors, "color_ids", { color: true });
    if (colorSection) panel.appendChild(colorSection);

    const extras = el("div", "filter-group filter-extras");
    const head = el("div", "filter-group-head");
    head.appendChild(el("strong", "", "Prix & tri Vinted"));
    head.appendChild(el("small", "", "Appliqué par le site avant la lecture des annonces."));
    extras.appendChild(head);
    const row = el("div", "filter-inputs");

    const priceFrom = el("label", "field");
    priceFrom.appendChild(el("span", "", "Prix min (€)"));
    const fromInput = document.createElement("input");
    fromInput.type = "number"; fromInput.min = "0"; fromInput.step = "1";
    fromInput.id = "fPriceFrom"; fromInput.placeholder = "—";
    fromInput.value = filters.price_from || "";
    priceFrom.appendChild(fromInput);

    const priceTo = el("label", "field");
    priceTo.appendChild(el("span", "", "Prix max (€)"));
    const toInput = document.createElement("input");
    toInput.type = "number"; toInput.min = "0"; toInput.step = "1";
    toInput.id = "fPriceTo"; toInput.placeholder = "—";
    toInput.value = filters.price_to || "";
    priceTo.appendChild(toInput);

    const orderField = el("label", "field");
    orderField.appendChild(el("span", "", "Tri"));
    const select = document.createElement("select");
    select.id = "fOrder";
    const none = document.createElement("option");
    none.value = ""; none.textContent = "Plus récentes (recommandé)";
    select.appendChild(none);
    for (const option of catalogue.orders || []) {
      if (option.id === "newest_first") continue;
      const node = document.createElement("option");
      node.value = option.id; node.textContent = option.label;
      select.appendChild(node);
    }
    select.value = filters.order || "";
    orderField.appendChild(select);

    row.append(priceFrom, priceTo, orderField);
    extras.appendChild(row);
    panel.appendChild(extras);

    syncFilterSummary();
  }

  function syncFilterSummary() {
    const label = $("#filterSummary");
    if (!label) return;
    const filters = state.formFilters || emptyFilters();
    const count = filterCount(filters);
    label.textContent = filterSummary(filters);
    label.classList.toggle("chip-accent", count > 0);
    label.classList.toggle("chip-muted", count === 0);
  }

  function setFilterValue(key, id, on) {
    const filters = state.formFilters || emptyFilters();
    const list = filters[key] || [];
    const value = String(id);
    filters[key] = on ? [...new Set([...list, value])] : list.filter((item) => item !== value);
    state.formFilters = filters;
  }

  function clearFilters() {
    state.formFilters = emptyFilters();
    renderFilterPanel();
    rebuildFormUrl();
    toast("Filtres Vinted effacés.", "success");
  }

  /* Crochets littéraux dans la query string, comme les liens de Vinted. */
  function encodeQuery(pairs) {
    return pairs
      .filter(([key]) => key)
      .map(([key, value]) =>
        `${encodeURIComponent(key).replace(/%5B%5D/g, "[]")}=${encodeURIComponent(value)}`)
      .join("&");
  }

  function splitSearchUrl(rawUrl) {
    const domain = profileDomainFromForm();
    const value = (rawUrl || "").trim();
    if (!value) return { domain, path: "/catalog", search: "" };

    const hasScheme = /^https?:\/\//i.test(value);
    const hasDomain = /^[\w.-]*vinted\.[a-z.]{2,}(\/|$)/i.test(value);
    const looksLikePath = value.startsWith("/") || /^catalog(\/|\?|$)/i.test(value);

    if (!hasScheme && !hasDomain && !looksLikePath) {
      // Simple mot-clé saisi à la main → recherche plein texte.
      if (value.includes("=")) {
        return { domain, path: "/catalog", search: `?${value.replace(/^\?/, "")}` };
      }
      return { domain, path: "/catalog", search: `?search_text=${encodeURIComponent(value)}` };
    }
    try {
      const url = new URL(hasScheme ? value : `https://${value.replace(/^\/+/, "")}`);
      return {
        domain: url.hostname || domain,
        path: url.pathname || "/catalog",
        search: url.search || "",
      };
    } catch (_) {
      return { domain, path: "/catalog", search: "" };
    }
  }

  function searchParams(rawUrl) {
    const { search } = splitSearchUrl(rawUrl);
    const raw = (search || "").replace(/^\?/, "");
    const params = [];
    if (!raw) return params;
    new URLSearchParams(raw).forEach((value, key) => params.push([key, value]));
    return params;
  }

  function catalogIdFrom(path) {
    const match = (path || "").match(/^\/catalog\/(\d+)/i);
    return match ? match[1] : "";
  }

  /* Écrit dans #pUrl la catégorie + les marques choisies, sans perdre mots-clés ni prix. */
  function rebuildFormUrl() {
    const current = splitSearchUrl($("#pUrl").value);
    const kept = searchParams($("#pUrl").value).filter(([key]) => !MANAGED_PARAMS.has(key));
    const catPath = (state.formCategory && state.formCategory.path) || "/catalog";
    const catId = catalogIdFrom(catPath);
    const brands = (state.formBrands || []).map((row) => row.id).filter(Boolean);
    const filterList = filterPairs(state.formFilters || emptyFilters());
    let url;
    if (brands.length || filterList.length) {
      /* Vinted n'applique brand_ids[] et les filtres qu'en paramètres
         (?catalog[]=…&brand_ids[]=…&size_ids[]=…) : c'est la forme qu'il génère lui-même. */
      const pairs = [];
      if (catId) pairs.push(["catalog[]", catId]);
      brands.forEach((id) => pairs.push(["brand_ids[]", id]));
      pairs.push(...filterList, ...kept);
      url = `https://${current.domain}/catalog${pairs.length ? `?${encodeQuery(pairs)}` : ""}`;
    } else {
      const path = catId ? catPath : "/catalog";
      url = `https://${current.domain}${path}${kept.length ? `?${encodeQuery(kept)}` : ""}`;
    }
    $("#pUrl").value = url;
    return url;
  }

  /* Devine la catégorie d'une URL collée à la main (chemin ou catalog[]). */
  function categoryFromUrl(rawUrl, fallbackLabel = "") {
    const { path } = splitSearchUrl(rawUrl);
    const query = searchParams(rawUrl).find(([key]) => key === "catalog[]" || key === "catalog");
    const slugMatch = path.match(/^\/catalog\/(\d+)(?:-([a-z0-9_-]+))?/i);
    const id = slugMatch ? slugMatch[1] : ((String(query ? query[1] : "").match(/^(\d+)/) || [])[1] || "");
    if (!id) return { path: "/catalog", label: "Toutes les catégories" };
    const slug = (slugMatch && slugMatch[2] ? slugMatch[2] : "").replace(/_/g, " ").replace(/-/g, " ");
    return {
      path: `/catalog/${id}${slugMatch && slugMatch[2] ? `-${slugMatch[2]}` : ""}`,
      label: fallbackLabel || (slug ? slug.charAt(0).toUpperCase() + slug.slice(1) : `Catégorie ${id}`),
    };
  }

  function brandsFromUrl(rawUrl, fallbackLabel = "") {
    const ids = [...new Set(
      searchParams(rawUrl)
        .filter(([key]) => key === "brand_ids[]" || key === "brand_ids")
        .map(([, value]) => String(value).trim())
        .filter((value) => /^\d+$/.test(value)),
    )];
    const names = (fallbackLabel || "").split(",").map((part) => part.trim()).filter(Boolean);
    return ids.map((id, index) => ({ id, name: names[index] || `Marque ${id}` }));
  }

  function syncCategoryPill(category) {
    const pill = $("#pCategoryLabel");
    const isAll = !category.path || category.path === "/catalog";
    pill.textContent = isAll ? "Toutes les catégories" : category.label;
    pill.classList.toggle("is-all", isAll);
    pill.title = isAll ? "Aucun filtre de catégorie" : category.path;
  }

  function syncBrandsPill() {
    const pill = $("#pBrandsLabel");
    if (!pill) return;
    const rows = state.formBrands || [];
    const isAll = !rows.length;
    pill.textContent = isAll ? "Toutes les marques" : rows.map((row) => row.name).join(", ");
    pill.classList.toggle("is-all", isAll);
    pill.title = isAll
      ? "Aucun filtre de marque"
      : rows.map((row) => `${row.name} (#${row.id})`).join(", ");
  }

  function selectCategory(category, { updateUrl = true } = {}) {
    state.formCategory = category;
    syncCategoryPill(category);
    if (updateUrl) rebuildFormUrl();
  }

  function selectBrands(rows, { updateUrl = true } = {}) {
    state.formBrands = rows;
    syncBrandsPill();
    if (updateUrl) rebuildFormUrl();
  }

  /* ── Marques Vinted ─────────────────────────────────────────────────── */

  const BRAND_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

  function renderBrandLetters() {
    const box = $("#brandLetters");
    box.replaceChildren();
    for (const letter of BRAND_LETTERS) {
      const button = el("button", "cat-letter", letter);
      button.type = "button";
      button.classList.toggle("is-active", letter === state.brandLetter);
      button.addEventListener("click", () => {
        state.brandLetter = letter;
        $("#brandSearch").value = "";
        renderBrandLetters();
        loadBrands({ letter });
      });
      box.appendChild(button);
    }
  }

  function renderBrandList() {
    const list = $("#brandList");
    list.replaceChildren();
    if (state.brandLoading) {
      list.appendChild(el("p", "cat-empty", "Lecture des marques sur Vinted…"));
      return;
    }
    const rows = state.brandRows || [];
    if (!rows.length) {
      list.appendChild(el("p", "cat-empty",
        "Aucune marque trouvée. Essayez une autre lettre, ou utilisez le nom de la marque comme mot-clé."));
      return;
    }
    const selected = new Set(state.brandDraft.map((row) => row.id));
    for (const row of rows) {
      const label = el("label", "brand-item");
      const input = document.createElement("input");
      input.type = "checkbox";
      input.value = row.id;
      input.checked = selected.has(row.id);
      input.addEventListener("change", () => toggleBrand(row, input.checked));
      label.appendChild(input);
      label.appendChild(el("span", "", row.name));
      label.appendChild(el("span", "chev", `#${row.id}`));
      list.appendChild(label);
    }
  }

  function renderBrandFooter() {
    const count = state.brandDraft.length;
    $("#brandSelected").textContent = count
      ? `${count} marque(s) sélectionnée(s) : ${state.brandDraft.map((row) => row.name).join(", ")}`
      : "Aucune marque sélectionnée (toutes les marques)";
    const button = $("#brandApply");
    button.textContent = count ? `Filtrer sur ${count} marque(s)` : "Chercher toutes les marques";
    button.disabled = count > 20;
  }

  function toggleBrand(row, checked) {
    const rows = state.brandDraft.filter((item) => item.id !== row.id);
    if (checked && rows.length < 20) rows.push({ id: row.id, name: row.name });
    state.brandDraft = rows;
    renderBrandFooter();
    renderBrandList();
  }

  function renderBrandIndex(data) {
    state.brandIndex = { total: data.total || 0, updated_at: data.updated_at || null };
    const label = $("#brandIndex");
    if (data.running) {
      label.textContent = `Import en cours… ${data.sitemaps}/${data.sitemaps_total || "?"} fichiers, `
        + `${(data.imported || 0).toLocaleString("fr-FR")} marques`;
      return true;
    }
    if (data.error) {
      label.textContent = `Import interrompu : ${data.error}`;
      return false;
    }
    const exportLink = document.querySelector("#brandExport");
    if (exportLink) exportLink.classList.toggle("hidden", !state.brandIndex.total);
    if (state.brandIndex.total) {
      const when = data.updated_at ? new Date(data.updated_at).toLocaleString("fr-FR") : "—";
      label.textContent = `${state.brandIndex.total.toLocaleString("fr-FR")} marques disponibles localement `
        + `(import du ${when}) — recherche instantanée, même hors ligne.`;
    } else {
      label.textContent = "Index local : aucun — importez-le une fois (≈10 s).";
    }
    return false;
  }

  async function refreshBrandIndex() {
    try {
      renderBrandIndex(await api("/brands/sync"));
    } catch (_) {
      /* le serveur répondra plus tard */
    }
  }

  async function importBrands(button) {
    button.disabled = true;
    state.brandAutoImportFailed = false;
    state.brandAutoImportFailedAt = 0;
    const domain = profileDomainFromForm();
    try {
      renderBrandIndex(await api(`/brands/sync?domain=${encodeURIComponent(domain)}`, { method: "POST" }));
      for (let attempt = 0; attempt < 120; attempt += 1) {
        await new Promise((resolve) => setTimeout(resolve, 1500));
        const data = await api("/brands/sync");
        const stillRunning = renderBrandIndex(data);
        if (!stillRunning) break;
      }
      await refreshBrandIndex();
      if (state.brandIndex.total) {
        toast(`${state.brandIndex.total.toLocaleString("fr-FR")} marques importées.`, "success");
        await loadBrands({ search: ($("#brandSearch").value || "").trim() });
      }
    } catch (error) {
      $("#brandIndex").textContent = `Import impossible : ${error.message}`;
    } finally {
      button.disabled = false;
    }
  }

  async function addBrandFromReference() {
    const input = $("#brandManual");
    const raw = (input.value || "").trim();
    if (!raw) return;
    try {
      const data = await api(`/brands/resolve?ref=${encodeURIComponent(raw)}`);
      const brand = data.brand;
      if (!state.brandDraft.some((row) => row.id === brand.id)) {
        if (state.brandDraft.length >= 20) {
          $("#brandNote").textContent = "20 marques maximum par profil.";
          return;
        }
        state.brandDraft.push({ id: brand.id, name: brand.name });
      }
      input.value = "";
      $("#brandNote").textContent = `Marque ajoutée : ${brand.name} (#${brand.id}).`;
      renderBrandFooter();
      renderBrandList();
    } catch (error) {
      $("#brandNote").textContent = `Référence non reconnue : ${error.message}`;
    }
  }

  /* L'index local est la seule source fiable pour « toutes les marques qui
     commencent par cp ». S'il est vide au moment d'une recherche, on l'importe
     une fois, tout seul, au lieu d'afficher « aucune marque ». */
  async function ensureBrandIndex(maxWaitMs = 45000) {
    if (state.brandIndex.total) return true;
    if (state.brandImporting) return Boolean(state.brandIndex.total);
    if (state.brandAutoImportFailedAt
        && Date.now() - state.brandAutoImportFailedAt < 60000) {
      return Boolean(state.brandIndex.total);
    }
    try {
      await refreshBrandIndex();
      if (state.brandIndex.total) return true;
      state.brandImporting = true;
      $("#brandNote").textContent =
        "Index des marques vide : import automatique en cours (une seule fois)…";
      const domain = profileDomainFromForm();
      renderBrandIndex(await api(`/brands/sync?domain=${encodeURIComponent(domain)}`, { method: "POST" }));
      const started = Date.now();
      while (Date.now() - started < maxWaitMs) {
        await new Promise((resolve) => setTimeout(resolve, 1000));
        const data = await api("/brands/sync");
        const stillRunning = renderBrandIndex(data);
        /* Progression visible : l'import dure parfois 20-30 s sur une petite
           connexion, et une attente muette ressemble à une panne. */
        $("#brandNote").textContent =
          `Import des ${(data.imported || 0).toLocaleString("fr-FR")} marques en cours`
          + ` (${data.sitemaps || 0}/${data.sitemaps_total || "?"} fichiers) — `
          + "la recherche complète s'active dès la fin.";
        if (!stillRunning) break;
      }
      if (state.brandIndex.total) {
        toast(`${state.brandIndex.total.toLocaleString("fr-FR")} marques importées : recherche complète active.`, "success");
        return true;
      }
      state.brandAutoImportFailedAt = Date.now();
      $("#brandNote").textContent =
        "Import encore en cours en arrière-plan (Vinted répond lentement). "
        + "Tapez à nouveau dans un instant, ou collez l'URL de la marque ci-dessus.";
      return false;
    } catch (error) {
      state.brandAutoImportFailedAt = Date.now();
      $("#brandNote").textContent = `Import impossible : ${error.message}. Le bouton ⬇ réessaiera.`;
      return false;
    } finally {
      state.brandImporting = false;
    }
  }

  async function loadBrands({ letter = "", search = "" } = {}) {
    if (search) await ensureBrandIndex();
    state.brandLoading = true;
    renderBrandList();
    const domain = profileDomainFromForm();
    const params = new URLSearchParams({ domain });
    if (search) {
      /* Mode préfixe : taper « n » propose TOUTES les marques commençant par N. */
      params.set("search", search);
      params.set("prefix", "1");
      params.set("limit", "500");
    }
    if (letter && !search) params.set("letter", letter);
    try {
      const data = await api(`/brands?${params.toString()}`);
      state.brandRows = data.brands || [];
      if (data.letter) state.brandLetter = data.letter;
      if (data.source === "index") {
        const total = typeof data.total === "number" ? data.total : (data.brands || []).length;
        const shown = (data.brands || []).length;
        $("#brandNote").textContent = total > shown
          ? `${total.toLocaleString("fr-FR")} marque(s) commencent par « ${data.search} » — ${shown} affichées.`
          : `${total.toLocaleString("fr-FR")} marque(s) pour « ${data.search} » — recherche instantanée, sans réseau.`;
      } else if (search) {
        $("#brandNote").textContent = "Importez l'index local (bouton ⬇) pour l'autocomplétion "
          + "complète : sans lui, seules les marques populaires de cette lettre sont proposées.";
      } else {
        $("#brandNote").textContent = data.source === "vinted"
          ? `Marques réelles lues sur ${domain} — cochez celles qui vous intéressent.`
          : "Marques populaires. Importez l'index complet pour chercher parmi toutes les marques.";
      }
    } catch (error) {
      state.brandRows = [];
      $("#brandNote").textContent = `Liste indisponible : ${error.message}`;
      try {
        const fallback = await api("/brands");
        state.brandRows = fallback.brands || [];
        $("#brandNote").textContent =
          "Vinted injoignable : marques populaires affichées. Vous pouvez aussi saisir la marque comme mot-clé.";
      } catch (_) {
        /* rien de plus à proposer */
      }
    } finally {
      state.brandLoading = false;
      renderBrandLetters();
      renderBrandList();
    }
  }

  function openBrandBrowser() {
    state.brandDraft = (state.formBrands || []).map((row) => ({ ...row }));
    state.brandRows = [];
    state.brandLetter = state.brandDraft.length
      ? (state.brandDraft[0].name[0] || "A").toUpperCase()
      : state.brandLetter || "A";
    $("#brandSearch").value = "";
    $("#brandNote").textContent = "Lecture des marques sur Vinted…";
    renderBrandLetters();
    renderBrandFooter();
    renderBrandList();
    openDialog("brandModal");
    refreshBrandIndex();
    loadBrands({ letter: state.brandLetter });
  }

  /* ── Actions profils ─────────────────────────────────────────────────── */

  async function scanNow(profile, button) {
    button.disabled = true;
    const original = button.textContent;
    button.textContent = "Lancement…";
    try {
      await api(`/profiles/${profile.id}/scan`, { method: "POST" });
      toast(`Scan lancé pour « ${profile.name} ».`, "success");
      setTimeout(refreshProfiles, 600);
    } catch (error) {
      toast(error.message, "error");
      button.disabled = false;
      button.textContent = original;
    }
  }

  async function duplicateProfile(profile) {
    try {
      await api(`/profiles/${profile.id}/duplicate`, { method: "POST" });
      toast("Profil dupliqué (désactivé par défaut).", "success");
      await refreshProfiles();
    } catch (error) {
      toast(error.message, "error");
    }
  }

  function deleteProfile(profile) {
    askConfirm(
      "Supprimer ce profil ?",
      `« ${profile.name} » et son historique d'annonces vues seront définitivement supprimés.`,
      async () => {
        try {
          await api(`/profiles/${profile.id}`, { method: "DELETE" });
          toast("Profil supprimé.", "success");
          await refreshProfiles();
          await refreshFeed();
          await refreshStatus();
        } catch (error) {
          toast(error.message, "error");
        }
      },
    );
  }

  function clearSeen(profile) {
    askConfirm(
      "Oublier les annonces vues ?",
      `Toutes les annonces déjà enregistrées pour « ${profile.name} » seront oubliées : les annonces actuellement en ligne pourront être re-notifiées.`,
      async () => {
        try {
          const result = await api(`/profiles/${profile.id}/clear-seen`, { method: "POST" });
          toast(result.message || "Historique du profil effacé.", "success");
          closeDialog("profileModal");
          await refreshFeed();
        } catch (error) {
          toast(error.message, "error");
        }
      },
    );
  }

  function askConfirm(title, text, handler) {
    $("#confirmTitle").textContent = title;
    $("#confirmText").textContent = text;
    state.confirmHandler = handler;
    openDialog("confirmModal");
  }

  /* ── Aperçu des filtres ──────────────────────────────────────────────── */

  async function openPreview(profile) {
    $("#previewSub").textContent = `Lecture des annonces en ligne pour « ${profile.name} »…`;
    $("#previewSummary").replaceChildren();
    const list = $("#previewList");
    list.replaceChildren(el("div", "hint", "Interrogation du catalogue Vinted…"));
    $("#previewNote").textContent = "";
    openDialog("previewModal");
    try {
      const result = await api(`/profiles/${profile.id}/preview`, { method: "POST" });
      $("#previewSub").textContent = `${result.total} annonce(s) analysée(s) · tri « Plus récent » · ${profile.name}`;
      const summary = $("#previewSummary");
      summary.appendChild(el("span", "chip chip-green", `${result.accepted} retenue(s)`));
      summary.appendChild(el("span", "chip chip-red", `${result.rejected} écartée(s)`));
      summary.appendChild(el("span", "chip chip-muted", result.url || ""));
      list.replaceChildren();
      if (!result.items.length) {
        list.appendChild(el("div", "hint", "Aucune annonce retournée par Vinted pour cette recherche."));
      }
      for (const item of result.items) {
        const row = el("div", `preview-row ${item.matched ? "" : "rejected"}`.trim());
        if (item.image_url) {
          const img = new Image();
          img.src = item.image_url;
          img.alt = "";
          img.loading = "lazy";
          img.referrerPolicy = "no-referrer";
          img.addEventListener("error", () => img.replaceWith(thumbFallback(item)));
          row.appendChild(img);
        } else {
          row.appendChild(thumbFallback(item));
        }
        const info = el("div", "preview-info");
        info.appendChild(el("strong", "", item.title || "Sans titre"));
        info.appendChild(el("span", "",
          `${formatMoney(item.price, item.currency)} · ${item.brand || "marque ?"} · ${item.size || "taille ?"}`
          + ` · @${item.seller_name || "vendeur ?"} ${item.seller_rating ? `★ ${Number(item.seller_rating).toFixed(1)}` : ""}`));
        row.appendChild(info);
        const verdict = el("span", `preview-verdict ${item.matched ? "ok" : "ko"}`,
          item.matched ? "✓ retenue" : `✕ ${item.reason}`);
        verdict.title = item.reason || "Correspond aux filtres";
        row.appendChild(verdict);
        list.appendChild(row);
      }
      $("#previewNote").textContent = result.note || "";
    } catch (error) {
      list.replaceChildren(el("div", "hint", `⚠ ${error.message}`));
      $("#previewSub").textContent = "Aperçu impossible";
    }
  }

  function thumbFallback(item) {
    return el("div", "thumb", (item.brand || "V").slice(0, 2).toUpperCase());
  }

  /* ── Actions globales ────────────────────────────────────────────────── */

  async function toggleEngine() {
    if (!state.status) return;
    const resume = Boolean(state.status.paused);
    try {
      await api("/engine/toggle", {
        method: "POST",
        body: JSON.stringify({ active: resume }),
      });
      toast(resume ? "Moteur relancé." : "Moteur en pause.", "success");
      await refreshStatus();
    } catch (error) {
      toast(error.message, "error");
    }
  }

  async function runAll() {
    const active = state.profiles.filter((profile) => profile.active && profile.url);
    if (!active.length) {
      toast("Aucun profil actif avec une URL de recherche.", "error");
      return;
    }
    let launched = 0;
    for (const profile of active) {
      try {
        await api(`/profiles/${profile.id}/scan`, { method: "POST" });
        launched += 1;
      } catch (_) { /* profil déjà en cours : on continue */ }
      await new Promise((resolve) => setTimeout(resolve, 180));
    }
    toast(`${launched} scan(s) lancé(s).`, launched ? "success" : "error");
    setTimeout(refreshProfiles, 800);
  }

  async function renewSession() {
    try {
      const result = await api("/engine/renew-sessions", { method: "POST" });
      toast(result.message || "Sessions renouvelées.", "success");
    } catch (error) {
      toast(error.message, "error");
    }
  }

  async function discoverProxies(button) {
    button.disabled = true;
    button.textContent = "Recherche…";
    try {
      const result = await api("/proxies/discover", { method: "POST" });
      toast(result.message || "Découverte terminée.", "success");
      await refreshStatus();
    } catch (error) {
      toast(error.message, "error");
    } finally {
      button.disabled = false;
      button.textContent = "Découvrir";
    }
  }

  async function resetProxies() {
    try {
      await api("/proxies/reset", { method: "POST" });
      toast("Quarantaines levées.", "success");
      await refreshStatus();
    } catch (error) {
      toast(error.message, "error");
    }
  }

  function openWebhookModal() {
    $("#webhookError").textContent = "";
    $("#testWebhookUrl").value = (state.config && state.config.discord
      && state.config.discord.default_webhook) || "";
    $("#testWebhookName").value = "Test Vinted Sniper";
    openDialog("webhookModal");
  }

  async function sendWebhookTest(event) {
    event.preventDefault();
    const url = $("#testWebhookUrl").value.trim();
    const name = $("#testWebhookName").value.trim() || "Test";
    const errorBox = $("#webhookError");
    errorBox.textContent = "";
    if (!url) {
      errorBox.textContent = "Renseignez un webhook Discord (ou un webhook global dans les réglages).";
      return;
    }
    try {
      const result = await api("/notifications/test", {
        method: "POST",
        body: JSON.stringify({ webhook: url, profile_name: name }),
      });
      toast(result.message || "Message de test envoyé.", "success");
      closeDialog("webhookModal");
    } catch (error) {
      errorBox.textContent = error.message;
    }
  }

  /* ── Diagnostic ─────────────────────────────────────────────────────── */

  function openDiagnostic() {
    $("#diagResults").replaceChildren();
    $("#diagAdvice").replaceChildren();
    $("#diagWebhook").value =
      (state.config && state.config.discord && state.config.discord.default_webhook) || "";
    openDialog("diagModal");
  }

  function renderDiagnostic(report) {
    const list = $("#diagResults");
    const advice = $("#diagAdvice");
    list.replaceChildren();
    advice.replaceChildren();
    for (const step of report.steps || []) {
      const icon = step.skipped ? "⏭️" : step.ok ? "✅" : "❌";
      const row = el("div", `diag-step ${step.skipped ? "skip" : step.ok ? "ok" : "ko"}`);
      row.appendChild(el("span", "diag-icon", icon));
      const body = el("div", "diag-body");
      body.appendChild(el("strong", "", step.label));
      body.appendChild(el("p", "", step.detail));
      if (step.key === "sample" && step.data && step.data.items) {
        const ul = el("ul", "diag-samples");
        for (const item of step.data.items.slice(0, 3)) {
          const li = el("li");
          const link = el("a", "", item.title);
          link.href = item.url;
          link.target = "_blank";
          link.rel = "noopener noreferrer";
          li.appendChild(link);
          li.append(` — ${item.price}`);
          ul.appendChild(li);
        }
        body.appendChild(ul);
      }
      row.appendChild(body);
      list.appendChild(row);
    }
    for (const line of report.advice || []) {
      advice.appendChild(el("p", "", line));
    }
    $("#diagHint").textContent =
      `Terminé en ${report.duration_ms} ms · recherche « ${report.query} » · ${report.domain}` +
      (report.ok ? " · accès réel confirmé" : " · voir les points à corriger");
  }

  async function runDiagnostic() {
    const button = $("#diagRun");
    const list = $("#diagResults");
    button.disabled = true;
    button.textContent = "Test en cours…";
    list.replaceChildren(el("div", "hint", "Connexion à Vinted et analyse de la page…"));
    $("#diagAdvice").replaceChildren();
    try {
      const report = await api("/diagnose", {
        method: "POST",
        body: JSON.stringify({
          query: $("#diagQuery").value.trim() || "nike",
          webhook: $("#diagWebhook").value.trim(),
          domain: "www.vinted.fr",
        }),
      });
      renderDiagnostic(report);
      toast(report.ok ? "Vinted répond : le scan réel fonctionne." : "Diagnostic terminé : voir les étapes.", report.ok ? "success" : "error");
    } catch (error) {
      list.replaceChildren(el("div", "hint", `⚠ ${error.message}`));
    } finally {
      button.disabled = false;
      button.textContent = "Lancer le diagnostic";
    }
  }

  /* ── Rafraîchissements ───────────────────────────────────────────────── */

  /* Déblocage gratuit : un vrai navigateur exécute la vérification Cloudflare,
     puis on récupère ses cookies (dont cf_clearance, invisible en JS). */
  async function unblockWithBrowser(button) {
    const label = button.textContent;
    button.disabled = true;
    button.textContent = "Fenêtre ouverte…";
    toast("Fenêtre du navigateur ouverte : laissez-la se valider (cochez si demandé).", "info");
    try {
      const result = await api("/session/unblock", {
        method: "POST",
        body: JSON.stringify({}),
        timeoutMs: 180000,
      });
      if (result.ok) {
        const count = (result.session && result.session.imported) || 0;
        toast(`Session importée (${count} cookie(s)) : les scans repartent tout de suite.`, "success");
        await Promise.all([refreshStatus(), refreshProfiles(), refreshLogs()]);
      } else {
        toast(result.detail || "Vérification non terminée : recommencez et validez la page.", "error");
      }
    } catch (error) {
      toast(`Déblocage : ${error.message}`, "error");
    } finally {
      button.disabled = false;
      button.textContent = label;
    }
  }

  /* Secours cURL : importer une session copiée du navigateur. */
  async function importCurlSession(button) {
    const box = $("#cfgCurl");
    const status = $("#cfgCurlStatus");
    const command = (box && box.value || "").trim();
    if (!command) {
      if (status) status.textContent = "Collez d'abord la commande cURL copiée du navigateur.";
      return;
    }
    button.disabled = true;
    const label = button.textContent;
    button.textContent = "Import…";
    if (status) status.textContent = "";
    try {
      const result = await api("/session/import", {
        method: "POST",
        body: JSON.stringify({ command }),
        timeoutMs: 20000,
      });
      const count = (result.session && result.session.imported) || 0;
      toast(`Session importée (${count} cookie(s)) : les scans repartent.`, "success");
      if (status) {
        status.textContent = result.clearance
          ? `${count} cookie(s) importé(s), cf_clearance présent — ${result.resumed} profil(s) relancé(s).`
          : `${count} cookie(s) importé(s) mais pas de cf_clearance : la vérification risque de revenir.`;
      }
      box.value = "";
      await Promise.all([refreshStatus(), refreshProfiles(), refreshLogs()]);
    } catch (error) {
      if (status) status.textContent = error.message;
      toast(`Import : ${error.message}`, "error");
    } finally {
      button.disabled = false;
      button.textContent = label;
    }
  }

  async function refreshStatus() {
    try {
      const status = await api("/status");
      state.statusFailures = 0;
      state.offline = false;
      renderStatus(status);
    } catch (error) {
      /* Un redémarrage du bot provoque 1 ou 2 échecs : inutile d'afficher
         « Hors ligne » pour un incident de 2 s. */
      state.statusFailures += 1;
      if (state.statusFailures >= 3) renderOffline();
    }
  }

  async function refreshProfiles() {
    try {
      const data = await api("/profiles");
      state.profiles = data.profiles || [];
      renderProfiles();
    } catch (error) {
      if (!state.offline) toast(`Profils : ${error.message}`, "error");
    }
  }

  async function refreshFeed() {
    try {
      const query = state.feedProfile === "all" ? "" : `?profile_id=${state.feedProfile}`;
      const data = await api(`/feed${query}`);
      state.feed = data.items || [];
      renderFeed();
    } catch (error) {
      /* silencieux : le statut global signale déjà la coupure */
    }
  }

  async function refreshLogs() {
    try {
      const data = await api("/logs?limit=120");
      state.logs = data.logs || [];
      renderLogs();
    } catch (error) {
      /* silencieux */
    }
  }

  async function refreshConfig() {
    try {
      state.config = await api("/config");
      fillSettings(state.config);
    } catch (error) {
      toast(`Configuration : ${error.message}`, "error");
    }
  }

  async function refreshAll() {
    await Promise.all([refreshStatus(), refreshProfiles(), refreshFeed(), refreshLogs()]);
  }

  function startTimers() {
    let running = { status: false, profiles: false, feed: false, logs: false };
    const guarded = (key, fn) => async () => {
      if (running[key] || document.hidden) return;
      running[key] = true;
      try { await fn(); } finally { running[key] = false; }
    };
    const statusTick = guarded("status", refreshStatus);
    const profilesTick = guarded("profiles", refreshProfiles);
    const feedTick = guarded("feed", refreshFeed);
    const logsTick = guarded("logs", refreshLogs);
    setInterval(statusTick, 1500);
    setInterval(profilesTick, 4000);
    // Le flux SSE pousse les nouveautés : ce poll n'est qu'un filet de sécurité
    // (et le moyen de rester synchrone après un redémarrage du serveur).
    setInterval(feedTick, 2500);
    setInterval(logsTick, 5000);
    setInterval(() => {
      if (document.hidden || !state.stream) return;
      if (state.streamState === "live" && Date.now() - state.lastEventAt > 45000) {
        connectStream();  // flux muet : on le relance
      }
    }, 10000);
    document.addEventListener("visibilitychange", () => {
      if (!document.hidden) refreshAll();
    });
  }

  /* ── Événements ──────────────────────────────────────────────────────── */

  function bindEvents() {
    $("#btnPause").addEventListener("click", toggleEngine);
    $("#btnNewProfile").addEventListener("click", () => openProfileModal());
    const quickForm = $("#quickForm");
    if (quickForm) quickForm.addEventListener("submit", submitQuickStart);
    const quickAdvanced = $("#qsAdvanced");
    if (quickAdvanced) {
      quickAdvanced.addEventListener("click", () => {
        const query = ($("#qsQuery").value || "").trim();
        openProfileModal();
        if (query) {
          $("#pName").value = query.slice(0, 60);
          $("#pUrl").value = query;
          rebuildFormUrl();
        }
        const maxPrice = ($("#qsMaxPrice").value || "").trim();
        if (maxPrice) $("#pMaxPrice").value = maxPrice;
        const webhook = ($("#qsWebhook").value || "").trim();
        if (webhook) $("#pWebhook").value = webhook;
      });
    }
    $("#profileForm").addEventListener("submit", submitProfile);
    const curlImport = $("#cfgCurlImport");
    if (curlImport) {
      curlImport.addEventListener("click", () => importCurlSession(curlImport));
    }
    const blockSolve = $("#blockBannerSolve");
    if (blockSolve) {
      blockSolve.addEventListener("click", () => unblockWithBrowser(blockSolve));
    }
    const blockTest = $("#blockBannerTest");
    if (blockTest) {
      blockTest.addEventListener("click", async () => {
        blockTest.disabled = true;
        const label = blockTest.textContent;
        blockTest.textContent = "Test en cours…";
        try {
          await runDiagnostic();
        } finally {
          blockTest.disabled = false;
          blockTest.textContent = label;
        }
      });
    }
    const blockHide = $("#blockBannerHide");
    if (blockHide) {
      blockHide.addEventListener("click", () => {
        state.blockBannerHiddenAt = Date.now();
        const panel = $("#blockBanner");
        if (panel) panel.classList.add("hidden");
      });
    }
    const bannerFix = $("#alertBannerFix");
    if (bannerFix) {
      bannerFix.addEventListener("click", () => {
        const input = $("#cfgWebhook");
        if (input) {
          input.scrollIntoView({ behavior: "smooth", block: "center" });
          input.focus();
        }
      });
    }
    $("#settingsForm").addEventListener("submit", saveSettings);
    $("#webhookForm").addEventListener("submit", sendWebhookTest);
    $("#diagRun").addEventListener("click", runDiagnostic);
    $("#pLiveMode").addEventListener("change", toggleIntervalField);
    $("#pPickCategory").addEventListener("click", openCategoryBrowser);
    $("#pClearCategory").addEventListener("click", () => {
      selectCategory({ path: "/catalog", label: "Toutes les catégories" });
    });
    $("#pPickBrands").addEventListener("click", openBrandBrowser);
    $("#filterClear").addEventListener("click", clearFilters);
    $("#filterPanel").addEventListener("click", (event) => {
      const chip = event.target.closest(".filter-chip");
      if (!chip) return;
      const key = chip.dataset.filterKey;
      const id = chip.dataset.filterId;
      const on = !chip.classList.contains("is-on");
      setFilterValue(key, id, on);
      chip.classList.toggle("is-on", on);
      chip.setAttribute("aria-pressed", on ? "true" : "false");
      syncFilterSummary();
      rebuildFormUrl();
    });
    $("#filterPanel").addEventListener("input", (event) => {
      const target = event.target;
      if (!target || !target.id) return;
      const filters = state.formFilters || emptyFilters();
      if (target.id === "fPriceFrom") filters.price_from = target.value.trim();
      else if (target.id === "fPriceTo") filters.price_to = target.value.trim();
      else return;
      state.formFilters = filters;
      syncFilterSummary();
      rebuildFormUrl();
    });
    $("#filterPanel").addEventListener("change", (event) => {
      const target = event.target;
      if (!target || target.id !== "fOrder") return;
      state.formFilters = { ...(state.formFilters || emptyFilters()), order: target.value };
      syncFilterSummary();
      rebuildFormUrl();
    });
    $("#pClearBrands").addEventListener("click", () => {
      selectBrands([]);
      toast("Filtre de marques retiré.", "success");
    });
    let brandSearchTimer = null;
    $("#brandSearch").addEventListener("input", () => {
      const query = ($("#brandSearch").value || "").trim();
      clearTimeout(brandSearchTimer);
      if (!query) {
        loadBrands({ letter: state.brandLetter });
        return;
      }
      brandSearchTimer = setTimeout(() => loadBrands({ search: query }), 160);
    });
    $("#brandImport").addEventListener("click", (event) => importBrands(event.currentTarget));
    $("#brandAdd").addEventListener("click", addBrandFromReference);
    $("#brandManual").addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        addBrandFromReference();
      }
    });
    $("#brandApply").addEventListener("click", () => {
      const rows = state.brandDraft;
      selectBrands(rows);
      closeDialog("brandModal");
      toast(rows.length
        ? `Marques appliquées : ${rows.map((row) => row.name).join(", ")}.`
        : "Recherche sur toutes les marques.", "success");
    });
    $("#catFilter").addEventListener("input", () => {
      state.catChildren = state.catChildren;
      renderCategoryList();
    });
    $("#catRoot").addEventListener("click", () => {
      state.catTrail = [];
      state.formCategory = { path: "/catalog", label: "Toutes les catégories" };
      renderCategoryTrail();
      loadCategories("/catalog");
    });
    $("#catUp").addEventListener("click", () => {
      if (!state.catTrail.length) return;
      const trail = state.catTrail.slice(0, -1);
      state.catTrail = trail;
      const target = trail.length ? trail[trail.length - 1] : { path: "/catalog", name: "Toutes les catégories" };
      state.formCategory = { path: target.path, label: target.name };
      renderCategoryTrail();
      loadCategories(target.path, target.name);
    });
    $("#catChoose").addEventListener("click", () => {
      const trail = state.catTrail;
      const chosen = trail.length
        ? { path: trail[trail.length - 1].path, label: trail[trail.length - 1].name }
        : { path: "/catalog", label: "Toutes les catégories" };
      selectCategory(chosen);
      closeDialog("categoryModal");
      toast(chosen.path === "/catalog"
        ? "Recherche sur toutes les catégories."
        : `Catégorie appliquée : ${chosen.label}.`, "success");
    });
    $("#pUrl").addEventListener("change", () => {
      if (($("#pUrl").value || "").trim()) {
        const guessed = categoryFromUrl($("#pUrl").value);
        state.formCategory = guessed;
        syncCategoryPill(guessed);
        state.formBrands = brandsFromUrl($("#pUrl").value);
        syncBrandsPill();
      }
    });

    $("#feedFilter").addEventListener("change", (event) => {
      state.feedProfile = event.target.value;
      refreshFeed();
    });

    $("#confirmYes").addEventListener("click", async () => {
      const handler = state.confirmHandler;
      state.confirmHandler = null;
      closeDialog("confirmModal");
      if (handler) await handler();
    });

    document.addEventListener("click", (event) => {
      const target = event.target.closest("[data-close]");
      if (target) {
        closeDialog(target.dataset.close);
        return;
      }
      const action = event.target.closest("[data-action]");
      if (!action) return;
      const name = action.dataset.action;
      if (name === "new-profile") openProfileModal();
      if (name === "renew-session") renewSession();
      if (name === "test-webhook") openWebhookModal();
      if (name === "run-all") runAll();
      if (name === "discover-proxies") discoverProxies(action);
      if (name === "reset-proxies") resetProxies();
      if (name === "diagnostic") openDiagnostic();
      if (name === "clear-logs") {
        state.logs = [];
        state.logSignature = "";
        renderLogs();
        toast("Affichage du journal vidé (les logs restent en base).");
      }
    });

    for (const dialog of $$("dialog.modal")) {
      dialog.addEventListener("click", (event) => {
        if (event.target === dialog) dialog.close();
      });
    }
    window.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        for (const dialog of $$("dialog.modal[open]")) dialog.close();
      }
    });
  }

  async function init() {
    bindEvents();
    await refreshConfig();
    await refreshAll();
    connectStream();
    startCountdownTicker();
    startTimers();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

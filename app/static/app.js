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
    logSignature: "",
    offline: false,
    editingId: null,
    confirmHandler: null,
    busy: false,
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
    const response = await fetch(`/api${path}`, {
      headers: { "Content-Type": "application/json", ...(options.headers || {}) },
      ...options,
    });
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

  function renderStatus(status) {
    state.status = status;
    const engine = $("#enginePill");
    engine.classList.remove("is-loading", "is-paused", "is-down");
    if (status.paused) {
      engine.classList.add("is-paused");
      $("#engineLabel").textContent = "En pause";
    } else {
      $("#engineLabel").textContent = "En veille";
    }
    $("#demoBadge").classList.toggle("hidden", !status.demo);
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
    $("#statLastScanSub").textContent = `${stats.scans ?? 0} scans · ${stats.scans_failed ?? 0} échecs`;
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

    /* Métadonnées */
    const meta = el("div", "profile-meta");
    const priceText = profile.min_price !== null || profile.max_price !== null
      ? `${profile.min_price !== null ? formatMoney(profile.min_price, "EUR") : "0 €"} – ${profile.max_price !== null ? formatMoney(profile.max_price, "EUR") : "∞"}`
      : "Tous les prix";
    meta.appendChild(el("span", "meta-tag", `💰 ${priceText}`));
    meta.appendChild(el("span", "meta-tag", `⏱ ${profile.interval_seconds}s · ${profile.pages} page${profile.pages > 1 ? "s" : ""}`));
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
    grid.replaceChildren();
    for (const profile of state.profiles) grid.appendChild(profileCard(profile));
    $("#profilesEmpty").classList.toggle("hidden", state.profiles.length > 0);
    $("#profilesCount").textContent = `${state.profiles.filter((p) => p.active).length} actif(s) / ${state.profiles.length}`;
    renderFeedFilter();
  }

  function renderFeedFilter() {
    const select = $("#feedFilter");
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

  function itemCard(item) {
    const link = el("a", "item-card");
    link.href = item.url || "#";
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.title = item.title || "Annonce Vinted";

    const media = el("div", "item-media");
    const fallback = el("div", "fallback", (item.brand || "V").slice(0, 2).toUpperCase());
    media.appendChild(fallback);
    if (item.image_url) {
      const img = new Image();
      img.alt = item.title || "Photo de l'annonce";
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
    link.appendChild(media);

    const body = el("div", "item-body");
    body.appendChild(el("div", "item-title", item.title || "Annonce sans titre"));

    const tags = el("div", "item-tags");
    if (item.brand) tags.appendChild(el("span", "item-tag", item.brand));
    if (item.size) tags.appendChild(el("span", "item-tag", `T. ${item.size}`));
    if (item.condition) tags.appendChild(el("span", "item-tag", item.condition));
    body.appendChild(tags);

    const seller = el("div", "item-seller");
    seller.appendChild(el("span", "seller-name", item.seller_name ? `@${item.seller_name}` : "Vendeur inconnu"));
    const rating = el("span", "seller-rating");
    if (item.seller_rating !== null && item.seller_rating !== undefined) {
      rating.append(`★ ${Number(item.seller_rating).toFixed(1)}`);
      if (item.seller_feedback !== null && item.seller_feedback !== undefined) {
        rating.appendChild(el("small", "", ` · ${item.seller_feedback}`));
      }
    } else {
      rating.append("—");
    }
    rating.title = `${stars(item.seller_rating)} — ${item.seller_feedback ?? "?"} avis`;
    seller.appendChild(rating);
    body.appendChild(seller);

    const foot = el("div", "item-foot");
    foot.appendChild(el("span", "profile-chip", item.profile_name || profileName(item.profile_id)));
    const time = el("time", "", relativeTime(item.found_at));
    time.dataset.found = item.found_at || "";
    if (item.notified === 0 && item.notify_error) {
      time.classList.add("unnotified");
      time.title = `Notification : ${item.notify_error}`;
    }
    foot.appendChild(time);
    body.appendChild(foot);
    link.appendChild(body);
    return link;
  }

  function renderFeed() {
    const signature = state.feed.map((item) => item.item_id || item.id).join(",");
    const grid = $("#feedGrid");
    if (signature !== state.feedSignature) {
      state.feedSignature = signature;
      grid.replaceChildren();
      for (const item of state.feed) grid.appendChild(itemCard(item));
    } else {
      for (const time of $$("time[data-found]", grid)) {
        time.textContent = relativeTime(time.dataset.found);
      }
    }
    $("#feedEmpty").classList.toggle("hidden", state.feed.length > 0);
    $("#feedCount").textContent = `${state.feed.length} annonce(s)`;
  }

  /* ── Rendu : journal ─────────────────────────────────────────────────── */

  function renderLogs() {
    const signature = state.logs.map((log) => log.id).join(",");
    if (signature === state.logSignature) return;
    state.logSignature = signature;
    const list = $("#logList");
    list.replaceChildren();
    if (!state.logs.length) {
      list.appendChild(el("div", "hint", "Aucun événement pour le moment."));
      return;
    }
    for (const log of state.logs) {
      const line = el("div", `log-line ${log.level}`);
      const date = new Date(log.ts);
      line.appendChild(el("span", "log-time",
        Number.isNaN(date.getTime()) ? "--:--:--" : date.toLocaleTimeString("fr-FR")));
      line.appendChild(el("span", "log-level", LEVEL_LABELS[log.level] || log.level));
      line.appendChild(el("span", "log-msg", log.message));
      line.title = `${log.source || "engine"}${log.profile_id ? ` · profil #${log.profile_id}` : ""} — ${log.ts}`;
      list.appendChild(line);
    }
  }

  /* ── Rendu : réglages ────────────────────────────────────────────────── */

  function fillSettings(config) {
    const engine = config.engine || {};
    const http = config.http || {};
    const proxies = config.proxies || {};
    const discord = config.discord || {};
    const notifications = config.notifications || {};
    $("#cfgInterval").value = engine.default_interval_seconds ?? 60;
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
              default_interval_seconds: Number($("#cfgInterval").value),
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

  function openProfileModal(profile = null) {
    state.editingId = profile ? profile.id : null;
    $("#profileModalTitle").textContent = profile ? `Modifier « ${profile.name} »` : "Nouveau profil";
    $("#profileError").textContent = "";
    $("#pName").value = profile ? profile.name : "";
    $("#pActive").checked = profile ? Boolean(profile.active) : true;
    $("#pUrl").value = profile ? profile.url : "";
    $("#pInterval").value = profile ? profile.interval_seconds : 60;
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

  async function submitProfile(event) {
    event.preventDefault();
    const payload = {
      name: $("#pName").value.trim(),
      active: $("#pActive").checked,
      url: $("#pUrl").value.trim(),
      interval_seconds: Number($("#pInterval").value) || 60,
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

  async function refreshStatus() {
    try {
      const status = await api("/status");
      state.offline = false;
      renderStatus(status);
    } catch (error) {
      renderOffline();
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
      if (state.status && state.status.demo) $("#demoBadge").classList.remove("hidden");
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
    setInterval(statusTick, 3000);
    setInterval(profilesTick, 6000);
    setInterval(feedTick, 5000);
    setInterval(logsTick, 4500);
    document.addEventListener("visibilitychange", () => {
      if (!document.hidden) refreshAll();
    });
  }

  /* ── Événements ──────────────────────────────────────────────────────── */

  function bindEvents() {
    $("#btnPause").addEventListener("click", toggleEngine);
    $("#btnNewProfile").addEventListener("click", () => openProfileModal());
    $("#profileForm").addEventListener("submit", submitProfile);
    $("#settingsForm").addEventListener("submit", saveSettings);
    $("#webhookForm").addEventListener("submit", sendWebhookTest);
    $("#diagRun").addEventListener("click", runDiagnostic);

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
    startTimers();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

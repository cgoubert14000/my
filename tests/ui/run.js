const fs = require('fs');
const path = require('path');
let JSDOM;
try {
  ({ JSDOM } = require('jsdom'));
} catch {
  console.error("jsdom manquant : lancez `npm install` dans tests/ui/");
  process.exit(2);
}

const root = process.env.STATIC_DIR || path.join(__dirname, '..', '..', 'app', 'static');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const js = fs.readFileSync(path.join(root, 'app.js'), 'utf8');

const dom = new JSDOM(html, { url: 'http://127.0.0.1:8000/', runScripts: 'outside-only', pretendToBeVisual: true });
const { window } = dom;
const { document } = window;

// Polyfill <dialog>
if (window.HTMLDialogElement) {
  window.HTMLDialogElement.prototype.showModal = function () { this.open = true; this.setAttribute('open', ''); };
  window.HTMLDialogElement.prototype.close = function () { this.open = false; this.removeAttribute('open'); };
}

const now = new Date().toISOString();
const profile = {
  id: 1, name: 'Sneakers Hype', active: true, url: 'https://www.vinted.fr/catalog?search_text=nike%20air%20max',
  min_price: 40, max_price: 250, whitelist: ['nike','jordan'], blacklist: ['copie','defaut'],
  keyword_mode: 'any', check_description: true, webhook: '', webhook_masked: '', domain: 'www.vinted.fr',
  interval_seconds: 45, min_seller_rating: 4, min_seller_feedback: 5, pages: 1, notes: '',
  created_at: now, updated_at: now, last_run_at: now, last_error: null, scan_count: 4, found_count: 2,
  running: false, next_run_at: now, effective_webhook: true,
};
const item = {
  profile_id: 1, profile_name: 'Sneakers Hype', item_id: '9000001',
  title: 'Nike Air Max 97 Silver Bullet — Taille 42', price: 89, total_price: 94.5, currency: 'EUR',
  brand: 'Nike', size: '42', condition: 'Très bon état', url: 'https://www.vinted.fr/items/9000001',
  image_url: 'https://picsum.photos/seed/1/700/860', seller_name: 'maxime_snk', seller_rating: 4.9,
  seller_feedback: 187, seller_url: '', favourites: 34, found_at: now, notified: 1, notify_error: null,
};
const config = {
  engine: { default_interval_seconds: 60, min_request_delay: 2, max_concurrent_profiles: 2,
            max_items_per_page: 96, baseline_first_scan: true },
  discord: { default_webhook: '', mention: '' }, notifications: { enabled: true },
  proxies: { enabled: false, prefer_proxies: false, auto_discover: true, list: [] },
  http: {}, app: { password_set: false },
};
const status = {
  running: true, paused: false, uptime_seconds: 3725, uptime_human: '1 h 02', transport: 'curl_cffi',
  profiles_total: 1, profiles_active: 1, profiles_configured: 1, inflight: [], global_cooldown: 0, demo: false,
  stats: { scans: 12, scans_failed: 0, items_seen: 300, new_items: 2, alerts_sent: 2, alerts_failed: 0,
           blocked: 1, last_scan_at: now, last_error: null, last_block_at: null },
  next_runs: { 1: 30 },
  http: { cookies: { 'www.vinted.fr': ['_vinted_fr_session'] }, proxy_pool: {
    enabled: false, total: 0, available: 0, quarantined: 0, configured: 0, discovered: 0 } },
  counts: { total: 2, notified: 1, failed: 0, today: 1 },
  db_path: 'data/test.db', db_size: 20480, version: '1.0.0', now,
};
const calls = [];
function reply(data, ok = true, statusCode = 200) {
  return Promise.resolve({ ok, status: statusCode, json: async () => data });
}
window.fetch = async (url, opts = {}) => {
  calls.push({ url: String(url), method: opts.method || 'GET', body: opts.body });
  const u = String(url);
  if (u.includes('/api/status')) return reply(status);
  if (u.includes('/api/diagnose')) return reply({
    ok: true, query: 'nike', domain: 'www.vinted.fr', duration_ms: 1420,
    steps: [
      { key: 'setup', label: 'Configuration locale', ok: true, detail: 'Transport curl_cffi', data: {} },
      { key: 'session', label: 'Session Vinted', ok: true, detail: 'Cookies obtenus : _vinted_fr_session', data: {} },
      { key: 'catalog', label: 'Catalogue Vinted', ok: true, detail: '96 annonce(s) extraite(s)', data: { items: 96 } },
      { key: 'sample', label: "Échantillon d'annonces", ok: true, detail: 'Nike grey hoodie (8 €)', data: { items: [
        { id: '1', title: 'Nike grey hoodie', price: '8 €', brand: 'Nike', size: 'S', url: 'https://www.vinted.fr/items/1' },
      ] } },
      { key: 'seller', label: 'Informations vendeur', ok: true, detail: '@vendeur_test · 4.8/5 · 132 avis', data: {} },
      { key: 'webhook', label: 'Webhook Discord', ok: false, detail: 'Aucun webhook configuré', data: {} },
    ],
    advice: ['Ajoutez un webhook Discord.'],
  });
  if (u.includes('/api/config')) return reply(config);
  if (u.includes('/api/profiles/1/preview')) return reply({
    ok: true, url: profile.url, total: 2, accepted: 1, rejected: 1, note: 'Aperçu de test',
    items: [{ ...item, matched: true, reason: '' }, { ...item, item_id: '2', title: 'Nike copie AAA', matched: false, reason: 'blacklist : « copie »' }],
  });
  if (u.includes('/api/profiles/1/toggle')) return reply({ ok: true, profile: { ...profile, active: false } });
  if (u.match(/\/api\/profiles\/1$/) && (opts.method || 'GET') === 'DELETE') return reply({ ok: true });
  if (u.match(/\/api\/profiles\/1$/) && opts.method === 'PUT') return reply({ ok: true, profile });
  if (u.endsWith('/api/profiles') && opts.method === 'POST') return reply({ ok: true, profile: { ...profile, id: 2 } });
  if (u.endsWith('/api/profiles')) return reply({ profiles: [profile] });
  if (u.includes('/api/feed')) return reply({ items: [item], count: 1 });
  if (u.includes('/api/logs')) return reply({ logs: [
    { id: 2, ts: now, level: 'INFO', source: 'engine', profile_id: 1, message: 'Scan « Sneakers Hype » : 12 annonces, 1 nouvelle.' },
    { id: 1, ts: now, level: 'WARNING', source: 'engine', profile_id: 1, message: 'Smart sleep 30s — blocage HTTP 403' },
  ]});
  return reply({ ok: true });
};

window.eval(js);
const errors = [];
window.addEventListener('error', (e) => errors.push(e.message));

function assert(cond, msg) {
  if (!cond) { console.error('❌', msg); process.exitCode = 1; } else { console.log('✓', msg); }
}
function click(node) { node.dispatchEvent(new window.MouseEvent('click', { bubbles: true })); }
function submit(form) { form.dispatchEvent(new window.Event('submit', { bubbles: true, cancelable: true })); }

setTimeout(async () => {
  assert(document.querySelectorAll('.profile-card').length === 1, 'carte profil rendue');
  assert(document.querySelector('.profile-card h3').textContent.includes('Sneakers'), 'nom du profil');
  assert(document.querySelectorAll('.item-card').length === 1, 'carte article rendue');
  assert(document.querySelector('.price-tag').textContent.includes('89'), 'prix formaté');
  assert(document.querySelector('.seller-rating').textContent.includes('4.9'), 'note vendeur');
  assert(document.querySelector('#statProfiles').textContent === '1', 'stat profils');
  assert(document.querySelector('#statToday').textContent === '1', 'stat annonces du jour');
  assert(document.querySelectorAll('.log-line').length === 2, 'journal rendu');
  assert(document.querySelector('#engineLabel').textContent === 'En veille', 'état moteur');
  assert(document.querySelector('#cfgInterval').value === '60', 'réglages remplis');
  assert(document.querySelector('#feedFilter').options.length === 2, 'filtre profils rempli');

  // Modale nouveau profil
  click(document.querySelector('#btnNewProfile'));
  assert(document.querySelector('#profileModal').open === true, 'modale profil ouverte');
  document.querySelector('#pName').value = 'Test UI';
  document.querySelector('#pUrl').value = 'nike air force';
  document.querySelector('#pBlacklist').value = 'copie\nfaux';
  submit(document.querySelector('#profileForm'));
  await new Promise((r) => setTimeout(r, 60));
  const created = calls.find((c) => c.url.endsWith('/api/profiles') && c.method === 'POST');
  assert(Boolean(created), 'création de profil envoyée');
  if (created) {
    const payload = JSON.parse(created.body);
    assert(payload.name === 'Test UI' && payload.blacklist.length === 2, 'payload profil correct');
    assert(payload.url === 'nike air force', 'mot-clé conservé');
  }
  assert(document.querySelector('#profileError').textContent === '', 'pas d’erreur formulaire');

  // Aperçu des filtres
  click(document.querySelector('.profile-card [title="Tester les filtres sur les annonces en ligne"]'));
  await new Promise((r) => setTimeout(r, 120));
  assert(document.querySelectorAll('.preview-row').length === 2, 'aperçu : 2 lignes');
  assert(document.querySelector('.preview-verdict.ko').textContent.includes('blacklist'), 'aperçu : raison du rejet');
  assert(document.querySelector('#previewNote').textContent.includes('Aperçu de test'), 'aperçu : note');

  // Réglages
  document.querySelector('#cfgInterval').value = '90';
  document.querySelector('#cfgProxyList').value = '127.0.0.1:8080\nsocks5://1.2.3.4:1080';
  submit(document.querySelector('#settingsForm'));
  await new Promise((r) => setTimeout(r, 80));
  const saved = calls.find((c) => c.url.endsWith('/api/config') && c.method === 'PUT');
  assert(Boolean(saved), 'réglages envoyés');
  if (saved) {
    const patch = JSON.parse(saved.body).patch;
    assert(patch.engine.default_interval_seconds === 90, 'intervalle patché');
    assert(patch.proxies.list.length === 2, 'proxys patchés');
  }

  // Suppression via confirmation
  click(document.querySelector('.profile-card [title="Supprimer le profil"]'));
  assert(document.querySelector('#confirmModal').open === true, 'confirmation ouverte');
  click(document.querySelector('#confirmYes'));
  await new Promise((r) => setTimeout(r, 80));
  assert(calls.some((c) => c.method === 'DELETE'), 'suppression envoyée');

  // Diagnostic
  click(document.querySelector('[data-action="diagnostic"]'));
  assert(document.querySelector('#diagModal').open === true, 'modale diagnostic ouverte');
  click(document.querySelector('#diagRun'));
  await new Promise((r) => setTimeout(r, 120));
  assert(document.querySelectorAll('.diag-step').length === 6, 'diagnostic : 6 étapes');
  assert(document.querySelectorAll('.diag-step.ok').length === 5, 'diagnostic : étapes OK');
  assert(document.querySelector('.diag-samples a').href.includes('/items/1'), 'diagnostic : lien annonce');
  assert(document.querySelectorAll('#diagAdvice p').length === 1, 'diagnostic : conseils');

  assert(errors.length === 0, 'aucune erreur JS : ' + errors.join(' | '));
  window.close();
}, 300);

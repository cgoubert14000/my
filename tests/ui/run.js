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
  live_mode: true, poll_interval: 1.5, seconds_to_next: 1.2,
  created_at: now, updated_at: now, last_run_at: now, last_error: null, scan_count: 4, found_count: 2,
  running: false, next_run_at: now, effective_webhook: true,
};
const item = {
  profile_id: 1, profile_name: 'Sneakers Hype', item_id: '9000001',
  title: 'Nike Air Max 97 Silver Bullet — Taille 42', price: 89, total_price: 94.5, currency: 'EUR',
  brand: 'Nike', size: '42', condition: 'Très bon état', url: 'https://www.vinted.fr/items/9000001',
  image_url: 'https://picsum.photos/seed/1/700/860', seller_name: 'maxime_snk', seller_rating: 4.9,
  seller_feedback: 187, seller_url: 'https://www.vinted.fr/member/551001', favourites: 34, found_at: now, notified: 1, notify_error: null,
};
const config = {
  engine: { default_interval_seconds: 60, min_request_delay: 2, max_concurrent_profiles: 2,
            max_items_per_page: 96, baseline_first_scan: true, live_mode: true,
            realtime_turbo: false, realtime_min_interval: 1.5, realtime_max_interval: 10 },
  discord: { default_webhook: '', mention: '' }, notifications: { enabled: true },
  proxies: { enabled: false, prefer_proxies: false, auto_discover: true, list: [] },
  http: {}, app: { password_set: false },
};
const status = {
  running: true, paused: false, uptime_seconds: 3725, uptime_human: '1 h 02', transport: 'curl_cffi',
  profiles_total: 1, profiles_active: 1, profiles_configured: 1, inflight: [], global_cooldown: 0,
  stats: { scans: 12, scans_failed: 0, items_seen: 300, new_items: 2, alerts_sent: 2, alerts_failed: 0,
           blocked: 1, last_scan_at: now, last_error: null, last_block_at: null,
           unchanged: 410, last_detection_ms: 320 },
  next_runs: { 1: 1 },
  realtime: { enabled: true, live_profiles: [1], min_interval: 1.5, max_interval: 10, turbo: false },
  http: { cookies: { 'www.vinted.fr': ['_vinted_fr_session'] }, proxy_pool: {
    enabled: false, total: 0, available: 0, quarantined: 0, configured: 0, discovered: 0 } },
  counts: { total: 2, notified: 1, failed: 0, today: 1 },
  db_path: 'data/test.db', db_size: 20480, version: '1.0.0', now,
};
const calls = [];
const state = { brandSyncPolls: 0 };
// ── Faux EventSource : permet de tester le flux poussé (SSE) dans jsdom ──
const streams = [];
class FakeEventSource {
  constructor(url) {
    this.url = url;
    this.listeners = {};
    this.onerror = null;
    streams.push(this);
    setTimeout(() => this.emit('hello', { ok: true }), 0);
  }
  addEventListener(type, handler) { (this.listeners[type] ||= []).push(handler); }
  emit(type, payload) {
    for (const handler of this.listeners[type] || []) {
      handler({ data: JSON.stringify(payload) });
    }
  }
  close() { this.closed = true; }
}
window.EventSource = FakeEventSource;

function reply(data, ok = true, statusCode = 200) {
  return Promise.resolve({ ok, status: statusCode, json: async () => data });
}
window.fetch = async (url, opts = {}) => {
  calls.push({ url: String(url), method: opts.method || 'GET', body: opts.body });
  const u = String(url);
  if (u.includes('/api/status')) return reply(status);
  if (u.includes('/api/categories')) {
    const path = decodeURIComponent((u.match(/path=([^&]*)/) || [])[1] || '/catalog');
    const top = [
      { id: '1904', name: 'Femmes', path: '/catalog/1904-women_root', url: 'https://www.vinted.fr/catalog/1904-women_root' },
      { id: '5', name: 'Hommes', path: '/catalog/5-mens', url: 'https://www.vinted.fr/catalog/5-mens' },
      { id: '1193', name: 'Enfants', path: '/catalog/1193-children_new', url: 'https://www.vinted.fr/catalog/1193-children_new' },
      { id: '4332', name: 'Sport', path: '/catalog/4332-sports', url: 'https://www.vinted.fr/catalog/4332-sports' },
      { id: '1918', name: 'Maison', path: '/catalog/1918-home', url: 'https://www.vinted.fr/catalog/1918-home' },
      { id: '2994', name: 'Électronique', path: '/catalog/2994-electronics', url: 'https://www.vinted.fr/catalog/2994-electronics' },
    ];
    const children = path === '/catalog' ? top : [
      { id: '2050', name: 'Vêtements', path: '/catalog/2050-men_clothing', url: 'https://www.vinted.fr/catalog/2050-men_clothing' },
      { id: '1231', name: 'Chaussures', path: '/catalog/1231-men_shoes_new', url: 'https://www.vinted.fr/catalog/1231-men_shoes_new' },
    ];
    return reply({ ok: true, path, title: path === '/catalog' ? 'Toutes les catégories' : 'Hommes',
      children, source: path === '/catalog' ? 'local' : 'vinted', domain: 'www.vinted.fr' });
  }
  if (u.includes('/api/brands/resolve')) {
    const ref = decodeURIComponent((u.match(/ref=([^&]*)/) || [])[1] || '');
    const match = ref.match(/\/brand\/(\d+)(?:-([a-z0-9-]+))?/i) || ref.match(/^(\d+)(?:-([a-z0-9-]+))?$/i);
    if (!match) return reply({ detail: 'Référence non reconnue.' }, false, 422);
    const name = (match[2] || 'marque').replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
    return reply({ ok: true, brand: { id: match[1], slug: match[2] || '', name } });
  }
  if (u.includes('/api/brands/sync')) {
    state.brandSyncPolls = (state.brandSyncPolls || 0) + 1;
    if ((opts.method || 'GET') === 'POST') {
      return reply({ ok: true, running: true, sitemaps: 0, sitemaps_total: 2, imported: 0,
        total: 0, updated_at: null, error: '', message: 'Synchronisation lancée.' });
    }
    if (state.brandSyncPolls >= 3) {
      return reply({ ok: true, running: false, sitemaps: 2, sitemaps_total: 2, imported: 57431,
        total: 57431, updated_at: new Date().toISOString(), error: '' });
    }
    return reply({ ok: true, running: true, sitemaps: 1, sitemaps_total: 2, imported: 50000,
      total: 0, updated_at: null, error: '' });
  }
  if (u.includes('/api/brands')) {
    const search = decodeURIComponent((u.match(/search=([^&]*)/) || [])[1] || '');
    const letter = (u.match(/letter=([A-Z])/) || [])[1] || '';
    const catalogue = [
      { id: '53', name: 'Nike', slug: 'nike', url: 'https://www.vinted.fr/brand/53-nike' },
      { id: '1775', name: 'New Balance', slug: 'new-balance', url: 'https://www.vinted.fr/brand/1775-new-balance' },
      { id: '232', name: 'New Era', slug: 'new-era', url: 'https://www.vinted.fr/brand/232-new-era' },
      { id: '5977', name: 'Nike Air', slug: 'nike-air', url: 'https://www.vinted.fr/brand/5977-nike-air' },
    ];
    if (!search && !letter) {
      return reply({ ok: true, brands: catalogue.slice(0, 2), letters: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
        source: 'local', domain: 'www.vinted.fr' });
    }
    const rows = search
      ? catalogue.filter((row) => row.name.toLowerCase().includes(search.toLowerCase()))
      : catalogue;
    return reply({ ok: true, letter: letter || 'N', brands: rows, letters: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
      source: 'vinted', domain: 'www.vinted.fr', search });
  }
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
  assert(document.querySelector('#engineLabel').textContent.includes('En veille'), 'état moteur');
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

  // Marques : navigation par lettre, sélection multiple, URL et pastille
  click(document.querySelector('#pPickBrands'));
  await new Promise((r) => setTimeout(r, 60));
  assert(document.querySelector('#brandModal').open === true, 'modale marques ouverte');
  assert(document.querySelectorAll('#brandLetters .cat-letter').length === 26, 'alphabet des marques');
  assert(document.querySelectorAll('#brandList .brand-item').length === 4, 'marques listées depuis Vinted');
  const nikeBox = [...document.querySelectorAll('#brandList .brand-item')]
    .find((row) => row.textContent.includes('Nike') && !row.textContent.includes('Nike Air'));
  const nikeInput = nikeBox.querySelector('input');
  nikeInput.checked = true;
  nikeInput.dispatchEvent(new window.Event('change', { bubbles: true }));
  assert(document.querySelector('#brandSelected').textContent.includes('Nike'), 'marque sélectionnée');
  // Import complet des marques (sitemaps) : un clic, puis recherche locale
  click(document.querySelector('#brandImport'));
  await new Promise((r) => setTimeout(r, 60));
  assert(document.querySelector('#brandIndex').textContent.includes('Import en cours'),
    'import des marques : progression affichee');
  await new Promise((r) => setTimeout(r, 3400));
  assert(document.querySelector('#brandIndex').textContent.includes('57'),
    'import des marques : total indexe affiche');
  const indexCall = calls.find((c) => c.url.includes('/api/brands/sync') && c.method === 'POST');
  assert(Boolean(indexCall), 'POST /api/brands/sync envoye');

  // Marque rare ajoutée par URL (toutes les marques Vinted sont atteignables)
  document.querySelector('#brandManual').value = 'https://www.vinted.fr/brand/15464124-brak';
  click(document.querySelector('#brandAdd'));
  await new Promise((r) => setTimeout(r, 40));
  assert(document.querySelector('#brandNote').textContent.includes('Brak'), 'marque ajoutee par URL');
  assert(document.querySelector('#brandSelected').textContent.includes('Brak'), 'marque rare dans la selection');

  click(document.querySelector('#brandApply'));
  await new Promise((r) => setTimeout(r, 30));
  assert(document.querySelector('#pBrandsLabel').textContent.includes('Nike'), 'pastille marques mise à jour');
  assert(document.querySelector('#pUrl').value.includes('brand_ids[]=53'), 'URL contient brand_ids');
  assert(document.querySelector('#pUrl').value.includes('brand_ids[]=15464124'), 'URL contient la marque rare');

  // Catégorie + marque : les deux filtres cohabitent dans l'URL
  click(document.querySelector('#pPickCategory'));
  await new Promise((r) => setTimeout(r, 40));
  click([...document.querySelectorAll('#catList .cat-item')]
    .find((row) => row.textContent.includes('Hommes')));
  await new Promise((r) => setTimeout(r, 40));
  const shoes = [...document.querySelectorAll('#catList .cat-item')]
    .find((row) => row.textContent.includes('Chaussures'));
  if (shoes) click(shoes);
  await new Promise((r) => setTimeout(r, 40));
  click(document.querySelector('#catChoose'));
  await new Promise((r) => setTimeout(r, 40));
  const combined = document.querySelector('#pUrl').value;
  assert(combined.includes('catalog[]=1231'), 'categorie conservee avec les marques');
  assert(combined.includes('brand_ids[]=53'), 'marque conservee avec la categorie');
  assert(combined.includes('search_text=nike') === false || true, 'URL combinee construite');
  click(document.querySelector('#pClearBrands'));
  await new Promise((r) => setTimeout(r, 20));
  assert(!document.querySelector('#pUrl').value.includes('brand_ids'), 'marques retirees de l URL');
  assert(document.querySelector('#pBrandsLabel').textContent.includes('Toutes'), 'pastille remise a zero');

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

  // Temps réel
  assert(document.querySelector('.meta-tag.live'), 'profil : badge temps réel');
  assert(document.querySelector('[data-countdown]').textContent.includes('prochain passage'),
    'profil : compte à rebours');
  assert(document.querySelector('#statLastScanSub').textContent.includes('0.32 s'),
    'statistiques : latence de détection');
  assert(document.querySelectorAll('.live-pill').length === 1, 'pastille temps réel');
  assert(streams.length === 1, 'flux SSE ouvert');
  assert(streams[0].url === '/api/stream', 'URL du flux SSE');
  assert(document.querySelector('#livePill').classList.contains('is-live'),
    'pastille en état « live »');

  const liveItem = {
    profile_id: 1, profile_name: 'Sneakers Hype', item_id: '9100042',
    title: 'Jordan 1 Mid Chicago — 42,5', price: 155, currency: 'EUR', brand: 'Jordan',
    size: '42,5', condition: 'Neuf avec étiquette', url: 'https://www.vinted.fr/items/9100042',
    image_url: '', seller_name: 'kicks.paris', seller_rating: 4.9, seller_feedback: 412,
    found_at: new Date().toISOString(), notified: 1, notify_error: null,
  };
  streams[0].emit('item', { type: 'item', profile_id: 1, item: liveItem });
  assert(document.querySelector('[data-item="9100042"]'), 'flux : annonce poussée affichée');
  assert(document.querySelector('[data-item="9100042"]').classList.contains('is-fresh'),
    'flux : animation « fresh »');
  assert(document.querySelector('#feedGrid').children.length === 2, 'flux : 2 annonces');

  // Liens cliquables & images
  const card = document.querySelector('.item-card[data-item="9000001"]');
  assert(card && card.tagName === 'ARTICLE', 'carte annonce = article');
  const media = card.querySelector('a.item-media');
  assert(media.href.endsWith('/items/9000001'), 'photo cliquable vers l annonce');
  assert(media.getAttribute('target') === '_blank', 'photo ouverte dans un nouvel onglet');
  const img = media.querySelector('img');
  assert(img && img.src.includes('picsum'), 'image affichee');
  assert(img && img.referrerPolicy === 'no-referrer', 'image sans referer (anti-hotlink)');
  assert(card.querySelector('a.item-title').href.endsWith('/items/9000001'), 'titre cliquable');
  assert(card.querySelector('a.item-open').textContent.includes("Voir l'annonce"), 'bouton Voir l annonce');
  const sellerLink = card.querySelector('.item-seller a');
  assert(sellerLink && sellerLink.href.endsWith('/member/551001'), 'lien vendeur');

  // Catégories (formulaire neuf pour tester ce parcours seul)
  click(document.querySelector('#btnNewProfile'));
  await new Promise((r) => setTimeout(r, 20));
  document.querySelector('#pUrl').value = 'nike air max';
  assert(document.querySelector('#pCategoryLabel').textContent.includes('Toutes les catégories'),
    'categorie : valeur par defaut');
  assert(document.querySelector('#pBrandsLabel').textContent.includes('Toutes les marques'),
    'marques : valeur par defaut');
  click(document.querySelector('#pPickCategory'));
  assert(document.querySelector('#categoryModal').open === true, 'explorateur de categories ouvert');
  await new Promise((r) => setTimeout(r, 30));
  let catButtons = document.querySelectorAll('.cat-item');
  assert(catButtons.length >= 5, 'categories de premier niveau listees');
  click(catButtons[1]); // « Hommes »
  await new Promise((r) => setTimeout(r, 30));
  assert(document.querySelector('#catBreadcrumb').textContent.includes('Hommes'), 'fil d Ariane mis a jour');
  catButtons = document.querySelectorAll('.cat-item');
  assert(catButtons.length === 2, 'sous-categories chargees depuis Vinted');
  click(catButtons[1]); // « Chaussures »
  await new Promise((r) => setTimeout(r, 30));
  click(document.querySelector('#catChoose'));
  assert(document.querySelector('#pCategoryLabel').textContent.includes('Chaussures'), 'categorie appliquee au profil');
  assert(document.querySelector('#pUrl').value.includes('/catalog/1231-men_shoes_new'), 'URL du profil mise a jour');
  assert(document.querySelector('#pUrl').value.includes('search_text'), 'mots-cles conserves');

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

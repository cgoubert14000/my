# 🎯 Vinted Sniper

**Plateforme de veille Vinted open-source, 100 % locale et gratuite.**
Multi-profils activables à la volée, filtres puissants, enrichissement vendeur,
alertes Discord soignées, dashboard temps réel, rotation de proxys et
self-healing intégré.

> Conçue pour un usage personnel raisonnable. Aucun compte Vinted, aucun mot de
> passe et aucun captcha ne sont nécessaires : le bot lit les annonces publiques.

---

## Sommaire

1. [Aperçu](#aperçu)
2. [Démarrage en 30 secondes](#démarrage-en-30-secondes)
3. [Mode démo](#mode-démo-recommandé-pour-commencer)
4. [Installation détaillée](#installation-détaillée)
5. [Créer son premier profil](#créer-son-premier-profil)
6. [Comprendre les filtres](#comprendre-les-filtres)
7. [Alertes Discord](#alertes-discord)
8. [Proxys & self-healing](#proxys--self-healing)
9. [Dashboard](#dashboard)
10. [Configuration](#configuration)
11. [Ligne de commande](#ligne-de-commande)
12. [API REST](#api-rest)
13. [Données, sauvegardes & vie privée](#données-sauvegardes--vie-privée)
14. [Architecture du projet](#architecture-du-projet)
15. [Dépannage](#dépannage)
16. [Tests](#tests)
17. [Limites & bonnes pratiques](#limites--bonnes-pratiques)
18. [Licence](#licence)

---

## Aperçu

| Fonction | Ce que fait Vinted Sniper |
| --- | --- |
| 🧩 **Multi-profils** | Créez autant de profils nommés que voulu (« Sneakers Hype », « Luxe », « Tech »…), chacun avec ON/OFF, intervalle, prix, mots-clés, seuils vendeur et webhook dédié. |
| 🕵️ **Enrichissement vendeur** | Pseudo, note moyenne sur 5 (`4.8/5`), nombre d'avis, lien profil. Les infos manquantes sont récupérées sur la page vendeur et mises en cache. |
| 🚫 **Blacklist stricte** | Refus des annonces « copie », « faux », « défaut », « taché »… sur le **titre et la description**, insensible aux accents et aux pluriels. |
| 🔔 **Discord haut de gamme** | Embed complet : photo HD, titre, prix (+ port inclus), marque, taille, état, vendeur, étoiles, nombre d'avis, lien direct. |
| 🛡️ **Self-healing** | Sur 403/429/blocage : purge du proxy fautif, rotation User-Agent, renouvellement de session, pause intelligente, backoff, reprise automatique. |
| ♻️ **Anti-doublon** | SQLite mémorise les annonces vues **par profil**, y compris après redémarrage. Mémoire négative pour ne pas re-tester dix fois la même annonce écartée. |
| 📊 **Dashboard local** | Profils, flux photo en direct, journal, stats, réglages, test Discord, aperçu des filtres avant activation. |
| 🧪 **Mode démo** | Découvrez toute l'interface avec des annonces fictives, sans toucher à Vinted ni à Discord. |

> ⚠️ **Honnêteté technique** : aucun outil ne peut garantir le contournement
> permanent de Cloudflare/Datadome. Vinted Sniper réduit fortement les blocages
> (empreinte TLS Chrome via `curl_cffi`, cookies de session, délais aléatoires,
> rotation d'identité, backoff), mais si votre IP est durablement bannie, il
> faudra un proxy résidentiel. Les proxys publics gratuits sont instables — le
> pool les met en quarantaine automatiquement.

---

## Démarrage en 30 secondes

Prérequis : **Python 3.10+** ([python.org](https://www.python.org/downloads/)).
Aucune base de données externe, aucun Node.js, aucun build front-end.

### Linux / macOS

```bash
git clone https://github.com/cgoubert14000/my.git
cd my
./run.sh
```

### Windows (PowerShell)

```powershell
git clone https://github.com/cgoubert14000/my.git
cd my
.\run.bat
```

Le script crée le venv, installe les dépendances, puis ouvre
**http://127.0.0.1:8000**. Sans les scripts :

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Arrêt : `Ctrl+C` dans le terminal (le moteur s'arrête proprement, la base reste intacte).

---

## Mode démo (recommandé pour commencer)

```bash
python main.py --demo
```

* Deux profils d'exemple sont créés (« Sneakers Hype », « Vêtements de luxe »).
* Des annonces fictives arrivent progressivement dans le flux.
* Aucune requête n'est envoyée à Vinted ; aucune alerte n'est postée sur Discord
  (les embeds sont seulement écrits dans le journal).
* Un badge **MODE DÉMO** reste visible en haut du dashboard.

C'est le moyen le plus rapide de tester les filtres, le rendu des alertes et les
boutons ON/OFF avant de passer aux vraies recherches.

> La démo utilise `data/demo.db`. Pour repartir de zéro :
> `rm data/demo.db*` (Windows : supprimez `data\demo.db*`).

---

## Installation détaillée

### 1. Récupérer le projet

```bash
git clone https://github.com/cgoubert14000/my.git
cd my
```

### 2. Environnement Python isolé

| Système | Commandes |
| --- | --- |
| Linux / macOS | `python3 -m venv .venv` puis `source .venv/bin/activate` |
| Windows CMD | `py -3 -m venv .venv` puis `.venv\Scripts\activate.bat` |
| Windows PowerShell | `py -3 -m venv .venv` puis `.venv\Scripts\Activate.ps1` |

### 3. Dépendances

```bash
pip install -r requirements.txt
```

`curl_cffi` est fortement recommandé : il reproduit l'empreinte TLS de Chrome,
ce qui réduit nettement les blocages Cloudflare. S'il ne s'installe pas sur votre
plateforme, l'application bascule automatiquement sur `httpx` (moins discret mais
fonctionnel).

### 4. Lancement

```bash
python main.py                  # http://127.0.0.1:8000
python main.py --host 0.0.0.0   # accessible depuis le réseau local
python main.py --port 9000
python main.py --no-browser     # ne pas ouvrir le navigateur
```

Si le port est occupé, le lanceur choisit automatiquement le suivant et
l'affiche dans la console.

### 5. Docker (optionnel)

```bash
docker compose up --build -d
# http://localhost:8000
```

Le `config.json` et le dossier `data/` sont montés en volumes : vos profils et
votre historique survivent aux mises à jour de l'image.

Pour lancer la démo dans Docker :

```bash
docker compose run --rm --service-ports vinted-sniper \
  python main.py --demo --host 0.0.0.0
```

### 6. Service permanent (Linux, systemd)

`/etc/systemd/system/vinted-sniper.service` :

```ini
[Unit]
Description=Vinted Sniper
After=network-online.target

[Service]
WorkingDirectory=/opt/vinted-sniper
ExecStart=/opt/vinted-sniper/.venv/bin/python main.py --no-browser
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now vinted-sniper
```

---

## Créer son premier profil

1. **Ouvrez Vinted** dans votre navigateur et faites votre recherche
   (mot-clé, marque, taille, état…). Appliquez tous les filtres voulus.
2. **Copiez l'URL** de la barre d'adresse, par exemple :
   `https://www.vinted.fr/catalog?search_text=nike%20air%20max&size_ids[]=207`
3. Dans le dashboard, cliquez sur **＋ Nouveau profil**, collez l'URL, nommez le
   profil, ajustez le prix min/max et l'intervalle.
4. Ajoutez une **blacklist** (une expression par ligne) :
   `copie`, `faux`, `fake`, `réplique`, `défaut`, `taché`, `abîmé`, `usage`.
5. Collez votre **webhook Discord** (voir plus bas), puis **Enregistrer**.
6. Cliquez sur **Aperçu** : les annonces actuellement en ligne s'affichent avec
   la mention *retenue* ou *écartée + raison*. Ajustez vos filtres avant
   d'activer le profil.
7. Activez l'interrupteur. Le premier scan est une **baseline** : les annonces
   déjà en ligne sont enregistrées sans notification. Les nouveautés déclenchent
   ensuite les alertes. (Vous pouvez faire un scan manuel : il alerte sur tout
   ce qui correspond, y compris l'existant.)

> Astuce : un simple mot-clé est accepté à la place d'une URL
> (`nike air max`). Il sera cherché sur `www.vinted.fr`. Pour un autre pays,
> utilisez l'URL complète (`https://www.vinted.de/catalog?search_text=…`).

### Bon à savoir sur les URL

* Le tri **« Plus récent »** (`order=newest_first`) et la pagination sont forcés
  automatiquement, même si votre URL contient un autre tri.
* Les paramètres Vinted existants (`brand_ids[]`, `size_ids[]`, `status_ids[]`,
  `catalog[]`…) sont conservés.
* Les prix min/max du profil sont ajoutés à l'URL **et** revérifiés localement.
* `search_text` peut contenir des accents : Vinted gère l'encodage.

---

## Comprendre les filtres

| Réglage | Comportement |
| --- | --- |
| **Prix min / max** | Filtre Vinted + contrôle local. Vide = pas de borne. |
| **Whitelist** | Si elle est vide, tout passe. Sinon, le titre, la marque, la taille, l'état ou la description doivent contenir au moins un mot (mode *Au moins un*) ou tous les mots (mode *Tous*). |
| **Blacklist** | Stricte. Un seul mot présent ⇒ annonce rejetée, sans appel Discord. Cherchée sur le titre **et** la description. |
| **Vérifier la description** | Active la lecture de la fiche annonce (requête supplémentaire, budget par scan). Désactivez-la pour économiser des requêtes si votre blacklist suffit sur les titres. |
| **Note vendeur min.** | Ex. `4.5` ⇒ les vendeurs à `4.2/5` sont écartés. Si la note est inconnue, elle est récupérée sur le profil vendeur. |
| **Avis vendeur min.** | Ex. `10` ⇒ protège des comptes créés la veille. Un vendeur sans nombre d'avis connu est ignoré **temporairement** (réessai au scan suivant). |

**Normalisation** : les comparaisons ignorent les accents, la casse et les
apostrophes (`Taché` ≡ `tache`, `DÉFAUT` ≡ `defaut`). Les mots sont cherchés en
début de mot, ce qui attrape les féminins/pluriels (`tachée`, `tachés`).

> ⚠️ La blacklist est volontairement **littérale** : le mot `défaut` rejette aussi
> une annonce qui dit « aucun défaut ». Préférez des expressions précises
> (`défaut fermeture`, `tache`, `pour pièces`) ou acceptez ce compromis : mieux
> vaut rater une bonne affaire que recevoir du bruit en permanence.

**Anti-redondance** : une annonce écartée est mémorisée (table
`ignored_items`). Si vous modifiez les filtres d'un profil, cette mémoire est
vidée automatiquement. Le bouton **« Oublier les annonces vues »** (dans l'édition
d'un profil) réinitialise tout le profil.

### Repères de prix et de scan

* Intervalle minimum : **15 s** (le dashboard propose 45–90 s).
* Délai entre deux requêtes : **2 s** par défaut. Ne descendez pas en dessous de
  1 s : c'est le meilleur moyen de vous faire bloquer.
* Budget de fiches détaillées : 15 par scan, réglable via
  `engine.detail_budget_per_scan`.
* Scans simultanés : 2 profils par défaut, 5 maximum.

---

## Alertes Discord

### Créer le webhook

1. Dans Discord : **Paramètres du serveur → Intégrations → Webhooks**.
2. **Nouveau webhook**, choisissez le salon, copiez l'**URL du webhook**.
3. Collez-la dans le profil (webhook dédié) ou dans **Réglages rapides →
   Webhook Discord par défaut** (webhook global).
4. Cliquez sur **Tester Discord** : un embed de confirmation arrive dans le salon.

Un webhook par profil permet de séparer les alertes par salon (sneakers d'un
côté, luxe de l'autre). Les webhooks sont stockés en clair dans `config.json` et
SQLite : ne partagez jamais ces fichiers.

### Contenu de l'embed

* **Titre** cliquable → ouvre l'annonce Vinted.
* **Photo HD** (pleine résolution quand Vinted la fournit).
* **Champs** : 💰 Prix (et prix port inclus si différent), 🏷️ Marque,
  📏 Taille, ✨ État, 👤 Vendeur (lien profil), ⭐ Réputation
  (`★★★★½ 4.8/5` + nombre d'avis), ❤️ Favoris.
* **Pied de page** : nom du profil + `Vinted Sniper`, horodatage.
* **Mention optionnelle** : `@here`, `@everyone` ou `<@&id_du_role>` via
  `discord.mention`.

Anti-spam : fenêtre glissante (20 messages/minute par défaut), respect des
`429` Discord (`retry_after`), reprise sur erreur réseau, abandon propre si le
webhook est supprimé/invalide.

---

## Proxys & self-healing

### Ce qui se passe en cas de blocage

1. Détection : statut `401/403/407/429/451/503`, page Cloudflare/Datadome,
   ou marqueur de challenge dans le HTML.
2. Le proxy utilisé est marqué en échec ; après plusieurs échecs il est **purgé**
   du pool (les proxys configurés sont mis en quarantaine, les proxys publics
   découverts sont supprimés).
3. Les cookies du domaine sont **jetés** et un nouveau User-Agent est choisi.
4. **Smart sleep** avec jitter (30 s → 900 s selon la configuration).
5. Le scan suivant déclenche un **renouvellement de session** (`_vinted_fr_session`)
   et reprend là où il en était. Aucun crash, aucune boucle infinie.
6. Un **watchdog** relance les boucles internes si elles s'arrêtaient.

Le moteur applique aussi un backoff par profil et une courte pause globale
lorsque plusieurs profils se font bloquer en même temps.

### Activer les proxys

Dans **Réglages rapides** :

* **Rotation de proxys** : ON pour activer le pool.
* **Priorité aux proxys** : ON pour privilégier la rotation large au lieu de vos
  proxys configurés.
* **Découverte auto** : récupère des listes publiques (GitHub / ProxyScrape) et
  les teste au fil de l'eau.
* **Vos proxys** : une ligne par proxy :
  `ip:port`, `http://ip:port`, `http://user:pass@ip:port`, `socks5://ip:port`.

Les mêmes réglages existent dans `config.json` (`proxies.list`,
`proxies.enabled`, `proxies.sources`…).

> Les proxys publics gratuits sont lents, souvent morts et parfois malveillants.
> Pour un usage intensif, utilisez **un** proxy résidentiel/mobile de confiance
> (souvent bien plus efficace que 40 proxys publics). Le bot ne transmet aucun
> identifiant Vinted à un proxy : il ne lit que des pages publiques.

### Sessions

Le client ouvre une session anonyme par domaine (`www.vinted.fr`,
`www.vinted.de`…) et la renouvelle toutes les 25 minutes environ. Le bouton
**↻ Session** du dashboard force un renouvellement immédiat. Aucune connexion à
un compte personnel n'est effectuée.

---

## Dashboard

* **Bandeau** : état du moteur (En veille / En pause / Hors ligne), uptime,
  badge démo, bouton pause, création de profil.
* **Cartes stats** : profils actifs, annonces du jour, alertes envoyées, dernier
  scan, blocages et santé du pool.
* **Profils** : interrupteur ON/OFF, URL/host, prix, intervalle, nombre de mots
  whitelist/blacklist, seuils vendeur, webhook, dernier scan, compteurs,
  erreurs éventuelles. Actions : **Scanner**, **Aperçu**, **Dupliquer**,
  **Supprimer**.
* **Flux en direct** : photo, prix, marque, taille, état, vendeur + étoiles,
  profil source, heure relative, lien direct. Filtrable par profil.
* **Contrôle** : compteurs de session, transport (`curl_cffi`/`httpx`), taille de
  la base, **↻ Session**, **Tester Discord**, **▶ Tout scanner**.
* **Proxys & réseau** : pool disponible/quarantaine, cookies présents,
  découverte et levée des bans.
* **Réglages rapides** : intervalle, délai, concurrence, page size, webhook,
  mention, notifications, proxys, baseline.
* **Journal** : logs INFO/DEBUG/WARN/ERROR en temps réel, y compris les raisons
  de rejet des annonces (`Écarté (blacklist : « copie »)`).

L'interface interroge l'API toutes les 3 à 6 secondes et s'arrête quand l'onglet
est masqué (économie de ressources).

---

## Configuration

Le fichier `config.json` est fusionné avec les valeurs par défaut : vous pouvez
n'y mettre que les clés qui vous intéressent. Les réglages modifiables depuis le
dashboard sont validés côté serveur (bornes, formats, URL Discord).

### `app`

| Clé | Défaut | Description |
| --- | --- | --- |
| `host` | `127.0.0.1` | Adresse d'écoute (mettez `0.0.0.0` pour le LAN/Docker). |
| `port` | `8000` | Port du dashboard. |
| `open_browser` | `true` | Ouvre le navigateur au démarrage. |
| `password` | `""` | Mot de passe HTTP Basic optionnel. **Non exposé** par l'API. |

### `engine`

| Clé | Défaut | Description |
| --- | --- | --- |
| `default_interval_seconds` | `60` | Intervalle par défaut (les profils ont le leur). |
| `min_request_delay` | `2.0` | Délai minimal entre requêtes (secondes). |
| `max_concurrent_profiles` | `2` | Scans simultanés (1–5). |
| `max_items_per_page` | `96` | Annonces demandées à Vinted par page (24–96). |
| `enrich_sellers` | `true` | Récupère note/nombre d'avis vendeur. |
| `detail_fetch` | `true` | Lit la fiche annonce (description, vendeur). |
| `detail_budget_per_scan` | `15` | Nombre max de fiches ouvertes par scan. |
| `seller_cache_ttl_hours` | `24` | Durée du cache vendeur. |
| `retention_days` | `30` | Purge auto des annonces et rejets plus anciens. |
| `baseline_first_scan` | `true` | Premier scan sans notification. |
| `start_paused` | `false` | Démarre le moteur en pause. |

### `http`

| Clé | Défaut | Description |
| --- | --- | --- |
| `impersonate` | `chrome124` | Profil TLS `curl_cffi`. |
| `timeout_seconds` | `25` | Timeout par requête. |
| `max_retries` | `3` | Tentatives supplémentaires. |
| `cookie_refresh_minutes` | `25` | Renouvellement de session. |
| `block_backoff_seconds` | `[30,60,120,300,600,900]` | Paliers de Smart Sleep. |
| `user_agents` | liste | User-Agents tournants. |

### `proxies`

| Clé | Défaut | Description |
| --- | --- | --- |
| `enabled` | `false` | Active le pool. |
| `prefer_proxies` | `false` | Favorise les proxys découverts. |
| `auto_discover` | `true` | Découverte de listes publiques (si pool actif). |
| `list` | `[]` | Vos proxys (`ip:port`, `http://`, `socks5://`). |
| `sources` | 3 URLs | Sources de découverte. |
| `max_pool_size` | `40` | Taille max des proxys découverts. |
| `cooldown_seconds` | `300` | Quarantaine de base. |
| `ban_after_failures` | `3` | Échecs avant quarantaine/purge. |
| `discover_interval_seconds` | `600` | Fréquence de découverte. |

### `discord`, `notifications`, `dashboard`

| Clé | Défaut | Description |
| --- | --- | --- |
| `discord.default_webhook` | `""` | Webhook global (fallback des profils). |
| `discord.username` | `Vinted Sniper` | Nom affiché de l'embed. |
| `discord.avatar_url` | `""` | Avatar du webhook. |
| `discord.mention` | `""` | Mention ajoutée devant l'embed. |
| `notifications.enabled` | `true` | Envoi Discord global. |
| `notifications.max_per_minute` | `20` | Débit maximum. |
| `notifications.max_attempts` | `5` | Tentatives par alerte. |
| `dashboard.feed_size` | `60` | Taille par défaut du flux. |
| `dashboard.logs_size` | `300` | Taille par défaut du journal. |

Un `config.json` partiel est accepté ; les nouvelles clés apparaissent avec leur
valeur par défaut au prochain lancement.

---

## Ligne de commande

```text
python main.py [options]

  --host HOST        Adresse d'écoute (défaut : config.json → 127.0.0.1)
  --port PORT        Port (défaut : 8000)
  --demo             Annonces fictives, aucun envoi réel
  --no-browser       N'ouvre pas le navigateur
  --config PATH      Fichier de configuration (défaut : config.json)
  --db PATH          Base SQLite (défaut : data/vinted_sniper.db)
  --version          Affiche la version
```

Exemples :

```bash
python main.py --demo --port 9001
python main.py --config /etc/vinted/config.json --db /var/lib/vinted/sniper.db
python main.py --host 0.0.0.0     # ⚠️ pensez à app.password si réseau partagé
```

---

## API REST

Toutes les routes sont sous `/api`, en JSON, sans authentification si
`app.password` est vide.

| Méthode | Route | Rôle |
| --- | --- | --- |
| `GET` | `/health` | Ping + version + mode démo. |
| `GET` | `/status` | Statut moteur, stats, HTTP, proxys, compteurs. |
| `GET` | `/profiles` | Liste des profils. |
| `POST` | `/profiles` | Création (validation complète). |
| `PUT` | `/profiles/{id}` | Modification. |
| `POST` | `/profiles/{id}/toggle` | `{ "active": true/false }`. |
| `POST` | `/profiles/{id}/duplicate` | Copie désactivée. |
| `DELETE` | `/profiles/{id}` | Suppression (+ historique). |
| `POST` | `/profiles/{id}/scan` | Scan immédiat. |
| `POST` | `/profiles/{id}/preview` | Teste les filtres sans rien enregistrer. |
| `POST` | `/profiles/{id}/clear-seen` | Réinitialise l'anti-doublon. |
| `GET` | `/feed` | Derniers articles (`limit`, `profile_id`). |
| `GET` | `/logs` | Journal (`limit`, `profile_id`). |
| `GET` | `/scans` | Derniers scans et erreurs. |
| `GET`/`PUT` | `/config` | Lecture / patch de configuration. |
| `POST` | `/engine/toggle` | Pause / reprise. |
| `POST` | `/engine/renew-sessions` | Force de nouveaux cookies. |
| `GET` | `/proxies` | État du pool. |
| `POST` | `/proxies/discover` | Découverte immédiate. |
| `POST` | `/proxies/reset` | Lève les quarantaines. |
| `POST` | `/notifications/test` | Envoie un embed de test. |

Exemple :

```bash
curl -X POST http://127.0.0.1:8000/api/profiles/1/scan
curl http://127.0.0.1:8000/api/feed?limit=5
```

---

## Données, sauvegardes & vie privée

* Tout reste **sur votre machine** : `config.json` et `data/vinted_sniper.db`.
* La base contient : profils, annonces vues, annonces écartées, cache vendeurs,
  logs, historique des scans.
* Sauvegarde : copiez `data/vinted_sniper.db` (application arrêtée), ou :
  `sqlite3 data/vinted_sniper.db ".backup backup.db"`.
* Purge automatique : annonces et rejets de plus de `retention_days` jours,
  journal limité à 5 000 lignes.
* Webhooks Discord stockés en clair : protégez vos fichiers (chmod 600 si
  nécessaire) et ne les commitez pas.
* Aucun télémétrie, aucun appel réseau hormis Vinted (et Discord si configuré).
* `app.password` protège l'accès au dashboard (HTTP Basic). Sans reverse proxy
  HTTPS, le mot de passe circule en clair sur le réseau local : n'exposez pas le
  dashboard sur Internet tel quel.

---

## Architecture du projet

```text
.
├── main.py                  # point d'entrée : python main.py
├── config.json              # configuration (fusionnée avec les défauts)
├── requirements.txt
├── run.sh / run.bat         # install + lancement en une commande
├── Dockerfile / docker-compose.yml
├── app/
│   ├── cli.py               # arguments, ouverture navigateur, uvicorn
│   ├── web.py               # FastAPI, auth Basic, fichiers statiques
│   ├── api.py               # routes REST du dashboard
│   ├── state.py             # composition config/DB/client/moteur
│   ├── config.py            # chargement, validation, patch de config
│   ├── models.py            # schémas Pydantic (profils, webhooks)
│   ├── database.py          # SQLite : profils, vus, écartés, vendeurs, logs
│   ├── engine.py            # ordonnanceur, scans, self-healing, alertes
│   ├── http_client.py       # curl_cffi, cookies, UA, pool de proxys
│   ├── vinted_api.py        # URLs de recherche, parsing, fiches, vendeurs
│   ├── filters.py           # prix, whitelist/blacklist, seuils vendeur
│   ├── notify.py            # embeds Discord, rate limit, retries
│   ├── utils.py             # texte, prix, dates, domaines
│   ├── demo.py              # mode démonstration hors-ligne
│   └── static/              # dashboard (HTML/CSS/JS, zéro dépendance)
│       ├── index.html
│       ├── styles.css
│       ├── app.js
│       └── favicon.svg
├── tests/                   # suite unittest (réseau local simulé)
└── data/                    # créé au lancement : SQLite + WAL
```

### Flux d'un scan

```text
Scheduler (1 tâche/profil actif)
        │
        ▼
Session Vinted (cookies anonymes, UA) ──► API /api/v2/catalog/items
        │                                      │
        │                                      ├─ 200 → annonces normalisées
        │                                      └─ blocage → rotation proxy/UA,
        │                                         purge cookies, sleep, retry
        ▼
Filtres locaux (prix, blacklist titre) ──► fiche annonce (description)
        │                                      │
        │                                      ▼
        │                              filtres complets (blacklist description)
        ▼                                      │
Enrichissement vendeur (cache) ────────────────┤
        │                                      ▼
        │                              déduplication SQLite
        ▼                                      │
Alerte Discord (embed) ◄───────────────────────┘
```

---

## Dépannage

| Symptôme | Piste |
| --- | --- |
| **403 / 429 en boucle** | Augmentez `min_request_delay` (3–5 s), réduisez le nombre de profils actifs, activez un proxy résidentiel, cliquez sur **↻ Session**. Le mode démo permet de vérifier que le reste fonctionne. |
| **Aucune alerte alors que des annonces existent** | Lancez un **Aperçu** : les annonces sont peut-être écartées par la blacklist ou les seuils vendeur. Vérifiez aussi que le profil est actif et que le premier scan (baseline) est passé. Consultez le journal. |
| **Pas de message Discord** | Testez avec **Tester Discord**. Vérifiez `notifications.enabled`, l'URL du webhook et que le salon autorise les webhooks. Les erreurs apparaissent en rouge dans le journal. |
| **Photos absentes** | Vinted peut changer ses CDN. L'URL est stockée telle que fournie ; le dashboard affiche un placeholder. Réessayez plus tard ou augmentez `detail_fetch`. |
| **Images non cliquables / liens cassés** | Vérifiez que l'URL du profil est bien sur un domaine `vinted.*`. L'aperçu affiche l'URL normalisée. |
| **Le port 8000 est occupé** | Le lanceur choisit le port suivant. Sinon `--port 8080`. |
| **`curl_cffi` ne s'installe pas** | L'app fonctionne avec `httpx` (fallback). Sur certaines architectures (Raspberry Pi ancien), installez une version récente de Python ou utilisez Docker. |
| **La base grossit** | `retention_days` (30 par défaut) purge automatiquement. Vous pouvez supprimer `data/vinted_sniper.db*` pour repartir de zéro. |
| **Le dashboard redémarre sans cesse** | Consultez la console : une erreur de configuration ou un `config.json` invalide est signalé. Le fichier est fusionné avec les défauts ; supprimez la clé fautive. |
| **Mode LAN / Docker** | Utilisez `--host 0.0.0.0` et définissez `app.password`. Vérifiez le pare-feu. |

---

## Tests

```bash
python -m unittest discover -s tests -v
```

* `tests/test_core.py` : normalisation, URLs Vinted, parsing, filtres, SQLite,
  config, embeds.
* `tests/test_app.py` : API FastAPI + moteur complet en mode démo (scan, flux,
  aperçu, pause, validation).
* `tests/test_http.py` : client HTTP contre un faux Vinted local (cookies,
  429 → retry, proxy mort → fallback direct, quarantaine).

Aucun test ne contacte Vinted ni Discord.

---

## Limites & bonnes pratiques

* **Pas de contournement de captcha** ni de résolution de challenge : le but est
  de rester sous les radars, pas de forcer. Si Vinted exige un captcha, le bot
  patiente et réessaie.
* **Les endpoints publics changent.** Le parsing est volontairement tolérant
  (API JSON puis HTML `__NEXT_DATA__`/JSON-LD/meta). Une mise à jour du projet
  peut être nécessaire si Vinted modifie sa structure.
* **Un usage massif nuira à tout le monde** : gardez des intervalles réalistes,
  limitez le nombre de profils, n'utilisez pas 50 proxys publics pour marteler
  le catalogue.
* **Respectez les CGU de Vinted** et le droit applicable. Vous êtes responsable
  de l'usage de cet outil. Ne l'utilisez pas pour du dropshipping abusif, du
  harcèlement de vendeurs ou de la revente de données.
* **Discord** : un webhook supprimé provoque une erreur définitive jusqu'à ce
  que vous le remplaciez. Les alertes échouées sont conservées avec leur raison
  dans le flux (`notify_error`).
* **Pas de comptes** : l'outil ne se connecte pas à Vinted et ne peut donc pas
  acheter, envoyer de messages ni négocier. Il observe, il alerte.

---

## Licence

MIT — voir [LICENSE](LICENSE).

Projet fourni tel quel, sans garantie. Vinted est une marque de Vinted UAB ;
ce projet n'est ni affilié ni approuvé par Vinted.

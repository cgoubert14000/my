# 🎯 Vinted Sniper

**Plateforme de veille Vinted open-source, 100 % locale et gratuite.**
Multi-profils activables à la volée, détection **en continu (≈1,5 s)**, filtres
puissants, enrichissement vendeur, alertes Discord soignées, dashboard temps réel
poussé par le serveur, rotation de proxys et self-healing intégré.

> Conçue pour un usage personnel raisonnable. Aucun compte Vinted, aucun mot de
> passe et aucun captcha ne sont nécessaires : le bot lit les annonces publiques.

---

## Sommaire

1. [Aperçu](#aperçu)
2. [Démarrage en 30 secondes](#démarrage-en-30-secondes)
3. [Mode temps réel](#mode-temps-réel--détecter-à-la-seconde)
4. [Toutes les catégories Vinted](#toutes-les-catégories-vinted)
5. [Filtrer par marque](#filtrer-par-marque)
6. [Filtrer par taille, état et couleur](#filtrer-par-taille-état-et-couleur-filtres-vinted)
7. [Vérifier que le scan réel fonctionne](#vérifier-que-le-scan-réel-fonctionne---check)
8. [Installation détaillée](#installation-détaillée)
9. [Créer son premier profil](#créer-son-premier-profil)
10. [Comprendre les filtres](#comprendre-les-filtres)
11. [Alertes Discord](#alertes-discord)
12. [Proxys & self-healing](#proxys--self-healing)
13. [Dashboard](#dashboard)
14. [Configuration](#configuration)
15. [Ligne de commande](#ligne-de-commande)
16. [API REST](#api-rest)
17. [Données, sauvegardes & vie privée](#données-sauvegardes--vie-privée)
18. [Architecture du projet](#architecture-du-projet)
19. [Dépannage](#dépannage)
20. [Tests](#tests)
21. [Limites & bonnes pratiques](#limites--bonnes-pratiques)
22. [Licence](#licence)

---

## Aperçu

| Fonction | Ce que fait Vinted Sniper |
| --- | --- |
| ⚡ **Détection en continu** | Chaque profil est sondé en boucle (1,5 s → 10 s adaptatif), pas toutes les 60 s. Détection incrémentale : page identique = analyse sautée. Flux poussé (SSE) vers le dashboard. |
| 🧩 **Multi-profils** | Créez autant de profils nommés que voulu (« Sneakers Hype », « Luxe », « Tech »…), chacun avec ON/OFF, intervalle, prix, mots-clés, seuils vendeur et webhook dédié. |
| 🧲 **Scraping à jour (2026)** | Lecture des cartes SSR de `/catalog` (96/page), replis RSC/JSON-LD/liens, tri « Plus récent », pagination. |
| 🕵️ **Enrichissement vendeur** | Pseudo, note moyenne sur 5 (`4.8/5`), nombre d'avis, lien profil. Les infos manquantes sont récupérées sur la page vendeur et mises en cache. |
| 🚫 **Blacklist stricte** | Refus des annonces « copie », « faux », « défaut », « taché »… sur le **titre et la description**, insensible aux accents et aux pluriels. |
| 🔔 **Discord haut de gamme** | Embed complet : photo HD, titre, prix (+ port inclus), marque, taille, état, vendeur, étoiles, nombre d'avis, lien direct. |
| 🛡️ **Self-healing** | Sur 403/429/blocage : purge du proxy fautif, rotation User-Agent, renouvellement de session, pause intelligente, backoff, reprise automatique. |
| ♻️ **Anti-doublon** | SQLite mémorise les annonces vues **par profil**, y compris après redémarrage. Mémoire négative pour ne pas re-tester dix fois la même annonce écartée. |
| 🏷️ **Toutes les marques** | Import en un clic des **~57 000 marques** du catalogue Vinted depuis ses sitemaps officiels, conservées en base locale : recherche instantanée, même hors ligne. Combinaison de plusieurs marques avec catégorie, mots-clés et prix, filtre strict côté Vinted (`brand_ids[]`). |
| 🗂️ **Toutes les catégories** | Navigateur intégré : 9 catégories racines puis les sous-catégories réelles lues sur Vinted, jusqu'au niveau le plus fin, combinables avec vos mots-clés. |
| 📊 **Dashboard local** | Profils, flux photo en direct (annonce cliquable, vendeur, catégorie), journal, stats, réglages, test Discord, aperçu des filtres avant activation. |

> ⚠️ **Changement Vinted (septembre 2026)** : l'API interne
> `/api/v2/catalog/items` renvoie désormais **404** et `__NEXT_DATA__` a
> disparu. Vinted Sniper lit donc les **cartes rendues côté serveur** de la page
> `/catalog` (`data-testid="grid-item"`, `product-item-id-*`), avec replis sur le
> payload RSC et le JSON-LD. C'est la méthode qui fonctionne aujourd'hui, et elle
> est testée sur des fixtures reproduisant le balisage réel.
>
> ⚠️ **Honnêteté technique** : aucun outil ne peut garantir le contournement
> permanent de Cloudflare/Datadome. Le bot réduit fortement les blocages
> (empreinte TLS Chrome via `curl_cffi`, cookies de session, délais aléatoires,
> rotation d'identité, backoff), mais si votre IP est durablement bannie, il
> faudra un proxy résidentiel. Les proxys publics gratuits sont instables — le
> pool les met en quarantaine automatiquement.
>
> 🩺 **Vérifiez toujours avec `python main.py --check`** : en 10–30 s, il teste la
> session, le catalogue, une fiche article, le vendeur et le webhook, et vous dit
> exactement ce qui bloque.

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

Avant tout, vérifiez l'accès réel à Vinted :

```bash
python main.py --check "air max 97"
```

Le rapport affiche ✅/❌ pour la session, le catalogue, la fiche article, le
vendeur et le webhook, avec des conseils ciblés en cas d'échec.

---

## Mode temps réel : détecter à la seconde

Le moteur ne dort plus entre deux scans : il enchaîne les passages sur chaque
profil actif, avec un intervalle **adaptatif**.

```text
annonce publiée          1 requête (page /catalog, tri « Plus récent »)
      │                        │
      ▼                        ▼
   t = 0 s  ──────────►  t = 0,3 s   tête de liste modifiée → analyse des 24 premières cartes
                                          │
                                          ▼
                                    t = 0,5 s   filtres + SQLite + flux SSE
                                          │
                                          ▼
                                    t = 0,6 s   alerte Discord envoyée
```

**Pourquoi c'est rapide sans marteler Vinted**

| Mécanisme | Effet |
| --- | --- |
| **Détection incrémentale** | On lit l'identifiant de la première annonce de la page. Identique au passage précédent → le HTML n'est **pas analysé** (0,1 ms au lieu de ~100 ms). |
| **Analyse en tête de page** | Seules les 24 premières cartes (les plus récentes) sont converties en annonces ; le reste de la page est ignoré. |
| **Relecture après rafale** | Dès qu'une nouveauté est trouvée, le passage suivant relit toute la page : aucune annonce n'est perdue si plusieurs arrivent d'un coup. |
| **Intervalle adaptatif** | Silence → l'intervalle s'allonge progressivement (jusqu'à 10 s) ; nouveauté → retour immédiat à 1,5 s pendant 90 s (rafale). |
| **Alerte avant enrichissement** | L'annonce part sur Discord dès qu'elle est validée ; description, photo HD et note vendeur sont complétées **après**, en tâche de fond, puis le dashboard est mis à jour. |
| **Fiche article bornée (1.3.2)** | Quand une description ou une note vendeur est nécessaire avant l'alerte, la lecture de la fiche est **limitée à 3,5 s au total** (une tentative, 6 s max). Au-delà, l'alerte part avec les données déjà lues : plus jamais 90 s d'attente. |
| **Requête unique (1.3.2)** | En temps réel, un passage bloqué échoue en **10 s maximum** au lieu de 3 × 30 s de tentatives. Le scan suivant repart aussitôt. |
| **Journal poussé (1.3.2)** | Les lignes de journal arrivent par le flux SSE, à la seconde, et non plus au rythme d'un rafraîchissement de 4 s. |
| **Anti-blocage auto-régulé** | Un 403/429 ralentit temporairement le profil (×1,6 par blocage, jusqu'à ×8) puis revient à la vitesse normale après des passages réussis. Un défi HTTP 200 (Datadome) ne ralentit que ×3 et conserve la session (1.3.3). |
| **Flux poussé (SSE)** | Le dashboard reçoit les nouveautés par `/api/stream` : elles apparaissent sans attendre le prochain rafraîchissement. |

**Fluidité de l'interface (1.3.2)**

Le dashboard ne reconstruit plus ses listes à chaque rafraîchissement : chaque
carte (profil, annonce, ligne de journal) est **réutilisée** et seuls les champs
qui changent sont réécrits. Résultat : plus d'animation rejouée toutes les 2 s,
plus de saut de défilement quand on lit le journal, et un flux qui s'ajoute
ligne par ligne.

| Avant 1.3.2 | Depuis 1.3.2 |
| --- | --- |
| `replaceChildren()` sur les 3 listes à chaque poll → tout clignote | rendu incrémental par clé (`item_id`, `id` de profil, `id` de journal) |
| compte à rebours réécrit en boucle → micro-saccades | re-synchronisé seulement si l'écart dépasse 1,2 s |
| `backdrop-filter` sur chaque panneau (coûteux à repeindre) | fond opaque équivalent, rendu stable |
| journal rafraîchi toutes les 4 s | poussé par SSE, à la seconde |

**Les trois vitesses**

| Réglage | Intervalle | Pour qui |
| --- | --- | --- |
| Par défaut (recommandé) | 1,5 s après une trouvaille, jusqu'à 10 s au calme | Usage normal : très réactif, discret. |
| `--interval 2.5` | Minimum forcé à 2,5 s | Connexions modestes, plusieurs profils. |
| `--turbo` | 1,5 s constant, aucun ralentissement | Chasse à la seconde près. **Risque de blocage nettement plus élevé.** |

```bash
python main.py                 # temps réel adaptatif (défaut)
python main.py --turbo         # vitesse maximale constante
python main.py --interval 3    # minimum personnalisé
```

Tout se règle aussi dans le dashboard : **Réglages → ⚡ Mode temps réel**,
intervalle mini/maxi, et l'interrupteur « ⚡ Suivi temps réel » par profil
(décochez-le pour revenir à un scan périodique classique).

**Ce que vous verrez**

* pastille **Temps réel** en haut à droite : le flux serveur est connecté ;
* sur chaque carte de profil : `⚡ 1,5 s` + `prochain passage 0,8 s` ;
* dans les statistiques : `⚡ 0,32 s de détection` (temps entre le début du
  passage et la première nouveauté validée) ;
* dans le flux : la nouvelle annonce apparaît avec un liseré et un toast ;
* dans le journal : `⚡ 1 nouvelle(s) annonce(s) « Sneakers Hype » en 320 ms`.

**Bande passante et fair-play**

Chaque passage télécharge la page catalogue (≈ 300 Ko compressés, 2–4 Mo
décompressés). À 1,5 s, cela représente plusieurs centaines de Mo par heure et
par profil. Le mode adaptatif réduit fortement ce volume au calme. Si vous
surveillez beaucoup de profils, espacez-les (`--interval`, ou décochez le temps
réel sur les profils secondaires) : c'est le meilleur moyen de rester
sous les radars **et** de garder une détection rapide sur l'essentiel.

---

## Toutes les catégories Vinted

Un profil n'est pas limité à une recherche par mots-clés : il peut cibler
n'importe quelle catégorie, y compris les sous-catégories les plus profondes.

Dans le formulaire de profil, cliquez sur **Choisir une catégorie** :

1. Le premier écran affiche les **9 univers Vinted** (Femmes, Hommes, Enfants,
   Sports, Maison, Électronique, Loisirs, Jeux, Beauté). Cette liste est locale :
   aucun appel réseau, ouverture instantanée.
2. Cliquez sur un univers : le bot lit la page réelle
   `https://www.vinted.fr/catalog/<id>` et affiche ses **sous-catégories
   exactes** (Vêtements, Chaussures, Accessoires…).
3. Continuez jusqu'au niveau voulu, puis **Choisir cette catégorie**.

Le résultat est une URL `https://www.vinted.fr/catalog/<id>-<slug>` **qui
conserve vos mots-clés et vos filtres de prix** :

```text
https://www.vinted.fr/catalog/1231-men_shoes_new?search_text=nike&price_from=20
```

* La catégorie choisie apparaît en pastille sur la carte du profil
  (**⌫** pour revenir à « Toutes les catégories »).
* Fonctionne sur tous les domaines (`vinted.fr`, `.de`, `.it`…) : l'URL est
  construite sur le domaine déjà présent dans le champ de recherche.
* Les sous-catégories sont mises en cache **1 heure** (elles changent très
  rarement) ; le premier niveau reste toujours disponible hors ligne.
* API : `GET /api/categories?path=/catalog/5-mens` et
  `POST /api/profiles/{id}/category` (voir [API REST](#api-rest)).

> Si Vinted répond 403/429 pendant la navigation, le dashboard affiche un
> message clair au lieu de planter ; réessayez après quelques minutes ou avec un
> proxy configuré. Une fois la catégorie validée, le scan se poursuit exactement
> comme une recherche classique.

---

## Filtrer par marque

En plus des catégories, chaque profil peut se limiter à une ou plusieurs marques.

Dans le formulaire de profil, cliquez sur **🏷️ Choisir des marques** :

1. **Tapez la première lettre suffit** : dans le champ *Rechercher une marque*,
   saisir « n » affiche **toutes** les marques qui commencent par N (Nike, New
   Balance, Naked Wolfe, Nina Ricci…), « ni » restreint à Nike/Nina Ricci. La
   recherche est un vrai **préfixe de mot**, insensible aux accents, à la casse
   et à la **ponctuation** : « cp » trouve **C.P. Company**, « hm » et « h&m »
   trouvent **H&M**, « coq » trouve Le Coq Sportif. Les marques qui commencent
   réellement par la saisie sont classées en premier.
   Si l'index local est vide au moment de la saisie, il est **importé
   automatiquement** (≈10 s, une seule fois) au lieu d'afficher « aucune marque ».
2. Elle interroge l'**index local** (`GET /api/brands?search=n&prefix=1`), donc
   instantanément et sans réseau. Le nombre total est affiché, même quand
   l'affichage est plafonné à 300 lignes pour rester fluide.
3. Les lettres A→Z restent un raccourci (liste live de ~100 marques par lettre,
   `https://www.vinted.fr/brands/by_letter/A`).
4. Cochez autant de marques que voulu (20 maximum), puis **Filtrer sur N
   marque(s)**. Les pastilles apparaissent dans le formulaire et sur la carte du
   profil ; **Toutes** retire le filtre.

Le filtre est **strict**, appliqué par Vinted lui-même :

```text
https://www.vinted.fr/catalog?catalog[]=1231&brand_ids[]=53&brand_ids[]=1775&search_text=nike
```

Cette forme (catégorie + marques + mots-clés + prix) a été vérifiée sur le
site : la page ne renvoie que les annonces des marques cochées, dans la
catégorie choisie, avec vos mots-clés. Le bot n'invente aucune marque : les
identifiants viennent des pages Vinted, et la liste est mise en cache 6 h.

* Si Vinted est momentanément inaccessible, le sélecteur affiche un **raccourci
  de marques populaires** (aucune requête réseau) au lieu d'échouer.
### Récupérer toutes les marques du catalogue (un clic)

Les pages `/brands/by_letter/…` de Vinted n'affichent que **~100 marques par
lettre** (≈2 600). Mais Vinted publie l'intégralité de son catalogue de marques
dans ses **sitemaps officiels**, déclarés dans `robots.txt` :

```text
https://vinted.fr/sitemap-fr.xml
   └── /sitemaps/fr/brands.xml    (~50 000 marques)
   └── /sitemaps/fr/brands1.xml   (le reste, ~7 000)
```

Dans la modale **🏷️ Choisir des marques**, cliquez sur
**⬇ Importer toutes les marques Vinted** :

* le bot lit `robots.txt`, suit les sitemaps de marques et enregistre chaque
  `id` + nom dans la base locale (`brands`) ;
* **2 à 3 requêtes** suffisent, aucune limite de débit, aucune page à parcourir ;
* une fois l'import fait (≈10 s), la recherche est **instantanée et hors ligne** :
  tapez « nike », « brak », « ginori »… et la marque apparaît, même sans
  connexion ;
* l'import est idempotent : relancez-le quand vous voulez (nouveautés Vinted),
  rien n'est dupliqué.

Le nombre de marques disponibles est affiché en permanence dans la modale.
Vous pouvez aussi restreindre à une lettre (liste live) ou ajouter une marque
isolée par son URL/identifiant.

---

## Filtrer par taille, état et couleur (filtres Vinted)

Le formulaire de profil contient un bloc **Filtres Vinted** : tailles, état,
couleurs, prix et tri. Ce ne sont pas des filtres « maison » : les identifiants
écrits dans l'URL sont **ceux du site**, donc Vinted applique le filtre *avant*
que le bot ne lise les annonces (moins de requêtes, résultats exacts).

```text
https://www.vinted.fr/catalog?size_ids[]=207&size_ids[]=209&status_ids[]=6
  &color_ids[]=1&price_from=20&price_to=120&order=newest_first&search_text=nike
```

### Correspondances vérifiées sur vinted.fr (20/10/2026)

La page `/catalog` réaffiche les filtres appliqués avec leur libellé : c'est
cette page qui a servi de preuve, sans passer par l'API privée.

| Filtre | Identifiants |
| --- | --- |
| État | `6` Neuf avec étiquette · `1` Neuf sans étiquette · `2` Très bon état · `3` Bon état · `4` Satisfaisant · `7` Ne fonctionne pas |
| Couleurs | `1` Noir · `2` Marron · `3` Gris · `4` Beige · `5` Fuchsia · `6` Violet · `7` Rouge · `8` Jaune · `9` Bleu · `10` Vert · `11` Orange · `12` Blanc |
| Tailles lettres | `205` XS · `206` S · `207` M · `209` L · `210` XL · `211` XXL · `212` XXXL · `213` Taille unique |
| Pointures | `55` 35 · `56` 36 · `57` 37 · `58` 38 · `59` 39 · `60` 40 · `61` 41 · `62` 42 · `63` 43 |
| Tailles FR / UK / US | `1` XS / 34 / 6 · `2` S / 36 / 8 · `3` M / 38 / 10 · `4` L / 40 / 12 · `5` XL / 42 / 14 · `6` XXL / 44 / 16 |
| Tri | `newest_first` · `relevance` · `price_low_to_high` · `price_high_to_low` |

> ⚠️ Deux pièges constatés en direct, et donc évités par le bot : l'identifiant
> `208` ne correspond à **aucune** taille (Vinted l'ignore), et les identifiants
> de taille **dépendent de la catégorie** (`1` = « XS / 34 / 6 » pour les tailles
> françaises, alors que `205` = « XS » pour les hauts). C'est pourquoi le
> sélecteur propose des groupes explicites, et pourquoi une pointure 44+ ou une
> taille enfant s'ajoute en collant l'URL filtrée depuis vinted.fr : le bot
> conserve alors **tous** les paramètres qu'elle contient.

Ce que fait le bot, concrètement :

* il **remplace** les filtres existants au lieu de les empiler (pas de doublons
  `size_ids[]`) et conserve mots-clés, catégorie et marques ;
* il n'envoie jamais un identifiant inconnu ou une valeur non numérique ;
* il passe en forme `?catalog[]=…` dès qu'un filtre existe, seule forme où
  Vinted applique réellement les paramètres ;
* le budget de scan ne change pas : le tri reste forcé sur `newest_first`.

---

## Vérifier que le scan réel fonctionne (`--check`)

```bash
python main.py --check                                 # recherche « nike » sur vinted.fr
python main.py --check "air max 97"                    # votre recherche
python main.py --check "chaussures" --brand nike       # avec le filtre de marque
python main.py --check "sneakers" --brand 1775         # par identifiant Vinted
python main.py --check "sac gucci" --webhook https://discord.com/api/webhooks/…
python main.py --check "nike" --domain www.vinted.de
```

`--brand` accepte un nom (« nike »), un identifiant (« 53 ») ou l'URL de la
marque, et résout la correspondance **sans réseau** (index local des marques
d'abord, puis les marques connues). Le rapport affiche alors l'URL exacte
testée, avec `brand_ids[]` : c'est la garantie que le filtre de marque
fonctionne, en plus du parsing.

Le diagnostic affiche **chaque étape dès qu'elle est terminée** (plus de terminal
muet) et s'arrête au bout de 90 s avec un message clair si le réseau bloque :

```text
✅ Configuration locale — Transport curl_cffi · base … · 0 profil(s)
⏳ Session Vinted — connexion à https://www.vinted.fr…
❌ Session Vinted — Aucun cookie reçu (page d'accueil inaccessible ou bloquée).
```

Ce que le diagnostic teste, dans l'ordre :

1. **Configuration** : transport (`curl_cffi`/`httpx`), base SQLite, profils.
2. **Session** : ouverture de `https://www.vinted.fr/`, cookies reçus
   (`_vinted_fr_session`, `datadome`…).
3. **Catalogue** : requête réelle `/catalog?search_text=…&order=newest_first`,
   taille de la page, nombre de cartes extraites, statut HTTP.
4. **Échantillon** : 3 annonces avec titre, prix, marque, taille et lien.
5. **Fiche article** : description, photo HD.
6. **Vendeur** : pseudo, note /5, nombre d'avis.
7. **Webhook** : envoi réel d'un embed de test (si fourni).

Aucun profil n'est créé et aucune annonce n'est enregistrée : c'est un test
lecture seule. Le même diagnostic est disponible dans le dashboard via
**🩺 Diagnostic**.

Exemple de sortie saine :

```text
✅ Configuration locale — Transport curl_cffi · base data/vinted_sniper.db · 2 profil(s)
✅ Session Vinted — Cookies obtenus : _vinted_fr_session, datadome
✅ Catalogue Vinted — 96 annonce(s) extraite(s) sur une page de 3612 Ko · tri « Plus récent »
✅ Échantillon d'annonces — Nike grey hoodie (8 €) · Nike Air Force 1 (15 €) …
   • Nike grey hoodie · 8 € · Nike S
     https://www.vinted.fr/items/10458643821-nike-grey-hoodie
✅ Fiche article — Description : oui · photo HD : oui
✅ Informations vendeur — @vendeur_test · 4.8/5 · 132 avis
✅ Webhook Discord — Message de test envoyé.
```

Si le catalogue échoue, le message distingue **blocage anti-bot** (403/429),
**page vide** (mot-clé sans résultat) et **structure HTML inconnue** (0 carte sur
une page de plusieurs Mo) — trois causes très différentes, trois solutions
différentes.

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

Deux dépendances méritent un mot :

* **`curl_cffi`** reproduit l'empreinte TLS de Chrome, ce qui réduit nettement les
  blocages Cloudflare/Datadome. S'il ne s'installe pas, l'application bascule
  automatiquement sur `httpx` (moins discret mais fonctionnel).
* **`beautifulsoup4`** analyse les cartes SSR de Vinted. Un repli par expressions
  régulières existe si elle est absente. Pour accélérer l'analyse des pages de
  ~3,5 Mo : `pip install lxml` (détecté automatiquement, facultatif).

### 4. Lancement

```bash
python main.py                  # http://127.0.0.1:8000
python main.py --host 0.0.0.0   # accessible depuis le réseau local
python main.py --port 9000
python main.py --no-browser     # ne pas ouvrir le navigateur
```

Si le port est occupé, le lanceur choisit automatiquement le suivant et
l'affiche dans la console. Notez l'adresse affichée : c'est votre dashboard.

### 5. Premier lancement, pas à pas

1. **Vérifier l'accès à Vinted** (10–30 s, aucun profil nécessaire) :

   ```bash
   python main.py --check "air max 97"
   ```

   Toutes les lignes doivent être ✅. Si une ligne est ❌, le rapport indique la
   cause (IP bloquée, proxy, structure de page) et la correction à appliquer.
   C'est la seule étape qui dépend de votre connexion : si elle passe, le reste
   fonctionnera chez vous.

2. **Démarrer le dashboard** : `python main.py`, puis ouvrez
   <http://127.0.0.1:8000>.

3. **Créer un profil** : bouton **+ Nouveau profil**. Saisissez un nom, la
   recherche (`nike air max 97` ou une URL Vinted complète), un prix min/max
   éventuel, vos mots-clés et votre blacklist. Cliquez sur **Choisir une
   catégorie** si vous voulez restreindre à un rayon précis (voir
   [Toutes les catégories Vinted](#toutes-les-catégories-vinted)).

4. **Tester avant d'activer** : bouton **Aperçu** sur la carte du profil. Il
   affiche les annonces réellement trouvées et celles qui sont écartées, avec le
   motif (prix, mot blacklisté, note vendeur…). Aucun doublon n'est enregistré.

5. **Brancher Discord** : collez l'URL du webhook dans le profil, puis
   **Tester Discord** dans le panneau de contrôle. Un embed d'exemple arrive dans
   le salon ; sinon, l'erreur exacte s'affiche dans le journal.

6. **Activer** l'interrupteur du profil. Les nouvelles annonces apparaissent
   dans le flux **en direct** (photo, titre cliquable, lien « Voir l'annonce »)
   et partent sur Discord dans la seconde.

> Le premier passage d'un profil sert de **référence** : il mémorise les
> annonces déjà en ligne sans alerter. Les alertes commencent dès la suivante.

### 6. Docker (optionnel)

```bash
docker compose up --build -d
# http://localhost:8000
```

Le `config.json` et le dossier `data/` sont montés en volumes : vos profils et
votre historique survivent aux mises à jour de l'image.

Pour un test immédiat sans toucher à Vinted :

```bash
docker compose run --rm vinted-sniper python main.py --check "air max 97"
```

### 7. Service permanent (Linux, systemd)

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
| **Filtres Vinted (taille, état, couleur, prix, tri)** | Écrits dans l'URL du profil, appliqués par le site. Voir la section dédiée ci-dessus. |
| **Avis vendeur min.** | Ex. `10` ⇒ protège des comptes créés la veille. Si l'information vendeur est momentanément inaccessible, l'alerte n'est **pas** sacrifiée : elle part avec « note inconnue » et le journal le signale. |

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

* Temps réel : **1,5 s minimum**, 10 s au repos (adaptatif), ou `--turbo` pour
  rester au minimum en permanence.
* Intervalle hors temps réel : 60 s par défaut (`interval_seconds` du profil).
* Délai entre deux requêtes « lourdes » (fiches article) : 2 s par défaut, mais
  il est ignoré en mode temps réel au profit de requêtes parallèles bornées.
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

## Blocage Datadome (HTTP 200) : ce que fait le bot depuis la 1.3.3

Symptôme typique dans le journal :

```text
Renouvellement de session sur www.vinted.fr…
Session www.vinted.fr prête (…)
Profil « new » en difficulté (échec #5) : blocage anti-bot (HTTP 200)
Self-healing : session www.vinted.fr programmée pour renouvellement, reprise dans 4 min
```

Vinted ne renvoie pas une erreur : il renvoie **HTTP 200 avec une page de
vérification** (Datadome). Trois comportements rendaient la situation pire
qu'elle ne l'est, et sont corrigés :

| Avant | Depuis |
| --- | --- |
| Les cookies étaient **purgés** à chaque page de vérification | Les cookies sont **conservés** sur un HTTP 200 : le cookie `datadome` posé par la page est justement ce qui permet de repasser. Purge uniquement sur 403/429/451. |
| La session était **renouvelée à chaque scan** bloqué (2 requêtes + nouvelle empreinte) | Renouvellement seulement après **3 blocages consécutifs** (ou un blocage dur) |
| Reprise après **4 min**, puis 15 min | Reprise après **20 s**, puis 40 s, 80 s — plafond **90 s** |
| Le **User-Agent changeait à chaque requête** alors que les cookies restaient | **Une identité par domaine** : Datadome lie son cookie à l'empreinte du navigateur, changer d'UA en gardant les cookies déclenchait un défi à chaque passage (1.3.4) |
| Le mot « datadome » figurait dans les **marqueurs de blocage** — or la page catalogue normale charge ce script | Un blocage n'est retenu que si la **grille d'annonces est absente** ; le journal nomme le marqueur exact (`page « just a moment »`, `défi Datadome « captcha-delivery »`) (1.3.4) |
| Attente de 30-60 s après une page de vérification HTTP 200 | Pause plafonnée à **5 s** : ce n'est pas un quota épuisé (1.3.4) |

### 1.3.9 — emporter les 57 000 marques avec soi

L'index des marques (≈56 400 entrées issues des sitemaps Vinted) vit dans
`data/vinted_sniper.db`. La 1.3.9 permet de le **sortir dans un fichier**, de
l'**embarquer** dans le bot, et donc de travailler **sans réseau** — utile quand
Cloudflare bloque tout.

| Commande | Effet |
| --- | --- |
| `vinted-sniper.exe --export-brands marques-vinted` | écrit `marques-vinted.csv` (**id,slug,name**) et `marques-vinted.json` |
| `vinted-sniper.exe --import-brands marques-vinted.csv` | charge un fichier dans la base locale (idempotent) |
| `python tools/make_brand_pack.py marques-vinted.csv` | fabrique `app/data/brands.csv` + `.json`, embarqués dans l'exécutable |
| Dashboard → Marques → **💾 Exporter la liste (CSV)** | téléchargement direct, sans ligne de commande |

**Chargement automatique** : au démarrage, si la table `brands` est vide, le
bot cherche `brands.csv` / `brands.json` / `marques.csv` / `marques-vinted.csv`
à côté de l'exécutable, dans `app/data/`, puis dans le dossier courant. Un index
déjà présent n'est **jamais** écrasé (données en ligne plus fraîches).

Format du fichier, volontairement le plus simple possible :

```csv
id,slug,name
53,nike,Nike
7,h-m,H&M
364,zara,Zara
```

Export réel chez un utilisateur : **56 433 marques**, CSV ≈ 1,8 Mo.

### 1.3.8 — « Le navigateur n'a pas ouvert son port de débogage »

Cette erreur est apparue chez un utilisateur sous Windows. Trois causes
possibles, toutes traitées :

| Cause | Correction 1.3.8 |
| --- | --- |
| Profil de débogage **déjà verrouillé** par une fenêtre restée ouverte : le nouveau processus se contente de rouvrir l'ancienne et sort sans port | le lancement est rejoué avec un **profil système neuf**, puis avec **un autre navigateur** (Chrome si Edge échoue) — jusqu'à 4 tentatives |
| Le navigateur s'arrête aussitôt (stratégie Windows, antivirus, profil insolite) | le **code de sortie** et la **sortie d'erreur** du navigateur sont désormais remontés dans le message, au lieu d'un simple délai dépassé |
| Port de débogage jamais détecté | port choisi explicitement, puis vérifié en **HTTP** (`/json/version`) en plus du fichier `DevToolsActivePort`, avec chemin de profil **absolu** |

Et un **secours qui marche toujours**, sans aucune automatisation :

> Réglages → *Déblocage Cloudflare* → **Secours : coller une session copiée du navigateur**.

Dans Edge ou Chrome : `F12` → onglet **Réseau** → clic droit sur la requête
`catalog` → **Copier → Copier en tant que cURL** → coller → *Importer cette
session*. La commande contient les cookies `HttpOnly` (`cf_clearance`) **et**
le User-Agent exact ; le bot récupère les deux ensemble, ce que Cloudflare
exige, puis relance les profils. C'est l'équivalent d'un FlareSolverr, mais
avec le navigateur que vous avez déjà.

### 1.3.7 — débloquer une vérification Cloudflare, gratuitement

Le bouton **🔓 Débloquer avec mon navigateur** (bandeau rouge du dashboard)
ouvre Edge ou Chrome sur la page Vinted, laisse la vérification Cloudflare se
terminer, puis **récupère les cookies de la session** — dont `cf_clearance`,
qui est `HttpOnly` et donc invisible depuis `document.cookie`. Ils sont
réinjectés dans le bot avec le **User-Agent exact** qui les a obtenus, et les
profils repartent immédiatement (plus d'attente de 5 min).

Pourquoi ça marche : `cf_clearance` est lié à l'adresse IP **et** au
User-Agent. `curl_cffi` imite déjà l'empreinte TLS de Chrome ; en gardant la
même IP et le même UA que le navigateur, la page catalogue est servie
normalement.

Comment c'est fait, dans ce dépôt :

| Élément | Détail |
| --- | --- |
| Pilotage | **Chrome DevTools Protocol** en WebSocket, implémenté avec la bibliothèque standard (`app/browser_session.py`) : aucune dépendance ajoutée, aucun `pip install` |
| Navigateur | Microsoft **Edge** (installé d'office sur Windows 10/11) ou Google Chrome, détectés automatiquement (`challenge.browser_path` pour forcer un chemin) |
| Cookie | `Network.getAllCookies` : récupère aussi les cookies `HttpOnly`, ce que le JavaScript de la page ne peut pas faire |
| Reprise | `POST /api/session/unblock` → `import_session()` + `resume_after_unblock()` : backoff et throttle remis à zéro |

**Marche à suivre**

1. Le bandeau rouge apparaît → cliquer **🔓 Débloquer avec mon navigateur** ;
2. une fenêtre s'ouvre sur Vinted : si Cloudflare affiche une case à cocher ou
   un « Vérifiez que vous êtes humain », **cochez-la** (le bot ne peut pas le
   faire à votre place, et c'est normal : c'est la preuve que la vérification
   est interactive) ;
3. dès que le catalogue s'affiche, la fenêtre se ferme, la session est
   importée et le journal affiche
   `Session importée depuis le navigateur (N cookie(s), clearance : oui) — 1 profil(s) relancé(s)`.

**Les solutions gratuites qui existent (et ce qu'elles valent)**

| Projet / moyen | Gratuit | Verdict |
| --- | --- | --- |
| **[FlareSolverr](https://github.com/FlareSolverr/FlareSolverr)** (Docker, port 8191) | oui | référence du domaine ; renseigner `challenge.solver_url` ou les réglages → le bot l'utilise en priorité. Ne résout **pas** les captchas interactifs |
| **[Byparr](https://github.com/ThePhaseless/Byparr)** (API compatible FlareSolverr, camoufox) | oui | même branchement que FlareSolverr (`solver_url`) |
| **[sarperavci/CloudflareBypassForScraping](https://github.com/sarperavci/CloudflareBypassForScraping)** | oui | navigateur furtif ; utile si vous préférez un service HTTP séparé |
| **Navigateur local (ce bot)** | oui | aucun service à lancer, Edge suffit ; validé par les tests du dépôt avec un faux serveur CDP |
| **Partage de connexion du téléphone** | oui | change l'IP : le blocage tombe souvent immédiatement |
| **[cloudscraper](https://github.com/VeNoMouS/cloudscraper)** | oui | **inutile ici** : ne résout plus les défis Cloudflare modernes (JavaScript + Turnstile) |
| Proxys publics gratuits | oui | quasi tous déjà signalés à Cloudflare : ne comptez pas dessus |
| Proxy **résidentiel** (payant) | non | la seule solution vraiment stable à long terme si le blocage revient chaque jour |

Ce qui reste vrai, sans langue de bois : si Cloudflare demande une action
**à chaque** requête, il faut la faire (ou payer un proxy résidentiel). Le bot
ne contourne pas un captcha — il réutilise proprement une session validée, ce
qui est exactement ce que fait FlareSolverr.

### 1.3.6 — les états trompeurs du dashboard

Un blocage Cloudflare affichait « Hors ligne » et « Flux interrompu » alors que
le moteur tournait. Trois corrections :

| Symptôme | Cause | Correction |
| --- | --- | --- |
| Pastille « Hors ligne » pendant un blocage | la pastille ne distinguait pas « moteur arrêté » de « Vinted refuse la requête » | la pastille affiche **« Vérification Vinted »** et le moteur reste annoncé actif |
| « Flux interrompu » alors que le serveur répond | le flux SSE n'était **jamais relancé** : un redémarrage du bot laissait l'onglet mort | reconnexion automatique (1,5 s → 30 s, plafond) + chien de garde : flux muet > 45 s = relance |
| « Hors ligne » sur un simple incident de 2 s | un seul échec de `/api/status` suffisait | il faut **3 échecs consécutifs** |

Trois ajouts pour aller avec :

* **bandeau Cloudflare** : nomme la cause (votre **adresse IP**), la marche à
  suivre (partage de connexion du téléphone, ou 1 h d'attente), l'âge du blocage,
  et un bouton **Tester la connexion** qui lance le diagnostic réel ;
* **bandeau webhook manquant** : sans webhook, une annonce est détectée mais
  aucune alerte ne part — le dashboard le dit maintenant en haut de page ;
* **démarrage express** : tant qu'aucun profil n'existe, un encadré demande un
  mot-clé, un prix max et un webhook, puis crée le profil en temps réel en un
  clic (bouton « Mode avancé » pour les filtres).

### « challenge-platform » : vérification Cloudflare

Si le journal affiche `page « challenge-platform »`, ce n'est plus un doute :
Vinted sert une **page de vérification navigateur** (Cloudflare) au lieu du
catalogue. Cette page contient du JavaScript que le bot ne peut pas exécuter —
et **insister aggrave le blocage** (les tentatives sont comptées).

Depuis la 1.3.5, le bot réagit comme il faut :

* pause de **60 s, 2 min, 5 min** (au lieu de réessayer toutes les 20 s) ;
* le bouton **scan manuel est refusé pendant 25 s** après un blocage, avec le
  temps restant — cliquer en boucle enfonçait le clou ;
* le message du dashboard conseille l'action utile au lieu de « self-healing ».

**Le test qui tranche en 60 secondes** : coupez le Wi-Fi, activez le partage de
connexion de votre téléphone, relancez le scan.

* les annonces arrivent → c'est bien l'adresse IP qui était visée ; attendez ou
  gardez cette connexion ;
* même blocage → ce n'est pas l'IP mais la détection navigateur : il faut un
  proxy résidentiel, ou attendre plusieurs heures.

Ce qui reste vrai, sans langue de bois : un défi Datadome est lié à votre
adresse IP. Si Vinted le sert à chaque requête, aucun outil honnête ne peut le
contourner. Dans ce cas :

1. **Attendez 15 à 60 min** sans interroger le site (le blocage se lève seul) ;
2. **Désactivez les scans manuels répétés** : chaque clic relance un défi ;
3. **Activez un proxy** (Réglages → Utiliser les proxys) — idéalement un proxy
   résidentiel ; les proxys publics gratuits sont souvent déjà bloqués ;
4. Vérifiez que le débit reste raisonnable (`pages = 1`, un profil par thème).

Le bot ne cherche plus à « insister » : il garde sa session, attend un peu, et
reprend à 20 s — c'est la seule stratégie qui, en pratique, laisse passer.

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

### Mon IP peut-elle être bloquée ?

Réponse honnête, sans promesse en l'air :

* Vinted (via Datadome) ne « bannit » pas une adresse résidentielle pour une
  simple consultation : il la **ralentit** — 403/429, page de vérification,
  puis des pauses de plus en plus longues. C'est exactement ce que montrent des
  journaux comme `Blocage détecté (HTTP 200, proxy=direct) → rotation + purge
  cookies` suivi de `Smart sleep 30s`.
* Un blocage **permanent** arrive surtout quand le rythme reste agressif
  pendant des heures, ou avec des dizaines de profils qui interrogent le même
  domaine en parallèle. Un compte Vinted n'est pas concerné ici : le bot ne se
  connecte jamais.
* Ce que le bot fait déjà pour vous : délais aléatoires, backoff progressif,
  rotation d'User-Agent et de cookies, purge de session après blocage, veille
  temps réel adaptative, et — depuis la 1.3.1 — **aucune requête de confort**
  (fiche article, profil vendeur) pendant une vague de blocages, car ces appels
  échouent et ajoutent des signaux.
* Ce qui réduit vraiment le risque : **un proxy (idéalement résidentiel)**,
  l'option « Utiliser les proxys » cochée, **un profil par thème**, un
  intervalle ≥ 1,5 s et `pages = 1`. Un pool public gratuit est souvent plus
  lent et plus bloqué que votre propre connexion : à utiliser en secours.
* Ce qui est garanti : rien. Aucun outil ne peut promettre « zéro blocage » ;
  le seul moyen de ne pas exposer son IP est de passer par un proxy ou un VPS.

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
  latence du dernier scan, bouton pause, création de profil.
* **Cartes stats** : profils actifs, annonces du jour, alertes envoyées, dernier
  scan, blocages et santé du pool.
* **Profils** : interrupteur ON/OFF, URL/host, prix, intervalle, nombre de mots
  whitelist/blacklist, seuils vendeur, webhook, dernier scan, compteurs,
  erreurs éventuelles. Actions : **Scanner**, **Aperçu**, **Dupliquer**,
  **Supprimer**.
* **Flux en direct** : chaque annonce est une carte avec sa **photo** (chargée
  sans référent pour éviter le hotlink), son **titre cliquable**, un bouton
  **« Voir l'annonce ↗ »**, le prix, la marque, la taille, l'état, le vendeur
  (`@pseudo` + étoiles, lui aussi cliquable) et les filtres du profil source
  (catégorie et marques).
  Filtrable par profil.
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
| `live_mode` | `true` | Suivi continu de tous les profils (temps réel). |
| `realtime_min_interval` | `1.5` | Intervalle minimal (secondes), après une trouvaille ou en rafale. |
| `realtime_max_interval` | `10.0` | Intervalle maximal (secondes) quand rien ne bouge. |
| `realtime_growth` | `1.6` | Facteur de croissance de l'intervalle au repos. |
| `realtime_burst_seconds` | `90` | Durée de la « rafale » rapide après une nouveauté. |
| `realtime_jitter` | `0.15` | Variation aléatoire (anti-rythme robotique). |
| `realtime_turbo` | `false` | Intervalle minimal constant (détection maximale). |
| `realtime_head_items` | `24` | Cartes analysées en tête de page à chaque passage. |
| `default_interval_seconds` | `60` | Intervalle des profils **hors** temps réel (les profils ont le leur). |
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
  --no-browser       N'ouvre pas le navigateur
  --config PATH      Fichier de configuration (défaut : config.json)
  --db PATH          Base SQLite (défaut : data/vinted_sniper.db)
  --check [QUERY]    Diagnostic réel Vinted puis sortie (sans dashboard)
  --brand MARQUE     Avec --check : teste une recherche filtrée sur une marque
                     (nom, identifiant ou URL ; index local d'abord)
  --webhook URL      Webhook Discord à tester avec --check
  --domain DOMAINE   Domaine pour --check (défaut : www.vinted.fr)
  --turbo            Vitesse maximale : intervalle minimal constant
  --interval SEC     Force l'intervalle minimal temps réel (ex. 2.5)
  --version          Affiche la version
```

Exemples :

```bash
python main.py --port 9001        # dashboard seul, sans ouvrir le navigateur (--no-browser)
python main.py --config /etc/vinted/config.json --db /var/lib/vinted/sniper.db
python main.py --host 0.0.0.0     # ⚠️ pensez à app.password si réseau partagé
python main.py --check "jordan 4" # diagnostic réel, sans lancer le dashboard
python main.py --check "chaussures" --brand nike   # avec le filtre de marque
python main.py --check "sneakers" --brand 1775     # par identifiant Vinted
python main.py --turbo            # détection maximale (assume le risque)
```

---

## API REST

Toutes les routes sont sous `/api`, en JSON, sans authentification si
`app.password` est vide.

| Méthode | Route | Rôle |
| --- | --- | --- |
| `GET` | `/health` | Ping + version + état du moteur. |
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
| `POST` | `/diagnose` | Test réel complet (`query`, `webhook`, `domain`). |
| `GET` | `/categories` | Catégories (`path` optionnel) : locales au 1er niveau, réelles ensuite. |
| `POST` | `/profiles/{id}/category` | Applique une catégorie au profil en gardant ses mots-clés. |
| `GET` | `/brands` | Marques : populaires sans paramètre, `letter=A` (live), `search=nike` (index local), ou `search=n&prefix=1` (toutes les marques commençant par N, `total` inclus). |
| `GET` | `/filters` | Catalogue des filtres Vinted (tailles, états, couleurs, tris) + `selected` lu depuis `?url=…`. |
| `POST` | `/filters/apply` | Applique des filtres à une URL (`url`, `size_ids`, `status_ids`, `color_ids`, `price_from`, `price_to`, `order`). |
| `POST` | `/profiles/{id}/brands` | Applique un filtre de marques (`brand_ids: [...]`) en conservant catégorie et mots-clés. |
| `GET` | `/brands/resolve` | Résout n'importe quelle marque depuis son URL ou son identifiant (`ref=…`). |
| `GET` | `/brands/sync` | État de l'index local (nombre de marques, import en cours). |
| `POST` | `/brands/sync` | Importe **toutes** les marques depuis les sitemaps officiels de Vinted. |

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
│   ├── engine.py            # sondage continu, détection incrémentale, SSE, alertes
│   ├── realtime.py          # intervalles adaptatifs (min/max, rafale, turbo)
│   ├── http_client.py       # curl_cffi, cookies, UA, pool de proxys
│   ├── vinted_api.py        # URLs, parsing des cartes SSR + RSC, fiches, vendeurs
│   ├── diagnostics.py       # test réel : session, catalogue, article, vendeur
│   ├── categories.py        # arbre des catégories Vinted (local + lecture live)
│   ├── brands.py            # marques : liste live, sitemaps complets, URLs
│   ├── filters.py           # prix, whitelist/blacklist, seuils vendeur
│   ├── notify.py            # embeds Discord, rate limit, retries
│   ├── utils.py             # texte, prix, dates, domaines
│   └── static/              # dashboard (HTML/CSS/JS, zéro dépendance)
│       ├── index.html
│       ├── styles.css
│       ├── app.js
│       └── favicon.svg
├── tests/                   # suite unittest (réseau local simulé)
│   ├── fake_vinted.py       # faux Vinted pour les tests, jamais chargé en prod
│   ├── test_categories.py   # catégories, URLs de profil, endpoints
│   └── ui/run.js            # test d'interface headless (jsdom, npm test)
└── data/                    # créé au lancement : SQLite + WAL
```

### Flux d'un passage (mode temps réel)

```text
Scheduler (tick 0,25 s) ─► profil dû ? ─► tâche de scan (concurrence bornée)
        │
        ▼
Session Vinted (cookies anonymes, UA) ──► page /catalog (HTML SSR)
        │                                      │
        │                                      ├─ 403/429 → rotation proxy/UA,
        │                                      │   purge cookies, backoff,
        │                                      │   ralentissement ×1,6…×8
        │                                      ▼
        │                      1re annonce identique ? ──oui──► fin immédiate
        │                                      │non
        │                                      ▼
        │                      cartes de tête (24) → annonces normalisées
        ▼
Filtres rapides (prix, blacklist titre) ─► description / vendeur en parallèle
        │                                      (seulement si un seuil l'exige)
        │                                      ▼
        │                              filtres complets
        ▼                                      │
déduplication (cache mémoire + SQLite)  ◄──────┘
        │
        ├─► flux SSE → dashboard (immédiat)
        ├─► alerte Discord (embed, immédiat)
        └─► enrichissement différé (photo HD, description, vendeur) → item_update
```

---

## Dépannage

| Symptôme | Piste |
| --- | --- |
| **`--check` reste silencieux ou semble figé** | Le diagnostic affiche désormais chaque étape en direct et s'arrête après 90 s. S'il s'arrête : lancé depuis une invite de commandes, testez `curl -I https://www.vinted.fr`. Un échec = pare-feu, antivirus, VPN ou proxy d'entreprise (et non le bot). |
| **403 / 429 en boucle** | Lancez `python main.py --check`. Augmentez `min_request_delay` (3–5 s), réduisez le nombre de profils actifs, activez un proxy résidentiel, cliquez sur **↻ Session**. |
| **0 annonce alors que Vinted répond** | Le diagnostic distingue page vide et structure inconnue. Si 0 carte sur une page de plusieurs Mo, Vinted a changé son HTML : ouvrez une issue avec la sortie de `--check`. |
| **Aucune alerte alors que des annonces existent** | Lancez un **Aperçu** : les annonces sont peut-être écartées par la blacklist ou les seuils vendeur. Vérifiez aussi que le profil est actif et que le premier scan (baseline) est passé. Consultez le journal. |
| **Pas de message Discord** | Testez avec **Tester Discord**. Vérifiez `notifications.enabled`, l'URL du webhook et que le salon autorise les webhooks. Les erreurs apparaissent en rouge dans le journal. |
| **Photos absentes** | Vinted peut changer ses CDN. L'URL est stockée telle que fournie ; le dashboard affiche un placeholder. Réessayez plus tard ou augmentez `detail_fetch`. |
| **Images non cliquables / liens cassés** | Vérifiez que l'URL du profil est bien sur un domaine `vinted.*`. L'aperçu affiche l'URL normalisée. |
| **Sous-catégories indisponibles** | Le 1er niveau est local ; les niveaux suivants sont lus sur Vinted (403/429 possible). Réessayez plus tard, les résultats sont mis en cache 1 h. |
| **Marques indisponibles** | La liste live est lue sur `/brands/by_letter/<lettre>` (cache 6 h). En cas de blocage, lancez **⬇ Importer toutes les marques** : l'index local reste consultable hors ligne, ou saisissez la marque comme mot-clé. |
| **Import des marques qui échoue** | Le message d'erreur exact s'affiche sous le bouton (sitemap introuvable, blocage, réseau). Vérifiez que `https://www.vinted.fr/robots.txt` est accessible depuis votre machine ; réessayez plus tard, l'index déjà importé reste utilisable. |
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

* `tests/test_core.py` : normalisation, URLs Vinted, textes compacts des cartes,
  filtres, SQLite, config, embeds.
* `tests/test_app.py` : API FastAPI + moteur complet sur un Vinted simulé
  (scan, flux, aperçu, pause, validation).
* `tests/test_http.py` : client HTTP contre un faux Vinted local (cookies,
  429 → retry, proxy mort → fallback direct, quarantaine).
* `tests/ui/run.js` : test d'interface headless (jsdom) du dashboard —
  `cd tests/ui && npm install && npm test`.
* `tests/test_realtime.py` : intervalles adaptatifs, throttling anti-blocage,
  détection incrémentale (page sautée, rafale > tête de page), flux SSE,
  migrations SQLite temps réel.
* `tests/test_parsing.py` : parseur SSR sur fixtures réalistes (cartes
  `grid-item`, payload RSC, page article OpenGraph, repli sans BeautifulSoup,
  filet de sécurité par liens).
* `tests/test_categories.py` : arbre des catégories, lecture du menu latéral
  réel, `build_profile_url` (mots-clés et prix conservés), endpoints
  `/api/categories` et `/api/profiles/{id}/category`.
* `tests/test_brands.py` : parsing des pages `/brands/by_letter/…`, filtre de
  recherche, URLs `catalog[]` + `brand_ids[]`, résolution d'une marque par URL
  ou identifiant, **import complet par sitemaps** (robots.txt, index, deux
  fichiers, doublons, échec réseau), endpoints `/api/brands`,
  `/api/brands/resolve`, `/api/brands/sync` et `/api/profiles/{id}/brands`.

**164 tests** au total. Aucun ne contacte Vinted ni Discord : le faux Vinted de
`tests/fake_vinted.py` n'est jamais importé par l'application.

---

## Limites & bonnes pratiques

* **Pas de contournement de captcha** ni de résolution de challenge : le but est
  de rester sous les radars, pas de forcer. Si Vinted exige un captcha, le bot
  patiente et réessaie.
* **Les endpoints publics changent.** C'est arrivé en septembre 2026 (API JSON
  → 404). Le parsing est volontairement tolérant : cartes SSR `grid-item`, puis
  payload RSC, puis JSON-LD, puis expressions régulières. Une mise à jour peut
  rester nécessaire si Vinted modifie encore sa structure — `--check` vous le
  dira immédiatement.
* **Pages article protégées** : Datadome protège davantage les fiches article que
  le catalogue. La description et la note vendeur sont donc « best-effort » :
  une alerte peut partir avec une note inconnue, jamais avec une annonce
  manquante à cause de ça.
* **« À la seconde » a une limite physique** : Vinted renvoie une page de
  plusieurs Mo par passage et Datadome compte les requêtes par IP. Le mode
  temps réel (1,5–10 s adaptatif) est le meilleur compromis ; `--turbo`
  (1,5 s constant) peut tenir sur une IP résidentielle propre, mais attendez-vous
  à des blocages si vous cumulez plusieurs profils ou un VPN partagé. Le moteur
  ralentit alors automatiquement au lieu de s'acharner.
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

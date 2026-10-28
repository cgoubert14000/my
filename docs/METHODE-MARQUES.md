# La méthode pour trouver les 56 433 marques (prompt pour Claude)

Ce document décrit **comment j'ai construit l'index des marques**, sans API
privée, sans compte Vinted et sans scraping agressif. Il est écrit pour être
donné tel quel à un agent qui code le même logiciel ailleurs.

Résumé de la chaîne :

```
robots.txt  →  sitemap index  →  sitemaps « brands »  →  URLs /brand/<id>-<slug>
            →  (id, slug) par marque  →  nom reconstruit depuis le slug  →  SQLite
```

---

## Étape 1 — `robots.txt` donne l'emplacement des sitemaps

```http
GET https://www.vinted.fr/robots.txt
```

On récupère toutes les lignes `Sitemap: …` (expression :
`^\s*Sitemap:\s*(\S+)\s*$`, insensible à la casse, multi-lignes).

Repères vérifiés sur `vinted.fr` : `ai-train=no`, `search=yes`, et un sitemap
index du type `https://www.vinted.fr/sitemap-fr.xml`.

> **Ne jamais coder l'URL en dur** : la lire dans `robots.txt` reste valable
> quand Vinted change de domaine (`vinted.fr`, `.de`, `.com`, `.it`…).
> Repli si `robots.txt` échoue : `https://<domaine>/sitemap.xml`.

## Étape 2 — l'index de sitemaps pointe vers les marques

```http
GET https://www.vinted.fr/sitemap-fr.xml
```

C'est un `<sitemapindex>` : on extrait toutes les balises `<loc>` puis on garde
celles dont l'URL finit par `/brands.xml` ou `/brand1.xml`, `/brand2.xml`…
(régression : `/brands?\d*\.xml$`).

Cas particulier à gérer : `robots.txt` peut **déjà** pointer un sitemap de
marques — dans ce cas inutile de passer par l'index.

Repère réel : `https://www.vinted.fr/sitemaps/fr/brands.xml`.

## Étape 3 — le sitemap de marques contient une URL par marque

```http
GET https://www.vinted.fr/sitemaps/fr/brands.xml
```

Chaque entrée ressemble à :

```xml
<url><loc>https://www.vinted.fr/brand/53-nike</loc></url>
<url><loc>https://www.vinted.fr/brand/7-h-m</loc></url>
<url><loc>https://www.vinted.fr/brand/364-zara</loc></url>
```

Extraction, par marque :

```python
re.search(r"/brand/(\d{1,10})(?:-([a-z0-9_-]+))?\s*$", url, re.I)
#  → id = "53",  slug = "nike"
```

* `id` = identifiant Vinted à mettre dans `brand_ids[]` (c'est **la seule**
  donnée indispensable) ;
* déduplication par `id` (un même identifiant peut apparaître deux fois) ;
* les sitemaps peuvent être volumineux **et gzippés** : accepter
  `Content-Encoding: gzip`, ou décompresser si le corps commence par `\x1f\x8b`.

## Étape 4 — le nom lisible se reconstruit depuis le slug

Le sitemap ne donne pas le nom commercial, seulement le slug. Règle appliquée :

1. découper le slug sur `-` et `_` ;
2. chaque mot : première lettre en majuscule ;
3. **sauf** les petits mots grammaticaux (à partir du 2ᵉ mot) :
   `de, du, des, la, le, les, et, and, of, the, for, by, x` ;
4. les nombres restent tels quels ;
5. tronquer à 80 caractères.

Exemples : `good-american-jeans` → **Good American Jeans**,
`levis` → **Levis**, `c-p-company` → **C P Company**, `h-m` → **H M**.

Deux améliorations qui valent le coup :

* un dictionnaire de correspondance pour les marques connues
  (`53` → `Nike`, `14` → `adidas`, `7` → `H&M`, `364` → `Zara`) ;
* reprendre le libellé réel vu sur la page `/brand/<id>-<slug>` quand on la
  visite plus tard (le HTML contient le nom exact, ex. `C.P. Company`).

## Étape 5 — stockage et recherche

Table SQLite unique :

```sql
CREATE TABLE IF NOT EXISTS brands (
    id         TEXT PRIMARY KEY,   -- identifiant Vinted, numérique
    slug       TEXT,
    name       TEXT,
    search_key TEXT NOT NULL,      -- nom normalisé, pour la recherche
    updated_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_brands_key ON brands (search_key);
```

Insertion en **une transaction**, en upsert :

```sql
INSERT INTO brands (id, slug, name, search_key, updated_at)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT(id) DO UPDATE SET
  slug=excluded.slug, name=excluded.name,
  search_key=excluded.search_key, updated_at=excluded.updated_at;
```

Normalisation de `search_key` (= ce qui rend la recherche utilisable) :
minuscules → suppression des accents (`NFKD` puis suppression des
diacritiques) → tout caractère non alphanumérique remplacé par une espace →
espaces compactés → `strip()`.

Recherche **par préfixe** (jamais `LIKE '%x%'` sur 56 000 lignes) :
`search_key LIKE 'cp%'` ou, mieux, `REPLACE(search_key,' ','') LIKE 'cp%'`
pour que `cp` trouve `C.P. Company`.

## Étape 6 — secours si les sitemaps sont bloqués

Dans cet ordre, et seulement en cas d'échec :

| Secours | Ce qu'on récupère | Limite |
| --- | --- | --- |
| `GET /brands/by_letter/<A..Z>` | liens `<a href="/brand/<id>-<slug>">` + libellé réel dans le texte du lien | ≈100 par lettre (triées par volume), donc quelques milliers |
| `GET /brands` | marques populaires du moment | très partiel |
| Liste locale en dur | ~23 marques connues (`53` Nike, `14` adidas…) | démarrage à froid uniquement |

Parsing de `/brands/by_letter/N` :

```python
r'<a\b[^>]*href="(?P<href>/brand/(?P<id>\d+)(?:-(?P<slug>[a-z0-9_-]+))?)"[^>]*>(?P<label>.*?)</a>'
```

Puis nettoyage du libellé : retirer les balises HTML, le compteur
(`"123 articles"`), le mot `Suivre`, compacter les espaces.

**Ce qui ne marche pas** (vérifié) : `/api/v2/brands` répond « jeton invalide »
sans session, et les endpoints de typeahead sont protégés par l'anti-bot.

## Étape 7 — politesse et robustesse

* un seul téléchargement par sitemap, **2 tentatives maximum** ;
* 1 requête toutes les ~1 s entre sitemaps, jamais en parallèle sur 5 sitemaps ;
* `timeout` 30–60 s (les sitemaps sont gros) ;
* `Accept-Encoding: gzip, deflate, br` et une empreinte TLS de navigateur
  (`curl_cffi impersonate="chrome"`) : ça suffit pour `robots.txt` et les
  sitemaps, même quand la page `/catalog` est bloquée par Cloudflare ;
* ne **jamais** réimporter l'index en boucle : un import réussi ne se rejoue
  pas (sinon 56 000 upserts à chaque démarrage) ;
* le résultat est vérifiable : `SELECT COUNT(*) FROM brands` → **56 433** sur
  `vinted.fr` (les sitemaps publient ~57 000 entrées, dont les doublons et les
  lignes sans identifiant exploitable sont écartés).

---

# Prompt à coller à Claude

> Tu vas implémenter dans ce projet la **découverte complète des marques
> Vinted** (≈56 000), sans API privée, sans compte, sans dépendance nouvelle.
> Ne l'invente pas depuis une liste : **télécharge-la** avec la méthode
> ci-dessous. Lis d'abord le projet (langage, base de données, conventions,
> tests) et réutilise l'existant ; adapte les noms mais garde exactement la
> logique. Implémente puis lance les tests, sans long plan préalable.
>
> **Chaîne de découverte**
>
> 1. `GET https://www.vinted.fr/robots.txt` → extraire toutes les lignes
>    `Sitemap: <url>` (regex `^\s*Sitemap:\s*(\S+)`, insensible à la casse).
>    Si aucune : repli sur `https://www.vinted.fr/sitemap.xml`.
> 2. Pour chaque sitemap listé : s'il finit par `/brands.xml` ou `/brand\d*\.xml`,
>    c'est un sitemap de marques → on le garde. Sinon `GET` l'URL et garder les
>    `<loc>` qui correspondent à `/brands?\d*\.xml$`.
> 3. `GET` chaque sitemap de marques (gérer `Content-Encoding: gzip` et le corps
>    qui commence par `\x1f\x8b`), extraire toutes les `<loc>`, puis pour chacune :
>    `re.search(r"/brand/(\d{1,10})(?:-([a-z0-9_-]+))?\s*$", url, re.I)`.
>    `id` = groupe 1 (identifiant `brand_ids[]`), `slug` = groupe 2 (peut être vide).
>    Dédupliquer par `id`.
> 4. Construire le nom lisible depuis le slug : split sur `-`/`_`, capitaliser
>    chaque mot, garder en minuscules les petits mots à partir du 2ᵉ mot
>    (`de, du, des, la, le, les, et, and, of, the, for, by, x`), laisser les
>    nombres tels quels, tronquer à 80 caractères. Écraser ce nom avec un
>    dictionnaire de marques connues (`53` Nike, `14` adidas, `7` H&M,
>    `364` Zara, `1775` New Balance, `1195` Asics, `11445` Converse,
>    `309` Dr. Martens, `567` Gucci). Si le slug est vide : `Marque <id>`.
> 5. Écrire en base (table `brands`) avec `id TEXT PRIMARY KEY`, `slug`, `name`,
>    `search_key`, `updated_at`, index sur `search_key`. `search_key` =
>    `nom + " " + slug + " " + id` → minuscules → accents supprimés (NFKD +
>    diacritiques) → tout caractère non alphanumérique devient une espace →
>    espaces compactés → `strip()`. Insertion **en une transaction** avec
>    `ON CONFLICT(id) DO UPDATE` (idempotent).
>
> **Contraintes techniques**
>
> - 2 tentatives maximum par URL, `timeout` 30 s (60 s pour un sitemap),
>   `Accept-Encoding: gzip`, une empreinte TLS de navigateur si le projet a
>   déjà `curl_cffi` (`impersonate="chrome"`) ;
> - une requête à la fois, ~1 s entre deux sitemaps ;
> - si un sitemap échoue : journaliser et **continuer** les autres (un index
>   partiel vaut mieux que rien) ;
> - ne relancer l'import que si la table est vide ou si l'utilisateur le
>   demande explicitement ;
> - journaliser une ligne à la fin :
>   `Index des marques synchronisé : 56 433 marques disponibles localement.`
>
> **Secours (uniquement si les sitemaps échouent)** : `GET
> https://www.vinted.fr/brands/by_letter/<A..Z>`, extraire
> `<a href="/brand/<id>-<slug>">…</a>`, nettoyer le libellé (retirer les
> balises, le compteur « N articles », le mot « Suivre »). Puis `/brands`.
> Enfin seulement, une petite liste en dur de ~20 marques connues pour que
> l'interface ne soit jamais vide.
>
> **Ce qui ne marche pas, ne le tente pas** : `/api/v2/brands` (« jeton
> invalide » sans session), les endpoints de typeahead (protégés par
> l'anti-bot), et mettre les 56 000 marques en dur dans le code.
>
> **Recherche attendue** : par **préfixe** sur `search_key` (jamais
> `LIKE '%x%'`), insensible à la casse et aux accents, résultats dès 1
> caractère (`cp` doit trouver `C.P. Company`), tri : vrais préfixes d'abord,
> puis longueur du nom, puis alphabétique, avec le total de correspondances.
> Objectif < 20 ms.
>
> **Tests obligatoires**
>
> 1. `brands_from_sitemap()` sur un extrait XML réaliste → bons `id`/`slug`,
>    doublons éliminés, nom reconstruit (`levis` → `Levis`,
>    `good-american-jeans` → `Good American Jeans`) ;
> 2. parsing de `robots.txt` (plusieurs lignes `Sitemap:`) → toutes les URL ;
> 3. filtrage des sitemaps : garde `/sitemaps/fr/brands.xml` et
>    `/brands2.xml`, rejette `/sitemaps/fr/items1.xml` ;
> 4. import deux fois → même nombre de lignes (upsert idempotent) ;
> 5. `search("cp")` contient `C.P. Company`, `search("cafe")` trouve `Café`,
>    `search("NIKE")` trouve `Nike` ;
> 6. recherche par préfixe et non « contient » : `search("ike")` ne doit pas
>    proposer `Nike` en tête ;
> 7. un sitemap en erreur (HTTP 503) → les autres sont quand même importés.
>    Aucun test ne doit toucher le réseau : injecter le HTML/XML en paramètre.
>
> **Critères d'acceptation à me montrer** : le nombre total importé
> (`SELECT COUNT(*) FROM brands`), le temps d'import, `git diff --stat`, la
> liste des fichiers créés/modifiés.

---

## Repères vérifiés (à rappeler à Claude si besoin)

| Élément | Valeur constatée |
| --- | --- |
| Nombre de marques importées (`vinted.fr`) | **56 433** |
| Sitemap de marques | `https://www.vinted.fr/sitemaps/fr/brands.xml` |
| Index sitemaps | `https://www.vinted.fr/sitemap-fr.xml` |
| Forme d'une URL de marque | `/brand/53-nike`, `/brand/7-h-m` |
| Filtre dans la recherche | `/catalog?catalog[]=1231&brand_ids[]=53` (la forme chemin `/catalog/1231-slug?brand_ids[]=` est ignorée) |
| Nombre de marques combinables par profil | 20 |
| `/api/v2/brands` | non utilisable sans jeton |

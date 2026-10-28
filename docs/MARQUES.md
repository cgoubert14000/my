# Les 57 000 marques : obtenir le fichier et l'intégrer

Ce document sert de **brief prêt à coller** pour un autre agent/développeur
(Claude, par exemple) qui doit embarquer la liste complète des marques Vinted
dans le bot, sans réseau.

---

## 1. Obtenir le fichier (côté utilisateur, 5 secondes)

L'index vit dans `data/vinted_sniper.db` (table `brands`), alimenté une fois
par les sitemaps Vinted. Trois façons de le sortir :

| Méthode | Commande / geste | Résultat |
| --- | --- | --- |
| **Dashboard** | bouton *Choisir des marques* → **💾 Exporter la liste (CSV)** | `marques-vinted.csv` téléchargé |
| **Ligne de commande** | `vinted-sniper.exe --export-brands marques-vinted` | `.csv` **et** `.json` à côté de l'exécutable |
| **API** | `GET /api/brands/export` | flux `text/csv` (en-tête `Content-Disposition`) |

Ordre de grandeur réel : **56 433 marques** → CSV ≈ 1,8 Mo, JSON ≈ 4,3 Mo.

---

## 2. Format attendu (contrat)

CSV, UTF-8 (BOM toléré), une ligne par marque :

```csv
id,slug,name
53,nike,Nike
7,h-m,H&M
364,zara,Zara
```

* `id` : identifiant numérique Vinted (utilisé dans `brand_ids[]`) — **obligatoire** ;
* `slug` : segment d'URL (`/brand/53-nike`) — informatif ;
* `name` : libellé affiché — informatif.

Variantes acceptées par le lecteur (`app/brand_pack.py`, `read_brand_file`) :

* colonnes dans un autre ordre (l'en-tête fait foi) ;
* CSV **sans en-tête** (`53,nike,Nike`) ;
* JSON : `[{"id":"53","slug":"nike","name":"Nike"}]`, liste de triplets
  `[["53","nike","Nike"]]`, ou objet `{"brands":[…]}` ;
* lignes vides, BOM, `id` non numérique (ignoré), `name` vide (repli sur le slug).

---

## 3. Intégration dans le bot (déjà faite en 1.3.9, à réutiliser)

Le chargement automatique existe : **il suffit de livrer le fichier**.

1. Copier le CSV dans `app/data/brands.csv` (versionné, embarqué par
   `tools/build_executable.py` via `--add-data app/data`) ;
2. ou le poser **à côté de l'exécutable** sous le nom `brands.csv`
   (reconnu aussi : `brands.json`, `marques.csv`, `marques.json`,
   `marques-vinted.csv`, `marques-vinted.json`).

Au démarrage, `AppState._seed_brand_index()` appelle
`brand_pack.seed_database(db)` :

* si la table `brands` contient déjà des données → **rien n'est écrasé**
  (l'index en ligne est plus frais qu'un fichier livré) ;
* sinon, le fichier est importé (upsert idempotent) et le journal affiche
  `Index des marques chargé depuis brands.csv : 56 433 marques…`.

Régénérer le pack depuis un export :

```bash
python tools/make_brand_pack.py marques-vinted.csv
```

Le script valide le fichier (doublons, identifiants non numériques, noms
génériques) puis écrit `app/data/brands.csv` et `app/data/brands.json`.

Import manuel dans une base existante :

```bash
vinted-sniper.exe --import-brands marques-vinted.csv
```

---

## 4. Points d'attention

* **Ne pas committer** `data/` (base locale) : le `.gitignore` l'exclut, avec
  une exception pour `app/data/**` (pack livré).
* Le fichier doit rester **stable et trié par nom** : le diff Git devient lisible.
* La recherche locale est insensible aux accents, à la casse et aux séparateurs
  (`brand_search_key`) : inutile de normaliser les noms à la main.
* Un index importé depuis un fichier ne se met **pas** à jour tout seul ; le
  bouton « Importer toutes les marques Vinted » reste le moyen de rafraîchir.

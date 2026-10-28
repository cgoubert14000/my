# Prompt à donner à Claude — intégrer les 56 433 marques Vinted

Deux étapes, dans cet ordre. Ne sautez pas la première : le prompt suppose que
le fichier est **déjà dans le projet** que Claude lit.

---

## Étape 1 — fournir le fichier (2 minutes)

1. Lancez **votre** bot Vinted (celui qui a déjà l'index) :
   - dashboard → *Choisir des marques* → **💾 Exporter la liste (CSV)**, ou
   - `vinted-sniper.exe --export-brands marques-vinted`
2. Vous obtenez `marques-vinted.csv` (~1,8 Mo, **56 433 lignes** + l'en-tête).
3. Déposez ce fichier **à la racine du projet** que Claude est en train de coder
   (à côté de son `README` / de son `pyproject.toml`, peu importe le nom exact).

Vérification en une commande (attendu : `56433` puis `marques-vinted.csv`) :

```bash
wc -l marques-vinted.csv
ls -lh marques-vinted.csv
```

---

## Étape 2 — coller ce prompt à Claude

> Tu vas ajouter à ce projet un **index local complet des marques Vinted**
> (56 433 marques), sans scraping, sans réseau, sans dépendance nouvelle.
>
> **Fichier fourni** : `marques-vinted.csv` à la racine du projet.
> Format UTF-8 : `id,slug,name` — `53,nike,Nike` / `364,zara,Zara` /
> `7,h-m,H&M`. Les `id` sont les identifiants Vinted utilisés dans
> `brand_ids[]`. **N'invente jamais d'identifiant** : la seule source est ce
> fichier.
>
> **Avant d'écrire du code** : lis le projet (langage, ORM ou SQLite brut,
> conventions, tests existants) et réutilise ce qui existe. Si le projet n'est
> pas en Python, adapte les noms mais **garde exactement le comportement
> décrit**. Ne fais pas de plan de 30 lignes : implémente, puis lance les tests.
>
> ### 1. Stockage
> Table `brands` (migration idempotente, jouée au démarrage si absente) :
> - `id TEXT PRIMARY KEY` (identifiant Vinted, numérique),
> - `slug TEXT`, `name TEXT`,
> - `search_key TEXT NOT NULL` (voir §2),
> - `updated_at TEXT`.
> - Index sur `search_key`.
>
> ### 2. Clé de recherche (le point qui fait tout marcher)
> `search_key = normalize(f"{name} {slug} {id}")` avec :
> minuscules → suppression des accents (`NFKD` + suppression des diacritiques)
> → remplacement de tout caractère non alphanumérique par un espace →
> espaces multiples compactés → `strip()`.
> Exemple : `C.P. Company` → `c p company`, `Levi's` → `levi s`,
> `H&M` → `h m`.
>
> ### 3. Import du CSV (tolérant)
> - BOM, guillemets, virgules dans un nom (`"Nike, Inc."`), lignes vides ;
> - en-tête `id,slug,name` **ou** aucun en-tête ;
> - colonnes dans un ordre différent (l'en-tête fait foi) ;
> - `id` non numérique → ligne ignorée ; `name` vide → repli sur le `slug` ;
> - doublon d'`id` → le dernier gagne ;
> - insertion en **une seule transaction** (`executemany` + upsert
>   `ON CONFLICT(id) DO UPDATE`).
> - **Performance exigée** : 56 433 lignes importées en **moins de 2 s**.
>
> ### 4. Chargement automatique au démarrage
> - Si la table `brands` est **vide**, chercher un fichier `brands.csv` (ou
>   `brands.json`, `marques.csv`, `marques-vinted.csv`) dans cet ordre :
>   à côté de l'exécutable → dans `app/data/` (ressources embarquées) → dossier courant.
> - Si la table contient **déjà** des données : **ne rien écraser** (un index
>   récupéré en ligne est plus frais qu'un fichier livré), et le dire en log.
> - Journaliser une seule ligne du type :
>   `Index des marques chargé depuis brands.csv : 56 433 marques disponibles.`
>
> ### 5. Recherche / autocomplétion
> - `search(query, limit=500)` : recherche **par préfixe** (pas `LIKE '%x%'`,
>   sinon 56 k lignes scannées à chaque frappe) ;
> - insensible à la casse **et aux accents** : taper `cafe` doit trouver `Café` ;
> - **dès 1 caractère** : taper `cp` doit proposer `C.P. Company` ;
> - tri : les marques qui **commencent** réellement par la saisie d'abord, puis
>   par longueur de nom, puis alphabétique ;
> - renvoyer aussi le **total** de correspondances (« 12 marque(s) commencent
>   par « cp » — 500 affichées ») ;
> - objectif de latence : **< 20 ms** par requête.
>
> ### 6. Interface
> - champ de recherche avec résultat **immédiat** (debounce ~150 ms, pas d'appel
>   réseau par frappe) ;
> - sélection **multiple** avec pastilles retirables ;
> - si aucun index : bouton « Importer les marques » (import du CSV local) ;
> - bouton « Exporter la liste (CSV) » qui retélécharge `id,slug,name`.
>
> ### 7. Ligne de commande
> - `--import-brands FICHIER` : importe puis affiche
>   `✅ N marque(s) importée(s) — index local : N`.
> - `--export-brands [FICHIER]` : écrit `.csv` **et** `.json`
>   (`[{"id","slug","name"}]`), triés par nom.
>
> ### 8. Tests à écrire (obligatoires)
> 1. import du vrai fichier → `SELECT COUNT(*) FROM brands` = **56 433** ;
> 2. `search("cp")` contient `C.P. Company` ;
> 3. `search("cafe")` trouve `Café` (accents) et `search("NIKE")` trouve `Nike` ;
> 4. CSV sans en-tête, avec BOM, avec `"Nike, Inc."`, avec un `id` vide → aucune
>    ligne invalide insérée, aucune exception ;
> 5. relancer l'import deux fois → **toujours 56 433** (upsert idempotent) ;
> 6. démarrage sur base vide → l'index se charge tout seul ;
> 7. démarrage sur base déjà remplie → fichier ignoré (pas d'écrasement) ;
> 8. perf : import < 2 s, recherche < 20 ms (mesure indicative, pas un test
>    qui casse la CI).
>
> ### 9. Critères d'acceptation (à me montrer à la fin)
> - la sortie du test 1 (`56433`) ;
> - les résultats de `search("cp")`, `search("nike")`, `search("zara")` ;
> - le temps d'import mesuré ;
> - `git diff --stat` ;
> - la liste des fichiers créés/modifiés.
>
> ### 10. Interdits
> - télécharger la liste depuis un site au démarrage (le fichier est fourni) ;
> - appeler une API par frappe clavier ;
> - stocker les marques en dur dans le code (`brands.py` de 56 000 lignes) ;
> - bloquer le démarrage si le fichier est absent (log + démarrage normal).

---

## Si Claude demande « d'où vient ce fichier ? »

Réponse courte à lui donner :

> Export de l'index des marques Vinted construit à partir des sitemaps publics
> (`/sitemaps/fr/brands.xml`), stocké localement. Les `id` sont ceux que Vinted
> utilise dans `brand_ids[]`. Repères vérifiés : `53` Nike, `14` adidas,
> `7` H&M, `364` Zara.

## Si vous n'avez pas encore le CSV

Deux options :

1. demandez-le moi (je le commite dans votre dépôt dès que vous me l'envoyez) ;
2. utilisez ma version du bot : **1.3.9**, où
   `--export-brands marques-vinted` produit le fichier en une commande
   (https://github.com/cgoubert14000/my/raw/arena/cbaec6f0-my/VintedSniper-1.3.9.zip).

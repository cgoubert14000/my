# 📋 Mes commandes — Programmateur Facebook « Bestofhumourofficiel »

> **Règle n°1 :** toutes les commandes se tapent **depuis le dossier `fb_auto`**
> (là où se trouvent `programmer.py`, `planning.txt`, le dossier `images`…).
>
> **Windows** → `python`
> **Mac / Linux** → `python3`
>
> ⚠️ Attention : ton `config.json` contient un token **permanent** qui permet de
> publier sur ta page. Ne le mets jamais sur GitHub, ne le partage jamais.

---

## ⚡ L'essentiel : programmer tes images en 3 commandes

### 1. Vérifier que tout est branché (à faire en premier)

```bash
python3 diagnostic.py
```

Tu dois lire **« Tout est bon ! »**.

---

### 2. APERÇU — voir le planning sans rien envoyer  ← c'est ça « analyser »

```bash
python3 programmer.py "13/10/2026" --par-jour 5 --limite 20 --test
```

Le `--test` **n'envoie rien**. Il affiche :

```
### MARDI 13 OCTOBRE ###

  Image 1 : 01.jpg
    programmee pour le 13/10/2026 a 12h00
    hashtags : #humour #humoriste #drole #rire #humournoir
```

C'est l'étape qui te montre ce qui va être publié, quand, et avec quelle image.

---

### 3. PROGRAMMER pour de vrai (sans `--test`)

```bash
python3 programmer.py "13/10/2026" --par-jour 5 --limite 20
```

Le script **demande confirmation** (`oui/non`) avant d'envoyer quoi que ce soit.

Puis vérifie dans **Meta Business Suite → Planificateur**.

---

### Pour voir ce qui est déjà programmé

```bash
python3 nettoyer.py
```

(et `python3 nettoyer.py --supprimer` pour tout effacer et repartir de zéro)

---

## 🖼️ Les images (planning.txt)

| Ce que je veux | La commande |
|---|---|
| Aperçu de 20 images, 5/jour | `python3 programmer.py "13/10/2026" --par-jour 5 --limite 20 --test` |
| Programmer ces 20 images | `python3 programmer.py "13/10/2026" --par-jour 5 --limite 20` |
| Tout le lot (63 actifs) | `python3 programmer.py "13/10/2026" --par-jour 5` |
| 1 seule image par post, toutes les heures | `python3 programmer.py "13/10/2026 18:00"` |
| Toutes les 2 heures | `python3 programmer.py "13/10/2026 18:00" --intervalle 120` |
| 3 images par jour | `python3 programmer.py "13/10/2026" --par-jour 3` |
| Mes heures précises | `python3 programmer.py "13/10/2026" --heures "12:30,19:00,21:30"` |
| Reprendre à partir de l'image 21 | `python3 programmer.py "13/10/2026" --par-jour 5 --depuis 21.jpg` |
| Démarrer demain | `python3 programmer.py "demain" --par-jour 5` |

**Rappels Facebook :** minimum **10 minutes** dans le futur, maximum **30 jours**.
Le premier post doit donc être au moins 10 min après l'heure à laquelle tu lances la commande.

Les grilles `--par-jour` (heures de forte audience) :

| `--par-jour` | Heures |
|---|---|
| 1 | 19:00 |
| 2 | 12:30 · 19:00 |
| 3 | 12:30 · 18:00 · 21:00 |
| 4 | 12:30 · 17:00 · 19:30 · 21:30 |
| **5** | **12:00 · 15:00 · 18:00 · 20:00 · 22:00** |
| 6 | 09:00 · 12:00 · 15:00 · 18:00 · 20:00 · 22:00 |

---

## ✍️ Les blagues écrites (planning_textes.txt)

```bash
# Aperçu
python3 programmer.py "13/10/2026" --planning planning_textes.txt --par-jour 5 --textes --limite 20 --test

# Programmation réelle
python3 programmer.py "13/10/2026" --planning planning_textes.txt --par-jour 5 --textes --limite 20
```

Le `--textes` utilise une grille d'heures **décalée** de celle des images
(10:00 · 13:30 · 16:30 · 19:00 · 21:00) pour qu'une image et une blague ne
tombent jamais à la même minute.

---

## 🎬 Les Reels (dossier `reel/`)

C'est le **seul** endroit du bot qui « analyse » vraiment des fichiers : il
ouvre chaque vidéo et dit si Facebook va l'accepter.

```bash
python3 reels.py --verifier        # analyse chaque vidéo (format, durée, ratio 9:16)
python3 reels.py --corriger        # recadre en 9:16 -> reel/pretes/
python3 reels.py --planning        # génère planning_reels.txt
python3 reels.py --programmer "13/10/2026" --heure 19:00 --test   # aperçu
python3 reels.py --programmer "13/10/2026" --heure 19:00          # pour de vrai
```

---

## 📥 Récupérer du contenu neuf

```bash
python3 scraper.py "funny cat" 10                                    # images libres de droits
python3 scraper.py "funny cat" 10 --planning --hashtags "#drole #rire"  # + planning
python3 scraper_textes.py 100                                        # blagues écrites
```

> Cherche **en anglais** (`"funny dog"` et pas `"chien drôle"`) : il y a 10× plus de résultats.
> `historique.json` évite de retélécharger deux fois la même image.

---

## 🪟 Si tu es sur Windows

**Solution la plus simple : double-clique sur `LANCER.bat`** dans le dossier `fb_auto`.
Un menu s'affiche, tu tapes juste un chiffre :

```
  1. Verifier la configuration
  2. Voir les posts deja programmes

  --- IMAGES ---
  3. Apercu       : 20 images, 5 par jour
  4. PROGRAMMER   : 20 images, 5 par jour

  --- TEXTES ---
  5. Apercu       : 20 blagues, 5 par jour
  6. PROGRAMMER   : 20 blagues, 5 par jour

  7. Supprimer TOUS les posts programmes
```

**Erreur `can't open file 'C:\programmer.py'`** = tu es dans le mauvais dossier :
ouvre le dossier `fb_auto`, clique dans la **barre d'adresse**, tape `cmd` puis
Entrée, et retape la commande.

**« python n'est pas reconnu »** → essaie `py` à la place de `python`.

---

## 🆘 En cas de problème

| Symptôme | Commande |
|---|---|
| « Invalid OAuth access token » (code 190) | `python3 trouver_ma_page.py` ← le token est mort, on le refait |
| « Permissions error » (code 200) | `python3 diagnostic.py` ← il dit quelle permission manque |
| N'importe quel doute | `python3 diagnostic.py` |
| Tout effacer et recommencer | `python3 nettoyer.py --supprimer` |

---

## ❌ Ce que ce bot NE fait PAS

Il n'y a **aucune commande qui « regarde » le contenu des images** avec de l'IA.
L'image est envoyée telle quelle, avec son texte et ses hashtags.

C'est pour ça que les 100 images de `planning.txt` ont été **inspectées une par
une à la main** : 37 sont marquées `ACTIF: non` avec la raison en commentaire
(ex. `# ECARTE : antisemitisme`).

Deux conséquences pratiques :

1. **Toute nouvelle image arrive sans filtre** → vérifie-la à l'œil avant de la
   programmer (ou demande un script `analyser.py`, voir plus bas).
2. Dans `planning.txt`, toutes les lignes `TEXTE:` sont **vides** : les posts
   partent donc avec les hashtags seuls. Si tu veux une légende écrite pour
   chaque image, elle doit être saisie à la main dans le fichier — ou générée
   automatiquement par un script d'analyse (IA de vision).

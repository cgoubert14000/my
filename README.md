# Bot Python de publication d’images sur Facebook

Ce projet publie automatiquement **uniquement sur la Page Facebook « Madame Portugais »**, à une heure aléatoire dans chacune de **3 plages horaires par jour**. Il utilise uniquement l’API Graph officielle de Meta — aucune automatisation du navigateur. Un contrôle du nom et de l’identifiant de la Page est effectué au démarrage avant tout envoi.

Configuration par défaut, en heure de Paris :

1. matin : `07:00–10:00` ;
2. midi : `12:00–15:00` ;
3. soir : `18:00–22:00`.

Les heures exactes sont tirées une seule fois puis enregistrées dans SQLite : redémarrer le PC ou le script ne change donc pas le planning et ne republie pas une image déjà envoyée.

> **Important :** l’API officielle permet ce fonctionnement pour une **Page Facebook**, pas pour un profil personnel. Le PC doit rester allumé, connecté à Internet et sans mise en veille pendant les horaires choisis.

## Fonctionnement

- surveille le dossier `images/to_post` ;
- choisit la prochaine image par ancienneté (modifiable) ;
- lit sa légende dans un fichier `.txt` du même nom ;
- publie via `/{PAGE_ID}/photos` ;
- mémorise l’empreinte SHA-256 pour empêcher les doublons ;
- déplace l’image publiée dans `images/posted/AAAA-MM-JJ` ;
- retente les erreurs réseau temporaires, mais pas un jeton expiré ;
- conserve son planning et son historique dans `data/facebook_bot.sqlite3`.

Formats acceptés par la file locale : `.jpg`, `.jpeg`, `.png`, `.gif` et `.webp`. JPEG ou PNG sont conseillés.

## 1. Préparer Meta for Developers

Vous devez être administrateur de la Page **Madame Portugais** et avoir une application sur [Meta for Developers](https://developers.facebook.com/apps/).

1. Ouvrez votre application Meta (une application de type **Business** convient).
2. Dans l’[Explorateur de l’API Graph](https://developers.facebook.com/tools/explorer/), sélectionnez cette application.
3. Générez un **User Access Token** avec :
   - `pages_show_list` ;
   - `pages_read_engagement` ;
   - `pages_manage_posts`.
4. Dans l’explorateur, exécutez :

   ```text
   GET /me/accounts?fields=id,name,access_token
   ```

5. Dans la réponse, repérez votre Page :
   - `id` devient `FACEBOOK_PAGE_ID` ;
   - `access_token` de cette entrée devient `FACEBOOK_PAGE_ACCESS_TOKEN`.

Utilisez bien **le jeton de la Page**, et non le jeton utilisateur. Ne collez jamais ce jeton dans une discussion, une capture d’écran ou un dépôt Git. Le fichier `.env` est déjà ignoré par Git.

### Mode développement et validation Meta

- Tant que l’application est en mode **Development**, seuls les comptes ayant un rôle dans l’application (administrateur, développeur ou testeur) peuvent normalement l’utiliser. Pour votre propre Page administrée par ce même compte, cela suffit souvent pour les essais.
- Pour permettre à d’autres utilisateurs de connecter leurs Pages, il faut généralement passer l’application en **Live**, demander l’**App Review** des permissions et éventuellement effectuer la vérification Business.
- Les jetons peuvent expirer ou être invalidés après un changement de mot de passe/permission. Contrôlez leur durée avec l’outil officiel **Access Token Debugger** et prévoyez leur renouvellement. Ne mettez jamais l’App Secret dans ce bot.

## 2. Installer le bot

Python **3.10 ou plus récent** est nécessaire.

### Windows — méthode simple

Après avoir extrait ou cloné ce projet, double-cliquez sur :

```text
CONFIGURER.bat
```

Le fichier installe le bot, demande le nouveau jeton dans une saisie invisible, vérifie qu’il appartient à Madame Portugais et l’enregistre localement. Ensuite, double-cliquez sur :

```text
LANCER_BOT.bat
```

La fenêtre doit rester ouverte pour que les publications programmées fonctionnent.

### Windows — méthode PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
Copy-Item .env.example .env
```

Si PowerShell bloque l’activation, on peut lancer directement `.venv\Scripts\python.exe` à la place de `python`.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
cp .env.example .env
```

### Enregistrer le jeton sans l’afficher

La méthode recommandée demande le jeton dans une saisie masquée, vérifie immédiatement qu’il appartient à **Madame Portugais**, puis l’enregistre uniquement dans le fichier local `.env` :

```bash
python -m facebook_bot setup
```

Collez le **nouveau** jeton quand le programme le demande : aucun caractère ne s’affichera pendant la saisie. Ne passez jamais le jeton comme argument d’une commande et ne l’envoyez jamais dans une discussion.

La configuration enregistrée sera :

```dotenv
FACEBOOK_EXPECTED_PAGE_NAME=Madame Portugais
FACEBOOK_PAGE_ID=1098568206676051
FACEBOOK_PAGE_ACCESS_TOKEN=valeur_masquée
FACEBOOK_API_VERSION=v26.0
```

Si l’ID appartient à une autre Page, la commande refuse le jeton et n’enregistre rien. Le fichier `.env` persiste sur l’ordinateur et est ignoré par Git, mais Meta peut toujours expirer ou révoquer un jeton : aucun jeton ne peut être garanti « pour toujours ». Il faudra relancer `setup` lors d’un renouvellement.

Aucun identifiant Facebook, mot de passe, App Secret ou jeton utilisateur n’est nécessaire dans le code.

## 3. Régler les 3 plages horaires

Dans `.env` :

```dotenv
BOT_TIMEZONE=Europe/Paris
POSTING_WINDOWS=07:00-10:00,12:00-15:00,18:00-22:00
```

Il faut exactement trois plages, sans chevauchement, au format `HH:MM-HH:MM`. Elles doivent commencer et finir le même jour. Exemple alternatif :

```dotenv
POSTING_WINDOWS=06:30-08:00,11:45-13:15,19:00-23:00
```

À chaque nouvelle journée, le bot choisit une heure aléatoire différente dans chaque plage. Un créneau déjà créé reste stable dans la base SQLite.

## 4. Ajouter les images et légendes

Déposez les fichiers dans `images/to_post` :

```text
images/to_post/
├── 001-plage.jpg
├── 001-plage.txt
├── 002-ville.png
└── 002-ville.txt
```

Contenu possible de `001-plage.txt` :

```text
Belle journée au bord de la mer ☀️
#voyage #photo
```

Le texte UTF-8 entier devient la légende. Sans fichier `.txt`, la valeur `DEFAULT_CAPTION` du `.env` est utilisée. Avec `QUEUE_ORDER=oldest`, l’image ajoutée la plus ancienne part en premier. Les autres choix sont `alphabetical` et `random`.

## 5. Tester sans publier

Afficher les heures choisies aujourd’hui et demain :

```bash
facebook-image-bot schedule --days 2
```

Vérifier la prochaine image sans contacter Facebook :

```bash
facebook-image-bot post-now --dry-run
```

Vérifier le jeton et la Page (lecture seule, aucune publication) :

```bash
facebook-image-bot doctor
```

Le diagnostic doit finir par :

```text
✓ Destination verrouillée : Madame Portugais (ID ...)
Le bot est prêt. Ce test n'a rien publié.
```

## 6. Faire un premier envoi puis lancer le bot

Publier immédiatement la prochaine image :

```bash
facebook-image-bot post-now
```

Une fois le résultat vérifié sur la Page, lancer le service continu :

```bash
facebook-image-bot run
```

Laissez cette fenêtre ouverte. `Ctrl+C` arrête proprement le bot. Pour voir davantage de détails :

```bash
facebook-image-bot -v run
```

Pour une simulation continue totalement séparée du vrai planning :

```bash
facebook-image-bot run --dry-run
```

Compter les nouvelles images restantes :

```bash
facebook-image-bot queue
```

Si la commande `facebook-image-bot` n’est pas reconnue, utilisez l’équivalent :

```bash
python -m facebook_bot doctor
python -m facebook_bot run
```

## Démarrage automatique sur un PC

Le plus simple sous Windows est le **Planificateur de tâches** :

1. créer une tâche « au démarrage » ou « à l’ouverture de session » ;
2. programme : chemin complet vers `.venv\Scripts\pythonw.exe` (ou `python.exe` pour conserver la console) ;
3. arguments : `-m facebook_bot run` ;
4. « Démarrer dans » : chemin complet de ce projet ;
5. autoriser le redémarrage de la tâche en cas d’échec ;
6. désactiver la mise en veille automatique du PC sur les plages concernées.

Sous macOS/Linux, un service `systemd`, `launchd` ou une tâche de démarrage équivalente peut lancer `python -m facebook_bot run` avec le dossier du projet comme répertoire de travail.

## Comportement en cas de problème

- **Le dossier est vide à l’heure choisie :** le bot vérifie à nouveau toutes les 5 minutes jusqu’à la fin de la plage.
- **Coupure réseau / erreur Meta temporaire :** jusqu’à 3 tentatives espacées de 10 minutes, tant que la plage n’est pas terminée.
- **Jeton expiré ou permission refusée :** le créneau passe en échec et le message indique quoi corriger ; aucun essai en boucle.
- **Bot lancé après une plage :** cette plage est marquée comme manquée ; le bot ne publie pas en dehors de l’horaire prévu.
- **Arrêt pendant l’appel de publication :** après 15 minutes, le créneau passe à « à vérifier » et n’est pas retenté automatiquement, afin d’éviter un doublon éventuel.
- **Échec d’archivage après publication :** l’empreinte est déjà enregistrée, donc le fichier resté dans l’entrée ne sera pas republié.

Les réglages correspondants se trouvent dans `.env.example`.

## Sécurité et bonnes pratiques

- Utilisez uniquement l’API Graph officielle et respectez les règles de la Plateforme Meta et la fréquence attendue par les abonnés de la Page.
- Ne versionnez jamais `.env`, un jeton, un App Secret ou un export de la base locale.
- Révoquez immédiatement un jeton qui aurait été exposé.
- Donnez uniquement les permissions nécessaires.
- Avant un usage réel, testez avec une Page de test ou une publication de contrôle.

## Développement et tests

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

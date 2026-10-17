# Bot Python de publication d’images sur Facebook

Ce projet publie automatiquement **uniquement sur la Page Facebook « Madame Portugais »**. Il utilise l’API Graph officielle de Meta — aucune automatisation du navigateur — et vérifie le nom ainsi que l’identifiant de la Page avant tout envoi.

Le bot lit quatre documents texte modifiables : `horraire1.txt`, `horraire2.txt`, `horraire3.txt` et `hashtags.txt`. Après avoir demandé la date, il affiche les trois plannings et vous laisse choisir le planning 1, 2, 3, ou les trois avec une répartition égale des images.

Les fichiers fournis contiennent par défaut :

1. `horraire1.txt` : `07:30`, `08:30`, `09:30`… `23:30` ;
2. `horraire2.txt` : `07:15`, `08:15`, `09:15`… `23:15` ;
3. `horraire3.txt` : `07:45`, `08:45`, `09:45`… `23:45`.

Les heures et hashtags peuvent être modifiés directement dans ces fichiers sans toucher au code. Après confirmation, le bot **envoie immédiatement tout le planning futur à Facebook**. Facebook conserve alors les dates et heures et effectue les publications : le programme peut être fermé et le PC peut être éteint.

Le planning et les identifiants renvoyés par Facebook sont aussi enregistrés dans SQLite. Une publication déjà acceptée par Facebook n’est jamais envoyée une seconde fois.

> **Important :** l’API officielle permet ce fonctionnement pour une **Page Facebook**, pas pour un profil personnel. Au moment de la programmation, Meta impose actuellement une heure située au moins 10 minutes et au plus 75 jours dans le futur. Le bot utilise une marge de 15 minutes lors de la création du planning.

## Fonctionnement

- compte automatiquement les images de `images/to_post` ;
- analyse les trois documents d’horaires et propose le planning 1, 2, 3 ou les trois ;
- demande la date et affiche toutes les heures avant confirmation ;
- limite automatiquement le nombre d’images au nombre de créneaux disponibles ;
- choisit les images par ancienneté (modifiable) ;
- lit la légende dans un fichier `.txt` du même nom ;
- ajoute à chaque publication les mots-dièse présents dans `hashtags.txt` ;
- téléverse chaque photo en média temporaire non publié via `/{PAGE_ID}/photos` ;
- crée ensuite le post programmé via `/{PAGE_ID}/feed`, avec son heure future ;
- mémorise l’identifiant du post et l’empreinte SHA-256 pour empêcher les doublons ;
- déplace l’image acceptée dans `images/posted/AAAA-MM-JJ` ;
- arrête le lot si Facebook refuse un envoi, tout en conservant le reste à reprendre ;
- bloque toute répétition si la réponse de Facebook a été perdue et que le résultat est incertain ;
- conserve son planning et son historique dans `data/facebook_bot.sqlite3`.

Formats acceptés par la file locale : `.jpg`, `.jpeg`, `.png`, `.gif` et `.webp`. JPEG ou PNG sont conseillés.

## 1. Préparer Meta for Developers

Vous devez être administrateur de la Page **Madame Portugais**, disposer de la tâche de Page **CREATE_CONTENT** et avoir une application sur [Meta for Developers](https://developers.facebook.com/apps/).

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

> **Obligatoire :** faites d’abord un clic droit sur le ZIP puis **Extraire tout**. Ne lancez jamais un fichier `.bat` directement depuis l’aperçu du ZIP, car Windows ne trouverait pas les autres fichiers.

Après avoir extrait ou cloné ce projet, double-cliquez sur :

```text
CONFIGURER.bat
```

Le fichier installe le bot puis ouvre automatiquement **`token madame portugais.txt`** dans le Bloc-notes. Remplacez la première ligne par un nouveau jeton Meta, enregistrez et fermez le document. Le bot vérifie que le jeton appartient à Madame Portugais, le transfère dans le fichier local `.env`, puis efface le jeton du document texte pour éviter une fuite. Vous n’avez rien à coller dans la fenêtre noire.

Ensuite :

1. placez les images dans `images\to_post` ;
2. double-cliquez sur **`PLANIFIER.bat`**, saisissez la date et choisissez 1, 2, 3 ou 4 ;
3. vérifiez les heures et hashtags proposés, puis répondez `o` pour confirmer ;
4. attendez le message **« Facebook possède le planning complet »**.

C’est terminé : fermez la fenêtre et éteignez le PC si vous le souhaitez. Il n’est pas nécessaire de lancer un programme aux heures prévues. `LANCER_BOT.bat` sert désormais seulement à envoyer d’éventuels éléments restés en attente et à afficher leur état.

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

### Enregistrer le jeton avec le document texte

Le ZIP contient le document :

```text
token madame portugais.txt
```

`CONFIGURER.bat` l’ouvre automatiquement. Remplacez `COLLEZ_VOTRE_NOUVEAU_JETON_ICI` par un **nouveau** jeton, enregistrez et fermez le Bloc-notes. La commande exécutée automatiquement est :

```powershell
python -m facebook_bot setup --token-file "token madame portugais.txt"
```

Après vérification, le jeton est enregistré dans `.env` et retiré du document texte. Le bot le retrouvera ensuite automatiquement dans `.env` à chaque démarrage. Le mode presse-papiers reste disponible avec `setup --clipboard`, et macOS/Linux peuvent utiliser la saisie masquée avec `setup`.

Ne passez jamais le jeton comme argument d’une commande et ne l’envoyez jamais dans une discussion.

La configuration enregistrée sera :

```dotenv
FACEBOOK_EXPECTED_PAGE_NAME=Madame Portugais
FACEBOOK_PAGE_ID=1098568206676051
FACEBOOK_PAGE_ACCESS_TOKEN=valeur_masquée
FACEBOOK_API_VERSION=v26.0
```

Si l’ID appartient à une autre Page, la commande refuse le jeton et n’enregistre rien. Le fichier `.env` persiste sur l’ordinateur et est ignoré par Git, mais Meta peut toujours expirer ou révoquer un jeton : aucun jeton ne peut être garanti « pour toujours ». Il faudra relancer `setup` lors d’un renouvellement.

Aucun identifiant Facebook, mot de passe, App Secret ou jeton utilisateur n’est nécessaire dans le code.

## 3. Planifier une date

Déposez d’abord les images dans `images/to_post`, puis double-cliquez sur `PLANIFIER.bat`. Le bot demande :

```text
Date de publication (JJ/MM/AAAA) :
```

Le bot analyse les documents et propose :

```text
1. Utiliser horraire1.txt
2. Utiliser horraire2.txt
3. Utiliser horraire3.txt
4. Utiliser les trois et répartir les images également
```

Si vous choisissez `1`, toutes les images possibles utilisent uniquement les heures de `horraire1.txt`. Pour obtenir **entre 15 et 17 images dans chacun des trois plannings**, choisissez `4` et placez entre 45 et 51 images : 45 donne 15 par planning, 48 donne 16 par planning et 51 donne 17 par planning.

Le bot n’utilise jamais plus d’images que le nombre d’heures disponible dans le ou les documents sélectionnés. Les images restantes attendent une autre date. Après vérification, répondez `o` à la demande de confirmation. Une copie est créée dans `data/planning-AAAA-MM-JJ.csv`.

Si un planning de cette date existe déjà et que toutes ses publications sont encore à l’état « prévu », le bot propose de le remplacer. Il refuse tout autre état afin d’éviter les doublons.

Le bot vérifie alors une dernière fois la Page **Madame Portugais**, téléverse toutes les images retenues et crée tous les posts programmés chez Facebook. Attendez le bilan final avant de fermer la fenêtre. Après le message de succès, aucune tâche ne reste à exécuter sur le PC.

La première publication doit laisser une marge d’au moins 15 minutes et la dernière ne peut pas dépasser 75 jours. Vous pouvez modifier les heures, mais une même heure ne doit pas apparaître dans deux documents : le diagnostic bloquera la configuration pour empêcher deux publications au même moment.

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
```

Modifiez `hashtags.txt` pour choisir les hashtags ajoutés à toutes les publications. Le fichier fourni contient :

```text
#portugal #portugais #france #francais #cours #apprendre #quiz
```

Vous pouvez les remplacer librement. Écrivez-les avec ou sans `#` : le bot normalise automatiquement la liste et retire les doublons. Le texte UTF-8 du fichier `.txt` associé à une image devient la première partie de sa légende. Sans légende individuelle, `DEFAULT_CAPTION` est utilisé. Avec `QUEUE_ORDER=oldest`, l’image la plus ancienne part en premier.

## 5. Commandes de contrôle

Créer interactivement un planning **et l’envoyer immédiatement à Facebook** :

```bash
facebook-image-bot plan
```

Reprendre uniquement les publications qui sont encore en attente locale, sans renvoyer celles déjà acceptées :

```bash
facebook-image-bot send-schedule
```

Afficher les publications déjà planifiées sur les 7 prochains jours :

```bash
facebook-image-bot schedule --days 7
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

## 6. Programmer puis fermer le bot

Ordre recommandé sous Windows :

```text
1. CONFIGURER.bat
2. placer les images dans images\to_post
3. PLANIFIER.bat
4. attendre la confirmation complète de Facebook
5. fermer la fenêtre et, si souhaité, éteindre le PC
```

Il n’existe plus de processus à laisser en attente jusqu’aux heures choisies. `LANCER_BOT.bat` et `ENVOYER_PLANNING.bat` peuvent reprendre les éléments encore marqués « prévu » après une erreur certaine, puis afficher le résultat. Les posts déjà acceptés ne sont pas renvoyés.

En ligne de commande :

```bash
facebook-image-bot plan
facebook-image-bot schedule --days 31
```

Compter les images qui ne sont ni publiées ni déjà réservées dans un planning :

```bash
facebook-image-bot queue
```

Une publication immédiate reste possible, mais elle choisit uniquement une image non réservée :

```bash
facebook-image-bot post-now
```

Si la commande `facebook-image-bot` n’est pas reconnue, utilisez l’équivalent :

```bash
python -m facebook_bot plan
python -m facebook_bot send-schedule
```

## Comportement en cas de problème

- **Dossier vide au moment de planifier :** aucun planning n’est créé.
- **Image déplacée ou modifiée avant l’envoi :** le lot est arrêté avant de contacter Facebook afin de ne pas envoyer le mauvais fichier.
- **Date trop proche ou trop lointaine :** la création est refusée en respectant la fenêtre Meta de 10 minutes à 75 jours et la marge locale de 15 minutes.
- **Facebook refuse clairement une requête :** l’élément et les suivants restent « prévu ». Corrigez la cause puis utilisez `ENVOYER_PLANNING.bat` ; les éléments déjà acceptés ne repartent pas.
- **Réponse perdue après la demande de création du post :** l’élément passe à « à vérifier » et n’est jamais retenté automatiquement. Contrôlez Meta Business Suite avant toute action afin d’éviter un doublon.
- **Jeton expiré ou permission refusée :** le lot s’arrête et le message indique quoi corriger ; aucun essai en boucle.
- **Interruption brutale pendant un envoi :** l’état « envoi à Facebook » est conservé puis devient « à vérifier » après le délai de sécurité ; il n’est pas repris aveuglément.
- **Échec d’archivage après acceptation :** l’empreinte et l’identifiant Facebook sont déjà enregistrés, donc le fichier resté dans l’entrée ne sera pas republié.

## Sécurité et bonnes pratiques

- Utilisez uniquement l’API Graph officielle et respectez les règles de la Plateforme Meta et la fréquence attendue par les abonnés de la Page.
- La capacité de 51 publications est une limite technique du bot, pas une recommandation : une fréquence élevée peut être considérée comme indésirable par l’audience ou par Meta.
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

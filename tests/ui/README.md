# Test d'interface (headless)

Vérifie `app/static/` dans un DOM simulé (jsdom) : rendu des profils, feed,
réglages, formulaires, modale de diagnostic — sans lancer le serveur.

```bash
cd tests/ui
npm install       # une seule fois (jsdom)
npm test
```

Sortie attendue : une suite de lignes `✓ …` puis `✓ aucune erreur JS`.
Le script renvoie `0` si tout passe, `1` en cas d'assertion en échec.

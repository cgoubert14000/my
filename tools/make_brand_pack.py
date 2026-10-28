"""Fabrique le pack de marques embarqué dans le bot.

Usage
-----
    python tools/make_brand_pack.py marques-vinted.csv

Le fichier d'entrée peut venir de deux endroits :

* ``vinted-sniper.exe --export-brands marques-vinted`` (recommandé : c'est
  l'index réel déjà présent dans la base, 56 000+ entrées) ;
* n'importe quelle liste ``id,slug,name`` (ou un JSON équivalent).

Le script écrit ``app/data/brands.csv`` et ``app/data/brands.json`` : ce sont
les fichiers que le bot charge **tout seul** au premier démarrage, sans réseau.
Ils sont ajoutés à l'exécutable par ``tools/build_executable.py`` et au zip de
distribution par ``tools/make_release_zip.py``.

Il vérifie aussi la cohérence (doublons, identifiants non numériques, noms
manquants) et affiche un résumé : utile pour savoir en une ligne si le fichier
est exploitable avant de le livrer.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.brand_pack import read_brand_file, write_brand_files  # noqa: E402


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    source = Path(argv[0])
    if not source.is_file():
        print(f"[ERREUR] Fichier introuvable : {source}")
        return 1

    print(f"[1/3] Lecture de {source.name}…")
    rows = read_brand_file(source)
    if not rows:
        print("[ERREUR] Aucune marque valide : attendu des lignes « id,slug,name ».")
        return 1

    print("[2/3] Contrôles…")
    ids = [row["id"] for row in rows]
    duplicates = [brand_id for brand_id, count in Counter(ids).items() if count > 1]
    generic = [row for row in rows if row["name"].startswith("Marque ")]
    print(f"      {len(rows):,} marque(s), {len(set(ids)):,} identifiant(s) unique(s)")
    if duplicates:
        print(f"      ⚠ {len(duplicates)} identifiant(s) en double (le dernier gagne)")
    if generic:
        print(f"      ⚠ {len(generic)} nom(s) génériques (« Marque 123 ») : slug vide à la source")

    target = ROOT / "app" / "data" / "brands"
    print(f"[3/3] Écriture du pack dans {target.parent}…")
    report = write_brand_files(rows, target)
    print(
        f"[OK] {report['rows']:,} marques — "
        f"CSV {report['csv_bytes'] / 1024:.0f} Ko, JSON {report['json_bytes'] / 1024:.0f} Ko"
    )
    print(f"     {report['csv']}")
    print(f"     {report['json']}")
    print(
        "\nProchaine étape : reconstruire l'exécutable (workflow « Build executables »)\n"
        "ou simplement poser brands.csv à côté du binaire existant."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

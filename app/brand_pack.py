"""Export / import du catalogue complet des marques Vinted.

L'index des marques est construit à partir des sitemaps Vinted (≈57 000
entrées) puis stocké dans la table SQLite ``brands``. Ce module permet de le
**sortir dans un fichier portable** — CSV et JSON — pour le donner à un autre
projet (ou à un autre agent) qui doit embarquer la liste :

* ``marques-vinted.csv``  → ``id,slug,name`` (une ligne par marque) : lisible
  partout, y compris par un tableur ;
* ``marques-vinted.json`` → ``[{"id": "53", "slug": "nike", "name": "Nike"}]`` :
  directement consommable par du code.

Le bot relit ces fichiers tout seul :

1. au premier démarrage, si la table est vide, il cherche
   ``app/data/brands.csv`` (fichier **embarqué** dans l'exécutable) ;
2. sinon, un fichier posé **à côté de l'exécutable** (ou de la base) :
   ``brands.csv``, ``brands.json``, ``marques.csv`` ou ``marques-vinted.csv``.

Ainsi « ajouter les 57 000 marques au bot » = déposer le fichier au bon
endroit, sans code à écrire.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

#: Noms de fichiers reconnus, dans l'ordre de priorité.
SEED_FILENAMES = (
    "brands.csv",
    "brands.json",
    "marques.csv",
    "marques.json",
    "marques-vinted.csv",
    "marques-vinted.json",
)


def _resource_dir() -> Path:
    """Dossier des fichiers embarqués (PyInstaller : ``_MEIPASS``)."""
    bundled = getattr(sys, "_MEIPASS", None)
    if bundled:
        return Path(bundled) / "app" / "data"
    return Path(__file__).resolve().parent / "data"


def runtime_dirs(extra: list[str | Path] | None = None) -> list[Path]:
    """Dossiers où chercher un fichier de marques, du plus prioritaire au moins."""
    dirs: list[Path] = []
    for candidate in extra or []:
        if candidate:
            dirs.append(Path(candidate))
    if getattr(sys, "frozen", False):
        dirs.append(Path(sys.executable).resolve().parent)
    dirs.append(_resource_dir())
    dirs.append(Path.cwd())
    ordered: list[Path] = []
    for folder in dirs:
        try:
            resolved = folder.resolve()
        except OSError:  # pragma: no cover - chemin invalide
            continue
        if resolved not in ordered:
            ordered.append(resolved)
    return ordered


def find_brand_file(extra: list[str | Path] | None = None) -> Path | None:
    """Premier fichier de marques trouvé, ou ``None``."""
    for folder in runtime_dirs(extra):
        for name in SEED_FILENAMES:
            candidate = folder / name
            if candidate.is_file() and candidate.stat().st_size > 32:
                return candidate
    return None


def read_brand_file(path: str | Path) -> list[dict]:
    """Lit un CSV ou un JSON de marques et renvoie ``[{"id","slug","name"}]``.

    Tolérant par construction : un fichier produit par un autre outil peut
    avoir les colonnes dans un autre ordre, des guillemets, un BOM, des lignes
    vides ou un identifiant non numérique (ignoré).
    """
    file_path = Path(path)
    raw = file_path.read_text(encoding="utf-8-sig", errors="replace")
    if not raw.strip():
        return []
    if file_path.suffix.lower() == ".json" or raw.lstrip()[:1] in "[{":
        return _read_json(raw)

    rows: list[dict] = []
    reader = csv.reader(raw.splitlines())
    try:
        header = next(reader)
    except StopIteration:
        return []
    columns = [cell.strip().lower() for cell in header]
    has_header = "id" in columns
    if has_header:
        index = {name: columns.index(name) for name in ("id", "slug", "name") if name in columns}
    else:
        index = {"id": 0, "slug": 1, "name": 2}
        reader = csv.reader(raw.splitlines())  # la 1re ligne est une donnée
    for cells in reader:
        if not cells:
            continue
        brand_id = str(cells[index["id"]]).strip() if index.get("id", -1) < len(cells) else ""
        if not brand_id.isdigit():
            continue
        slug = ""
        if "slug" in index and index["slug"] < len(cells):
            slug = str(cells[index["slug"]]).strip().lower()
        name = ""
        if "name" in index and index["name"] < len(cells):
            name = str(cells[index["name"]]).strip()
        rows.append({"id": brand_id, "slug": slug, "name": name or slug or f"Marque {brand_id}"})
    return rows


def _read_json(raw: str) -> list[dict]:
    data = json.loads(raw)
    if isinstance(data, dict):
        data = data.get("brands") or data.get("items") or []
    rows: list[dict] = []
    for entry in data if isinstance(data, list) else []:
        if isinstance(entry, (list, tuple)) and len(entry) >= 1:
            brand_id, slug, name = (list(entry) + ["", ""])[:3]
            entry = {"id": brand_id, "slug": slug, "name": name}
        if not isinstance(entry, dict):
            continue
        brand_id = str(entry.get("id") or entry.get("brand_id") or "").strip()
        if not brand_id.isdigit():
            continue
        slug = str(entry.get("slug") or "").strip().lower()
        name = str(entry.get("name") or entry.get("title") or "").strip()
        rows.append({"id": brand_id, "slug": slug, "name": name or slug or f"Marque {brand_id}"})
    return rows


def export_rows(db) -> list[dict]:
    """Toutes les marques de la base, triées par nom."""
    stats = db.brand_stats()
    if not stats.get("total"):
        return []
    return db.list_brands()


def write_brand_files(rows: list[dict], destination: str | Path) -> dict:
    """Écrit le CSV et le JSON ; renvoie les chemins et les tailles."""
    target = Path(destination)
    if target.suffix.lower() in {".csv", ".json"}:
        target = target.with_suffix("")
    target.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(rows, key=lambda row: (row.get("name") or "").lower())
    csv_path = target.with_suffix(".csv")
    json_path = target.with_suffix(".json")

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["id", "slug", "name"])
        for row in ordered:
            writer.writerow([row["id"], row.get("slug", ""), row.get("name", "")])
    json_path.write_text(
        json.dumps(ordered, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    return {
        "rows": len(ordered),
        "csv": str(csv_path),
        "csv_bytes": csv_path.stat().st_size,
        "json": str(json_path),
        "json_bytes": json_path.stat().st_size,
    }


def seed_database(
    db,
    path: str | Path | None = None,
    extra_dirs: list[str | Path] | None = None,
) -> dict:
    """Importe un fichier de marques dans la base (idempotent).

    Sans ``path``, cherche un fichier connu (à côté de l'exécutable, embarqué,
    ou dans le dossier courant). Ne fait rien si la table contient déjà des
    marques : un index récupéré en ligne est plus frais qu'un fichier.
    """
    existing = db.brand_stats().get("total", 0)
    if existing:
        return {"imported": 0, "skipped": True, "total": existing, "source": ""}
    file_path = Path(path) if path else find_brand_file(extra_dirs)
    if not file_path or not file_path.is_file():
        return {"imported": 0, "skipped": True, "total": 0, "source": ""}
    rows = read_brand_file(file_path)
    imported = db.upsert_brands(rows) if rows else 0
    return {
        "imported": imported,
        "skipped": False,
        "total": db.brand_stats().get("total", 0),
        "source": str(file_path),
    }

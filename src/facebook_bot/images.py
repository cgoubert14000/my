from __future__ import annotations

import hashlib
import logging
import random
import shutil
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

LOGGER = logging.getLogger(__name__)
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


@dataclass(frozen=True)
class ImageItem:
    path: Path
    caption_path: Path | None
    caption: str
    fingerprint: str


class ImageQueue:
    def __init__(
        self,
        *,
        image_dir: Path,
        archive_dir: Path,
        queue_order: str,
        default_caption: str,
        fixed_hashtags: str = "",
    ) -> None:
        self.image_dir = image_dir
        self.archive_dir = archive_dir
        self.queue_order = queue_order
        self.default_caption = default_caption
        self.fixed_hashtags = " ".join(fixed_hashtags.split())

    def next_item(self, is_unavailable: Callable[[str], bool]) -> ImageItem | None:
        items = self.available_items(is_unavailable, limit=1)
        return items[0] if items else None

    def available_items(
        self,
        is_unavailable: Callable[[str], bool],
        *,
        limit: int | None = None,
    ) -> list[ImageItem]:
        items: list[ImageItem] = []
        seen_fingerprints: set[str] = set()
        for path in self._ordered_images():
            item = self._load_item(path)
            if item is None:
                continue
            if item.fingerprint in seen_fingerprints or is_unavailable(item.fingerprint):
                LOGGER.debug("Image déjà publiée, planifiée ou dupliquée : %s", path.name)
                continue
            seen_fingerprints.add(item.fingerprint)
            items.append(item)
            if limit is not None and len(items) >= limit:
                break
        return items

    def archive(self, item: ImageItem, posted_at: datetime) -> Path:
        destination_dir = self.archive_dir / posted_at.strftime("%Y-%m-%d")
        destination_dir.mkdir(parents=True, exist_ok=True)
        destination = _available_path(destination_dir / item.path.name)
        shutil.move(str(item.path), str(destination))

        if item.caption_path is not None and item.caption_path.exists():
            caption_destination = destination.with_suffix(".txt")
            if caption_destination.exists():
                caption_destination = _available_path(caption_destination)
            try:
                shutil.move(str(item.caption_path), str(caption_destination))
            except OSError as exc:
                # La photo est déjà enregistrée comme publiée : ne jamais la republier
                # uniquement parce que l'archivage de sa légende a échoué.
                LOGGER.warning("Impossible d'archiver la légende %s : %s", item.caption_path, exc)

        return destination

    def count_available(self, is_unavailable: Callable[[str], bool]) -> int:
        return len(self.available_items(is_unavailable))

    def _load_item(self, path: Path) -> ImageItem | None:
        try:
            if path.stat().st_size == 0:
                LOGGER.warning("Image vide ignorée : %s", path.name)
                return None
            fingerprint = file_sha256(path)
        except OSError as exc:
            LOGGER.warning("Impossible de lire %s : %s", path.name, exc)
            return None

        caption_path = path.with_suffix(".txt")
        if caption_path.is_file():
            try:
                base_caption = caption_path.read_text(encoding="utf-8").strip()
            except (OSError, UnicodeError) as exc:
                LOGGER.warning(
                    "Légende %s illisible (%s), légende par défaut utilisée.",
                    caption_path.name,
                    exc,
                )
                base_caption = self.default_caption.strip()
                caption_path = None
        else:
            base_caption = self.default_caption.strip()
            caption_path = None

        caption_parts = [base_caption] if base_caption else []
        if self.fixed_hashtags and self.fixed_hashtags not in base_caption:
            caption_parts.append(self.fixed_hashtags)
        return ImageItem(
            path=path,
            caption_path=caption_path,
            caption="\n\n".join(caption_parts),
            fingerprint=fingerprint,
        )

    def _ordered_images(self) -> list[Path]:
        try:
            paths = [
                path
                for path in self.image_dir.iterdir()
                if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
            ]
        except OSError as exc:
            LOGGER.error("Impossible de parcourir le dossier d'images : %s", exc)
            return []

        if self.queue_order == "alphabetical":
            return sorted(paths, key=lambda path: path.name.casefold())
        if self.queue_order == "random":
            random.SystemRandom().shuffle(paths)
            return paths
        return sorted(paths, key=_mtime_and_name)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _mtime_and_name(path: Path) -> tuple[float, str]:
    try:
        modified = path.stat().st_mtime
    except OSError:
        modified = float("inf")
    return modified, path.name.casefold()


def _available_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(f"{path.stem}_{index}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise OSError(f"Impossible de trouver un nom libre pour archiver {path.name}")

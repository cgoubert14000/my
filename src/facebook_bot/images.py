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
    ) -> None:
        self.image_dir = image_dir
        self.archive_dir = archive_dir
        self.queue_order = queue_order
        self.default_caption = default_caption

    def next_item(self, was_posted: Callable[[str], bool]) -> ImageItem | None:
        for path in self._ordered_images():
            try:
                if path.stat().st_size == 0:
                    LOGGER.warning("Image vide ignorée : %s", path.name)
                    continue
                fingerprint = file_sha256(path)
            except OSError as exc:
                LOGGER.warning("Impossible de lire %s : %s", path.name, exc)
                continue

            if was_posted(fingerprint):
                LOGGER.debug("Image déjà publiée, ignorée : %s", path.name)
                continue

            caption_path = path.with_suffix(".txt")
            if caption_path.is_file():
                try:
                    caption = caption_path.read_text(encoding="utf-8").strip()
                except (OSError, UnicodeError) as exc:
                    LOGGER.warning(
                        "Légende %s illisible (%s), légende par défaut utilisée.",
                        caption_path.name,
                        exc,
                    )
                    caption = self.default_caption
                    caption_path = None
            else:
                caption = self.default_caption
                caption_path = None

            return ImageItem(
                path=path,
                caption_path=caption_path,
                caption=caption,
                fingerprint=fingerprint,
            )
        return None

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
                # La photo est déjà enregistrée en base comme publiée : ne jamais la republier
                # uniquement parce que l'archivage de sa légende a échoué.
                LOGGER.warning("Impossible d'archiver la légende %s : %s", item.caption_path, exc)

        return destination

    def count_available(self, was_posted: Callable[[str], bool]) -> int:
        count = 0
        for path in self._ordered_images():
            try:
                if path.stat().st_size and not was_posted(file_sha256(path)):
                    count += 1
            except OSError:
                continue
        return count

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

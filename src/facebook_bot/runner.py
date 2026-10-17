from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

from facebook_bot.config import Config
from facebook_bot.facebook import (
    FacebookError,
    FacebookPublisher,
    FacebookSchedulingUncertain,
    PublishReceipt,
)
from facebook_bot.images import ImageItem, ImageQueue, file_sha256
from facebook_bot.state import ScheduledPost, StateError, StateStore
from facebook_bot.text_settings import load_hashtags

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class AdvanceScheduleResult:
    scheduled: int
    pending: int
    uncertain: int

    @property
    def succeeded(self) -> bool:
        return self.pending == 0 and self.uncertain == 0


class BotRunner:
    def __init__(self, config: Config, *, dry_run: bool = False) -> None:
        self.config = config
        self.dry_run = dry_run
        self.state = StateStore(config.state_db)
        hashtags = load_hashtags(Path.cwd(), fallback=config.fixed_hashtags)
        self.queue = ImageQueue(
            image_dir=config.image_dir,
            archive_dir=config.archive_dir,
            queue_order=config.queue_order,
            default_caption=config.default_caption,
            fixed_hashtags=hashtags,
        )
        self.publisher = FacebookPublisher(
            page_id=config.page_id,
            access_token=config.page_access_token,
            api_version=config.api_version,
            timeout_seconds=config.http_timeout_seconds,
        )

    def run_forever(self) -> None:
        """Ancien point d'entrée : programme désormais le lot chez Facebook puis quitte."""
        LOGGER.warning(
            "Le mode d'attente local est désactivé ; le planning est envoyé à Facebook."
        )
        result = self.schedule_pending_on_facebook()
        if not result.succeeded:
            raise StateError(
                "Le planning complet n'est pas confirmé par Facebook ; consultez les états."
            )

    def post_now(self) -> PublishReceipt | None:
        self.config.prepare_directories()
        self.state.initialize()
        item = self.queue.next_item(self.state.is_unavailable)
        if item is None:
            LOGGER.warning("Aucune image non planifiée dans %s", self.config.image_dir)
            return None

        if self.dry_run:
            self._log_simulation(item, prefix="Publication immédiate")
            return PublishReceipt(photo_id="simulation", post_id=None)

        page = self.publisher.verify_destination(self.config.expected_page_name)
        LOGGER.info("Destination vérifiée : %s (ID %s).", page.name, page.id)
        LOGGER.info("Publication immédiate de %s…", item.path.name)
        receipt = self.publisher.publish_photo(item.path, item.caption)
        posted_at = datetime.now(self.config.timezone)
        self.state.record_manual_success(item, receipt, posted_at)
        self._archive_after_success(item, posted_at)
        LOGGER.info("Photo publiée avec succès (ID Facebook : %s).", receipt.photo_id)
        return receipt

    def schedule_pending_on_facebook(
        self,
        *,
        day: date | None = None,
    ) -> AdvanceScheduleResult:
        """Envoie maintenant les publications futures afin que Facebook les exécute."""
        self.config.prepare_directories()
        self.state.initialize()
        stale_count = self.state.recover_stale_running()
        if stale_count:
            LOGGER.warning(
                "%d envoi(s) interrompu(s) ont été marqués « à vérifier » pour éviter "
                "un doublon.",
                stale_count,
            )
        publications = self.state.pending_publications(day)
        if not publications:
            counts = self.state.publication_status_counts(day)
            return AdvanceScheduleResult(
                scheduled=0,
                pending=0,
                uncertain=counts.get("uncertain", 0) + counts.get("scheduling", 0),
            )

        now = datetime.now(self.config.timezone)
        earliest = now + timedelta(minutes=10)
        latest = now + timedelta(days=75)
        too_soon = [post for post in publications if post.scheduled_at < earliest]
        too_late = [post for post in publications if post.scheduled_at > latest]
        if too_soon:
            first = too_soon[0]
            raise StateError(
                f"{first.item.path.name} est prévu à {first.scheduled_at:%d/%m/%Y %H:%M}. "
                "Facebook exige au moins 10 minutes d'avance."
            )
        if too_late:
            first = too_late[0]
            raise StateError(
                f"{first.item.path.name} est prévu à {first.scheduled_at:%d/%m/%Y %H:%M}. "
                "Facebook n'accepte pas une programmation à plus de 75 jours."
            )

        for publication in publications:
            item = publication.item
            if not item.path.is_file():
                raise StateError(f"Image planifiée introuvable : {item.path}")
            try:
                current_fingerprint = file_sha256(item.path)
            except OSError as exc:
                raise StateError(
                    f"Impossible de lire l'image planifiée {item.path.name} : {exc}"
                ) from exc
            if current_fingerprint != item.fingerprint:
                raise StateError(
                    f"{item.path.name} a été modifiée après la création du planning."
                )

        page = self.publisher.verify_destination(self.config.expected_page_name)
        LOGGER.info("Destination vérifiée : %s (ID %s).", page.name, page.id)
        scheduled_count = 0
        for publication in publications:
            if not self.state.claim_for_facebook_scheduling(publication):
                LOGGER.warning(
                    "%s n'est plus en attente ; elle n'est pas renvoyée.",
                    publication.item.path.name,
                )
                continue

            LOGGER.info(
                "Programmation de %s pour le %s à %s…",
                publication.item.path.name,
                publication.scheduled_at.strftime("%d/%m/%Y"),
                publication.scheduled_at.strftime("%H:%M"),
            )
            try:
                receipt = self.publisher.schedule_photo(
                    publication.item.path,
                    publication.item.caption,
                    publication.scheduled_at,
                )
            except FacebookSchedulingUncertain as exc:
                self.state.release_facebook_scheduling(
                    publication,
                    status="uncertain",
                    error=str(exc),
                    photo_id=exc.photo_id,
                )
                LOGGER.error("ARRÊT DE SÉCURITÉ pour %s : %s", publication.item.path.name, exc)
                break
            except FacebookError as exc:
                self.state.release_facebook_scheduling(
                    publication,
                    status="pending",
                    error=str(exc),
                )
                LOGGER.error(
                    "Facebook a refusé %s ; les envois suivants restent en attente : %s",
                    publication.item.path.name,
                    exc,
                )
                break

            # Le succès est mémorisé avant l'archivage : si le déplacement local échoue,
            # cette image ne sera jamais renvoyée à Facebook.
            self.state.record_facebook_scheduled(publication, receipt)
            self._archive_after_success(publication.item, publication.scheduled_at)
            scheduled_count += 1
            LOGGER.info(
                "✓ %s programmée sur Facebook (post %s).",
                publication.item.path.name,
                receipt.post_id,
            )

        counts = self.state.publication_status_counts(day)
        return AdvanceScheduleResult(
            scheduled=scheduled_count,
            pending=counts.get("pending", 0),
            uncertain=counts.get("uncertain", 0) + counts.get("scheduling", 0),
        )

    def _process_publication(self, publication: ScheduledPost, now: datetime) -> None:
        item = publication.item
        if self.state.was_posted(item.fingerprint):
            self.state.finish_publication(
                publication,
                "skipped",
                "Image déjà publiée",
            )
            LOGGER.warning("%s est déjà publiée ; créneau ignoré.", item.path.name)
            return

        if not item.path.is_file():
            self.state.finish_publication(publication, "failed", "Fichier image introuvable")
            LOGGER.error("Image planifiée introuvable : %s", item.path)
            return
        try:
            current_fingerprint = file_sha256(item.path)
        except OSError as exc:
            self.state.finish_publication(publication, "failed", str(exc))
            LOGGER.error("Impossible de lire l'image planifiée %s : %s", item.path.name, exc)
            return
        if current_fingerprint != item.fingerprint:
            error = "Le fichier a été modifié après la création du planning"
            self.state.finish_publication(publication, "failed", error)
            LOGGER.error("%s : %s.", item.path.name, error)
            return

        if self.dry_run:
            self._log_simulation(item, prefix=f"Publication {publication.id}")
            self.state.finish_publication(publication, "simulated")
            return

        attempts = self.state.mark_scheduled_attempt(publication)
        LOGGER.info(
            "Publication de %s (horaire %d, tentative %d/%d)…",
            item.path.name,
            publication.window_index,
            attempts,
            self.config.max_post_attempts,
        )
        try:
            receipt = self.publisher.publish_photo(item.path, item.caption)
        except FacebookError as exc:
            self._handle_publish_error(publication, now, attempts, exc)
            return

        posted_at = datetime.now(self.config.timezone)
        # Enregistrer le succès avant l'archivage empêche une seconde publication si le
        # déplacement local échoue après que Facebook a accepté la photo.
        self.state.record_scheduled_success(publication, receipt, posted_at)
        self._archive_after_success(item, posted_at)
        LOGGER.info(
            "%s publiée avec succès (ID Facebook : %s).",
            item.path.name,
            receipt.photo_id,
        )

    def _handle_publish_error(
        self,
        publication: ScheduledPost,
        now: datetime,
        attempts: int,
        error: FacebookError,
    ) -> None:
        retry_at = now + timedelta(minutes=self.config.retry_interval_minutes)
        may_retry = (
            error.retryable
            and attempts < self.config.max_post_attempts
            and retry_at < publication.window_end
        )
        if may_retry:
            self.state.reschedule_publication(publication, retry_at, str(error))
            LOGGER.warning(
                "Échec temporaire de %s : %s Nouvel essai à %s.",
                publication.item.path.name,
                error,
                retry_at.strftime("%H:%M:%S"),
            )
        else:
            self.state.finish_publication(publication, "failed", str(error))
            LOGGER.error("Échec définitif de %s : %s", publication.item.path.name, error)

    def _archive_after_success(self, item: ImageItem, posted_at: datetime) -> None:
        try:
            archived_path = self.queue.archive(item, posted_at)
        except OSError as exc:
            LOGGER.warning(
                "La photo est acceptée par Facebook mais son archivage a échoué : %s",
                exc,
            )
            return
        self.state.update_archive_path(item.fingerprint, archived_path)
        LOGGER.info("Image archivée dans %s", archived_path)

    @staticmethod
    def _log_simulation(item: ImageItem, *, prefix: str) -> None:
        caption_preview = item.caption.replace("\n", " ")
        if len(caption_preview) > 80:
            caption_preview = f"{caption_preview[:77]}…"
        LOGGER.info(
            "%s [SIMULATION] : publierait %s%s",
            prefix,
            item.path.name,
            f' — légende « {caption_preview} »' if caption_preview else " — sans légende",
        )

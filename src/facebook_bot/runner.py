from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta

from facebook_bot.config import Config
from facebook_bot.facebook import FacebookError, FacebookPublisher, PublishReceipt
from facebook_bot.images import ImageItem, ImageQueue, file_sha256
from facebook_bot.state import ScheduledPost, StateStore

LOGGER = logging.getLogger(__name__)


class BotRunner:
    def __init__(self, config: Config, *, dry_run: bool = False) -> None:
        self.config = config
        self.dry_run = dry_run
        self.state = StateStore(config.state_db)
        self.queue = ImageQueue(
            image_dir=config.image_dir,
            archive_dir=config.archive_dir,
            queue_order=config.queue_order,
            default_caption=config.default_caption,
            fixed_hashtags=config.fixed_hashtags,
        )
        self.publisher = FacebookPublisher(
            page_id=config.page_id,
            access_token=config.page_access_token,
            api_version=config.api_version,
            timeout_seconds=config.http_timeout_seconds,
        )

    def run_forever(self) -> None:
        self.config.prepare_directories()
        self.state.initialize()
        if not self.dry_run:
            page = self.publisher.verify_destination(self.config.expected_page_name)
            LOGGER.info("Destination vérifiée : %s (ID %s).", page.name, page.id)
        stale_count = self.state.recover_stale_running()
        if stale_count:
            LOGGER.warning(
                "%d publication(s) interrompue(s) ont été marquées « uncertain » pour éviter "
                "des doublons.",
                stale_count,
            )

        LOGGER.info(
            "Bot démarré — Page %s, fuseau %s%s",
            self.config.page_id or "(simulation)",
            self.config.timezone_name,
            " [SIMULATION]" if self.dry_run else "",
        )
        LOGGER.info("Le bot attend les publications créées avec PLANIFIER.bat.")

        try:
            while True:
                now = datetime.now(self.config.timezone)
                expired_count = self.state.expire_scheduled(
                    now,
                    max_late=timedelta(minutes=self.config.max_late_minutes),
                )
                if expired_count:
                    LOGGER.warning(
                        "%d publication(s) trop en retard ont été marquées comme manquées.",
                        expired_count,
                    )

                publication = self.state.claim_due_publication(now)
                if publication is not None:
                    self._process_publication(publication, now)
                    continue
                time.sleep(self.config.poll_interval_seconds)
        except KeyboardInterrupt:
            LOGGER.info("Arrêt demandé. Le planning sera repris au prochain lancement.")

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
            LOGGER.warning("La photo est publiée mais son archivage local a échoué : %s", exc)
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

from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta

from facebook_bot.config import Config
from facebook_bot.facebook import FacebookError, FacebookPublisher, PublishReceipt
from facebook_bot.images import ImageItem, ImageQueue
from facebook_bot.state import Slot, StateStore

LOGGER = logging.getLogger(__name__)


class BotRunner:
    def __init__(self, config: Config, *, dry_run: bool = False) -> None:
        self.config = config
        self.dry_run = dry_run
        state_path = config.state_db
        if dry_run:
            state_path = state_path.with_name(f"{state_path.stem}.dry-run{state_path.suffix}")
        self.state = StateStore(state_path)
        self.queue = ImageQueue(
            image_dir=config.image_dir,
            archive_dir=config.archive_dir,
            queue_order=config.queue_order,
            default_caption=config.default_caption,
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
            "Bot démarré — Page %s, fuseau %s, plages %s%s",
            self.config.page_id or "(simulation)",
            self.config.timezone_name,
            ", ".join(str(window) for window in self.config.posting_windows),
            " [SIMULATION]" if self.dry_run else "",
        )
        LOGGER.info("Dossier surveillé : %s", self.config.image_dir)

        try:
            while True:
                now = datetime.now(self.config.timezone)
                self.state.ensure_day(
                    now.date(),
                    self.config.posting_windows,
                    self.config.timezone,
                    now=now,
                )
                expired_count = self.state.expire_pending(now)
                if expired_count:
                    LOGGER.warning("%d créneau(x) dépassé(s) sans publication.", expired_count)

                slot = self.state.claim_due_slot(now)
                if slot is not None:
                    self._process_slot(slot, now)
                    continue
                time.sleep(self.config.poll_interval_seconds)
        except KeyboardInterrupt:
            LOGGER.info("Arrêt demandé. Le planning enregistré sera repris au prochain lancement.")

    def post_now(self) -> PublishReceipt | None:
        self.config.prepare_directories()
        self.state.initialize()
        item = self.queue.next_item(self.state.was_posted)
        if item is None:
            LOGGER.warning("Aucune nouvelle image dans %s", self.config.image_dir)
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

    def _process_slot(self, slot: Slot, now: datetime) -> None:
        item = self.queue.next_item(self.state.was_posted)
        if item is None:
            retry_at = now + timedelta(minutes=self.config.empty_queue_recheck_minutes)
            if retry_at < slot.window_end:
                self.state.reschedule(slot, retry_at, "File d'images vide")
                LOGGER.warning(
                    "Créneau %d : aucune nouvelle image ; nouvel essai à %s.",
                    slot.index,
                    retry_at.strftime("%H:%M:%S"),
                )
            else:
                self.state.finish_slot(slot, "empty", "Aucune image disponible")
                LOGGER.warning("Créneau %d terminé : aucune image disponible.", slot.index)
            return

        if self.dry_run:
            self._log_simulation(item, prefix=f"Créneau {slot.index}")
            self.state.finish_slot(slot, "simulated")
            return

        attempts = self.state.mark_post_attempt(slot)
        LOGGER.info(
            "Créneau %d : publication de %s (tentative %d/%d)…",
            slot.index,
            item.path.name,
            attempts,
            self.config.max_post_attempts,
        )
        try:
            receipt = self.publisher.publish_photo(item.path, item.caption)
        except FacebookError as exc:
            self._handle_publish_error(slot, now, attempts, exc)
            return

        posted_at = datetime.now(self.config.timezone)
        # Enregistrer le succès avant de déplacer le fichier empêche une seconde publication si
        # l'archivage local échoue après que Facebook a accepté la photo.
        self.state.record_slot_success(slot, item, receipt, posted_at)
        self._archive_after_success(item, posted_at)
        LOGGER.info(
            "Créneau %d terminé : %s publiée (ID Facebook : %s).",
            slot.index,
            item.path.name,
            receipt.photo_id,
        )

    def _handle_publish_error(
        self, slot: Slot, now: datetime, attempts: int, error: FacebookError
    ) -> None:
        retry_at = now + timedelta(minutes=self.config.retry_interval_minutes)
        may_retry = (
            error.retryable
            and attempts < self.config.max_post_attempts
            and retry_at < slot.window_end
        )
        if may_retry:
            self.state.reschedule(slot, retry_at, str(error))
            LOGGER.warning(
                "Échec temporaire du créneau %d : %s Nouvel essai à %s.",
                slot.index,
                error,
                retry_at.strftime("%H:%M:%S"),
            )
        else:
            self.state.finish_slot(slot, "failed", str(error))
            LOGGER.error("Échec définitif du créneau %d : %s", slot.index, error)

    def _archive_after_success(self, item: ImageItem, posted_at: datetime) -> None:
        try:
            archived_path = self.queue.archive(item, posted_at)
        except OSError as exc:
            LOGGER.warning(
                "La photo est publiée mais son archivage local a échoué : %s", exc
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

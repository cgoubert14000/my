from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import requests


class FacebookError(RuntimeError):
    """Erreur sûre à afficher, sans exposer le jeton d'accès."""

    def __init__(
        self,
        message: str,
        *,
        retryable: bool = False,
        code: int | None = None,
        subcode: int | None = None,
    ) -> None:
        super().__init__(message)
        self.retryable = retryable
        self.code = code
        self.subcode = subcode


class FacebookSchedulingUncertain(FacebookError):
    """Facebook a peut-être accepté le post ; une répétition risquerait un doublon."""

    def __init__(self, message: str, *, photo_id: str) -> None:
        super().__init__(message)
        self.photo_id = photo_id


@dataclass(frozen=True)
class PageInfo:
    id: str
    name: str


@dataclass(frozen=True)
class PublishReceipt:
    photo_id: str
    post_id: str | None


class FacebookPublisher:
    """Petit client pour l'API Graph officielle de Meta."""

    _TRANSIENT_CODES = {1, 2, 4, 17, 32, 341, 613}

    def __init__(
        self,
        *,
        page_id: str,
        access_token: str,
        api_version: str,
        timeout_seconds: int = 120,
        session: requests.Session | None = None,
    ) -> None:
        self.page_id = page_id
        self.api_version = api_version
        self.timeout_seconds = timeout_seconds
        self.session = session or requests.Session()
        # Le jeton reste dans un en-tête et n'apparaît jamais dans l'URL ou les logs.
        self.session.headers.update({"Authorization": f"Bearer {access_token}"})

    @property
    def base_url(self) -> str:
        return f"https://graph.facebook.com/{self.api_version}"

    def get_page_info(self) -> PageInfo:
        response = self._request(
            "GET",
            f"{self.base_url}/{self.page_id}",
            params={"fields": "id,name"},
            timeout=(10, self.timeout_seconds),
        )
        payload = self._json(response)
        return PageInfo(id=str(payload.get("id", "")), name=str(payload.get("name", "")))

    def verify_destination(self, expected_page_name: str) -> PageInfo:
        """Refuse tout envoi si l'ID ne désigne pas la Page attendue."""
        page = self.get_page_info()
        if page.id != self.page_id:
            raise FacebookError(
                f"La Page retournée ({page.id}) ne correspond pas à l'ID configuré. "
                "Aucune publication n'a été effectuée."
            )
        if expected_page_name and _normalized_name(page.name) != _normalized_name(
            expected_page_name
        ):
            raise FacebookError(
                f"Sécurité : l'ID configuré correspond à « {page.name} », pas à "
                f"« {expected_page_name} ». Aucune publication n'a été effectuée."
            )
        return page

    def publish_photo(self, image_path: Path, caption: str) -> PublishReceipt:
        try:
            with image_path.open("rb") as image_file:
                response = self._request(
                    "POST",
                    f"{self.base_url}/{self.page_id}/photos",
                    data={"caption": caption, "published": "true"},
                    files={"source": (image_path.name, image_file)},
                    timeout=(10, self.timeout_seconds),
                )
        except OSError as exc:
            raise FacebookError(f"Impossible de lire l'image {image_path.name} : {exc}") from exc

        payload = self._json(response)
        photo_id = str(payload.get("id", ""))
        if not photo_id:
            raise FacebookError("Facebook n'a pas renvoyé l'identifiant de la photo.")
        post_id = payload.get("post_id")
        return PublishReceipt(photo_id=photo_id, post_id=str(post_id) if post_id else None)

    def schedule_photo(
        self,
        image_path: Path,
        caption: str,
        scheduled_at: datetime,
    ) -> PublishReceipt:
        """Téléverse une photo temporaire puis crée un Page Post programmé."""
        try:
            with image_path.open("rb") as image_file:
                upload_response = self._request(
                    "POST",
                    f"{self.base_url}/{self.page_id}/photos",
                    data={"published": "false", "temporary": "true"},
                    files={"source": (image_path.name, image_file)},
                    timeout=(10, self.timeout_seconds),
                )
        except OSError as exc:
            raise FacebookError(f"Impossible de lire l'image {image_path.name} : {exc}") from exc

        upload_payload = self._json(upload_response)
        photo_id = str(upload_payload.get("id", ""))
        if not photo_id:
            raise FacebookError("Facebook n'a pas renvoyé l'identifiant de la photo temporaire.")

        try:
            feed_response = self._request(
                "POST",
                f"{self.base_url}/{self.page_id}/feed",
                data={
                    "message": caption,
                    "attached_media": json.dumps([{"media_fbid": photo_id}]),
                    "published": "false",
                    "scheduled_publish_time": str(int(scheduled_at.timestamp())),
                    "unpublished_content_type": "SCHEDULED",
                },
                timeout=(10, self.timeout_seconds),
            )
        except FacebookError as exc:
            if not exc.retryable:
                raise
            raise FacebookSchedulingUncertain(
                "Réponse perdue après l'envoi du post programmé. Vérifiez-le dans "
                "Meta Business Suite avant toute nouvelle tentative.",
                photo_id=photo_id,
            ) from exc

        try:
            feed_payload = self._json(feed_response)
        except FacebookError as exc:
            raise FacebookSchedulingUncertain(
                "Réponse illisible après l'envoi du post programmé. Vérifiez-le dans "
                "Meta Business Suite avant toute nouvelle tentative.",
                photo_id=photo_id,
            ) from exc

        post_id = str(feed_payload.get("id", ""))
        if not post_id:
            raise FacebookSchedulingUncertain(
                "Facebook a répondu sans identifiant de post. Vérifiez la programmation "
                "dans Meta Business Suite avant toute nouvelle tentative.",
                photo_id=photo_id,
            )
        return PublishReceipt(photo_id=photo_id, post_id=post_id)

    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        try:
            response = self.session.request(method, url, **kwargs)
        except (requests.Timeout, requests.ConnectionError) as exc:
            raise FacebookError(
                "Connexion à Facebook impossible ou délai dépassé.", retryable=True
            ) from exc
        except requests.RequestException as exc:
            raise FacebookError(f"Erreur HTTP pendant l'appel à Facebook : {exc}") from exc

        if response.ok:
            return response

        try:
            payload = response.json()
        except ValueError:
            payload = {}
        error = payload.get("error", {}) if isinstance(payload, dict) else {}
        code = _optional_int(error.get("code")) if isinstance(error, dict) else None
        subcode = _optional_int(error.get("error_subcode")) if isinstance(error, dict) else None
        graph_message = error.get("message") if isinstance(error, dict) else None
        retryable = response.status_code >= 500 or code in self._TRANSIENT_CODES

        if code == 190:
            message = (
                "Jeton Facebook invalide ou expiré (code 190). "
                "Créez un nouveau jeton d'accès de Page."
            )
        elif code == 200:
            message = (
                "Permission Facebook refusée (code 200). Vérifiez pages_manage_posts, "
                "pages_read_engagement et que ce jeton appartient bien à la Page."
            )
            if graph_message:
                message = f"{message} Détail Meta : {graph_message}"
        elif graph_message:
            message = f"Facebook a refusé la requête : {graph_message}"
        else:
            message = f"Facebook a répondu avec le statut HTTP {response.status_code}."

        suffix = []
        if code is not None:
            suffix.append(f"code={code}")
        if subcode is not None:
            suffix.append(f"sous-code={subcode}")
        if suffix and f"code {code}" not in message:
            message = f"{message} ({', '.join(suffix)})"

        raise FacebookError(message, retryable=retryable, code=code, subcode=subcode)

    @staticmethod
    def _json(response: requests.Response) -> dict[str, Any]:
        try:
            payload = response.json()
        except ValueError as exc:
            raise FacebookError("Réponse JSON invalide reçue de Facebook.") from exc
        if not isinstance(payload, dict):
            raise FacebookError("Format de réponse Facebook inattendu.")
        return payload


def _optional_int(value: Any) -> int | None:
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def _normalized_name(value: str) -> str:
    return " ".join(value.split()).casefold()

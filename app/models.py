"""Modèles Pydantic échangés avec le dashboard."""

from __future__ import annotations

import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from .utils import clean_terms, is_vinted_host

WEBHOOK_RE = re.compile(
    r"^https://(?:ptb\.|canary\.)?discord(?:app)?\.com/api/webhooks/\d+/[\w-]+(?:[?#].*)?$"
)


class ProfileBase(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    active: bool = True
    url: str = ""
    min_price: float | None = Field(default=None, ge=0, le=1_000_000)
    max_price: float | None = Field(default=None, ge=0, le=1_000_000)
    whitelist: list[str] = Field(default_factory=list)
    blacklist: list[str] = Field(default_factory=list)
    keyword_mode: Literal["any", "all"] = "any"
    check_description: bool = True
    webhook: str = ""
    interval_seconds: int = Field(default=60, ge=15, le=3600)
    min_seller_rating: float | None = Field(default=None, ge=0, le=5)
    min_seller_feedback: int | None = Field(default=None, ge=0, le=1_000_000)
    pages: int = Field(default=1, ge=1, le=5)
    notes: str = Field(default="", max_length=600)

    model_config = ConfigDict(str_strip_whitespace=True)

    @field_validator("name")
    @classmethod
    def _name(cls, value: str) -> str:
        value = (value or "").strip()
        if not value:
            raise ValueError("Le nom du profil est obligatoire.")
        return value

    @field_validator("url")
    @classmethod
    def _url(cls, value: str) -> str:
        value = (value or "").strip()
        if not value:
            return ""
        if value.startswith(("http://", "https://")):
            host = value.split("/")[2] if len(value.split("/")) > 2 else ""
            if not is_vinted_host(host):
                raise ValueError(
                    "URL Vinted invalide : utilisez un domaine vinted.fr / vinted.de / vinted.com…"
                )
            return value
        # Domaine sans schéma : « www.vinted.fr/catalog?search_text=nike »
        if re.match(r"^[\w.-]*vinted\.[a-z.]{2,}(/.*)?$", value, re.I):
            return "https://" + value
        # Sinon : simple mot-clé (recherche sur le domaine Vinted par défaut).
        return value

    @field_validator("whitelist", "blacklist", mode="before")
    @classmethod
    def _terms(cls, value):
        return clean_terms(value)

    @field_validator("webhook")
    @classmethod
    def _webhook(cls, value: str) -> str:
        value = (value or "").strip()
        if value and not WEBHOOK_RE.match(value):
            raise ValueError(
                "Webhook Discord invalide (https://discord.com/api/webhooks/<id>/<token>)."
            )
        return value

    @model_validator(mode="after")
    def _coherence(self) -> "ProfileBase":
        if self.min_price is not None and self.max_price is not None:
            if self.min_price > self.max_price:
                raise ValueError("Le prix minimum doit être inférieur au prix maximum.")
        return self


class ProfileIn(ProfileBase):
    pass


class ProfileOut(ProfileBase):
    id: int
    domain: str
    webhook_masked: str = ""
    created_at: str | None = None
    updated_at: str | None = None
    last_run_at: str | None = None
    last_error: str | None = None
    scan_count: int = 0
    found_count: int = 0
    last_found_at: str | None = None
    running: bool = False
    next_run_at: str | None = None
    effective_webhook: bool = False


class ToggleIn(BaseModel):
    active: bool


class ConfigPatch(BaseModel):
    patch: dict = Field(default_factory=dict)


class WebhookTestIn(BaseModel):
    webhook: str = Field(default="")
    profile_name: str = Field(default="Test")

    @field_validator("webhook")
    @classmethod
    def _check(cls, value: str) -> str:
        value = (value or "").strip()
        if not value:
            return ""
        if not WEBHOOK_RE.match(value):
            raise ValueError("Webhook Discord invalide.")
        return value

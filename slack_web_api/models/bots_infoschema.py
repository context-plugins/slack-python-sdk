from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bot import Bot, BotDict


class BotsInfoschema(SdkBaseModel):
    """Schema for successful response from bots.info method"""

    bot: Bot
    ok: bool


class BotsInfoschemaDict(TypedDict):
    bot: BotDict
    ok: bool

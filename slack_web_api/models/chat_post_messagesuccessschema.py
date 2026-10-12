from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .messageobject import Messageobject, MessageobjectDict


class ChatPostMessagesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.postMessage method"""

    channel: str
    message: Messageobject
    ok: bool
    ts: str


class ChatPostMessagesuccessschemaDict(TypedDict):
    channel: str
    message: MessageobjectDict
    ok: bool
    ts: str

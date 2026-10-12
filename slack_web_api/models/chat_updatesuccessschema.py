from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .messageobject1 import Messageobject1, Messageobject1Dict


class ChatUpdatesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.update method"""

    channel: str
    message: Messageobject1
    ok: bool
    text: str
    ts: str


class ChatUpdatesuccessschemaDict(TypedDict):
    channel: str
    message: Messageobject1Dict
    ok: bool
    text: str
    ts: str

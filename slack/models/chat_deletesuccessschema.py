from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChatDeletesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.delete method"""

    channel: str
    ok: bool
    ts: str


class ChatDeletesuccessschemaDict(TypedDict):
    channel: str
    ok: bool
    ts: str

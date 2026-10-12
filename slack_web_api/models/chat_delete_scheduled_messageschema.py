from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChatDeleteScheduledMessageschema(SdkBaseModel):
    """Schema for successful response from chat.deleteScheduledMessage method"""

    ok: bool


class ChatDeleteScheduledMessageschemaDict(TypedDict):
    ok: bool

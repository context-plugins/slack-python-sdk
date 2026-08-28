from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChatPostEphemeralsuccessschema(SdkBaseModel):
    """Schema for successful response from chat.postEphemeral method"""

    message_ts: str
    ok: bool


class ChatPostEphemeralsuccessschemaDict(TypedDict):
    message_ts: str
    ok: bool

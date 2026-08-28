from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsKicksuccessschema(SdkBaseModel):
    """Schema for successful response conversations.kick method"""

    ok: bool


class ConversationsKicksuccessschemaDict(TypedDict):
    ok: bool

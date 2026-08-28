from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminConversationsUnarchiveschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.unarchive"""

    ok: bool


class AdminConversationsUnarchiveschemaDict(TypedDict):
    ok: bool

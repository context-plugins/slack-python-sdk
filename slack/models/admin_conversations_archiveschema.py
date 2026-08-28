from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminConversationsArchiveschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.archive"""

    ok: bool


class AdminConversationsArchiveschemaDict(TypedDict):
    ok: bool

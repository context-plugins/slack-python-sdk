from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminConversationsConvertToPrivateschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.convertToPrivate"""

    ok: bool


class AdminConversationsConvertToPrivateschemaDict(TypedDict):
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminConversationsInviteschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.invite"""

    ok: bool


class AdminConversationsInviteschemaDict(TypedDict):
    ok: bool

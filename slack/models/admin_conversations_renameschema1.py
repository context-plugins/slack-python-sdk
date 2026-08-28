from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminConversationsRenameschema1(SdkBaseModel):
    """Schema for successful response of admin.conversations.rename"""

    ok: bool


class AdminConversationsRenameschema1Dict(TypedDict):
    ok: bool

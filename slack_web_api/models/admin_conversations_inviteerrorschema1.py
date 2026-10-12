from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_invite_error_enum import AdminConversationsInviteErrorEnumOrStr


class AdminConversationsInviteerrorschema1(SdkBaseModel):
    """Schema for error response from admin.conversations.invite"""

    error: AdminConversationsInviteErrorEnumOrStr
    ok: bool


class AdminConversationsInviteerrorschema1Dict(TypedDict):
    error: AdminConversationsInviteErrorEnumOrStr
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_disconnect_shared_error_enum import AdminConversationsDisconnectSharedErrorEnumOrStr


class AdminConversationsDisconnectSharederrorschema1(SdkBaseModel):
    """Schema for error response from admin.conversations.disconnectShared"""

    error: AdminConversationsDisconnectSharedErrorEnumOrStr
    ok: bool


class AdminConversationsDisconnectSharederrorschema1Dict(TypedDict):
    error: AdminConversationsDisconnectSharedErrorEnumOrStr
    ok: bool

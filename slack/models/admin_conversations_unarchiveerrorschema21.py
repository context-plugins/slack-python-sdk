from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_rename_error_enum import AdminConversationsRenameErrorEnumOrStr


class AdminConversationsUnarchiveerrorschema21(SdkBaseModel):
    """Schema for error response from admin.conversations.rename"""

    error: AdminConversationsRenameErrorEnumOrStr
    ok: bool


class AdminConversationsUnarchiveerrorschema21Dict(TypedDict):
    error: AdminConversationsRenameErrorEnumOrStr
    ok: bool

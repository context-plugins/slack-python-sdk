from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_rename_error_enum import AdminConversationsRenameErrorEnumOrStr


class AdminConversationsUnarchiveerrorschema21Error(SdkBaseModel):
    """Schema for error response from admin.conversations.rename"""

    error: AdminConversationsRenameErrorEnumOrStr
    ok: bool


class AdminConversationsUnarchiveerrorschema21ErrorDict(TypedDict):
    error: AdminConversationsRenameErrorEnumOrStr
    ok: bool

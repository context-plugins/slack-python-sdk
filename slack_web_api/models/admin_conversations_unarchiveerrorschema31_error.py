from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_unarchive_error_enum import AdminConversationsUnarchiveErrorEnumOrStr


class AdminConversationsUnarchiveerrorschema31Error(SdkBaseModel):
    """Schema for error response from admin.conversations.unarchive"""

    error: AdminConversationsUnarchiveErrorEnumOrStr
    ok: bool


class AdminConversationsUnarchiveerrorschema31ErrorDict(TypedDict):
    error: AdminConversationsUnarchiveErrorEnumOrStr
    ok: bool

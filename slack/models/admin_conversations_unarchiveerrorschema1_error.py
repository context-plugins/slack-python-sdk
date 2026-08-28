from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_get_conversation_prefs_error_enum import (
    AdminConversationsGetConversationPrefsErrorEnumOrStr,
)


class AdminConversationsUnarchiveerrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.getConversationPrefs"""

    error: AdminConversationsGetConversationPrefsErrorEnumOrStr
    ok: bool


class AdminConversationsUnarchiveerrorschema1ErrorDict(TypedDict):
    error: AdminConversationsGetConversationPrefsErrorEnumOrStr
    ok: bool

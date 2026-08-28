from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_search_error_enum import AdminConversationsSearchErrorEnumOrStr


class AdminConversationsSearcherrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.search"""

    error: AdminConversationsSearchErrorEnumOrStr
    ok: bool


class AdminConversationsSearcherrorschema1ErrorDict(TypedDict):
    error: AdminConversationsSearchErrorEnumOrStr
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_create_error_enum import AdminConversationsCreateErrorEnumOrStr


class AdminConversationsCreateerrorschema1(SdkBaseModel):
    """Schema for error response from admin.conversations.create"""

    error: AdminConversationsCreateErrorEnumOrStr
    ok: bool


class AdminConversationsCreateerrorschema1Dict(TypedDict):
    error: AdminConversationsCreateErrorEnumOrStr
    ok: bool

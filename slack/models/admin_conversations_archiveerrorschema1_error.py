from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_archive_error_enum import AdminConversationsArchiveErrorEnumOrStr


class AdminConversationsArchiveerrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.archive"""

    error: AdminConversationsArchiveErrorEnumOrStr
    ok: bool


class AdminConversationsArchiveerrorschema1ErrorDict(TypedDict):
    error: AdminConversationsArchiveErrorEnumOrStr
    ok: bool

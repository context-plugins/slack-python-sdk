from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_convert_to_private_error_enum import AdminConversationsConvertToPrivateErrorEnumOrStr


class AdminConversationsConvertToPrivateerrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.convertToPrivate"""

    error: AdminConversationsConvertToPrivateErrorEnumOrStr
    ok: bool


class AdminConversationsConvertToPrivateerrorschema1ErrorDict(TypedDict):
    error: AdminConversationsConvertToPrivateErrorEnumOrStr
    ok: bool

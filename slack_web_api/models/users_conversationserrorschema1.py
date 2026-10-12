from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_conversations_error_enum import UsersConversationsErrorEnumOrStr


class UsersConversationserrorschema1(SdkBaseModel):
    """Schema for error response from users.conversations method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsersConversationsErrorEnumOrStr
    ok: bool


class UsersConversationserrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: UsersConversationsErrorEnumOrStr
    ok: bool

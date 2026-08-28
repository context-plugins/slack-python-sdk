from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_history_error_enum import ConversationsHistoryErrorEnumOrStr


class ConversationsHistoryerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.history method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsHistoryErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: bool
    provided: Optional[str] = UNSET


class ConversationsHistoryerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsHistoryErrorEnumOrStr
    needed: NotRequired[str]
    ok: bool
    provided: NotRequired[str]

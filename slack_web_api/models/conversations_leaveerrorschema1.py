from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_leave_error_enum import ConversationsLeaveErrorEnumOrStr


class ConversationsLeaveerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.leave method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsLeaveErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: bool
    provided: Optional[str] = UNSET


class ConversationsLeaveerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsLeaveErrorEnumOrStr
    needed: NotRequired[str]
    ok: bool
    provided: NotRequired[str]

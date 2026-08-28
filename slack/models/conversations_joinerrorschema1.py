from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_join_error_enum import ConversationsJoinErrorEnumOrStr


class ConversationsJoinerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.join method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsJoinErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: bool
    provided: Optional[str] = UNSET


class ConversationsJoinerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsJoinErrorEnumOrStr
    needed: NotRequired[str]
    ok: bool
    provided: NotRequired[str]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_create_error_enum import ConversationsCreateErrorEnumOrStr


class ConversationsCreateerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.create method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    detail: Optional[str] = UNSET
    error: ConversationsCreateErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: bool
    provided: Optional[str] = UNSET


class ConversationsCreateerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    detail: NotRequired[str]
    error: ConversationsCreateErrorEnumOrStr
    needed: NotRequired[str]
    ok: bool
    provided: NotRequired[str]

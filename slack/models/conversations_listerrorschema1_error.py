from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_list_error_enum import ConversationsListErrorEnumOrStr


class ConversationsListerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsListErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: bool
    provided: Optional[str] = UNSET


class ConversationsListerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsListErrorEnumOrStr
    needed: NotRequired[str]
    ok: bool
    provided: NotRequired[str]

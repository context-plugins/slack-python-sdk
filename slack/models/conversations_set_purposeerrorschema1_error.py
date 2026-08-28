from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_set_purpose_error_enum import ConversationsSetPurposeErrorEnumOrStr


class ConversationsSetPurposeerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.setPurpose method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsSetPurposeErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: bool
    provided: Optional[str] = UNSET


class ConversationsSetPurposeerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsSetPurposeErrorEnumOrStr
    needed: NotRequired[str]
    ok: bool
    provided: NotRequired[str]

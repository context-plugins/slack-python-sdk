from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_set_purpose_error_enum import ConversationsSetPurposeErrorEnumOrStr


class ConversationsSetTopicerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.setTopic method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsSetPurposeErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: bool
    provided: Optional[str] = UNSET


class ConversationsSetTopicerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsSetPurposeErrorEnumOrStr
    needed: NotRequired[str]
    ok: bool
    provided: NotRequired[str]

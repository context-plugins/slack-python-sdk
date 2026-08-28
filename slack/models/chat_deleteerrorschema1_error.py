from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_delete_error_enum import ChatDeleteErrorEnumOrStr


class ChatDeleteerrorschema1Error(SdkBaseModel):
    """Schema for error response from chat.delete method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatDeleteErrorEnumOrStr
    ok: bool


class ChatDeleteerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ChatDeleteErrorEnumOrStr
    ok: bool

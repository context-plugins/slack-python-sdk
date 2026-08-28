from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_schedule_message_error_enum import ChatScheduleMessageErrorEnumOrStr


class ChatScheduleMessageerrorschema1(SdkBaseModel):
    """Schema for error response chat.scheduleMessage method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatScheduleMessageErrorEnumOrStr
    ok: bool


class ChatScheduleMessageerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ChatScheduleMessageErrorEnumOrStr
    ok: bool

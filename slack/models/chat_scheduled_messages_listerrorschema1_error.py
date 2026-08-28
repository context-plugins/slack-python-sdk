from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_scheduled_messages_list_error_enum import ChatScheduledMessagesListErrorEnumOrStr


class ChatScheduledMessagesListerrorschema1Error(SdkBaseModel):
    """Schema for error response from chat.scheduledMessages.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatScheduledMessagesListErrorEnumOrStr
    ok: bool


class ChatScheduledMessagesListerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ChatScheduledMessagesListErrorEnumOrStr
    ok: bool

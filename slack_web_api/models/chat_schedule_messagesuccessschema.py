from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .message import Message, MessageDict


class ChatScheduleMessagesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.scheduleMessage method"""

    channel: str
    message: Message
    ok: bool
    post_at: int
    scheduled_message_id: str


class ChatScheduleMessagesuccessschemaDict(TypedDict):
    channel: str
    message: MessageDict
    ok: bool
    post_at: int
    scheduled_message_id: str

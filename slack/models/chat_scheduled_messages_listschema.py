from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_metadata import ResponseMetadata, ResponseMetadataDict
from .scheduled_message import ScheduledMessage, ScheduledMessageDict


class ChatScheduledMessagesListschema(SdkBaseModel):
    """Schema for successful response from chat.scheduledMessages.list method"""

    ok: bool
    response_metadata: ResponseMetadata
    scheduled_messages: list[ScheduledMessage]


class ChatScheduledMessagesListschemaDict(TypedDict):
    ok: bool
    response_metadata: ResponseMetadata | ResponseMetadataDict
    scheduled_messages: list[ScheduledMessage | ScheduledMessageDict]

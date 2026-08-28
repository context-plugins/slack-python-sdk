from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .messageobject import Messageobject, MessageobjectDict


class ConversationsHistorysuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.history method"""

    channel_actions_count: int
    channel_actions_ts: Any
    has_more: bool
    messages: list[Messageobject]
    ok: bool
    pin_count: int


class ConversationsHistorysuccessschemaDict(TypedDict):
    channel_actions_count: int
    channel_actions_ts: Any
    has_more: bool
    messages: list[Messageobject | MessageobjectDict]
    ok: bool
    pin_count: int

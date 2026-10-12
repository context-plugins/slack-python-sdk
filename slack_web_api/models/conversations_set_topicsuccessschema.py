from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsSetTopicsuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.setTopic method"""

    channel: Any
    ok: bool


class ConversationsSetTopicsuccessschemaDict(TypedDict):
    channel: Any
    ok: bool

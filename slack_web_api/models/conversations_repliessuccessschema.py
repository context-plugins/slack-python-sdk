from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsRepliessuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.replies method"""

    has_more: Optional[bool] = UNSET
    messages: list[Any]
    ok: bool


class ConversationsRepliessuccessschemaDict(TypedDict):
    has_more: NotRequired[bool]
    messages: list[Any]
    ok: bool

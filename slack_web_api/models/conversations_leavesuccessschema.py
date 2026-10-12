from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsLeavesuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.leave method"""

    not_in_channel: Optional[bool] = UNSET
    ok: bool


class ConversationsLeavesuccessschemaDict(TypedDict):
    not_in_channel: NotRequired[bool]
    ok: bool

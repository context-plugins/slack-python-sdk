from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsInviteerrorschema(SdkBaseModel):
    """Schema for successful response from conversations.invite method"""

    channel: Any
    ok: bool


class ConversationsInviteerrorschemaDict(TypedDict):
    channel: Any
    ok: bool

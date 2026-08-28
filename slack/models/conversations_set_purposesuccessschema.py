from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsSetPurposesuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.setPurpose method"""

    channel: Any
    ok: bool


class ConversationsSetPurposesuccessschemaDict(TypedDict):
    channel: Any
    ok: bool

from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsInfosuccessschema(SdkBaseModel):
    """Schema for successful response conversations.info"""

    channel: Any
    ok: bool


class ConversationsInfosuccessschemaDict(TypedDict):
    channel: Any
    ok: bool

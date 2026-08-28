from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsCreatesuccessschema(SdkBaseModel):
    """Schema for successful response conversations.create method"""

    channel: Any
    ok: bool


class ConversationsCreatesuccessschemaDict(TypedDict):
    channel: Any
    ok: bool

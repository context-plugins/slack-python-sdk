from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminConversationsDeleteschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.delete"""

    ok: bool


class AdminConversationsDeleteschemaDict(TypedDict):
    ok: bool

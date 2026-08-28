from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsMarksuccessschema(SdkBaseModel):
    """Schema for successful response conversations.mark method"""

    ok: bool


class ConversationsMarksuccessschemaDict(TypedDict):
    ok: bool

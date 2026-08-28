from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsArchivesuccessschema(SdkBaseModel):
    """Schema for successful response conversations.archive method"""

    ok: bool


class ConversationsArchivesuccessschemaDict(TypedDict):
    ok: bool

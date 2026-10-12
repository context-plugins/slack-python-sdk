from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsUnarchivesuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.unarchive method"""

    ok: bool


class ConversationsUnarchivesuccessschemaDict(TypedDict):
    ok: bool

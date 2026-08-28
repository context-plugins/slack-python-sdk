from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConversationsRenamesuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.rename method"""

    channel: Any
    ok: bool


class ConversationsRenamesuccessschemaDict(TypedDict):
    channel: Any
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChatGetPermalinksuccessschema(SdkBaseModel):
    """Schema for successful response chat.getPermalink"""

    channel: str
    ok: bool
    permalink: str


class ChatGetPermalinksuccessschemaDict(TypedDict):
    channel: str
    ok: bool
    permalink: str

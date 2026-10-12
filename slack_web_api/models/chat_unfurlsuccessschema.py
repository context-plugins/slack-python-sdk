from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChatUnfurlsuccessschema(SdkBaseModel):
    """Schema for successful response from chat.unfurl method"""

    ok: bool


class ChatUnfurlsuccessschemaDict(TypedDict):
    ok: bool

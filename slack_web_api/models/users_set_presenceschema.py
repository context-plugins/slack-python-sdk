from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersSetPresenceschema(SdkBaseModel):
    """Schema for successful response from users.setPresence method"""

    ok: bool


class UsersSetPresenceschemaDict(TypedDict):
    ok: bool

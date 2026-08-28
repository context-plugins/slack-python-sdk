from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersSetActiveschema(SdkBaseModel):
    """Schema for successful response from users.setActive method"""

    ok: bool


class UsersSetActiveschemaDict(TypedDict):
    ok: bool

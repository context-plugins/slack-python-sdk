from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersCountserrorschema1Error(SdkBaseModel):
    """Schema for error response users.getPresence method"""

    error: str
    ok: bool


class UsersCountserrorschema1ErrorDict(TypedDict):
    error: str
    ok: bool

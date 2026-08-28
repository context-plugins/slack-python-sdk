from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_set_presence_error_enum import UsersSetPresenceErrorEnumOrStr


class UsersSetPresenceerrorschema1Error(SdkBaseModel):
    """Schema for error response from users.setPresence method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsersSetPresenceErrorEnumOrStr
    ok: bool


class UsersSetPresenceerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsersSetPresenceErrorEnumOrStr
    ok: bool

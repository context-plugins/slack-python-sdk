from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_set_active_error_enum import UsersSetActiveErrorEnumOrStr


class UsersSetActiveerrorschema1Error(SdkBaseModel):
    """Schema for error response from users.setActive method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsersSetActiveErrorEnumOrStr
    ok: bool


class UsersSetActiveerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsersSetActiveErrorEnumOrStr
    ok: bool

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.usergroups_update_error_enum import UsergroupsUpdateErrorEnumOrStr


class UsergroupsUsersUpdateerrorschema1(SdkBaseModel):
    """Schema for error response from usergroups.users.update method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsergroupsUpdateErrorEnumOrStr
    ok: bool


class UsergroupsUsersUpdateerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: UsergroupsUpdateErrorEnumOrStr
    ok: bool

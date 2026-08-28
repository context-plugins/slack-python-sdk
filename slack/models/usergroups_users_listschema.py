from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsergroupsUsersListschema(SdkBaseModel):
    """Schema for successful response from usergroups.users.list method"""

    ok: bool
    users: list[str]


class UsergroupsUsersListschemaDict(TypedDict):
    ok: bool
    users: list[str]

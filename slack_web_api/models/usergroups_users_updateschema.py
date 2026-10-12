from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsUsersUpdateschema(SdkBaseModel):
    """Schema for successful response from usergroups.users.update method"""

    ok: bool
    usergroup: SubteamUsergroupObject


class UsergroupsUsersUpdateschemaDict(TypedDict):
    ok: bool
    usergroup: SubteamUsergroupObjectDict

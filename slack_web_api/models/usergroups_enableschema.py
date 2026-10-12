from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsEnableschema(SdkBaseModel):
    """Schema for successful response from usergroups.enable method"""

    ok: bool
    usergroup: SubteamUsergroupObject


class UsergroupsEnableschemaDict(TypedDict):
    ok: bool
    usergroup: SubteamUsergroupObjectDict

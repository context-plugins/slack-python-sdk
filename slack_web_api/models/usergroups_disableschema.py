from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsDisableschema(SdkBaseModel):
    """Schema for successful response from usergroups.disable method"""

    ok: bool
    usergroup: SubteamUsergroupObject


class UsergroupsDisableschemaDict(TypedDict):
    ok: bool
    usergroup: SubteamUsergroupObjectDict

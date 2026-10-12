from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsCreateschema(SdkBaseModel):
    """Schema for successful response from usergroups.create method"""

    ok: bool
    usergroup: SubteamUsergroupObject


class UsergroupsCreateschemaDict(TypedDict):
    ok: bool
    usergroup: SubteamUsergroupObjectDict

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsUpdateschema(SdkBaseModel):
    """Schema for successful response from usergroups.update method"""

    ok: bool
    usergroup: SubteamUsergroupObject


class UsergroupsUpdateschemaDict(TypedDict):
    ok: bool
    usergroup: SubteamUsergroupObjectDict

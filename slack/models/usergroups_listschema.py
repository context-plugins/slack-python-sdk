from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsListschema(SdkBaseModel):
    """Schema for successful response from usergroups.list method"""

    ok: bool
    usergroups: list[SubteamUsergroupObject]


class UsergroupsListschemaDict(TypedDict):
    ok: bool
    usergroups: list[SubteamUsergroupObject | SubteamUsergroupObjectDict]

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .login import Login, LoginDict
from .pagingobject import Pagingobject, PagingobjectDict


class TeamAccessLogsschema(SdkBaseModel):
    """Schema for successful response from team.accessLogs method"""

    logins: list[Login]
    ok: bool
    paging: Pagingobject


class TeamAccessLogsschemaDict(TypedDict):
    logins: list[Login | LoginDict]
    ok: bool
    paging: Pagingobject | PagingobjectDict

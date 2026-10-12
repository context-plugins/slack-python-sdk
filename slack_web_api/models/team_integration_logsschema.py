from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .log import Log, LogDict
from .pagingobject import Pagingobject, PagingobjectDict


class TeamIntegrationLogsschema(SdkBaseModel):
    """Schema for successful response from team.integrationLogs method"""

    logs: list[Log]
    ok: bool
    paging: Pagingobject


class TeamIntegrationLogsschemaDict(TypedDict):
    logs: list[LogDict]
    ok: bool
    paging: PagingobjectDict

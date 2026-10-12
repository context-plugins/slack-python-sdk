from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .team_object import TeamObject, TeamObjectDict


class TeamInfoschema(SdkBaseModel):
    """Schema for successful response from team.info method"""

    ok: bool
    team: TeamObject


class TeamInfoschemaDict(TypedDict):
    ok: bool
    team: TeamObjectDict

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.team_profile_get_error_enum import TeamProfileGetErrorEnumOrStr


class TeamProfileGeterrorschema1Error(SdkBaseModel):
    """Schema for error response from team.profile.get method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: TeamProfileGetErrorEnumOrStr
    ok: bool


class TeamProfileGeterrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: TeamProfileGetErrorEnumOrStr
    ok: bool

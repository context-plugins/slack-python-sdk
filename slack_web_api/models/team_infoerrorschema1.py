from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.rtm_connect_error_enum import RtmConnectErrorEnumOrStr


class TeamInfoerrorschema1(SdkBaseModel):
    """Schema for error response from team.info method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: RtmConnectErrorEnumOrStr
    ok: bool


class TeamInfoerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: RtmConnectErrorEnumOrStr
    ok: bool

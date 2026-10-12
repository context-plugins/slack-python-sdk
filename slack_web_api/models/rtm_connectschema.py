from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .self_model import SelfModel, SelfModelDict
from .team1 import Team1, Team1Dict


class RtmConnectschema(SdkBaseModel):
    """Schema for successful response from rtm.connect method"""

    ok: bool
    self: SelfModel
    team: Team1
    url: str


class RtmConnectschemaDict(TypedDict):
    ok: bool
    self: SelfModelDict
    team: Team1Dict
    url: str

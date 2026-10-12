from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .profile import Profile, ProfileDict


class TeamProfileGetsuccessschema(SdkBaseModel):
    """Schema for successful response from team.profile.get method"""

    ok: bool
    profile: Profile


class TeamProfileGetsuccessschemaDict(TypedDict):
    ok: bool
    profile: ProfileDict

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .profile1 import Profile1, Profile1Dict


class UsersSetPhotoschema(SdkBaseModel):
    """Schema for successful response from users.setPhoto method"""

    ok: bool
    profile: Profile1


class UsersSetPhotoschemaDict(TypedDict):
    ok: bool
    profile: Profile1 | Profile1Dict

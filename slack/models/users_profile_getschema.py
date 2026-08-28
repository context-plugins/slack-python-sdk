from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .userprofileobject import Userprofileobject, UserprofileobjectDict


class UsersProfileGetschema(SdkBaseModel):
    """Schema for successful response from users.profile.get method"""

    ok: bool
    profile: Userprofileobject


class UsersProfileGetschemaDict(TypedDict):
    ok: bool
    profile: Userprofileobject | UserprofileobjectDict

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .userprofileobject import Userprofileobject, UserprofileobjectDict


class UsersProfileSetschema(SdkBaseModel):
    """Schema for successful response from users.profile.set method"""

    email_pending: Optional[str] = UNSET
    ok: bool
    profile: Userprofileobject
    username: str


class UsersProfileSetschemaDict(TypedDict):
    email_pending: NotRequired[str]
    ok: bool
    profile: Userprofileobject | UserprofileobjectDict
    username: str

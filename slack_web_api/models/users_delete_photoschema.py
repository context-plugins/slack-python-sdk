from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersDeletePhotoschema(SdkBaseModel):
    """Schema for successful response from users.deletePhoto method"""

    ok: bool


class UsersDeletePhotoschemaDict(TypedDict):
    ok: bool

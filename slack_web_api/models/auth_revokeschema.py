from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuthRevokeschema(SdkBaseModel):
    """Schema for successful response from auth.revoke method"""

    ok: bool
    revoked: bool


class AuthRevokeschemaDict(TypedDict):
    ok: bool
    revoked: bool

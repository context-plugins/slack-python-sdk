from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersLookupByEmailsuccessschema(SdkBaseModel):
    """Schema for successful response from users.lookupByEmail method"""

    ok: bool
    user: Any


class UsersLookupByEmailsuccessschemaDict(TypedDict):
    ok: bool
    user: Any

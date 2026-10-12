from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersInfosuccessschema(SdkBaseModel):
    """Schema for successful response from users.info method"""

    ok: bool
    user: Any


class UsersInfosuccessschemaDict(TypedDict):
    ok: bool
    user: Any

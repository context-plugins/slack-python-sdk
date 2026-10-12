from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.stars_add_error_enum import StarsAddErrorEnumOrStr


class StarsAdderrorschema1(SdkBaseModel):
    """Schema for error response from stars.add method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: StarsAddErrorEnumOrStr
    ok: bool


class StarsAdderrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: StarsAddErrorEnumOrStr
    ok: bool

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.stars_remove_error_enum import StarsRemoveErrorEnumOrStr


class StarsRemoveerrorschema1(SdkBaseModel):
    """Schema for error response from stars.remove method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: StarsRemoveErrorEnumOrStr
    ok: bool


class StarsRemoveerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: StarsRemoveErrorEnumOrStr
    ok: bool

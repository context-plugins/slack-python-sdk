from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reactions_remove_error_enum import ReactionsRemoveErrorEnumOrStr


class ReactionsRemoveerrorschema1Error(SdkBaseModel):
    """Schema for error response from reactions.remove method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ReactionsRemoveErrorEnumOrStr
    ok: bool


class ReactionsRemoveerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ReactionsRemoveErrorEnumOrStr
    ok: bool

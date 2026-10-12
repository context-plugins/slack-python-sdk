from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pins_list_error_enum import PinsListErrorEnumOrStr


class PinsListerrorschema1Error(SdkBaseModel):
    """Schema for error response from pins.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: PinsListErrorEnumOrStr
    ok: bool


class PinsListerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: PinsListErrorEnumOrStr
    ok: bool

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dnd_set_snooze_error_enum import DndSetSnoozeErrorEnumOrStr


class DndSetSnoozeerrorschema1Error(SdkBaseModel):
    """Schema for error response from dnd.setSnooze method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: DndSetSnoozeErrorEnumOrStr
    ok: bool


class DndSetSnoozeerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: DndSetSnoozeErrorEnumOrStr
    ok: bool

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dnd_end_snooze_error_enum import DndEndSnoozeErrorEnumOrStr


class DndEndSnoozeerrorschema1Error(SdkBaseModel):
    """Schema for error response from dnd.endSnooze method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: DndEndSnoozeErrorEnumOrStr
    ok: bool


class DndEndSnoozeerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: DndEndSnoozeErrorEnumOrStr
    ok: bool

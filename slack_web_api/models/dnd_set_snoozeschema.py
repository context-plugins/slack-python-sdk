from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DndSetSnoozeschema(SdkBaseModel):
    """Schema for successful response from dnd.setSnooze method"""

    ok: bool
    snooze_enabled: bool
    snooze_endtime: int
    snooze_remaining: int


class DndSetSnoozeschemaDict(TypedDict):
    ok: bool
    snooze_enabled: bool
    snooze_endtime: int
    snooze_remaining: int

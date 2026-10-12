from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DndEndSnoozeschema(SdkBaseModel):
    """Schema for successful response from dnd.endSnooze method"""

    dnd_enabled: bool
    next_dnd_end_ts: int
    next_dnd_start_ts: int
    ok: bool
    snooze_enabled: bool


class DndEndSnoozeschemaDict(TypedDict):
    dnd_enabled: bool
    next_dnd_end_ts: int
    next_dnd_start_ts: int
    ok: bool
    snooze_enabled: bool

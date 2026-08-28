from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemindersCompleteschema(SdkBaseModel):
    """Schema for successful response from reminders.complete method"""

    ok: bool


class RemindersCompleteschemaDict(TypedDict):
    ok: bool

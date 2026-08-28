from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemindersDeleteschema(SdkBaseModel):
    """Schema for successful response from reminders.delete method"""

    ok: bool


class RemindersDeleteschemaDict(TypedDict):
    ok: bool

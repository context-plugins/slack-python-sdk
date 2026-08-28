from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .objs_reminder import ObjsReminder, ObjsReminderDict


class RemindersInfoschema(SdkBaseModel):
    """Schema for successful response from reminders.info method"""

    ok: bool
    reminder: ObjsReminder


class RemindersInfoschemaDict(TypedDict):
    ok: bool
    reminder: ObjsReminder | ObjsReminderDict

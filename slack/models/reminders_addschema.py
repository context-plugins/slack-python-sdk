from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .objs_reminder import ObjsReminder, ObjsReminderDict


class RemindersAddschema(SdkBaseModel):
    """Schema for successful response from reminders.add method"""

    ok: bool
    reminder: ObjsReminder


class RemindersAddschemaDict(TypedDict):
    ok: bool
    reminder: ObjsReminder | ObjsReminderDict

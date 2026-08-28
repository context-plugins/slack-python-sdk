from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .objs_reminder import ObjsReminder, ObjsReminderDict


class RemindersListschema(SdkBaseModel):
    """Schema for successful response from reminders.list method"""

    ok: bool
    reminders: list[ObjsReminder]


class RemindersListschemaDict(TypedDict):
    ok: bool
    reminders: list[ObjsReminder | ObjsReminderDict]

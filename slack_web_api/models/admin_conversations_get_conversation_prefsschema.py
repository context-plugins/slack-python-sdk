from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prefs1 import Prefs1, Prefs1Dict


class AdminConversationsGetConversationPrefsschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.getConversationPrefs"""

    ok: bool
    prefs: Optional[Prefs1] = UNSET


class AdminConversationsGetConversationPrefsschemaDict(TypedDict):
    ok: bool
    prefs: NotRequired[Prefs1Dict]

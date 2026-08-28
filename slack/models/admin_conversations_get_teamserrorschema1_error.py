from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_get_teams_error_enum import AdminConversationsGetTeamsErrorEnumOrStr


class AdminConversationsGetTeamserrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.getTeams"""

    error: AdminConversationsGetTeamsErrorEnumOrStr
    ok: bool


class AdminConversationsGetTeamserrorschema1ErrorDict(TypedDict):
    error: AdminConversationsGetTeamsErrorEnumOrStr
    ok: bool

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response_metadata import ResponseMetadata, ResponseMetadataDict


class AdminConversationsGetTeamsschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.getTeams"""

    ok: bool
    response_metadata: Optional[ResponseMetadata] = UNSET
    team_ids: list[str]


class AdminConversationsGetTeamsschemaDict(TypedDict):
    ok: bool
    response_metadata: NotRequired[ResponseMetadataDict]
    team_ids: list[str]

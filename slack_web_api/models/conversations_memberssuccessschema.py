from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_metadata import ResponseMetadata, ResponseMetadataDict


class ConversationsMemberssuccessschema(SdkBaseModel):
    """Schema for successful response conversations.members method"""

    members: list[str]
    ok: bool
    response_metadata: ResponseMetadata


class ConversationsMemberssuccessschemaDict(TypedDict):
    members: list[str]
    ok: bool
    response_metadata: ResponseMetadataDict

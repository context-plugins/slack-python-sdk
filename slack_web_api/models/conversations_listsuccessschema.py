from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response_metadata import ResponseMetadata, ResponseMetadataDict


class ConversationsListsuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.list method"""

    channels: list[Any]
    ok: bool
    response_metadata: Optional[ResponseMetadata] = UNSET


class ConversationsListsuccessschemaDict(TypedDict):
    channels: list[Any]
    ok: bool
    response_metadata: NotRequired[ResponseMetadataDict]

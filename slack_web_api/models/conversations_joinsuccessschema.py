from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .responsemetadata3 import Responsemetadata3, Responsemetadata3Dict


class ConversationsJoinsuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.join method"""

    channel: Any
    ok: bool
    response_metadata: Optional[Responsemetadata3] = UNSET
    warning: Optional[str] = UNSET


class ConversationsJoinsuccessschemaDict(TypedDict):
    channel: Any
    ok: bool
    response_metadata: NotRequired[Responsemetadata3Dict]
    warning: NotRequired[str]

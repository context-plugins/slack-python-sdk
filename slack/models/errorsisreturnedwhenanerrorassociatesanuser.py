from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_invite_error_enum import ConversationsInviteErrorEnumOrStr


class Errorsisreturnedwhenanerrorassociatesanuser(SdkBaseModel):
    error: ConversationsInviteErrorEnumOrStr
    ok: bool
    user: Optional[str] = UNSET


class ErrorsisreturnedwhenanerrorassociatesanuserDict(TypedDict):
    error: ConversationsInviteErrorEnumOrStr
    ok: bool
    user: NotRequired[str]

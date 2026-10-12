from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagingobject import Pagingobject, PagingobjectDict


class ReactionsListschema(SdkBaseModel):
    """Schema for successful response from reactions.list method"""

    items: list[Any]
    ok: bool
    paging: Optional[Pagingobject] = UNSET
    response_metadata: Optional[Any] = UNSET


class ReactionsListschemaDict(TypedDict):
    items: list[Any]
    ok: bool
    paging: NotRequired[PagingobjectDict]
    response_metadata: NotRequired[Any]

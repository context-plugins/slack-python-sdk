from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReactionsRemoveschema(SdkBaseModel):
    """Schema for successful response from reactions.remove method"""

    ok: bool


class ReactionsRemoveschemaDict(TypedDict):
    ok: bool

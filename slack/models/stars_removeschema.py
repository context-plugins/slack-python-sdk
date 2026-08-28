from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StarsRemoveschema(SdkBaseModel):
    """Schema for successful response from stars.remove method"""

    ok: bool


class StarsRemoveschemaDict(TypedDict):
    ok: bool

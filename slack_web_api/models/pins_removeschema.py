from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PinsRemoveschema(SdkBaseModel):
    """Schema for successful response from pins.remove method"""

    ok: bool


class PinsRemoveschemaDict(TypedDict):
    ok: bool

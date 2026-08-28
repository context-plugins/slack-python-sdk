from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PinsAddschema(SdkBaseModel):
    """Schema for successful response from pins.add method"""

    ok: bool


class PinsAddschemaDict(TypedDict):
    ok: bool

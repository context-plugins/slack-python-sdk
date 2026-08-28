from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StarsAddschema(SdkBaseModel):
    """Schema for successful response from stars.add method"""

    ok: bool


class StarsAddschemaDict(TypedDict):
    ok: bool

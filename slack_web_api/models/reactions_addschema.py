from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReactionsAddschema(SdkBaseModel):
    """Schema for successful response from reactions.add method"""

    ok: bool


class ReactionsAddschemaDict(TypedDict):
    ok: bool

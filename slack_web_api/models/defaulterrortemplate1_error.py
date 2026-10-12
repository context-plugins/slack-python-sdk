from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Defaulterrortemplate1Error(SdkBaseModel):
    """This method either only returns a brief _not OK_ response or a verbose schema is not available for this
    method."""

    ok: bool


class Defaulterrortemplate1ErrorDict(TypedDict):
    ok: bool

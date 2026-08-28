from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Defaultsuccesstemplate(SdkBaseModel):
    """This method either only returns a brief _OK_ response or a verbose schema is not available for this method."""

    ok: bool


class DefaultsuccesstemplateDict(TypedDict):
    ok: bool

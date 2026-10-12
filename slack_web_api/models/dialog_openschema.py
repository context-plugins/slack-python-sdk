from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DialogOpenschema(SdkBaseModel):
    """Schema for successful response from dialog.open method"""

    ok: bool


class DialogOpenschemaDict(TypedDict):
    ok: bool

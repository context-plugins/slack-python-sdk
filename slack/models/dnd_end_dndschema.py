from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DndEndDndschema(SdkBaseModel):
    """Schema for successful response from dnd.endDnd method"""

    ok: bool


class DndEndDndschemaDict(TypedDict):
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FilesDeleteschema(SdkBaseModel):
    """Schema for successful response files.delete method"""

    ok: bool


class FilesDeleteschemaDict(TypedDict):
    ok: bool

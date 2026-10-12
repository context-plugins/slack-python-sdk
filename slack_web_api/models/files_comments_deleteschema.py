from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FilesCommentsDeleteschema(SdkBaseModel):
    """Schema for successful response files.comments.delete method"""

    ok: bool


class FilesCommentsDeleteschemaDict(TypedDict):
    ok: bool

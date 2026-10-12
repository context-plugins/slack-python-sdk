from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fileobject import Fileobject, FileobjectDict


class FilesUploadschema(SdkBaseModel):
    """Schema for successful response files.upload method"""

    file: Fileobject
    ok: bool


class FilesUploadschemaDict(TypedDict):
    file: FileobjectDict
    ok: bool

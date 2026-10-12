from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fileobject import Fileobject, FileobjectDict


class FilesSharedPublicUrlschema(SdkBaseModel):
    """Schema for successful response from files.sharedPublicURL method"""

    file: Fileobject
    ok: bool


class FilesSharedPublicUrlschemaDict(TypedDict):
    file: FileobjectDict
    ok: bool

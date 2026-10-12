from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fileobject import Fileobject, FileobjectDict


class FilesRevokePublicUrlschema(SdkBaseModel):
    """Schema for successful response from files.revokePublicURL method"""

    file: Fileobject
    ok: bool


class FilesRevokePublicUrlschemaDict(TypedDict):
    file: FileobjectDict
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fileobject import Fileobject, FileobjectDict
from .pagingobject import Pagingobject, PagingobjectDict


class FilesListschema(SdkBaseModel):
    """Schema for successful response from files.list method"""

    files: list[Fileobject]
    ok: bool
    paging: Pagingobject


class FilesListschemaDict(TypedDict):
    files: list[Fileobject | FileobjectDict]
    ok: bool
    paging: Pagingobject | PagingobjectDict

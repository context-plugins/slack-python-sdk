from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_list_error_enum import FilesListErrorEnumOrStr


class FilesListerrorschema1Error(SdkBaseModel):
    """Schema for error response from files.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesListErrorEnumOrStr
    ok: bool


class FilesListerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: FilesListErrorEnumOrStr
    ok: bool

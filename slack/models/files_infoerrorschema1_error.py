from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_info_error_enum import FilesInfoErrorEnumOrStr


class FilesInfoerrorschema1Error(SdkBaseModel):
    """Schema for error response from files.info method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesInfoErrorEnumOrStr
    ok: bool


class FilesInfoerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: FilesInfoErrorEnumOrStr
    ok: bool

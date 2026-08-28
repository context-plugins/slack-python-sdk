from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_shared_public_urlerror_enum import FilesSharedPublicUrlerrorEnumOrStr


class FilesSharedPublicUrlerrorschema1Error(SdkBaseModel):
    """Schema for error response from files.sharedPublicURL method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesSharedPublicUrlerrorEnumOrStr
    ok: bool


class FilesSharedPublicUrlerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: FilesSharedPublicUrlerrorEnumOrStr
    ok: bool

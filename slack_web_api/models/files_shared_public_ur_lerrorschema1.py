from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_shared_public_url_error_enum import FilesSharedPublicUrlErrorEnumOrStr


class FilesSharedPublicUrLerrorschema1(SdkBaseModel):
    """Schema for error response from files.sharedPublicURL method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesSharedPublicUrlErrorEnumOrStr
    ok: bool


class FilesSharedPublicUrLerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: FilesSharedPublicUrlErrorEnumOrStr
    ok: bool

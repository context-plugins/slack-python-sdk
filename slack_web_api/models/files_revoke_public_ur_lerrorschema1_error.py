from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_revoke_public_url_error_enum import FilesRevokePublicUrlErrorEnumOrStr


class FilesRevokePublicUrLerrorschema1Error(SdkBaseModel):
    """Schema for error response from files.revokePublicURL method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesRevokePublicUrlErrorEnumOrStr
    ok: bool


class FilesRevokePublicUrLerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: FilesRevokePublicUrlErrorEnumOrStr
    ok: bool

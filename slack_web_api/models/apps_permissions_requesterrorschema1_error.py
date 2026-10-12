from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.apps_permissions_request_error_enum import AppsPermissionsRequestErrorEnumOrStr


class AppsPermissionsRequesterrorschema1Error(SdkBaseModel):
    """Schema for error response from apps.permissions.request method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: AppsPermissionsRequestErrorEnumOrStr
    ok: bool


class AppsPermissionsRequesterrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: AppsPermissionsRequestErrorEnumOrStr
    ok: bool

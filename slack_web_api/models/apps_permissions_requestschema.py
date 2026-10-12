from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AppsPermissionsRequestschema(SdkBaseModel):
    """Schema for successful response from apps.permissions.request method"""

    ok: bool


class AppsPermissionsRequestschemaDict(TypedDict):
    ok: bool

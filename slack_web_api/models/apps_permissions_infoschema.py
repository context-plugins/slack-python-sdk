from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .info import Info, InfoDict


class AppsPermissionsInfoschema(SdkBaseModel):
    """Schema for successful response from apps.permissions.info method"""

    info: Info
    ok: bool


class AppsPermissionsInfoschemaDict(TypedDict):
    info: InfoDict
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AppsUninstallschema(SdkBaseModel):
    """Schema for successful response from apps.uninstall method"""

    ok: bool


class AppsUninstallschemaDict(TypedDict):
    ok: bool

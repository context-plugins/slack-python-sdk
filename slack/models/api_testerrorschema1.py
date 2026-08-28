from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiTesterrorschema1(SdkBaseModel):
    """Schema for error response api.test method"""

    error: str
    ok: bool


class ApiTesterrorschema1Dict(TypedDict):
    error: str
    ok: bool

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiTesterrorschema1Error(SdkBaseModel):
    """Schema for error response api.test method"""

    error: str
    ok: bool


class ApiTesterrorschema1ErrorDict(TypedDict):
    error: str
    ok: bool

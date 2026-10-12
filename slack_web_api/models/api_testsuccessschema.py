from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiTestsuccessschema(SdkBaseModel):
    """Schema for successful response api.test method"""

    ok: bool


class ApiTestsuccessschemaDict(TypedDict):
    ok: bool

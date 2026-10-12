from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scopes import Scopes, ScopesDict


class ApiPermissionsScopesListsuccessschema(SdkBaseModel):
    """Schema for successful response api.permissions.scopes.list method"""

    ok: bool
    scopes: Scopes


class ApiPermissionsScopesListsuccessschemaDict(TypedDict):
    ok: bool
    scopes: ScopesDict

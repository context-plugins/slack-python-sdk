from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .app_home import AppHome, AppHomeDict
from .channel import Channel, ChannelDict
from .group import Group, GroupDict
from .im import Im, ImDict
from .mpim import Mpim, MpimDict
from .team import Team, TeamDict


class Info(SdkBaseModel):
    app_home: AppHome
    channel: Channel
    group: Group
    im: Im
    mpim: Mpim
    team: Team


class InfoDict(TypedDict):
    app_home: AppHomeDict
    channel: ChannelDict
    group: GroupDict
    im: ImDict
    mpim: MpimDict
    team: TeamDict

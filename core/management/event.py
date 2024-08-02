from datetime import datetime
from .data import UserInfo


class Event:
    _time: datetime
    _user_info:  UserInfo
    _args: tuple

    @property
    def time(self) -> datetime:
        return self._time

    @property
    def args(self) -> tuple:
        return self._args

    def __init__(self, user: UserInfo, time: datetime, *args):
        self._time = time
        self._user_info = user
        self._args = args


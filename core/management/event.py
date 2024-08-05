from datetime import datetime
from .data import UserInfo


class Event:
    _user_info:  UserInfo
    _args: tuple

    @property
    def args(self) -> tuple:
        return self._args

    @property
    def user(self) -> UserInfo:
        return self._user_info

    def __init__(self, user: UserInfo, *args):
        self._user_info = user
        self._args = args


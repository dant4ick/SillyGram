from utility import SillyDB
from .tracker import Tracker
from .users import Users
from .tracker import Tracker
from .types import DECLARATIVE_BASE


class Data(SillyDB):
    _users: Users
    _tracker: Tracker

    @property
    def users(self) -> Users:
        return self._users

    @property
    def tracker(self) -> Tracker:
        return self._tracker

    def __init__(self):
        super().__init__("sillygram", DECLARATIVE_BASE)
        self._users = Users(self)
        self._tracker = Tracker(self)


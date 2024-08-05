from utility import SillyDB
from .pages import Pages
from .tracker import Tracker
from .users import Users
from .tracker import Tracker
from .pages import Pages
from .types import DECLARATIVE_BASE
from ...ui import Page

from typing import *


class Data(SillyDB):
    _users: Users
    _tracker: Tracker
    _pages: Pages

    @property
    def users(self) -> Users:
        return self._users

    @property
    def tracker(self) -> Tracker:
        return self._tracker

    @property
    def pages(self) -> Pages:
        return self._pages

    def __init__(self, *pages: Page):
        super().__init__("sillygram", DECLARATIVE_BASE)
        self._users = Users(self)
        self._tracker = Tracker(self)
        self._pages = Pages(*pages)


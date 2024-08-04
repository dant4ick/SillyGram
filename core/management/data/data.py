from utility import SillyDB
from .tracker import Tracker
from .users import Users
from .tracker import Tracker
from .types import DECLARATIVE_BASE
from ...ui import Page

from typing import *


class Data(SillyDB):
    _users: Users
    _tracker: Tracker
    _pages: Dict[Any, Page]

    @property
    def users(self) -> Users:
        return self._users

    @property
    def tracker(self) -> Tracker:
        return self._tracker

    @staticmethod
    def _pages_to_dict(*pages: Page) -> Dict[Any, Page]:
        pages_dict = {}
        for page in pages:
            if page.name in pages_dict.keys():
                raise ValueError(f"Page named {page.name} already exists")
            if page in pages_dict.values():
                continue
            pages_dict[page.name] = page

        return pages_dict

    def get_page(self, name: Any) -> Page:
        return self._pages[name]

    def __init__(self, *pages: Page):
        self._pages = Data._pages_to_dict(*pages)
        super().__init__("sillygram", DECLARATIVE_BASE)
        self._users = Users(self)
        self._tracker = Tracker(self)


from ...ui import Page
from typing import *

_HOME_PAGE_NAME = "$HOME$"
_START_PAGE_NAME = "$START$"


class Pages:
    _pages: Dict[Any, Page]
    _start_page: Page = None
    _home_page: Page = None

    @property
    def home_page_name(self) -> str:
        return self._home_page.name

    @property
    def start_page_name(self) -> str:
        return self._start_page.name

    @property
    def names(self) -> Tuple[str, ...]:
        return tuple(self._pages.keys())

    def get(self, name: Any) -> Page:
        return self._pages[name]

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

    def _setup_specials(self):
        for page in self._pages.values():
            if page.is_home:
                if self._home_page is None:
                    self._home_page = page
                else:
                    raise ValueError(f"Page {page.name} is labeled as home page,"
                                     f" but there already is one ({self._home_page.name})")

            if page.is_start:
                if self._start_page is None:
                    self._start_page = page
                else:
                    raise ValueError(f"Page {page.name} is labeled as start page,"
                                     f" but there already is one ({self._start_page.name})")

    def __init__(self, *pages: Page):
        self._pages = self._pages_to_dict(*pages)
        self._setup_specials()

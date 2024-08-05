from typing import *

from .keyboard import Keyboard
from .button import Button


class Page:
    _default_text: str
    _keyboard: Keyboard
    _name: Any

    _is_home: bool = False
    _is_start: bool = False

    @property
    def default_text(self) -> str:
        return self._default_text

    @property
    def is_home(self) -> bool:
        return self._is_home

    @property
    def is_start(self) -> bool:
        return self._is_start

    @property
    def keyboard(self) -> Keyboard:
        return self._keyboard


    @property
    def name(self) -> Any:
        return self._name

    def __init__(self, name: Any, default_text: str, keyboard: Optional[Keyboard],
                 is_home_page: bool = False, is_start_page: bool = False):

        self._name = name
        self._default_text = default_text
        self._keyboard = keyboard

        self._is_home = is_home_page
        self._is_start = is_start_page


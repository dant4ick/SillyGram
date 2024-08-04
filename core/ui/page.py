from typing import List, Any

from .keyboard import Keyboard


class Page:
    _default_text: str
    _keyboard: Keyboard
    _name: Any

    @property
    def keyboard(self) -> Keyboard:
        return self._keyboard

    @property
    def name(self) -> Any:
        return self._name

    def __init__(self, name: Any, default_text: str, keyboard: Keyboard):
        self._name = name
        self._default_text = default_text
        self._keyboard = keyboard


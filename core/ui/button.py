from .aiogramable import Aiogramable
from aiogram.types import InlineKeyboardButton
from typing import *
#from ..management import Manager, Event


_button_ids: List[int] = list()
_BUTTON_IDENTITY_TEMPLATE = "Button-[{}]"


class Button(Aiogramable):
    _text: str
    _id: int
    #_on_click: Callable[[Manager, Event], Awaitable[None]]
    _on_click: Any

    @property
    def text(self) -> str:
        return self._text

    @property
    def identity(self) -> str:
        return _BUTTON_IDENTITY_TEMPLATE.format(self._id)

    @property
    def on_click(self) -> Any:
        return self._on_click

    def _generate_id(self):
        if len(_button_ids) == 0:
            self._id = 0
            _button_ids.append(self._id)
            return

        max_id = max(_button_ids)
        self._id = max_id + 1
        _button_ids.append(self._id)

    def __init__(self, text: str, on_click: Any = None):
        self._text = text
        self._generate_id()
        self._on_click = on_click

    def aiogramify(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=self._text, callback_data=self.identity)






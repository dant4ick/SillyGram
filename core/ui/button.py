from .aiogramable import Aiogramable
from aiogram.types import InlineKeyboardButton


_buttons_ids: list = list()


class Button(Aiogramable):
    _text: str
    _id: int

    @property
    def text(self) -> str:
        return self._text

    @property
    def id(self) -> int:
        return self._id

    def __init__(self, text: str):
        self._text = text
        self._generate_id()

    def _generate_id(self):
        max_id = max(_buttons_ids) + 1
        self._id = max_id
        _buttons_ids.append(max_id)

    def aiogramify(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=self._text, callback_data="button")






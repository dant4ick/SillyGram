from .aiogramable import Aiogramable
from aiogram.types import InlineKeyboardMarkup


class Keyboard(Aiogramable):
    _default_text: str
    _buttons: tuple

    def __init__(self, default_text: str, *buttons):
        self._buttons = buttons
        self._default_text = default_text

    def aiogramify(self) -> InlineKeyboardMarkup:
        buttons = [row.aiogramify() for row in self._buttons]
        return InlineKeyboardMarkup(inline_keyboard=buttons)




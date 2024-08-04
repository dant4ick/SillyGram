from typing import Tuple

from .aiogramable import Aiogramable
from aiogram.types import InlineKeyboardMarkup


class Keyboard(Aiogramable):
    _rows: tuple

    def __init__(self, *rows):
        self._rows = rows

    def aiogramify(self) -> InlineKeyboardMarkup:
        buttons = [row.aiogramify() for row in self._rows]
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    @property
    def buttons(self) -> Tuple:
        return tuple(*row.buttons for row in self._rows)

    @property
    def rows(self) -> Tuple:
        return self._rows







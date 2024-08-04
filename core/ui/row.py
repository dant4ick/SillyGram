from .button import Button
from .aiogramable import Aiogramable


class Row(Aiogramable):
    _buttons: tuple

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._buttons):
            raise StopIteration()

        result = self._buttons[self.index]
        self.index += 1

        return result

    @property
    def buttons(self) -> tuple:
        return self._buttons

    def aiogramify(self) -> list:
        return [button.aiogramify() for button in self.buttons]

    def __init__(self, *buttons: Button) -> None:
        if len(buttons) <= 0:
            raise ValueError("Each ButtonsRow must have at least one button")
        if len(buttons) > 3:
            raise ValueError("There cannot be more than 3 buttons in a ButtonsRow")

        self._buttons = buttons



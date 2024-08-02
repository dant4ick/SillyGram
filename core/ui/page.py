from .keyboard import Keyboard


class Page:
    _default_text: str
    _keyboard: Keyboard

    def __init__(self, default_text: str, keyboard: Keyboard):
        self.default_text = default_text
        self.keyboard = keyboard



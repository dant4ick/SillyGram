from aiogram import Bot as AiogramBot


class GlobalManager:
    _aiogram_bot: AiogramBot

    def __init__(self, aiogram_bot: AiogramBot):
        self._aiogram_bot = aiogram_bot

    async def goto_page(self, page, user_identifier: int):
        ...

    async def send_notification(self, text: str, user_id: int):
        ...

    async def send_interruption(self, text: str, user_id: int):
        ...

    async def get_input(self, prompt: str, user_id: int) -> str | None:
        ...

    async def get_yes_no_answer(self, question: str, user_id: int) -> bool:
        ...

    async def send_broadcast(self, text: str, user_ids: list[int]):
        ...

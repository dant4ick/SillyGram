from aiogram import Bot as AiogramBot
from aiogram.types import InlineKeyboardMarkup, Message as AiogramMessage

from core.management.data.user_info import UserInfo
from .data import Data


class Manager:
    _aiogram_bot: AiogramBot
    _data: Data

    @property
    def statistics(self):
        return self._data.tracker.statistics

    @property
    def recent_users_count(self):
        return self._data.tracker.recent_users_count

    def __init__(self, aiogram_bot: AiogramBot, data: Data) -> None:
        self._aiogram_bot = aiogram_bot
        self._data = data

    def get_user_info(self, user_id: int) -> UserInfo:
        return self._data.users.get_info(user_id)

    async def goto_page(self, page, user_id: int):
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

    async def reset_tracker(self):
        self._data.tracker.reset()

    async def _show_in_target_message(self, user_id: int, text: str, keyboard: InlineKeyboardMarkup):
        target_message_id = self._data.users.get_target_message_id(user_id)

        if target_message_id is not None:
            await self._send_new_target_message(user_id, text, keyboard)
        else:
            try:
                await self._aiogram_bot.edit_message_text(text, message_id=target_message_id, reply_markup=keyboard)
            except Exception as e:
                await self._send_new_target_message(user_id, text, keyboard)

    async def _send_new_target_message(self, user_id: int, text: str, keyboard: InlineKeyboardMarkup):
        message: AiogramMessage = await self._aiogram_bot.send_message(user_id, text, reply_markup=keyboard)
        self._data.users.set_target_message_id(user_id, message.message_id)

    async def _replace_target_message(self, user_id: int, text: str, keyboard: InlineKeyboardMarkup):
        target_message_id = self._data.users.get_target_message_id(user_id)
        if target_message_id is not None:
            try:
                await self._aiogram_bot.delete_message(user_id, target_message_id)
            except Exception as e:
                ...

        await self._send_new_target_message(user_id, text, keyboard)


    
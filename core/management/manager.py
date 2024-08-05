import asyncio

from aiogram import Bot as AiogramBot
from aiogram.types import InlineKeyboardMarkup, Message as AiogramMessage

from .data import Data, UserInfo

from typing import *


class Manager:
    _aiogram_bot: AiogramBot
    _data: Data

    # region Properties etc.

    @property
    def statistics(self):
        return self._data.tracker.statistics

    @property
    def recent_users_count(self):
        return self._data.tracker.recent_users_count

    def get_user_info(self, user_id: int) -> UserInfo:
        return self._data.users.get_info(user_id)

    # endregion

    # region High-level messaging methods

    async def goto_page(self, page_name: Any, user_id: int):
        page = self._data.pages.get(page_name)
        await self._edit_target_message(user_id, page.default_text, page.keyboard.aiogramify())

    async def goto_page_detached(self, name: str, user_id: int):
        page = self._data.pages.get(name)

        for i in range(0, 5):
            await self._aiogram_bot.send_message(user_id, text="✨")
            await asyncio.sleep(0.15)

        await self._send_new_target_message(user_id, page.default_text, page.keyboard.aiogramify())

    async def goto_home_page(self, user_id: int):
        ...

    async def goto_start_page(self, user_id: int):
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

    # endregion

    # region Low-level messaging methods

    async def _edit_target_message(self, user_id: int, text: str, keyboard: InlineKeyboardMarkup):
        target_message_id = self._data.users.get_target_message_id(user_id)

        if target_message_id is None:
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

    # endregion

    def __init__(self, aiogram_bot: AiogramBot, data: Data):
        self._aiogram_bot = aiogram_bot
        self._data = data




    
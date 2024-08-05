import asyncio
from typing import *

from aiogram import Bot, Dispatcher, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from .management import Event, Manager
from .management.data import Data
from .ui import Page

DEFAULT_PARSE_MODE = "HTML"
DEFAULT_BOT_PROPERTIES = DefaultBotProperties(parse_mode=DEFAULT_PARSE_MODE)


class SillyBot:
    _bot: Bot
    _dispatcher: Dispatcher = Dispatcher()
    _router_for_default_handler: Router

    _data: Data
    _manager: Manager
    
    # region Starting

    @staticmethod
    async def _on_startup():
        print("SillyBot is polling...")

    def launch_async(self):
        """
        Use this method to start the bot asynchronously. It must be called from synchronous code.

        After this method is called, the program goes into an endless loop,
        and the program will be blocked until the bot is terminated. Therefore, all the settings must be up
        before the SillyBot is launched.
        """

        asyncio.run(self.launch())

    async def launch(self):
        """
        Use this method to start the bot. It must be called from asynchronous code.

        After this method is called, the program goes into an endless loop,
        and the program will be blocked until the bot is terminated. Therefore, all the settings must be up
        before the SillyBot is launched.
        """

        await self._dispatcher.start_polling(self._bot, skip_updates=True)

    # endregion

    # region Events handlers

    def _setup_handlers(self):
        if self._data.pages.home_page_name is not None:
            self._register_command("home", self._on_home)

        if self._data.pages.start_page_name is not None:
            self._register_command("start", self._on_start)

        pages = (self._data.pages.get(name) for name in self._data.pages.names)
        buttons = []
        for page in pages:
            for button in page.keyboard.buttons:
                if button not in buttons:
                    buttons.append(button)

        for button in buttons:
            self._register_callback(button.identity, button.on_click)

    def _register_command(self, command: str, handler: Any):
        async def aiogram_handler(message: Message):
            try:
                await message.delete()
            except Exception:
                ...

            user_info = self._data.users.indicate(message.from_user)

            args = message.text.split()[1:]
            event = Event(user_info, *args)
            return await handler(self._manager, event)

        self._dispatcher.message.register(aiogram_handler, Command(command))

    def _register_callback(self, callback_identity: str, handler: Any):
        async def aiogram_handler(callback: CallbackQuery):
            user_info = self._data.users.indicate(callback.from_user)
            event = Event(user_info)
            return await handler(self._manager, event)

        self._dispatcher.callback_query.register(aiogram_handler, F.data.startswith(callback_identity))

    # region Default handlers

    async def _on_start(self, manager: Manager, event: Event):
        await manager.goto_page_detached(self._data.pages.start_page_name, event.user.id)

    async def _on_home(self, manager: Manager, event: Event):
        await manager.goto_page_detached(self._data.pages.home_page_name, event.user.id)

    # endregion

    # endregion

    # region Decorators

    def track(self, key: str):
        return self._data.tracker.track(key)

    # endregion

    def __init__(self, token: str, *pages: Page):
        """
        :param token: Telegram-API token received from BotFather.
        :param pages: Page objects to include. Names must be unique.
        """

        self._data = Data(*pages)
        self._bot = Bot(token=token, default=DEFAULT_BOT_PROPERTIES)
        self._dispatcher.startup.register(SillyBot._on_startup)
        self._manager = Manager(self._bot, self._data)

        self._setup_handlers()

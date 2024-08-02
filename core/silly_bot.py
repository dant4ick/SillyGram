import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from .management import Event, Manager
from .management.data import Data

DEFAULT_PARSE_MODE = "HTML"
DEFAULT_BOT_PROPERTIES = DefaultBotProperties(parse_mode=DEFAULT_PARSE_MODE)


class SillyBot:
    _bot: Bot
    _dispatcher: Dispatcher = Dispatcher()

    _router_for_default_handler: Router
    _data: Data

    _manager: Manager

    def __init__(self, token: str):
        """
        :param token: Telegram-API token received from BotFather.
        """
        self._data = Data()
        self._bot = Bot(token=token, default=DEFAULT_BOT_PROPERTIES)
        self._dispatcher.startup.register(self._on_startup)
        self._manager = Manager(self._bot, self._data)

    async def _on_startup(self):
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

    def _on_command(self, command_text: str):
        """
        A decorator to mark command handlers.

        The /start and /continue commands are reserved by SillyGram,
        so use on_start and on_continue decorators to redefine them.

        SillyGram is meant to design bots that only use inline keyboards, therefore this method is protected
        and SillyGram bots are not allowed to define any more commands.

        :param command_text: e.g. "start" for a /start command
        """
        def decorator(silly_handler):
            @self._dispatcher.message(Command(command_text))
            async def aiogram_handler(message: Message):
                try:
                    await message.delete()
                except Exception:
                    ...

                user_info = self._data.users.indicate(message.from_user)

                args = message.text.split()[1:]
                event = Event(user_info, message.date, *args)
                return await silly_handler(self._manager, event)

            return aiogram_handler

        return decorator

    def _on_callback(self, callback_identity: str):
        ...

    def track(self, key: str):
        return self._data.tracker.track(key)


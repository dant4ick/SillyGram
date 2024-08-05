from config import TOKEN
from core import *


async def on_button_clicked(manager: Manager, event: Event):
    await manager.goto_page_detached("Start", event.user.id)


page = Page(name="Start",
            default_text="Welcome to Silly-Bot!",
            keyboard=Keyboard(
                (
                    Button(text="OK", on_click=on_button_clicked),
                )
            ),
            is_start_page=True,
            is_home_page=True,
            )

silly_bot: SillyBot = SillyBot(TOKEN,
                               page)

if __name__ == '__main__':
    silly_bot.launch_async()

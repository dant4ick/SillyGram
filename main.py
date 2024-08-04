from config import TOKEN
from core.silly_bot import SillyBot
from core.ui import *

page = Page(name="page",
            default_text="Welcome to Silly-Bot!",
            keyboard=Keyboard(
                Row(
                    Button("OK")
                )
            ))

silly_bot: SillyBot = SillyBot(TOKEN, page)

if __name__ == '__main__':
    silly_bot.launch_async()

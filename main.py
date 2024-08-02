from config import TOKEN
from core.silly_bot import SillyBot

silly_bot: SillyBot = SillyBot(TOKEN)

if __name__ == '__main__':
    silly_bot.launch_async()

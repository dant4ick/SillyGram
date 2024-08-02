from utility import SillyDataSection
from aiogram.types import User as AiogramUser
from .user_info import UserInfo


class Users(SillyDataSection):

    def indicate(self, aiogram_user: AiogramUser) -> UserInfo:
        ...

    def get_info(self, user_id: int) -> UserInfo | None:
        ...

    def get_target_message_id(self, user_id: int) -> int | None:
        ...

    def set_target_message_id(self, user_id: int, message_id: int):
        ...

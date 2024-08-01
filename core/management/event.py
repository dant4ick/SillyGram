from datetime import datetime
from .user import User


class Event:
    _time: datetime
    _user: User

    def __init__(self, user_identifier: int, time: datetime):
        self._time = time
        self._user = User(user_identifier)


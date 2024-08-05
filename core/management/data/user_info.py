class UserInfo:
    _id: int

    @property
    def id(self) -> int:
        return self._id

    def __init__(self, user_id: int):
        self._id = user_id

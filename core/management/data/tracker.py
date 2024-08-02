import asyncio
from datetime import datetime
from utility import SillyDataSection


class Tracker(SillyDataSection):
    __statistics: dict[str, int] = {}
    __recent_users_id_list: list[int] = []
    __start_time: datetime = datetime.now()

    @property
    def recent_users_count(self) -> int:
        return len(self.__recent_users_id_list)

    @property
    def statistics(self) -> dict[str, int]:
        return self.__statistics

    def _increment_key(self, key: str, user_id: int):
        if key in self.__statistics:
            self.__statistics[key] += 1
        else:
            self.__statistics[key] = 1

        if user_id not in self.__recent_users_id_list and user_id is not None:
            self.__recent_users_id_list.append(user_id)

    def track(self, key: str):
        def decorator(function):
            async def wrapper(*args, **kwargs):
                user_id = None

                for arg in args:
                    if isinstance(arg, int):
                        user_id = arg
                        break

                self._increment_key(key, user_id)

                return await function(*args, **kwargs)

            return wrapper

        return decorator



from abc import abstractmethod, ABCMeta


class Aiogramable(metaclass=ABCMeta):

    @abstractmethod
    def aiogramify(self) -> any:
        raise NotImplementedError()

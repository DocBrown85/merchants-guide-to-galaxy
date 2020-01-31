from abc import ABC, abstractmethod


class ICommandResponseFormatter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def format(self):
        pass

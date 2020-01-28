from abc import ABC, abstractmethod


class ICommand(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass

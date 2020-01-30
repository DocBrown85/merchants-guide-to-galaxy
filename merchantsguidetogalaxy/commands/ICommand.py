from abc import ABC, abstractmethod


class ICommand(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class ICommandResponse:
    _response = None

    def __init__(self):
        pass

    def format(self):
        return self._response

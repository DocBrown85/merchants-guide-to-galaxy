from abc import ABC, abstractmethod


class ICommandParser(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def parseCommand(self, input):
        pass


class ICommandParserError(Exception):
    pass

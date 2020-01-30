from .CommandParserFactory import CommandParserFactory
from .ICommandParser import ICommandParser, ICommandParserError

_commandParserFactory = CommandParserFactory()


def getCommandParser(type):
    return _commandParserFactory.getCommandParser(type)

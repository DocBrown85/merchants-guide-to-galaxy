from .StringCommandParser import StringCommandParser, StringCommandParserError


class CommandParserFactory:
    def __init__(self):
        self._commandParsersRegistry = {"default": StringCommandParser}

    def getCommandParser(self, type):
        if not type in self._commandParsersRegistry:
            raise CommandParserFactoryError(
                "unknown command parser type: {}".format(type)
            )

        commandParser = self._commandParsersRegistry[type]()
        return commandParser


class CommandParserFactoryError(Exception):
    pass

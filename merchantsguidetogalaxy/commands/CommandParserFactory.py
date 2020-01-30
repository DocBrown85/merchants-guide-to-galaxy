from .StringCommandParser import StringCommandParser, StringCommandParserError


class CommandParserFactory:
    def __init__(self):
        pass

    def getCommandParser(self, type):
        if type == "default":
            return StringCommandParser()
        else:
            raise CommandParserFactoryError(
                "unknown command parser type: {}".format(type)
            )


class CommandParserFactoryError(Exception):
    pass

import sys
import traceback

from . import commands


class MerchantsGuideToGalaxy:
    def __init__(self, commandParserType="default"):
        self._commandParser = commands.getCommandParser(commandParserType)

    def getHelp(self, request):
        response = None
        try:
            command = self._commandParser.parseCommand(request)
            response = command.execute()
        except commands.ICommandParserError as e:
            response = "I have no idea what you are talking about"
        except Exception as e:
            traceback.print_exc(file=sys.stderr)

        return response

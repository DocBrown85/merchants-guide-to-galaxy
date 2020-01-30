import sys
import traceback

from . import commandparsers


class MerchantsGuideToGalaxy:
    def __init__(self, commandParserType="default", responseFormatType="default"):
        self._commandParserType = commandParserType
        self._responseFormatType = responseFormatType
        self._commandParser = commandparsers.getCommandParser(commandParserType)

    def getHelp(self, request):
        response = None
        try:
            command = self._commandParser.parseCommand(request)
            commandResponse = command.execute()
            response = commandResponse.format(self._responseFormatType)
        except commandparsers.ICommandParserError as e:
            response = "I have no idea what you are talking about"
        except Exception as e:
            traceback.print_exc(file=sys.stderr)

        return response

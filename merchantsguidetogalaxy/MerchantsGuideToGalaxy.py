import sys
import traceback

from . import commandparsers
from . import commandresponseformatters


class MerchantsGuideToGalaxy:
    def __init__(self, commandParserType="default", responseFormatType="default"):
        self._commandParser = commandparsers.getCommandParser(commandParserType)
        self._commandResponseFormatter = commandresponseformatters.getCommandResponseFormatter(
            responseFormatType
        )

    def help(self, request):
        response = None
        try:
            command = self._commandParser.parseCommand(request)
            commandResponse = command.execute()
            response = self._commandResponseFormatter.format(commandResponse)
        except commandparsers.ICommandParserError as e:
            response = "I have no idea what you are talking about"
        except Exception as e:
            traceback.print_exc(file=sys.stderr)

        return response

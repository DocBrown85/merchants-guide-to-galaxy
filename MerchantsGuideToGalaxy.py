import traceback

import commands


class MerchantsGuideToGalaxy:
    def __init__(self):
        self._commandParser = commands.CommandParser()

    def getHelp(self, request):
        response = None
        try:
            command = self._commandParser.parseCommand(request)
            response = command.execute()
        except Exception as e:
            # traceback.print_exc(file=sys.stderr)
            response = "I have no idea what you are talking about"

        return response

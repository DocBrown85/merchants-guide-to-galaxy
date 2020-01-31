from .CommandResponseStringFormatter import CommandResponseStringFormatter


class CommandResponseFormattersFactory:
    def __init__(self):
        self._commandResponseFormattersRegistry = {
            "default": CommandResponseStringFormatter
        }

    def getCommandResponseFormatter(self, responseFormatType):
        if not (responseFormatType in self._commandResponseFormattersRegistry):
            raise CommandResponseFormattersFactoryError(
                "unknown command response type: {}".format(responseFormatType)
            )
        formatter = self._commandResponseFormattersRegistry[responseFormatType]()
        return formatter


class CommandResponseFormattersFactoryError(Exception):
    pass

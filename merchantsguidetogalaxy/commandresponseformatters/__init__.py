from .CommandResponseFormattersFactory import CommandResponseFormattersFactory

_commandResponseFormattersFactory = CommandResponseFormattersFactory()


def getCommandResponseFormatter(responseFormatType):
    return _commandResponseFormattersFactory.getCommandResponseFormatter(
        responseFormatType
    )

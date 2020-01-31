from .ICommandResponseFormatter import ICommandResponseFormatter


class TranslateFromIntergalacticNumeralCommandResponseStringFormatter(
    ICommandResponseFormatter
):
    def format(self, translateFromIntergalacticNumeralCommandResponse):
        formattedResponse = "{} is {}".format(
            " ".join(
                translateFromIntergalacticNumeralCommandResponse._argIntergalacticUnits
            ),
            translateFromIntergalacticNumeralCommandResponse._response,
        )
        return formattedResponse

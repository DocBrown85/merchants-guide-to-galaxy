from .ICommandResponseFormatter import ICommandResponseFormatter


class TranslateUnitsOfGoodWorthCommandResponseStringFormatter(
    ICommandResponseFormatter
):
    def format(self, translateUnitsOfGoodWorthCommandResponse):
        formattedResponse = "{} {} is {:0.0f} Credits".format(
            " ".join(translateUnitsOfGoodWorthCommandResponse._argIntergalacticUnits),
            translateUnitsOfGoodWorthCommandResponse._argGoodName.capitalize(),
            translateUnitsOfGoodWorthCommandResponse._response,
        )
        return formattedResponse

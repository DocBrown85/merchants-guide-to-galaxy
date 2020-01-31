from .ICommandResponseFormatter import ICommandResponseFormatter


class SetIntergalacticDigitToRomanDigitTranslationCommandResponseStringFormatter(
    ICommandResponseFormatter
):
    def format(self, setIntergalacticDigitToRomanDigitTranslationCommandResponse):
        return setIntergalacticDigitToRomanDigitTranslationCommandResponse._response

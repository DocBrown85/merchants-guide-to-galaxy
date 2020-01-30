from .ICommand import ICommand, ICommandResponse

from .. import translators


class CommandSetIntergalacticDigitToRomanDigitTranslation(ICommand):
    def __init__(self, intergalacticDigit, romanDigit):
        self._intergalacticDigit = intergalacticDigit
        self._romanDigit = romanDigit

    def execute(self):
        intergalacticDigitToRomanDigitTranslator = (
            translators.IntergalacticDigitToRomanDigitTranslator()
        )

        intergalacticDigitToRomanDigitTranslator.setIntergalacticDigitToRomanDigitTranslation(
            self._intergalacticDigit, self._romanDigit
        )

        return SetIntergalacticDigitToRomanDigitTranslationCommandResponse(
            self._intergalacticDigit, self._romanDigit, None
        )


class SetIntergalacticDigitToRomanDigitTranslationCommandResponse(ICommandResponse):
    def __init__(self, argIntergalacticDigit, argRomanDigit, response):
        self._argIntergalacticDigit = argIntergalacticDigit
        self._argRomanDigit = argRomanDigit
        self._response = response

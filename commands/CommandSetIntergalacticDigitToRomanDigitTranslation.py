from .ICommand import ICommand

import translators


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

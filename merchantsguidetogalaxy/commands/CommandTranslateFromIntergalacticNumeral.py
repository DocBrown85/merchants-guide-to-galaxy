from .ICommand import ICommand, ICommandResponse

from .. import translators


class CommandTranslateFromIntergalacticNumeral(ICommand):
    def __init__(self, intergalacticUnits):
        self._intergalacticUnits = intergalacticUnits

    def execute(self):
        intergalacticDigitToRomanDigitTranslator = (
            translators.IntergalacticDigitToRomanDigitTranslator()
        )

        romanDigits = intergalacticDigitToRomanDigitTranslator.translateIntergalacticNumeralToRomanNumeral(
            self._intergalacticUnits
        )

        romanNumeralArabicNumeralTranslator = (
            translators.RomanNumeralArabicNumeralTranslator()
        )

        arabicNumeral = romanNumeralArabicNumeralTranslator.getArabicNumeralFromRomanNumeral(
            "".join(romanDigits)
        )

        return TranslateFromIntergalacticNumeralCommandResponse(
            self._intergalacticUnits, arabicNumeral
        )


class TranslateFromIntergalacticNumeralCommandResponse(ICommandResponse):
    def __init__(self, argIntergalacticUnits, response):
        self._argIntergalacticUnits = argIntergalacticUnits
        self._response = response

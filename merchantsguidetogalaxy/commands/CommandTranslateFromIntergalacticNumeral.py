from .ICommand import ICommand

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

        response = "{} is {}".format(" ".join(self._intergalacticUnits), arabicNumeral)

        return response

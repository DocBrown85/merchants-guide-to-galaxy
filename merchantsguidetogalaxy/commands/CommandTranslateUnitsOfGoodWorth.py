from .ICommand import ICommand

from .. import translators


class CommandTranslateUnitsOfGoodWorth(ICommand):
    def __init__(self, intergalacticUnits, goodName):
        self._intergalacticUnits = intergalacticUnits
        self._goodName = goodName

    def execute(self):
        intergalacticDigitToRomanDigitTranslator = (
            translators.IntergalacticDigitToRomanDigitTranslator()
        )

        romanDigits = intergalacticDigitToRomanDigitTranslator.translateIntergalacticNumeralToRomanNumeral(
            self._intergalacticUnits
        )

        romanNumeralToArabicNumeralTranslator = (
            translators.RomanNumeralToArabicNumeralTranslator()
        )

        arabicNumeral = romanNumeralToArabicNumeralTranslator.translate(
            "".join(romanDigits)
        )

        unitsOfGoodWorthTranslator = translators.UnitsOfGoodWorthTranslator()

        translatedGoodWorth = unitsOfGoodWorthTranslator.getUnitsOfGoodWorth(
            self._goodName, arabicNumeral
        )

        response = "{} {} is {:0.0f} Credits".format(
            " ".join(self._intergalacticUnits), self._goodName, translatedGoodWorth
        )

        return response
from .ICommand import ICommand

from .. import translators


class CommandSetUnitsOfGoodsWorth(ICommand):
    def __init__(self, intergalacticUnits, goodName, goodWorth):
        self._intergalacticUnits = intergalacticUnits
        self._goodName = goodName
        self._goodWorth = goodWorth

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

        unitsOfGoodWorthTranslator = translators.UnitsOfGoodWorthTranslator()

        unitsOfGoodWorthTranslator.setUnitsOfGoodWorth(
            self._goodName, arabicNumeral, self._goodWorth
        )

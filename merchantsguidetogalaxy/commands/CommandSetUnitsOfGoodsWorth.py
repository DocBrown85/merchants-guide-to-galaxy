from .ICommand import ICommand, ICommandResponse

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

        return SetUnitsOfGoodsWorthCommandResponse(
            self._intergalacticUnits, self._goodName, self._goodWorth, None
        )


class SetUnitsOfGoodsWorthCommandResponse(ICommandResponse):
    def __init__(self, argIntergalacticUnits, argGoodName, argGoodWorth, response):
        self._argIntergalacticUnits = argIntergalacticUnits
        self._argGoodName = argGoodName
        self._argGoodWorth = argGoodWorth
        self._response = response

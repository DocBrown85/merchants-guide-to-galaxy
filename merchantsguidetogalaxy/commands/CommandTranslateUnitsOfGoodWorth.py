from .ICommand import ICommand, ICommandResponse

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

        romanNumeralArabicNumeralTranslator = (
            translators.RomanNumeralArabicNumeralTranslator()
        )

        arabicNumeral = romanNumeralArabicNumeralTranslator.getArabicNumeralFromRomanNumeral(
            "".join(romanDigits)
        )

        unitsOfGoodWorthTranslator = translators.UnitsOfGoodWorthTranslator()

        translatedGoodWorth = unitsOfGoodWorthTranslator.getUnitsOfGoodWorth(
            self._goodName, arabicNumeral
        )

        return TranslateUnitsOfGoodWorthCommandResponse(
            self._intergalacticUnits, self._goodName, translatedGoodWorth
        )


class TranslateUnitsOfGoodWorthCommandResponse(ICommandResponse):
    def __init__(self, argIntergalacticUnits, argGoodName, response):
        self._argIntergalacticUnits = argIntergalacticUnits
        self._argGoodName = argGoodName
        self._response = response

    def format(self, responseFormat):
        formattedResponse = None
        if responseFormat == "default":
            formattedResponse = self._formatString()
        else:
            raise Exception("unknown format type: {}".format(responseFormat))
        return formattedResponse

    def _formatString(self):
        formattedResponse = "{} {} is {:0.0f} Credits".format(
            " ".join(self._argIntergalacticUnits),
            self._argGoodName.capitalize(),
            self._response,
        )
        return formattedResponse

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

    def format(self, responseFormat):
        formattedResponse = None
        if responseFormat == "default":
            formattedResponse = self._formatString()
        else:
            raise Exception("unknown format type: {}".format(responseFormat))
        return formattedResponse

    def _formatString(self):
        formattedResponse = "{} is {}".format(
            " ".join(self._argIntergalacticUnits), self._response
        )
        return formattedResponse

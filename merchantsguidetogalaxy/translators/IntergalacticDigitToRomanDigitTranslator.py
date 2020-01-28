class IntergalacticDigitToRomanDigitTranslator(object):

    _intergalacticDigitToRomanDigitTranslationTable = {}

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(
                IntergalacticDigitToRomanDigitTranslator, cls
            ).__new__(cls)
        return cls._instance

    def setIntergalacticDigitToRomanDigitTranslation(
        self, intergalacticDigit, romanDigit
    ):
        self._intergalacticDigitToRomanDigitTranslationTable[
            intergalacticDigit
        ] = romanDigit

    def translateIntergalacticNumeralToRomanNumeral(self, intergalacticNumeralDigits):

        romanNumeral = []
        for intergalacticNumeralDigit in intergalacticNumeralDigits:
            if (
                intergalacticNumeralDigit
                in self._intergalacticDigitToRomanDigitTranslationTable
            ):
                romanNumeral.append(
                    self._intergalacticDigitToRomanDigitTranslationTable[
                        intergalacticNumeralDigit
                    ]
                )
            else:
                raise IntergalacticDigitToRomanDigitTranslatorError(
                    "unknown intergalactic digit: {}".format(intergalacticNumeralDigit)
                )
        return romanNumeral


class IntergalacticDigitToRomanDigitTranslatorError(Exception):
    pass

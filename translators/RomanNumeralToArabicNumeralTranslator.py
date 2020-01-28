class RomanNumeralToArabicNumeralTranslator:
    _romanDigitToArabicDigitConversionTable = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def __init__(self):
        pass

    def translate(self, romanNumeral):
        romanNumeral = romanNumeral.upper()

        arabicNumeral = 0
        for i in range(len(romanNumeral)):
            if (
                i > 0
                and self._romanDigitToArabicDigitConversionTable[romanNumeral[i]]
                > self._romanDigitToArabicDigitConversionTable[romanNumeral[i - 1]]
            ):
                arabicNumeral += (
                    self._romanDigitToArabicDigitConversionTable[romanNumeral[i]]
                    - 2
                    * self._romanDigitToArabicDigitConversionTable[romanNumeral[i - 1]]
                )
            else:
                arabicNumeral += self._romanDigitToArabicDigitConversionTable[
                    romanNumeral[i]
                ]

        return arabicNumeral

class RomanNumeralArabicNumeralTranslator:
    def __init__(self):
        pass

    def getArabicNumeralFromRomanNumeral(self, romanNumeral):
        romanNumeral = romanNumeral.upper()
        romanDigitToArabicDigitConversionTable = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        arabicNumeral = 0
        for i in range(len(romanNumeral)):
            try:
                value = romanDigitToArabicDigitConversionTable[romanNumeral[i]]
                if (
                    i + 1 < len(romanNumeral)
                    and romanDigitToArabicDigitConversionTable[romanNumeral[i + 1]]
                    > value
                ):
                    arabicNumeral -= value
                else:
                    arabicNumeral += value
            except KeyError:
                raise RomanNumeralArabicNumeralTranslatorError(
                    "%s is not a valid Roman numeral.".format(romanNumeral)
                )
        if self.getRomanNumeralFromArabicNumeral(arabicNumeral) != romanNumeral:
            raise RomanNumeralArabicNumeralTranslatorError(
                "%s is not a valid Roman numeral.".format(romanNumeral)
            )

        return arabicNumeral

    def getRomanNumeralFromArabicNumeral(self, arabicNumeral):
        if not 0 < arabicNumeral < 4000:
            raise RomanNumeralArabicNumeralTranslatorError(
                "Argument must be between 1 and 3999"
            )
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        romanNumeral = []
        for i in range(len(ints)):
            count = int(arabicNumeral / ints[i])
            romanNumeral.append(nums[i] * count)
            arabicNumeral -= ints[i] * count
        return "".join(romanNumeral)


class RomanNumeralArabicNumeralTranslatorError(Exception):
    pass

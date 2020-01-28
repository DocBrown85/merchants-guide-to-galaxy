class UnitsOfGoodWorthTranslator(object):

    _goodsWorthTranslationTable = {}

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UnitsOfGoodWorthTranslator, cls).__new__(cls)
        return cls._instance

    def setUnitsOfGoodWorth(self, good, units, worth):
        self._goodsWorthTranslationTable[good] = worth / units

    def getUnitsOfGoodWorth(self, good, units):
        if not good in self._goodsWorthTranslationTable:
            raise UnitsOfGoodWorthTranslatorError("unknown good: {}".format(good))

        worth = self._goodsWorthTranslationTable[good] * units

        return worth


class UnitsOfGoodWorthTranslatorError(Exception):
    pass

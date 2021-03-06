import unittest
import merchantsguidetogalaxy


class TestMerchantsGuideToGalaxyWithWhitespaces(unittest.TestCase):
    def setUp(self):
        self._merchantsGuideToGalaxy = merchantsguidetogalaxy.MerchantsGuideToGalaxy()

        initialisationCommands = [
            " glob   means  I ",
            "prok means  V ",
            "  pish    means X ",
            " tegj   means    L ",
            "   glob  glob    units  of   Silver   are   worth 34 Credits   ",
            "glob   prok  units   of   Gold   are   worth  57800   Credits  ",
            "pish pish    units of   Iron   are  worth 3910   Credits",
        ]

        for command in initialisationCommands:
            self._merchantsGuideToGalaxy.help(command)

    def tearDown(self):
        pass

    def test_translateIntergalacticNumeralToArabicNumeralWithWhitespaces(self):
        response = self._merchantsGuideToGalaxy.help(
            "  how   much     is   pish   tegj   glob glob  ?"
        )
        self.assertTrue(response == "pish tegj glob glob is 42")

    def test_translateIntergalacticNumeralToArabicNumeralWithNoWhitespacesBeforeQuestionMark(
        self
    ):
        response = self._merchantsGuideToGalaxy.help(
            "  how   much     is   pish   tegj   glob glob?"
        )
        self.assertTrue(response == "pish tegj glob glob is 42")

    def test_translateUnitsOfGoodWorthGoldWithNoWhitespacesBeforeQuestionMark(self):
        response = self._merchantsGuideToGalaxy.help(
            "  how   many     Credits   is    glob  prok    Gold?"
        )
        self.assertTrue(response == "glob prok Gold is 57800 Credits")

    def test_translateUnitsOfGoodWorthGoldWithWhitespaces(self):
        response = self._merchantsGuideToGalaxy.help(
            "  how   many     Credits   is    glob  prok    Gold ?"
        )
        self.assertTrue(response == "glob prok Gold is 57800 Credits")

    def test_translateUnitsOfGoodWorthIronWithWhitespaces(self):
        response = self._merchantsGuideToGalaxy.help(
            "   how    many    Credits          is   glob   prok   Iron   ?   "
        )
        self.assertTrue(response == "glob prok Iron is 782 Credits")

    def test_translateUnitsOfGoodWorthSilverWithWhitespaces(self):
        response = self._merchantsGuideToGalaxy.help(
            "how   many   Credits    is   glob   prok   Silver   ?"
        )
        self.assertTrue(response == "glob prok Silver is 68 Credits")

    def test_unknownCommandWithWhitespaces(self):
        response = self._merchantsGuideToGalaxy.help(
            "how much wood   could   a   woodchuck   chuck   if   a   woodchuck   could   chuck   wood ?"
        )
        self.assertTrue(response == "I have no idea what you are talking about")


if __name__ == "__main__":
    unittest.main()

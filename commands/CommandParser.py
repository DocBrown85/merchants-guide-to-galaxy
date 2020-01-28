import re

from .CommandSetIntergalacticDigitToRomanDigitTranslation import (
    CommandSetIntergalacticDigitToRomanDigitTranslation,
)
from .CommandSetUnitsOfGoodsWorth import CommandSetUnitsOfGoodsWorth
from .CommandTranslateFromIntergalacticNumeral import (
    CommandTranslateFromIntergalacticNumeral,
)
from .CommandTranslateUnitsOfGoodWorth import CommandTranslateUnitsOfGoodWorth


class CommandParser:

    _COMMAND_SET_INTERGALACTIC_DIGIT_TO_ROMAN_DIGIT_TRANSLATION = 0
    _COMMAND_SET_UNITS_OF_GOOD_WORTH = 1
    _COMMAND_TRANSLATE_FROM_INTERGALACTIC_NUMERAL = 2
    _COMMAND_TRANSLATE_UNITS_OF_GOOD_WORTH = 3
    _availableCommands = {
        _COMMAND_SET_INTERGALACTIC_DIGIT_TO_ROMAN_DIGIT_TRANSLATION: "^(\S*) means (\S*)$",
        _COMMAND_SET_UNITS_OF_GOOD_WORTH: "^(.*) units of (\S*) are worth (\S*) Credits$",
        _COMMAND_TRANSLATE_FROM_INTERGALACTIC_NUMERAL: "^how much is (.*) \\?$",
        _COMMAND_TRANSLATE_UNITS_OF_GOOD_WORTH: "^how many Credits is (.*) (\S*) \\?$",
    }

    def __init__(self):
        pass

    def parseCommand(self, text):

        requestedCommand = None
        for commandId, commandLine in self._availableCommands.items():
            match = re.search(commandLine, text)
            if match:
                requestedCommand = commandId
                break

        if (
            requestedCommand
            == self._COMMAND_SET_INTERGALACTIC_DIGIT_TO_ROMAN_DIGIT_TRANSLATION
        ):
            intergalacticDigit = match.group(1)
            romanDigit = match.group(2)

            command = CommandSetIntergalacticDigitToRomanDigitTranslation(
                intergalacticDigit, romanDigit
            )
        elif requestedCommand == self._COMMAND_SET_UNITS_OF_GOOD_WORTH:
            intergalacticUnits = match.group(1).split(" ")
            goodName = match.group(2)
            try:
                goodWorth = int(match.group(3))
            except Exception as e:
                raise CommandParserError(str(e))

            command = CommandSetUnitsOfGoodsWorth(
                intergalacticUnits, goodName, goodWorth
            )
        elif requestedCommand == self._COMMAND_TRANSLATE_FROM_INTERGALACTIC_NUMERAL:
            intergalacticUnits = match.group(1).split(" ")
            command = CommandTranslateFromIntergalacticNumeral(intergalacticUnits)
        elif requestedCommand == self._COMMAND_TRANSLATE_UNITS_OF_GOOD_WORTH:
            intergalacticUnits = match.group(1).split(" ")
            goodName = match.group(2)
            command = CommandTranslateUnitsOfGoodWorth(intergalacticUnits, goodName)
        else:
            raise CommandParserError("unknown command: {}".format(text))

        return command


class CommandParserError(Exception):
    pass

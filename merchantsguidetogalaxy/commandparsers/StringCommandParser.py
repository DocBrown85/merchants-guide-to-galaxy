import re

from .ICommandParser import ICommandParser, ICommandParserError

from .. import commands


class StringCommandParser(ICommandParser):
    def __init__(self):
        self._availableCommands = {
            "^(\S*) means (\S*)$": self._buildCommandSetIntergalacticDigitToRomanDigitTranslation,
            "^(.*) units of (\S*) are worth (\S*) credits$": self._buildCommandSetUnitsOfGoodsWorth,
            "^how much is (.*) \\?$": self._buildCommandTranslateFromIntergalacticNumeral,
            "^how many credits is (.*) (\S*) \\?$": self._buildCommandTranslateUnitsOfGoodWorth,
        }

    def parseCommand(self, text):
        text = text.lower().strip()

        for expectedCommandLine, commandBuilder in self._availableCommands.items():
            match = re.search(expectedCommandLine, text)
            if match:
                command = commandBuilder(match)
                return command

        raise StringCommandParserError("unknown command: {}".format(text))

    def _buildCommandSetIntergalacticDigitToRomanDigitTranslation(self, match):
        intergalacticDigit = match.group(1)
        romanDigit = match.group(2)

        command = commands.CommandSetIntergalacticDigitToRomanDigitTranslation(
            intergalacticDigit, romanDigit
        )

        return command

    def _buildCommandSetUnitsOfGoodsWorth(self, match):
        intergalacticUnits = match.group(1).split(" ")
        goodName = match.group(2)
        try:
            goodWorth = int(match.group(3))
        except Exception as e:
            raise StringCommandParserError(str(e))

        command = commands.CommandSetUnitsOfGoodsWorth(
            intergalacticUnits, goodName, goodWorth
        )

        return command

    def _buildCommandTranslateFromIntergalacticNumeral(self, match):
        intergalacticUnits = match.group(1).split(" ")
        command = commands.CommandTranslateFromIntergalacticNumeral(intergalacticUnits)
        return command

    def _buildCommandTranslateUnitsOfGoodWorth(self, match):
        intergalacticUnits = match.group(1).split(" ")
        goodName = match.group(2)
        command = commands.CommandTranslateUnitsOfGoodWorth(
            intergalacticUnits, goodName
        )
        return command


class StringCommandParserError(ICommandParserError):
    pass

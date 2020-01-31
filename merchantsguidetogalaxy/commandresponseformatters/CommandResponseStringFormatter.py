from ..commands.CommandSetIntergalacticDigitToRomanDigitTranslation import (
    SetIntergalacticDigitToRomanDigitTranslationCommandResponse,
)
from ..commands.CommandSetUnitsOfGoodsWorth import SetUnitsOfGoodsWorthCommandResponse
from ..commands.CommandTranslateFromIntergalacticNumeral import (
    TranslateFromIntergalacticNumeralCommandResponse,
)
from ..commands.CommandTranslateUnitsOfGoodWorth import (
    TranslateUnitsOfGoodWorthCommandResponse,
)

from .SetIntergalacticDigitToRomanDigitTranslationCommandResponseStringFormatter import (
    SetIntergalacticDigitToRomanDigitTranslationCommandResponseStringFormatter,
)
from .SetUnitsOfGoodsWorthCommandResponseStringFormatter import (
    SetUnitsOfGoodsWorthCommandResponseStringFormatter,
)
from .TranslateFromIntergalacticNumeralCommandResponseStringFormatter import (
    TranslateFromIntergalacticNumeralCommandResponseStringFormatter,
)
from .TranslateUnitsOfGoodWorthCommandResponseStringFormatter import (
    TranslateUnitsOfGoodWorthCommandResponseStringFormatter,
)


class CommandResponseStringFormatter:
    def __init__(self):
        self._commandResponseStringFormattersRegistry = {
            SetIntergalacticDigitToRomanDigitTranslationCommandResponse: SetIntergalacticDigitToRomanDigitTranslationCommandResponseStringFormatter,
            SetUnitsOfGoodsWorthCommandResponse: SetUnitsOfGoodsWorthCommandResponseStringFormatter,
            TranslateFromIntergalacticNumeralCommandResponse: TranslateFromIntergalacticNumeralCommandResponseStringFormatter,
            TranslateUnitsOfGoodWorthCommandResponse: TranslateUnitsOfGoodWorthCommandResponseStringFormatter,
        }

    def format(self, commandResponse):
        for (
            supportedCommandResponseType,
            commandResponseStringFormatter,
        ) in self._commandResponseStringFormattersRegistry.items():
            if isinstance(commandResponse, supportedCommandResponseType):
                formatter = self._commandResponseStringFormattersRegistry[
                    supportedCommandResponseType
                ]()
                return formatter.format(commandResponse)

        raise CommandResponseStringFormatterError(
            "unknown command response: {}".format(str(commandResponse))
        )


class CommandResponseStringFormatterError(Exception):
    pass

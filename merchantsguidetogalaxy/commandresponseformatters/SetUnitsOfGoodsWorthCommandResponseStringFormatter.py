from .ICommandResponseFormatter import ICommandResponseFormatter


class SetUnitsOfGoodsWorthCommandResponseStringFormatter(ICommandResponseFormatter):
    def format(self, setUnitsOfGoodsWorthCommandResponse):
        return setUnitsOfGoodsWorthCommandResponse._response

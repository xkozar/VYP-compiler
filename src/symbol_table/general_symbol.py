from enum import Enum


class SymbolType(Enum):
    CLASS = 1
    FUNCTION = 2
    VARIABLE = 3
    LITERAL = 4


class GeneralSymbol:

    def __init__(self, identifier: str, symbolType: SymbolType, dataType, line="", column=""):
        self.id = identifier
        self.symbolType = symbolType
        # For function, data type is it's return type
        self.dataType = dataType
        self.isDefined = False
        if line != '':
            self.codeName = f"{line}:{column}:{self.id}"
        else:
            self.codeName = self.id

    def setAsDefined(self):
        self.isDefined = True

    def __eq__(self, other):
        if not isinstance(other, GeneralSymbol):
            return False
        return self.dataType == other.dataType

    def __str__(self):
        return f'Symbol(id: {self.id}, type: {self.symbolType}, dataType: {self.dataType.id or self.dataType}'

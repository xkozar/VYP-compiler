from enum import Enum

class SymbolType(Enum):
    CLASS = 1
    FUNCTION = 2
    VARIABLE = 3

class GeneralSymbol:
    
    def __init__(self, symbolType:SymbolType, ID:str):
        self.symbolType = symbolType
        self.ID = ID
        self.dataType = None
        self.returnDataType = None

    def setDataType(self, dataType):
        self.dataType = dataType

    def setReturnDataType(self, returnDataType):
        self.returnDataType = returnDataType

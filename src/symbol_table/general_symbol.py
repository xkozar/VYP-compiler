from enum import Enum

class SymbolType(Enum):
    CLASS = 1
    FUNCTION = 2
    VARIABLE = 3
    LITERAL = 4

class GeneralSymbol:
    
    def __init__(self, id:str, symbolType:SymbolType, dataType):
        self.id = id
        self.symbolType = symbolType
        self.dataType = dataType
        self.returnDataType = None
        self.isDefined = False

    def setDataType(self, dataType):
        self.dataType = dataType

    def setReturnDataType(self, returnDataType):
        self.returnDataType = returnDataType
    
    def setAsDefined(self):
        self.isDefined = True

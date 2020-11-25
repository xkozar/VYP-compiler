from enum import Enum

class SymbolType(Enum):
    CLASS = 1
    FUNCTION = 2
    VARIABLE = 3
    LITERAL = 4

class GeneralSymbol:
    
    def __init__(self, identifier:str, symbolType:SymbolType, dataType):
        self.id = identifier
        self.symbolType = symbolType
        # For function, data type is it's return type
        self.dataType = dataType
        self.isDefined = False
    
    def setAsDefined(self):
        self.isDefined = True

    def __str__(self):
        return f'Symbol(id: {self.id}, type: {self.symbolType}, dataType: {self.dataType}'

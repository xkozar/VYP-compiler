from symbol_table import GeneralSymbol, SymbolType, PartialSymbolTable, PartialClassSymbolTable
from symbol_table.class_partial_symbol_table import ClassPartialSymbolTable

class ClassSymbol(GeneralSymbol):

    # This constructor is only for special behaviour of Object class
    def __init__(self, identifier, parent, parentClosure=ClassPartialSymbolTable()):
        super().__init__(identifier, SymbolType.CLASS, identifier)
        self.parent = parent
        self.methodTable = PartialClassSymbolTable()
        self.fieldTable = PartialClassSymbolTable()

    def getMethod(self, key):
        return self.symbols.get(key) or self.parent.getSymbol(key)

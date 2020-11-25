from symbol_table import GeneralSymbol, SymbolType, PartialSymbolTable
from symbol_table.class_partial_symbol_table import ClassPartialSymbolTable

class ClassSymbol(GeneralSymbol):
    # This constructor should be used by default
    def __int__(self, identifier, parent):
        self.__init__(identifier, parent, ClassPartialSymbolTable())

    # This constructor is only for special behaviour of Object class
    def __init__(self, identifier, parent, parentClosure):
        super().__init__(identifier, SymbolType.CLASS, identifier)
        self.parent = parent
        self.methodTable = PartialSymbolTable(parentClosure)
        self.fieldTable = PartialSymbolTable(parentClosure)

    def getMethod(self, key):
        return self.symbols.get(key) or self.parent.getSymbol(key)

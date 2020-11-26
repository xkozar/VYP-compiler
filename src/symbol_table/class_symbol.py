from symbol_table import GeneralSymbol, SymbolType, PartialSymbolTable, PartialClassSymbolTable
from symbol_table.class_partial_symbol_table import ClassPartialSymbolTable
from compiler.custom_exceptions import SemanticGeneralError


class ClassSymbol(GeneralSymbol):

    # This constructor is only for special behaviour of Object class
    def __init__(self, identifier, parent, parentClosure=ClassPartialSymbolTable()):
        super().__init__(identifier, SymbolType.CLASS, identifier)
        self.parent = parent
        self.methodTable = PartialClassSymbolTable()
        self.fieldTable = PartialClassSymbolTable()

    def getMethod(self, key):
        return self.methodTable.getSymbol(key) or self.parent.getMethod(key)

    def getField(self, key):
        return self.fieldTable.getSymbol(key) or self.parent.getField(key)

    def defineField(self, variableSymbol: GeneralSymbol):
        if self.getField(variableSymbol.id):
            raise SemanticGeneralError(f"Redefinition of field \'{variableSymbol.id}\' in class \'{self.id}\'")
        self.fieldTable.addSymbol(variableSymbol.id, variableSymbol)


class StubParentSymbol:

    def getMethod(self, key):
        return None

    def getField(self, key):
        return None

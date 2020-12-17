from compiler import SemanticGeneralError
from symbol_table.class_partial_symbol_table import ClassPartialSymbolTable


class PartialSymbolTable:

    def __init__(self, parentClosure):
        self.symbols = {}
        self.__parentClosure = parentClosure

    def getSymbol(self, key: str):
        return self.symbols.get(key) or self.__parentClosure.getSymbol(key)

    def isSymbolDefined(self, key):
        if self.symbols.get(key):
            return True
        else:
            return self.__parentClosure.isSymbolDefined(key)

    def addSymbol(self, key, symbol):
        if self.isSymbolDefined(key):
            raise SemanticGeneralError(f'Symbol with id:\'{key}\' is already defined')
        self.symbols.update({key: symbol})

    def getParentClosure(self):
        return self.__parentClosure.getClosure()

    def getClosure(self):
        return self

    def containsKey(self, key):
        return key in self.symbols

    def getAllCurrentSymbols(self):
        return list(self.symbols.values())

    def getAllCurrentSymbolsAsDict(self):
        return self.symbols.copy()

    def getAllSymbols(self):
        return self.getAllCurrentSymbols() + self.__parentClosure.getAllSymbols()


    def __str__(self):
        return f'{{ \n {self.__parentClosure.__str__()} \n\t {self.symbols.keys()} \n }}'


class PartialClassSymbolTable(PartialSymbolTable):

    def __init__(self):
        super().__init__(ClassPartialSymbolTable())

    def addSymbol(self, key, symbol):
        if self.symbols.get(key):
            raise SemanticGeneralError(f'Symbol with id:\'{key}\' is already defined in this class')
        self.symbols.update({key: symbol})

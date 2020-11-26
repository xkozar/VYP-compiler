from .partial_symbol_table import PartialSymbolTable
from .static_partial_symbol_table import StaticPartialSymbolTable
from .general_symbol import GeneralSymbol

class SymbolTable:

    def __init__(self):
        self.currentSymbolClosure = None
        self.resetToDefaultState()

    def getSymbol(self, key) -> GeneralSymbol:
        return self.currentSymbolClosure.getSymbol(key)

    def isSymbolDefined(self, key):
        return self.currentSymbolClosure.isSymbolDefined(key)

    def addSymbol(self, key, symbol):
        self.currentSymbolClosure.addSymbol(key, symbol)
        return symbol

    def addClosure(self):
        self.currentSymbolClosure = PartialSymbolTable(self.currentSymbolClosure)

    def removeClosure(self):
        self.currentSymbolClosure = self.currentSymbolClosure.getParentClosure()

    def resetToDefaultState(self):
        self.currentSymbolClosure = PartialSymbolTable(StaticPartialSymbolTable())

    def setAsDefined(self, key):
        self.currentSymbolClosure.getSymbol(key).setAsDefined()

    def getAllSymbols(self):
        return self.currentSymbolClosure.getAllSymbols()

    def __str__(self):
        return self.currentSymbolClosure.__str__()
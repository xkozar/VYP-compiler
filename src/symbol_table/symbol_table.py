from .partial_symbol_table import PartialSymbolTable
from .static_partial_symbol_table import StaticPartialSymbolTable
from .general_symbol import GeneralSymbol

class SymbolTable:

    def __init__(self):
        self.resetToDefaultState()

    def findSymbolByKey(self, key) -> GeneralSymbol:
        return self.currentSymbolClosure.getSymbol(key)

    def addSymbol(self, key, symbol):
        self.currentSymbolClosure.setSymbol(key, symbol)

    def addClosure(self):
        self.currentSymbolClosure = PartialSymbolTable(self.currentSymbolClosure)

    def removeClosure(self):
        self.currentSymbolClosure = self.currentSymbolClosure.getParentClosure()

    def resetToDefaultState(self):
        self.currentSymbolClosure = PartialSymbolTable(StaticPartialSymbolTable())

    def __str__(self):
        return self.currentSymbolClosure.__str__()
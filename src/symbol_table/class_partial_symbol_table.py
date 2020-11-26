from compiler import SemanticGeneralError
from symbol_table.static_partial_symbol_table import StaticPartialSymbolTable

class ClassPartialSymbolTable(StaticPartialSymbolTable):

    def getSymbol(self, key):
        return None

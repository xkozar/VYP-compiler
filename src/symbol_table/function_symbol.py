'''
    project: VYPlanguage compiler
    authros: Tomáš Kožár, xkozar02
'''

from symbol_table.general_symbol import GeneralSymbol, SymbolType
import functools


class FunctionSymbol(GeneralSymbol):

    def __init__(self, identifier, dataType, ownerClass=""):
        super().__init__(identifier, SymbolType.FUNCTION, dataType)
        self.parameterList = FunctionCallSignature()
        self.codeGenerator: FunctionCodeGenerator = None
        self.ownerClass = ownerClass

    def appendParameter(self, symbol):
        self.parameterList.appendParameter(symbol)

    def __eq__(self, other):
        if not isinstance(other, FunctionSymbol):
            return False
        return self.id == other.id and self.parameterList == other.parameterList


class FunctionCallSignature:

    def __init__(self):
        self.parameters = []

    def appendParameter(self, parameterSymbol):
        self.parameters.append(parameterSymbol)

    def __eq__(self, other):
        if not isinstance(other, FunctionCallSignature):
            return False
        return all(map(lambda x, y: x == y, zip(self.parameters, other.parameters)))

    def __len__(self):
        return len(self.parameters)

    def __str__(self):
        return '[' + functools.reduce(lambda x, y: str(x) + ', ' + str(y), self.parameters) + ']'


from symbol_table.general_symbol import GeneralSymbol, SymbolType
import functools


class FunctionSymbol(GeneralSymbol):

    def __init__(self, identifier, dataType):
        super().__init__(identifier, SymbolType.FUNCTION, dataType)
        self.parameterList = FunctionCallSignature()

    def appendParameter(self, symbol):
        self.parameterList.appendParameter(symbol)


class FunctionCallSignature:

    def __init__(self):
        self.parameters = []

    def appendParameter(self, parameterSymbol):
        self.parameters.append(parameterSymbol)

    def __eq__(self, other):
        return all(map(lambda x, y: x.dataType == y.dataType))

    def __len__(self):
        return len(self.parameters)

    def __str__(self):
        return '[' + functools.reduce(lambda x, y: str(x) + ', ' + str(y), self.parameters) + ']'

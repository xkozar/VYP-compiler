from antlr_generated.VYPListener import VYPListener
from antlr_generated.VYPParser import VYPParser
from symbol_table import GeneralSymbol, SymbolTable, SymbolType, FunctionSymbol, FunctionCallSignature


class DefinitionsTreeListener(VYPListener):

    def __init__(self):
        self.functionTable = SymbolTable()
        self.preemptiveFunctionCallTable = SymbolTable()
        self.functionParametersDict = {}
        self.currentFunctionId = ''
        self.__defineBuiltInFunctions()

    def getFunctionTable(self):
        return self.functionTable

    def __defineBuiltInFunctions(self):
        # TODO add parameters
        self.defineFunction('print', 'void')

        self.defineFunction('readInt', 'int')

        self.defineFunction('readString', 'void')

        self.defineFunction('length', 'int')

        self.defineFunction('subStr', 'string')

    def defineFunction(self, identifier, dataType):
        definitionSymbol = FunctionSymbol(identifier, dataType)
        self.functionTable.addSymbol(identifier, definitionSymbol)
        self.currentFunctionId = identifier

    ''' Enter function symbol to global function definitions '''
    def enterFunction_header(self, ctx: VYPParser.Function_headerContext):
        self.defineFunction(ctx.ID().getText(), ctx.variable_type().getText())

    ''' Function parameters need to be inserted into symbol table. If 'void' is 
        used as parameter, no action is needed. This rule is not used anywhere
        else, so this rule is entered only during function definition. '''
    def enterFunction_parameter_definition(self, ctx: VYPParser.Function_parametersContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, ctx.variable_type().getText())
        definitionSymbol.setAsDefined()
        self.defineFunctionParameter(definitionSymbol)


    def initializeFunctionSymbolTable(self, identifier):
        self.currentFunctionId = identifier

    def defineFunctionParameter(self, symbol: GeneralSymbol):
        self.functionTable.findSymbolByKey(self.currentFunctionId).appendParameter(symbol)
        pass

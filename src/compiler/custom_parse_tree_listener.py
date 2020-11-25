from antlr_generated.VYPListener import VYPListener
from antlr_generated.VYPParser import VYPParser
from symbol_table import GeneralSymbol, SymbolTable, SymbolType, FunctionSymbol, FunctionCallSignature


class CustomParseTreeListener(VYPListener):
    
    def __init__(self, functionDefinitionTable):
        self.localSymbolTable = SymbolTable()
        self.functionTable = functionDefinitionTable
        self.preemptiveFunctionCallTable = SymbolTable()
        self.functionParametersDict = {}
        self.currentFunctionId = ''

    ''' Reset symbol table since symbol table is valid only inside of function/method
        definition'''
    def exitFunction_definition(self, ctx:VYPParser.Function_definitionContext):
        self.localSymbolTable.resetToDefaultState()

    def enterFunction_header(self, ctx:VYPParser.Function_headerContext):
        self.currentFunctionId= ctx.ID().getText()

    ''' Function parameters need to be inserted into symbol table. If 'void' is 
        used as parameter, no action is needed. This rule is not used anywhere
        else, so this rule is entered only during function definition. '''
    def enterFunction_parameter_definition(self, ctx:VYPParser.Function_parametersContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, ctx.variable_type().getText())
        definitionSymbol.setAsDefined()
        self.defineFunctionParameter(definitionSymbol)

    def enterVariable_definition(self, ctx:VYPParser.Variable_definitionContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, ctx.variable_type().getText())
        self.localSymbolTable.addSymbol(ctx.ID().getText(), definitionSymbol)
        print("local symbol table", self.localSymbolTable)

    ''' Data type of variable must be taken from parent context'''
    def enterMultiple_variable_definition(self, ctx:VYPParser.Multiple_variable_definitionContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, ctx.parentCtx.variable_type().getText())
        self.localSymbolTable.addSymbol(ctx.ID().getText(), definitionSymbol)
        pass

    def enterCode_block(self, ctx:VYPParser.Code_blockContext):
        self.localSymbolTable.addClosure()

    def exitCode_block(self, ctx:VYPParser.Code_blockContext):
        self.localSymbolTable.removeClosure()
        pass

    def enterVariable_assignment(self, ctx:VYPParser.Variable_assignmentContext):
        symbol = self.localSymbolTable.findSymbolByKey(ctx.ID().getText())
        symbol.setAsDefined()

    def defineFunctionParameter(self, symbol: GeneralSymbol):
        self.localSymbolTable.addSymbol(symbol.id, symbol)

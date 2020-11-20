from antlr_generated.VYPListener import VYPListener
from antlr_generated.VYPParser import VYPParser
from symbol_table import *

class CustomParseTreeListener(VYPListener):
    
    def __init__(self): 
        self.localSymbolTable = SymbolTable()
        self.globalDefinitionTable = SymbolTable()

    def enterProgram(self, ctx:VYPParser.ProgramContext):
        pass

    def exitProgram(self, ctx:VYPParser.ProgramContext):
        pass

    def enterFunction_definition(self, ctx:VYPParser.Function_definitionContext):
        pass

    ''' Reset symbol table since symbol table is valid only inside of function/methon
        definition'''
    def exitFunction_definition(self, ctx:VYPParser.Function_definitionContext):
        self.localSymbolTable.resetToDefaultState()

    ''' Enter function symbol to global definitions '''
    def enterFunction_header(self, ctx:VYPParser.Function_headerContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.FUNCTION, None)
        self.globalDefinitionTable.addSymbol(ctx.ID().getText(), definitionSymbol)

    def exitFunction_header(self, ctx:VYPParser.Function_headerContext):
        pass

    ''' Function parameters need to be inserted into symbol table. If 'void' is 
        used as parameter, no action is needed. This rule is not used anywhere
        else, so this rule is entered only during function definition. '''
    def enterFunction_parameter_definition(self, ctx:VYPParser.Function_parametersContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, ctx.variable_type().getText())
        self.localSymbolTable.addSymbol(ctx.ID().getText(), definitionSymbol)

    def exitFunction_parameter_definition(self, ctx:VYPParser.Function_parametersContext):
        pass

    def enterVariable_definition(self, ctx:VYPParser.Variable_definitionContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, ctx.variable_type().getText())
        self.localSymbolTable.addSymbol(ctx.ID().getText(), definitionSymbol)
        print(self.localSymbolTable)
        pass

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

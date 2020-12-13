from collections import deque

from antlr_generated.VYPListener import VYPListener
from antlr_generated.VYPParser import VYPParser
from compiler.semantics_checker import SemanticsChecker
from symbol_table import GeneralSymbol, SymbolTable, SymbolType, FunctionSymbol, FunctionCallSignature
from code_generator import CodeGenerator


class CustomParseTreeListener(VYPListener):

    def __init__(self, functionDefinitionTable, classTable):
        self.localSymbolTable = SymbolTable()
        self.functionTable: SymbolTable() = functionDefinitionTable
        self.preemptiveFunctionCallTable = SymbolTable()
        self.semanticsChecker = SemanticsChecker()
        self.codeGenerator = CodeGenerator()
        self.expressionStack = deque()
        self.functionParametersDict = {}
        self.currentFunctionId = ''
        self.classTable = classTable
        self.checkClassDefinitionsSemantics()
        self.currentClass = None

    ''' Reset symbol table since symbol table is valid only inside of function/method
        definition'''

    def exitFunction_definition(self, ctx: VYPParser.Function_definitionContext):
        if self.currentClass is None:
            self.localSymbolTable.resetToDefaultState()

    def enterFunction_header(self, ctx: VYPParser.Function_headerContext):
        self.currentFunctionId = ctx.ID().getText()
        functionParameterNames = list(map(lambda x: x.id, self.functionTable.getSymbol(ctx.ID().getText()).parameterList.parameters))
        self.codeGenerator.generateFunctionHeader(self.currentFunctionId, functionParameterNames)

    ''' Function parameters need to be inserted into symbol table. If 'void' is 
        used as parameter, no action is needed. This rule is not used anywhere
        else, so this rule is entered only during function definition. '''

    def enterFunction_parameter_definition(self, ctx: VYPParser.Function_parametersContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, ctx.variable_type().getText())
        definitionSymbol.setAsDefined()
        self.defineFunctionParameter(definitionSymbol)

    def enterVariable_definition(self, ctx: VYPParser.Variable_definitionContext):
        variableType = ctx.variable_type().getText() if ctx.variable_type().getText() in ['int',
                                                                                          'string'] else self.classTable.getSymbol(
            ctx.variable_type().getText())
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE, variableType)
        self.localSymbolTable.addSymbol(ctx.ID().getText(), definitionSymbol)
        self.codeGenerator.defineVariable(definitionSymbol.id, self.currentFunctionId)

    ''' Data type of variable must be taken from parent context'''

    def enterMultiple_variable_definition(self, ctx: VYPParser.Multiple_variable_definitionContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE,
                                         ctx.parentCtx.variable_type().getText())
        self.localSymbolTable.addSymbol(ctx.ID().getText(), definitionSymbol)
        self.codeGenerator.defineVariable(definitionSymbol.id, self.currentFunctionId)

    def enterCode_block(self, ctx: VYPParser.Code_blockContext):
        self.localSymbolTable.addClosure()

    def exitCode_block(self, ctx: VYPParser.Code_blockContext):
        self.localSymbolTable.removeClosure()

    def enterVariable_assignment(self, ctx: VYPParser.Variable_assignmentContext):
        symbol = self.localSymbolTable.getSymbol(ctx.ID().getText())
        symbol.setAsDefined()

    def exitVariable_assignment(self, ctx: VYPParser.Variable_assignmentContext):
        symbol = self.localSymbolTable.getSymbol(ctx.ID().getText())
        expression = self.expressionStack.pop()
        self.semanticsChecker.checkVariableAssignment(symbol.dataType, expression.dataType)

    def enterStatement(self, ctx: VYPParser.StatementContext):
        self.expressionStack.clear()

    def enterClass_definition(self, ctx: VYPParser.Class_definitionContext):
        self.currentClass = self.classTable.getSymbol(ctx.class_header().class_id.text)
        self.localSymbolTable = self.currentClass.fieldTable

    def exitClass_definition(self, ctx: VYPParser.Class_definitionContext):
        self.currentClass = None
        self.localSymbolTable = SymbolTable()

    def defineFunctionParameter(self, symbol: GeneralSymbol):
        self.localSymbolTable.addSymbol(symbol.id, symbol)

    def checkClassDefinitionsSemantics(self):
        self.semanticsChecker.checkMethodOverrideTypes(self.classTable)

    def exitProgram(self, ctx:VYPParser.ProgramContext):
        self.codeGenerator.generateCode()

from collections import deque

from antlr_generated.VYPListener import VYPListener
from antlr_generated.VYPParser import VYPParser
from compiler.semantics_checker import SemanticsChecker
from compiler.custom_exceptions import SemanticGeneralError, SemanticTypeIncompatibilityError
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
        self.currentFunction = None
        self.classTable = classTable
        self.checkClassDefinitionsSemantics()
        self.currentClass = None
        self.currentFunctionReturn = False

    ''' Reset symbol table since symbol table is valid only inside of function/method
        definition'''

    def exitFunction_definition(self, ctx: VYPParser.Function_definitionContext):
        if self.currentClass is None:
            self.localSymbolTable.resetToDefaultState()

    def enterFunction_header(self, ctx: VYPParser.Function_headerContext):
        self.currentFunctionId = ctx.ID().getText()

        if self.currentClass == None:
            self.currentFunction = self.functionTable.getSymbol(self.currentFunctionId)
            functionParameterNames = list(map(lambda x: x.id, self.functionTable.getSymbol(ctx.ID().getText()).parameterList.parameters))
        else:
            self.currentFunction = self.currentClass.methodTable.getSymbol(self.currentFunctionId)
            functionParameterNames = list(map(lambda x: x.id, self.currentClass.methodTable.getSymbol(ctx.ID().getText()).parameterList.parameters))

        self.codeGenerator.generateFunctionHeader(self.currentFunction, functionParameterNames)

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
        if self.functionTable.isSymbolDefined(ctx.ID().getText()) or self.classTable.isSymbolDefined(ctx.ID().getText()):
            raise SemanticGeneralError(f"Symbol with id: {ctx.ID().getText()} is already defined")
        self.codeGenerator.defineVariable(definitionSymbol.id, self.currentFunction, variableType)

    ''' Data type of variable must be taken from parent context'''

    def enterMultiple_variable_definition(self, ctx: VYPParser.Multiple_variable_definitionContext):
        definitionSymbol = GeneralSymbol(ctx.ID().getText(), SymbolType.VARIABLE,
                                         ctx.parentCtx.variable_type().getText())
        self.localSymbolTable.addSymbol(ctx.ID().getText(), definitionSymbol)
        if self.functionTable.isSymbolDefined(ctx.ID().getText()) or self.classTable.isSymbolDefined(ctx.ID().getText()):
            raise SemanticGeneralError(f"Symbol with id: {ctx.ID().getText()} is already defined")
        self.codeGenerator.defineVariable(definitionSymbol.id, self.currentFunction, definitionSymbol.dataType)

    def enterField_definition(self, ctx:VYPParser.Field_definitionContext):
        if self.currentClass.methodTable.isSymbolDefined(ctx.ID().getText()):
            raise SemanticGeneralError(f"There is already method with id: {ctx.ID().getText()} defined")

    def enterMultiple_field_definition(self, ctx:VYPParser.Multiple_field_definitionContext):
        if self.currentClass.methodTable.isSymbolDefined(ctx.ID().getText()):
            raise SemanticGeneralError(f"There is already method with id: {ctx.ID().getText()} defined")

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
        self.codeGenerator.assignValueToVariable(self.currentFunction, ctx.ID().getText())


    def enterStatement(self, ctx: VYPParser.StatementContext):
        self.expressionStack.clear()
        pass

    def enterClass_definition(self, ctx: VYPParser.Class_definitionContext):
        self.currentClass = self.classTable.getSymbol(ctx.class_header().class_id.text)
        self.localSymbolTable = self.currentClass.fieldTable

    def exitClass_definition(self, ctx: VYPParser.Class_definitionContext):
        self.currentClass = None
        self.localSymbolTable = SymbolTable()

    def enterMethod_definition(self, ctx: VYPParser.Method_definitionContext):
        self.localSymbolTable = SymbolTable()

    def defineFunctionParameter(self, symbol: GeneralSymbol):
        self.localSymbolTable.addSymbol(symbol.id, symbol)

    def checkClassDefinitionsSemantics(self):
        self.semanticsChecker.checkMethodOverrideTypes(self.classTable)

    def enterProgram(self, ctx:VYPParser.ProgramContext):
        self.generateMethodVirtualTables()

    def exitProgram(self, ctx:VYPParser.ProgramContext):
        
        self.codeGenerator.generateCode()

    def exitFunction_body(self, ctx:VYPParser.Function_bodyContext):
        if self.currentClass == None:
            currentFunction = self.functionTable.getSymbol(self.currentFunctionId)
        else:
            currentFunction = self.currentClass.methodTable.getSymbol(self.currentFunctionId)

        if currentFunction.dataType != 'void':
            if self.currentFunctionReturn == False:
                pass
                #raise SemanticGeneralError("No return value specified")
        self.currentFunctionReturn = False
        setReturnValue = currentFunction.dataType != 'void'

        if setReturnValue:
            if currentFunction.dataType == 'string':
                self.codeGenerator.generateLiteralExpression(self.currentFunction, '""', 'string')
            else:
                self.codeGenerator.generateLiteralExpression(self.currentFunction, 0, 'int')
        if self.currentFunctionId != 'main':
            self.codeGenerator.generateReturnValue(self.currentFunction, setReturnValue)
        else:
            self.codeGenerator.returnFromFunction(self.currentFunction)

    def exitIf_part(self, ctx:VYPParser.If_partContext):
        self.codeGenerator.generateIfEnd(self.currentFunction, ctx.start.line, ctx.start.column)

    def exitElse_part(self, ctx:VYPParser.Else_partContext):
        self.codeGenerator.generateElseEnd(self.currentFunction, ctx.parentCtx.start.line, ctx.parentCtx.start.column)

    def enterWhile_block(self, ctx:VYPParser.While_blockContext):
        self.codeGenerator.generateWhileStart(self.currentFunction, ctx.start.line, ctx.start.column)

    def exitWhile_block(self, ctx:VYPParser.While_blockContext):
        self.codeGenerator.generateWhileEnd(self.currentFunction, ctx.start.line, ctx.start.column)

    def exitWhile_expression(self, ctx:VYPParser.While_expressionContext):
        expression = self.expressionStack.pop()
        if expression.dataType != 'int':
            raise SemanticTypeIncompatibilityError(f"WHILE expected data type 'int', got '{expression.dataType}' instead.")
        self.codeGenerator.generateEvaluateWhile(self.currentFunction, ctx.parentCtx.start.line, ctx.parentCtx.start.column)

    def exitIf_expression(self, ctx:VYPParser.If_expressionContext):
        expression = self.expressionStack.pop()
        if expression.dataType != 'int':
            raise SemanticTypeIncompatibilityError(f"IF expected data type 'int', got '{expression.dataType}' instead.")
        self.codeGenerator.generateIfStart(self.currentFunction, ctx.start.line, ctx.start.column)

    def generateMethodVirtualTables(self):
        for classSymbol in self.classTable.getAllSymbols():
            allMethods = classSymbol.getAllAvailableMethods()
            self.codeGenerator.generateVirtualMethodTable(classSymbol.id, allMethods)
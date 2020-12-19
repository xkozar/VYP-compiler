from antlr_generated.VYPListener import VYPListener
from antlr_generated.VYPParser import VYPParser
from symbol_table import GeneralSymbol, SymbolTable, SymbolType, FunctionSymbol, ClassSymbol, StaticPartialSymbolTable, StubParentSymbol
from compiler.custom_exceptions import SemanticGeneralError

class DefinitionsTreeListener(VYPListener):

    def __init__(self):
        self.functionTable = SymbolTable()
        self.classTable = SymbolTable()
        self.currentFunctionId = ''
        self.currentClass: ClassSymbol = None
        # can be function table or method table of current class
        self.currentFunctionTable = self.functionTable
        self.__defineBuiltInFunctions()
        self.__defineBuiltInClasses()

    def getFunctionTable(self):
        return self.functionTable

    def getClassTable(self):
        return self.classTable

    def __defineBuiltInClasses(self):

        objectSymbol = ClassSymbol('Object', StubParentSymbol(), StaticPartialSymbolTable())
        toStringSymbol = FunctionSymbol('toString', 'string', 'Object')
        getClassSymbol = FunctionSymbol('getClass', 'string', 'Object')
        objectSymbol.methodTable.addSymbol('toString', toStringSymbol)
        objectSymbol.methodTable.addSymbol('getClass', getClassSymbol)
        self.classTable.addSymbol('Object', objectSymbol)

    def defineMethod(self, identifier, dataType):
        definitionSymbol = FunctionSymbol(identifier, dataType, self.currentClass.id)
        self.functionTable.addSymbol(identifier, definitionSymbol)
        self.currentFunctionId = identifier

    def __defineBuiltInFunctions(self):
        # TODO add parameters
        self.defineFunction('print', 'void')

        self.defineFunction('readInt', 'int')

        self.defineFunction('readString', 'string')

        functionSymbol = self.defineFunction('length', 'int')
        definitionSymbol = GeneralSymbol('s', SymbolType.VARIABLE, 'string')
        definitionSymbol.setAsDefined()
        functionSymbol.appendParameter(definitionSymbol)

        functionSymbol = self.defineFunction('subStr', 'string')
        definitionSymbol = GeneralSymbol('s', SymbolType.VARIABLE, 'string')
        definitionSymbol.setAsDefined()
        functionSymbol.appendParameter(definitionSymbol)

        definitionSymbol = GeneralSymbol('i', SymbolType.VARIABLE, 'int')
        definitionSymbol.setAsDefined()
        functionSymbol.appendParameter(definitionSymbol)

        definitionSymbol = GeneralSymbol('n', SymbolType.VARIABLE, 'int')
        definitionSymbol.setAsDefined()
        functionSymbol.appendParameter(definitionSymbol)

    def defineFunction(self, identifier, dataType):
        ownerClass = ""
        if self.currentClass is not None:
            ownerClass = self.currentClass.id
        definitionSymbol = FunctionSymbol(identifier, dataType, ownerClass)
        self.currentFunctionTable.addSymbol(identifier, definitionSymbol)
        self.currentFunctionId = identifier
        return definitionSymbol

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

    def enterClass_header(self, ctx: VYPParser.Class_headerContext):
        parentClass = self.classTable.getSymbol(ctx.parent_id.text)
        self.defineClass(ctx.class_id.text, parentClass)

    def exitClass_body(self, ctx: VYPParser.Class_bodyContext):
        self.currentClass = None
        self.localSymbolTable = SymbolTable()

    def exitClass_definition(self, ctx: VYPParser.Class_definitionContext):
        self.currentFunctionTable = self.functionTable

    def enterField_definition(self, ctx: VYPParser.Field_definitionContext):
        self.defineField(ctx.ID().getText(), ctx.variable_type().getText())

    def enterMultiple_field_definition(self, ctx: VYPParser.Multiple_field_definitionContext):
        self.defineField(ctx.ID().getText(), ctx.parentCtx.variable_type().getText())

    def exitProgram(self, ctx):
        mainSymbol = self.functionTable.getSymbol('main')
        if mainSymbol.dataType != 'void' or len(mainSymbol.parameterList) != 0:
            raise SemanticGeneralError("Wrong definition of 'main' function")
        self.updateFunctionTypes()

    def defineField(self, fieldId, dataType):
        fieldSymbol = GeneralSymbol(fieldId, SymbolType.VARIABLE, dataType)
        self.currentClass.defineField(fieldSymbol)

    def defineClass(self, classId, parentId):
        classSymbol = ClassSymbol(classId, parentId)
        self.classTable.addSymbol(classId, classSymbol)
        self.currentClass = classSymbol
        self.currentFunctionTable = classSymbol.methodTable

    def initializeFunctionSymbolTable(self, identifier):
        self.currentFunctionId = identifier

    def defineFunctionParameter(self, symbol: GeneralSymbol):
        self.currentFunctionTable.getSymbol(self.currentFunctionId).appendParameter(symbol)

    def updateFunctionTypes(self):
        self.updateFuntionTypesHelper(self.functionTable.getAllSymbols())
        for classSymbol in self.classTable.getAllSymbols():
            self.updateFuntionTypesHelper(classSymbol.methodTable.getAllCurrentSymbols())
            classSymbol.dataType = self.classTable.getSymbol(classSymbol.dataType)
        self.checkMethorOverriding()

    def checkMethorOverriding(self):
        for classSymbol in self.classTable.getAllSymbols():
            for methodSymbol in classSymbol.methodTable.getAllCurrentSymbols():
                pass

    def updateFuntionTypesHelper(self, functionList):
        for function in functionList:
            if function.ownerClass == function.id:
                if function.dataType != 'void' or len(function.parameterList) != 0:
                    raise SemanticGeneralError("Wrong constructor definition")
            if function.dataType not in ['int', 'void', 'string']:
                classSymbol = self.classTable.getSymbol(function.dataType)
                function.dataType = classSymbol
            self.updateFunctionParameterList(function.parameterList)

    def updateFunctionParameterList(self, parameterList):
        for parameter in parameterList.parameters:
            if parameter.dataType in ['int', 'void', 'string']:
                continue
            classSymbol = self.classTable.getSymbol(parameter.dataType)
            parameter.dataType = classSymbol


from antlr_generated.VYPParser import VYPParser
from compiler import CustomParseTreeListener
from compiler.semantics_checker import SemanticsChecker
from compiler.custom_exceptions import SemanticTypeIncompatibilityError

intResultOperators = ['<', '>', '<=', '>=', '==']

class BinaryExpression:

    def __init__(self, leftExpression, rightExpression, operator):
        if leftExpression.dataType == 'string' and operator in intResultOperators:
            self.dataType = 'int'
        else:
            self.dataType = leftExpression.dataType
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression
        self.operator = operator

    def __str__(self):
        return f'{self.leftExpression.__str__()} {self.operator} {self.rightExpression}'


class CastExpression:

    def __init__(self, expression, dataType):
        self.dataType = dataType
        self.expression = expression
        self.operator = f'({self.dataType})'

    def __str__(self):
        return f'{self.operator} {self.expression}'


class UnaryExpression:

    def __init__(self, expression, operator):
        self.dataType = expression.dataType
        self.expression = expression
        self.operator = operator

    def __str__(self):
        return f'{self.operator} {self.expression}'


class LiteralExpression:

    def __init__(self, dataType, value):
        self.dataType = dataType
        self.value = value

    def __str__(self):
        return f'{self.value}'

class ObjectExpression:

    def __init__(self, dataType):
        self.dataType = dataType

    def __str__(self):
        return f'Object: {self.dataType}'


class VariableExpression:

    def __init__(self, dataType, identifier):
        self.dataType = dataType
        self.id = identifier

    def __str__(self):
        return f'{self.id}'


class FunctionExpression:

    def __init__(self, identifier, dataType, callExpressions):
        self.id = identifier
        self.dataType = dataType
        self.callExpressions = callExpressions

    def __str__(self):
        stringExpressionsList = list(map(lambda expr: expr.__str__(), self.callExpressions[::-1]))
        return f'{self.id}({", ".join(stringExpressionsList).__str__()})'


class ExpressionListener(CustomParseTreeListener):

    def __init__(self, functionDefinitionTable, classTable):
        super().__init__(functionDefinitionTable, classTable)
        self.functionCallParametersList = []
        self.nestedObjectList = []

    def exitEquality_expression(self, ctx: VYPParser.Equality_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitMuldiv_expression(self, ctx: VYPParser.Muldiv_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitCastExpression(self, ctx: VYPParser.CastExpressionContext):
        castType = ctx.cast.text
        expressionType = castType if castType in ['int', 'string'] else self.classTable.getSymbol(castType).dataType
        expression = self.expressionStack.pop()
        if expressionType == 'string' and expression.dataType == 'int':
            self.codeGenerator.generateIntToStringCast(self.currentFunction)
        elif expressionType == 'int':
            raise SemanticTypeIncompatibilityError("Cannot cast to 'int'.")
        self.expressionStack.append(CastExpression(expression, expressionType))

    def exitFunction_expression(self, ctx: VYPParser.Function_expressionContext):
        functionId = ctx.function_call().ID().getText()
        functionSymbol = self.functionTable.getSymbol(functionId)
        self.semanticsChecker.checkFunctionCallSemantics(functionId, self.functionCallParametersList,
                                                         functionSymbol.parameterList.parameters)
        functionExpression = FunctionExpression(functionId, functionSymbol.dataType,
                                                self.functionCallParametersList.copy())
        self.expressionStack.append(functionExpression)
        if functionId != 'print':
            self.codeGenerator.callFunction(self.currentFunction, functionId)
        else:
            for parameter in self.functionCallParametersList:
                if parameter.dataType == 'int':
                    self.codeGenerator.callFunction(self.currentFunction, 'printi')
                else:
                    self.codeGenerator.callFunction(self.currentFunction, 'prints')

        self.functionCallParametersList = []

    def exitComparison_expression(self, ctx: VYPParser.Comparison_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitOr_expression(self, ctx: VYPParser.Or_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitVariable_expression(self, ctx: VYPParser.Variable_expressionContext):
        variableSymbol = self.localSymbolTable.getSymbol(ctx.ID().getText())
        variableExpression = VariableExpression(variableSymbol.dataType, variableSymbol.id)
        self.expressionStack.append(variableExpression)
        self.codeGenerator.generateVariableExpression(self.currentFunction, variableSymbol.id);

    def exitAnd_expression(self, ctx: VYPParser.And_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    '''Nothing needs to be done, rule is just used to get proper order of operations'''

    def exitBracket_expression(self, ctx: VYPParser.Bracket_expressionContext):
        pass

    def exitNegation_expression(self, ctx: VYPParser.Negation_expressionContext):
        self.processUnaryExpression('!')
        self.codeGenerator.generateNotExpression(self.currentFunction)

    def exitNegative_expression(self, ctx:VYPParser.Negative_expressionContext):
        self.processUnaryExpression('-')
        self.codeGenerator.generateUnaryMinusExpression(self.currentFunction)

    def exitPlusminus_expression(self, ctx: VYPParser.Plusminus_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitInstance_creation(self, ctx:VYPParser.Instance_creationContext):
        classSymbol = self.getObjectFromReference(ctx.ID().getText())
        objectExpression = ObjectExpression(classSymbol)
        self.expressionStack.append(objectExpression)
        
    def exitLiteral_expression(self, ctx: VYPParser.Literal_expressionContext):
        dataType = 'string' if ctx.literal_value().STRING_LITERAL() is not None else 'int'
        literalExpression = LiteralExpression(dataType, ctx.literal_value().getText())
        self.expressionStack.append(literalExpression)
        self.codeGenerator.generateLiteralExpression(self.currentFunction, ctx.literal_value().getText(), dataType)

    def exitFinal_field_expression(self, ctx: VYPParser.Final_field_expressionContext):
        variableExpression = VariableExpression(None, ctx.ID().getText())
        self.nestedObjectList.append(variableExpression)

    def exitFinal_method_expression(self, ctx: VYPParser.Final_method_expressionContext):
        functionExpression = FunctionExpression(ctx.function_call().ID().getText(), None,
                                                self.functionCallParametersList)
        self.functionCallParametersList = []
        self.nestedObjectList.append(functionExpression)

    def exitInstance_expression_value(self, ctx: VYPParser.Instance_expression_valueContext):
        classSymbol = self.getObjectFromReference(ctx.instance_expression().reference.text)
        variableExpression = VariableExpression(classSymbol, ctx.instance_expression().reference.text)
        for nestedObject in self.nestedObjectList:
            variableExpression = self.processObjectInvocation(variableExpression, nestedObject)
        self.expressionStack.append(variableExpression)
        self.nestedObjectList = []

    def exitInstance_assignment(self, ctx: VYPParser.Instance_assignmentContext):
        self.nestedObjectList = []

    def exitReturn_statement(self, ctx: VYPParser.Return_statementContext):
        returnExpression = self.expressionStack.pop()
        if self.currentClass == None:
            currentFunction = self.functionTable.getSymbol(self.currentFunctionId)
        else:
            currentFunction = self.currentClass.methodTable.getSymbol(self.currentFunctionId)
        self.semanticsChecker.checkVariableAssignment(currentFunction.dataType, returnExpression.dataType)
        self.currentFunctionReturn = True
        setReturnValue = currentFunction.dataType != 'void'
        self.codeGenerator.generateReturnValue(self.currentFunction, setReturnValue)

    # TODO check empty constructor exists!!!

    def processObjectInvocation(self, baseExpression, nextExpression):
        if isinstance(nextExpression, VariableExpression):
            symbol = baseExpression.dataType.getField(nextExpression.id)
            expression = VariableExpression(symbol.dataType, nextExpression.id)
            # TODO generate field access
            return expression
        if isinstance(nextExpression, FunctionExpression):
            symbol = baseExpression.dataType.getMethod(nextExpression.id)
            expression = FunctionExpression(nextExpression.id, symbol.dataType, self.functionCallParametersList.copy())
            # TODO generate method call
            self.functionCallParametersList = []
            return expression

    def exitNext_expression(self, ctx: VYPParser.Next_expressionContext):
        self.processFunctionParameter()

    def exitExpression_list(self, ctx: VYPParser.Expression_listContext):
        self.processFunctionParameter()            

    def processBinaryExpression(self, operator):
        rightExpression = self.expressionStack.pop()
        leftExpression = self.expressionStack.pop()
        self.semanticsChecker.checkBinaryExpressionSemantics(leftExpression, rightExpression, operator)
        binaryExpression = BinaryExpression(leftExpression, rightExpression, operator)
        self.expressionStack.append(binaryExpression)
        if binaryExpression.dataType == 'string' and operator == '+':
            self.codeGenerator.callFunction(self.currentFunction, 'concat')
        else:
            self.codeGenerator.generateBinaryExpression(self.currentFunction, operator, leftExpression.dataType)

    def processUnaryExpression(self, operator):
        expression = self.expressionStack.pop()
        self.semanticsChecker.checkUnaryExpressionSemantics(expression, operator)
        unaryExpression = UnaryExpression(expression, operator)
        self.expressionStack.append(unaryExpression)

    def processFunctionParameter(self):
        expression = self.expressionStack.pop()
        self.functionCallParametersList.append(expression)

    def getObjectFromReference(self, reference):
        if reference == 'this':
            return self.currentClass
        if reference == 'super':
            return self.currentClass.parent
        return self.classTable.getSymbol(reference)

    def exitStatement(self, ctx):
        #self.expressionStack.clear()
        self.codeGenerator.restoreStackPointer(self.currentFunction)

# TODO OBJECT EXPRESSIONS

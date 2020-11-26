from antlr_generated.VYPParser import VYPParser
from compiler import CustomParseTreeListener
from compiler.semantics_checker import SemanticsChecker


class BinaryExpression:

    def __init__(self, leftExpression, rightExpression, operator):
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
        print(expressionType)
        expression = self.expressionStack.pop()
        self.expressionStack.append(CastExpression(expression, expressionType))

    def exitFunction_expression(self, ctx: VYPParser.Function_expressionContext):
        functionId = ctx.function_call().ID().getText()
        functionSymbol = self.functionTable.getSymbol(functionId)
        self.semanticsChecker.checkFunctionCallSemantics(functionId, self.functionCallParametersList,
                                                         functionSymbol.parameterList.parameters)
        functionExpression = FunctionExpression(functionId, functionSymbol.dataType,
                                                self.functionCallParametersList.copy())
        self.expressionStack.append(functionExpression)
        self.functionCallParametersList = []

    def exitComparison_expression(self, ctx: VYPParser.Comparison_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitOr_expression(self, ctx: VYPParser.Or_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitVariable_expression(self, ctx: VYPParser.Variable_expressionContext):
        variableSymbol = self.localSymbolTable.getSymbol(ctx.ID().getText())
        self.semanticsChecker.checkVariableIsDefined(variableSymbol)
        variableExpression = VariableExpression(variableSymbol.dataType, variableSymbol.id)
        self.expressionStack.append(variableExpression)

    def exitAnd_expression(self, ctx: VYPParser.And_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    '''Nothing needs to be generated, rule is just used to get proper order of operations'''

    def exitBracket_expression(self, ctx: VYPParser.Bracket_expressionContext):
        pass

    def exitNegation_expression(self, ctx: VYPParser.Negation_expressionContext):
        self.processUnaryExpression('!')

    def exitPlusminus_expression(self, ctx: VYPParser.Plusminus_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitNew_expression(self, ctx: VYPParser.New_expressionContext):
        pass

    def exitLiteral_expression(self, ctx: VYPParser.Literal_expressionContext):
        dataType = 'string' if ctx.literal_value().STRING_LITERAL() is not None else 'int'
        literalExpression = LiteralExpression(dataType, ctx.literal_value().getText())
        self.expressionStack.append(literalExpression)

    def exitNested_object(self, ctx:VYPParser.Nested_objectContext):
        pass

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

    def processUnaryExpression(self, operator):
        expression = self.expressionStack.pop()
        self.semanticsChecker.checkUnaryExpressionSemantics(expression, operator)
        unaryExpression = UnaryExpression(expression, operator)
        self.expressionStack.append(unaryExpression)

    def processFunctionParameter(self):
        expression = self.expressionStack.pop()
        self.functionCallParametersList.append(expression)

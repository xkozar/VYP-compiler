from collections import deque

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

    def __init__(self, dataType, id):
        self.dataType = dataType
        self.id = id

    def __str__(self):
        return f'{self.id}'

class FunctionExpression:

    def __init__(self, id, dataType, callExpressions):
        self.id = id
        self.dataType = dataType
        self.callExpressions = callExpressions

    def __str__(self):
        return f'{self.id}({", ".join(self.callExpressions)})'


class ExpressionListener(CustomParseTreeListener):
    
    def __init__(self):
        super().__init__()
        self.expressionStack = deque()
        self.semanticsChecker = SemanticsChecker()
        self.functionCallParametersList = []


    def exitEquality_expression(self, ctx:VYPParser.Equality_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitMuldiv_expression(self, ctx:VYPParser.Muldiv_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitMethod_expression(self, ctx:VYPParser.Method_expressionContext):
        pass

    def exitFunction_expression(self, ctx:VYPParser.Function_expressionContext):
        functionId = ctx.function_call().ID().getText()
        functionSymbol = self.globalDefinitionTable.findSymbolByKey(functionId)
        self.semanticsChecker.checkFunctionCallSemantics(functionId, self.functionCallParametersList, self.functionParametersDict[functionId])
        self.functionCallParametersList = []

    def exitComparison_expression(self, ctx:VYPParser.Comparison_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitOr_expression(self, ctx:VYPParser.Or_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitVariable_expression(self, ctx:VYPParser.Variable_expressionContext):
        variableSymbol = self.localSymbolTable.findSymbolByKey(ctx.ID().getText())
        self.semanticsChecker.checkVariableIsDefined(variableSymbol)
        variableExpression = VariableExpression(variableSymbol.dataType, variableSymbol.id)
        self.expressionStack.append(variableExpression)

    def exitAnd_expression(self, ctx:VYPParser.And_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    '''Nothing needs to be generated, rule is just used to get proper order of operations'''
    def exitBracket_expression(self, ctx:VYPParser.Bracket_expressionContext):
        pass

    def exitNegation_expression(self, ctx:VYPParser.Negation_expressionContext):
        self.processUnaryExpression('!')

    def exitPlusminus_expression(self, ctx:VYPParser.Plusminus_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitNew_expression(self, ctx:VYPParser.New_expressionContext):
        pass

    def exitLiteral_expression(self, ctx:VYPParser.Literal_expressionContext):
        dataType = 'string' if ctx.literal_value().STRING_LITERAL() != None else 'int'
        literalExpression = LiteralExpression(dataType, ctx.literal_value().getText())
        self.expressionStack.append(literalExpression)

    def exitField_expression(self, ctx:VYPParser.Field_expressionContext):
        pass

        # Exit a parse tree produced by VYPParser#next_expression.
    def exitNext_expression(self, ctx:VYPParser.Next_expressionContext):
        self.processFunctionParameter()

    def exitExpression_list(self, ctx:VYPParser.Expression_listContext):
        self.processFunctionParameter()


    def processBinaryExpression(self, operator):
        rightExpression = self.expressionStack.pop()
        leftExpression = self.expressionStack.pop()
        self.semanticsChecker.checkBinaryExpressionSemantics(leftExpression, rightExpression, operator)
        binaryExpression = BinaryExpression(leftExpression, rightExpression, operator)
        self.expressionStack.append(binaryExpression)
        print(binaryExpression)

    def processUnaryExpression(self, operator):
        expression = self.expressionStack.pop()
        self.semanticsChecker.checkUnaryExpressionSemantics(expression, operator)
        unaryExpression = UnaryExpression(expression, operator)
        self.expressionStack.append(unaryExpression)
        print(unaryExpression)

    def processFunctionParameter(self):
        expression = self.expressionStack.pop()
        self.functionCallParametersList.append(expression)

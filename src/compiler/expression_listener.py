from collections import deque
from antlr_generated.VYPParser import VYPParser
from .custom_parse_tree_listener import CustomParseTreeListener

class ExpressionListener(CustomParseTreeListener):
    
    def __init__(self):
        super().__init__()
        self.expressionStack = deque()


    def exitEquality_expression(self, ctx:VYPParser.Equality_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitMuldiv_expression(self, ctx:VYPParser.Muldiv_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitMethod_expression(self, ctx:VYPParser.Method_expressionContext):
        pass

    def exitFunction_expression(self, ctx:VYPParser.Function_expressionContext):
        pass

    def exitComparison_expression(self, ctx:VYPParser.Comparison_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitOr_expression(self, ctx:VYPParser.Or_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitVariable_expression(self, ctx:VYPParser.Variable_expressionContext):
        self.expressionStack.append(ctx.ID().getText())
        pass

    def exitAnd_expression(self, ctx:VYPParser.And_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitBracket_expression(self, ctx:VYPParser.Bracket_expressionContext):
        pass

    def exitNegation_expression(self, ctx:VYPParser.Negation_expressionContext):
        pass

    def exitPlusminus_expression(self, ctx:VYPParser.Plusminus_expressionContext):
        self.processBinaryExpression(ctx.operator.text)

    def exitNew_expression(self, ctx:VYPParser.New_expressionContext):
        pass

    def exitLiteral_expression(self, ctx:VYPParser.Literal_expressionContext):
        self.expressionStack.append(ctx.literal_value().getText())

    def exitField_expression(self, ctx:VYPParser.Field_expressionContext):
        pass

    def processBinaryExpression(self, operator):
        rightExpression = self.expressionStack.pop()
        leftExpression = self.expressionStack.pop()
        print(leftExpression, operator, rightExpression)
        self.expressionStack.append(leftExpression + operator + rightExpression)

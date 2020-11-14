from .custom_parse_tree_listener import CustomParseTreeListener
from antlr_generated.VYPParser import VYPParser

class ExpressionListener(CustomParseTreeListener):
    
    def __init__(self):
        super().__init__()
        self.expression = ''
        self.t = ''
        self.lastDataType = None
    
    def enterEquality_expression(self, ctx:VYPParser.Equality_expressionContext):
        pass

    def exitEquality_expression(self, ctx:VYPParser.Equality_expressionContext):
        pass


    def enterMuldiv_expression(self, ctx:VYPParser.Muldiv_expressionContext):
        pass

    def exitMuldiv_expression(self, ctx:VYPParser.Muldiv_expressionContext):
        pass


    def enterMethod_expression(self, ctx:VYPParser.Method_expressionContext):
        pass

    def exitMethod_expression(self, ctx:VYPParser.Method_expressionContext):
        pass


    def enterFunction_expression(self, ctx:VYPParser.Function_expressionContext):
        pass

    def exitFunction_expression(self, ctx:VYPParser.Function_expressionContext):
        pass


    def enterComparison_expression(self, ctx:VYPParser.Comparison_expressionContext):
        pass

    def exitComparison_expression(self, ctx:VYPParser.Comparison_expressionContext):
        pass


    def enterOr_expression(self, ctx:VYPParser.Or_expressionContext):
        pass

    def exitOr_expression(self, ctx:VYPParser.Or_expressionContext):
        pass


    def enterVariable_expression(self, ctx:VYPParser.Variable_expressionContext):
        variableSymbol = self.localSymbolTable.findSymbolByKey(ctx.ID().getText())
        self.lastDataType = variableSymbol.dataType
        pass

    def exitVariable_expression(self, ctx:VYPParser.Variable_expressionContext):
        pass


    def enterAnd_expression(self, ctx:VYPParser.And_expressionContext):
        pass

    def exitAnd_expression(self, ctx:VYPParser.And_expressionContext):
        pass


    def enterBracket_expression(self, ctx:VYPParser.Bracket_expressionContext):
        pass

    def exitBracket_expression(self, ctx:VYPParser.Bracket_expressionContext):
        pass


    def enterNegation_expression(self, ctx:VYPParser.Negation_expressionContext):
        pass

    def exitNegation_expression(self, ctx:VYPParser.Negation_expressionContext):
        pass


    def enterPlusminus_expression(self, ctx:VYPParser.Plusminus_expressionContext):
        pass

    def exitPlusminus_expression(self, ctx:VYPParser.Plusminus_expressionContext):
        pass


    def enterNew_expression(self, ctx:VYPParser.New_expressionContext):
        pass

    def exitNew_expression(self, ctx:VYPParser.New_expressionContext):
        pass


    def enterLiteral_expression(self, ctx:VYPParser.Literal_expressionContext):
        pass

    def exitLiteral_expression(self, ctx:VYPParser.Literal_expressionContext):
        pass


    def enterField_expression(self, ctx:VYPParser.Field_expressionContext):
        pass

    def exitField_expression(self, ctx:VYPParser.Field_expressionContext):
        pass
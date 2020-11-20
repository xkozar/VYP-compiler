from compiler import SemanticTypeIncompabilityError, SemanticGeneralError

class SemanticsChecker:

    def __init__(self):
        self.binaryTypeMap = {
            '*': ['int'],
            '/': ['int'],
            '+': ['int', 'string'],
            '-': ['int'],
            '<': ['int', 'string'],
            '>': ['int', 'string'],
            '>=': ['int', 'string'],
            '<=': ['int', 'string'],
            '<=': ['int', 'string'],
            '==': ['int', 'string', 'object'],
            '!=': ['int', 'string', 'object'],
            '&&': ['int', 'object'],
            '||': ['int', 'object']
        }
        self.unaryTypeMap = {
            '!': ['int']
        }

    def checkBinaryExpressionSemantics(self, leftExpression, rightExpression, operator):
        if leftExpression.dataType != rightExpression.dataType:
            raise SemanticTypeIncompabilityError
        acceptedTypeValues = self.binaryTypeMap[operator]
        if not (leftExpression.dataType in acceptedTypeValues or ('object' in acceptedTypeValues and leftExpression.dataType != 'string')):
            raise SemanticTypeIncompabilityError

    def checkUnaryExpressionSemantics(self, expression, operator):
        if expression.dataType not in self.unaryTypeMap[operator]:
            raise SemanticTypeIncompabilityError

    def checkVariableIsDefined(self, variableSymbol):
        if variableSymbol.isDefined == False:
            raise SemanticGeneralError

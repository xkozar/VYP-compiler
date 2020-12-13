from compiler import SemanticTypeIncompatibilityError, SemanticGeneralError
from symbol_table.general_symbol import GeneralSymbol
from symbol_table.symbol_table import SymbolTable


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
            raise SemanticTypeIncompatibilityError
        acceptedTypeValues = self.binaryTypeMap[operator]
        if not (leftExpression.dataType in acceptedTypeValues or (
                'object' in acceptedTypeValues and leftExpression.dataType != 'string')):
            raise SemanticTypeIncompatibilityError

    def checkUnaryExpressionSemantics(self, expression, operator):
        if expression.dataType not in self.unaryTypeMap[operator]:
            raise SemanticTypeIncompatibilityError

    def checkFunctionCallSemantics(self, functionId, callExpressionList: list, callParameterList: list):
        if functionId == 'print':
            return self.checkPrintFunctionCall(callExpressionList)
        if len(callExpressionList) != len(callParameterList):
            raise SemanticGeneralError
        self.checkFunctionParametersTypes(callExpressionList, callParameterList)

    def checkMethodOverrideTypes(self, classTable: SymbolTable):
        definedClasses = classTable.getAllSymbols()
        for definedClass in definedClasses:
            for method in definedClass.getAllClassDefinedMethods():
                parentMethod = definedClass.getMethodFromParents(method.id)
                if parentMethod is None:
                    continue
                if method.dataType != parentMethod.dataType:
                    raise SemanticTypeIncompatibilityError

    @staticmethod
    def checkFunctionParametersTypes(callExpressionList: list, callParameterList: list):
        for callExpression, callParameter in zip(callExpressionList[::-1], callParameterList):
            if callParameter.dataType != callExpression.dataType:
                raise SemanticTypeIncompatibilityError(f"Expected type {callParameter.dataType} but got {callExpression.dataType} insted.")

    ''' Function 'print' takes arbitrary (but more than 1) number of primitive data type parameters.
    Since this behaviour is not supported anywhere else, special method for checking 'print' is 
    sufficient. '''

    @staticmethod
    def checkPrintFunctionCall(callExpressionList):
        if len(callExpressionList) == 0:
            raise SemanticGeneralError
        for callExpression in callExpressionList:
            if callExpression.dataType not in ['int', 'string']:
                raise SemanticTypeIncompatibilityError

    @staticmethod
    def checkVariableIsDefined(variableSymbol: GeneralSymbol):
        if not variableSymbol.isDefined:
            raise SemanticGeneralError(f"Variable with id:{variableSymbol.id} is not yet defined")

    @staticmethod
    def checkVariableAssignment(variableDataType, expressionDataType):
        if variableDataType != expressionDataType:
            raise SemanticTypeIncompatibilityError(f"{variableDataType} is not compatible with {expressionDataType}")

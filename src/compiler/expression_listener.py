from antlr_generated.VYPParser import VYPParser
from compiler import CustomParseTreeListener
from compiler.semantics_checker import SemanticsChecker
from compiler.custom_exceptions import SemanticTypeIncompatibilityError, SemanticGeneralError
from symbol_table.class_symbol import ClassSymbol

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

    def exitFunction_call(self, ctx: VYPParser.Function_callContext):
        if isinstance(ctx.parentCtx, VYPParser.Final_method_expressionContext):
            return
        functionId = ctx.ID().getText()
        functionSymbol = self.functionTable.getSymbol(functionId)
        self.semanticsChecker.checkFunctionCallSemantics(functionId, self.functionCallParametersList,
                                                         functionSymbol.parameterList.parameters)
        functionExpression = FunctionExpression(functionId, functionSymbol.dataType,
                                                self.functionCallParametersList.copy())
        self.expressionStack.append(functionExpression)
        if functionId != 'print':
            self.codeGenerator.callFunction(self.currentFunction, functionId)
        else:
            self.codeGenerator.generatePrint(self.currentFunction, self.functionCallParametersList.copy())
            # for parameter in self.functionCallParametersList:
            #     if parameter.dataType == 'int':
            #         self.codeGenerator.callFunction(self.currentFunction, 'printi')
            #     else:
            #         self.codeGenerator.callFunction(self.currentFunction, 'prints')

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

    def exitNew_expression(self, ctx:VYPParser.New_expressionContext):
        classSymbol = self.classTable.getSymbol(ctx.children[0].ID().getText())
        objectExpression = ObjectExpression(classSymbol)
        self.expressionStack.append(objectExpression)
        self.codeGenerator.generateInstance(self.currentFunction, classSymbol)
        
    def exitLiteral_expression(self, ctx: VYPParser.Literal_expressionContext):
        dataType = 'string' if ctx.literal_value().STRING_LITERAL() is not None else 'int'
        literalExpression = LiteralExpression(dataType, ctx.literal_value().getText())
        self.expressionStack.append(literalExpression)
        self.codeGenerator.generateLiteralExpression(self.currentFunction, ctx.literal_value().getText(), dataType)

    def enterFinal_field_expression(self, ctx:VYPParser.Final_field_expressionContext):
        lastExpression = self.expressionStack.pop()
        if lastExpression.id == 'super':
            raise SemanticGeneralError(f"Cannot variable on 'super' reference")
        if not isinstance(lastExpression.dataType, ClassSymbol):
            raise SemanticGeneralError(f"Cannot invoke variable on non-object data type '{lastExpression.dataType}'")
        symbol = lastExpression.dataType.getField(ctx.ID().getText())
        if symbol is None:
            raise SemanticGeneralError(f"Field '{ctx.ID().getText()}' is not defined in class '{lastExpression.dataType.id}'")
        expression = VariableExpression(symbol.dataType, symbol.id)
        if not isinstance(ctx.parentCtx.parentCtx.parentCtx, VYPParser.Instance_assignmentContext):
            self.codeGenerator.generateFieldExpression(self.currentFunction, self.nestedObjectList[-1].dataType, symbol.id, 0)
            pass
        self.expressionStack.append(expression)
        self.nestedObjectList.append(expression)

    def enterFinal_method_expression(self, ctx:VYPParser.Final_method_expressionContext):
        lastExpression = self.expressionStack.pop()
        if not isinstance(lastExpression.dataType, ClassSymbol):
            raise SemanticGeneralError(f"Cannot invoke method on non-object data type '{lastExpression.dataType}'")
        symbol = lastExpression.dataType.getMethod(ctx.function_call().ID().getText())
        if symbol is None:
            raise SemanticGeneralError(f"Method '{ctx.function_call().ID().getText()}' is not defined in class '{lastExpression.dataType.id}'")
        expression = VariableExpression(symbol.dataType, symbol.id)
        self.expressionStack.append(lastExpression)
        self.nestedObjectList.append(lastExpression)

    # def exitFinal_method_expression(self, ctx:VYPParser.Final_method_expressionContext):
    #     pass
    #     self.codeGenerator.callMethod(self.currentFunction, )

    def exitFinal_method_expression(self, ctx: VYPParser.Final_method_expressionContext):
        lastExpression = self.expressionStack.pop()

        functionId = ctx.function_call().ID().getText()
        functionSymbol = lastExpression.dataType.getMethod(functionId)
        self.semanticsChecker.checkFunctionCallSemantics(functionId, self.functionCallParametersList,
                                                         functionSymbol.parameterList.parameters)
        functionExpression = FunctionExpression(functionId, functionSymbol.dataType,
                                                self.functionCallParametersList.copy())
        self.codeGenerator.callMethod(self.currentFunction, lastExpression.dataType.id, functionExpression)

        self.expressionStack.append(functionExpression)
        self.functionCallParametersList = []
# TODO call method        self.codeGenerator.callFunction(self.currentFunction, functionId)


    def enterFirst_instance(self, ctx: VYPParser.First_instanceContext):
        self.nestedObjectList = []
        if ctx.reference is not None:
            classSymbol = self.getObjectFromReference(ctx.reference.text)
            variableExpression = VariableExpression(classSymbol, ctx.reference.text)
            self.expressionStack.append(variableExpression)
            self.nestedObjectList.append(variableExpression)
        # TODO generate object value

    def exitFirst_instance(self, ctx: VYPParser.First_instanceContext):
        if ctx.reference is None:
            self.nestedObjectList.append(self.expressionStack[-1])
            pass

    def exitInstance_assignment(self, ctx: VYPParser.Instance_assignmentContext):
        self.codeGenerator.assignValueToField(self.currentFunction, self.nestedObjectList[-2].dataType, self.nestedObjectList[-1].id)
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

    def exitNext_expression(self, ctx: VYPParser.Next_expressionContext):
        #self.processFunctionParameter()
        expression = self.expressionStack.pop()
        self.functionCallParametersList.insert(0, expression)

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
            if self.currentClass is None:
                raise SemanticGeneralError("Cannot access 'this' reference outside of class definition")
            self.codeGenerator.generateVariableExpression(self.currentFunction, reference)
            return self.currentClass
        if reference == 'super':
            if self.currentClass is None:
                raise SemanticGeneralError("Cannot access 'super' reference outside of class definition")
            return self.currentClass.parent
        symbol = self.localSymbolTable.getSymbol(reference)
        self.codeGenerator.generateVariableExpression(self.currentFunction, reference)
        return symbol.dataType

    def exitStatement(self, ctx):
        #self.expressionStack.clear()
        self.codeGenerator.restoreStackPointer(self.currentFunction)

# TODO OBJECT EXPRESSIONS

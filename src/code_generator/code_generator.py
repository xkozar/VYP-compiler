from symbol_table.function_symbol import FunctionSymbol

binaryOperationsMap = {
    '*': 'MULI',
    '/': 'DIVI',
    '+': 'ADDI',
    '-': 'SUBI',
    '<': 'LTI',
    '>': 'GTI',
    '==': 'EQI',
    '&&': 'AND',
    '||': 'OR'
}

printIntFunction = '''
LABEL printi
	WRITEI [$SP - 2]
    WRITES "\\n"
	SUBI $SP, $SP, 2
	RETURN [$SP + 2]

'''

printStringFunction = '''
LABEL prints
	WRITES [$SP - 2]
    WRITES "\\n"
	SUBI $SP, $SP, 2
	RETURN [$SP + 2]

'''

def incrementRegister(register):
    return f"ADDI {register}, {register}, 1"

def decrementRegister(register):
    return f"SUBI {register}, {register}, 1"

class FunctionCodeGenerator:
    stackPointer = '$SP'
    functionPointer = '$FP'
    programCounter = '$PC'
    expressionResultReg1 = '$4'
    expressionResultReg2 = '$5'
    chunkPointer = '$6'

    def __init__(self, name, parameters):
        self.name = name
        self.label = f"LABEL {name}"
        self.header = f'''\t#Function start
\t{incrementRegister(self.stackPointer)}
\tSET {self.functionPointer}, {self.stackPointer}
'''
        self.body = ""
        self.returnCall = ""
        self.parametersList = parameters
        self.variablesList = []

    def getVariableOffset(self, variable):
        if variable in self.variablesList:
            value = self.variablesList.index(variable)
            return f'+ {value}'
        else:
            value = - 3 - (len(self.parametersList) - 1 - self.parametersList.index(variable))
            return f'{value}'

    def defineVariable(self, variableName):
        self.variablesList.append(variableName)
        self.body += f'\t#Create variable {variableName}\n'
        self.body += f'\tCREATE $1, 1\n'
        #self.body += f'\t{incrementRegister(self.stackPointer)}\n'
        self.body += f'\tSET [{self.functionPointer}{self.getVariableOffset(variableName)}], $1\n\n'

    def intLiteralExpression(self, value):
        self.body += f'\t#Int literal expression {value}\n'
        self.body += f'\tSET [{self.stackPointer}], {value}\n'
        self.body += f'\t{incrementRegister(self.stackPointer)}\n\n'

    def stringLiteralExpression(self, value):
        self.body += f'\t#String literal expression {value}\n'
        self.body += f'\tCREATE {self.chunkPointer}, 1\n'
        self.body += f'\tSETWORD {self.chunkPointer}, 0, {value}\n'
        self.body += f'\tGETWORD {self.chunkPointer}, {self.chunkPointer}, 0\n'
        self.body += f'\tSET [{self.stackPointer}], {self.chunkPointer}\n'
        self.body += f'\t{incrementRegister(self.stackPointer)}\n\n'


    def assignValueToVariable(self, variable):
        self.body += f'\t# Variable assignment {variable}\n'
        self.body += f'\t{decrementRegister(self.stackPointer)}\n'        
        self.body += f'\tSET [{self.functionPointer}{self.getVariableOffset(variable)}], [{self.stackPointer}]\n\n'

    def callFunction(self, functionName):
        self.body += f'\t# Calling function {functionName}\n'
        #self.body += f'\t{incrementRegister(self.stackPointer)}\n'
        self.body += f'\tSET [{self.stackPointer}], {self.functionPointer}\n'
        self.body += f'\t{incrementRegister(self.stackPointer)}\n'
        # self.body += f'\tSET [{self.stackPointer}], {self.programCounter}\n'
        self.body += f'\tCALL [{self.stackPointer}], {functionName}\n\n'

    def restoreStackPointer(self):
        self.body += f'\t# Restore stack pointer\n'
        self.body += f'\tADDI {self.stackPointer}, {self.functionPointer}, {len(self.variablesList)}\n\n'

    def returnCallCode(self):
        if self.name == 'main':
            self.returnCall += f'\tJUMP __END\n'
        else:
            self.returnCall += f"\tRETURN [{self.functionPointer} - 1]"

    def generateReturnValue(self):
        self.body += f'\t# Return value\n'
        #self.body += f'\tSET [{self.functionPointer}], [{self.functionPointer} - 1]\n'
        self.body += f'\tSET $2, [{self.functionPointer} - 1]\n'
        self.body += f'\tSET $3, [{self.functionPointer} - 2]\n'
        self.body += f'\t{decrementRegister(self.stackPointer)}\n'
        self.body += f'\tSET [{self.functionPointer} - {2 + len(self.parametersList)}], [{self.stackPointer}]\n'
        self.body += f'\tSUBI {self.stackPointer}, {self.functionPointer}, {1 + len(self.parametersList)}\n'
        self.body += f'\tSET {self.functionPointer}, $3\n'
        self.body += f"\tRETURN $2\n"

    def generateVariableExpression(self, variable):
        self.body += f'\t# Variable expression\n'
        self.body += f'\tSET [{self.stackPointer}], [{self.functionPointer}{self.getVariableOffset(variable)}]\n'
        self.body += f'\t{incrementRegister(self.stackPointer)}\n\n'

    def generateBinaryExpression(self, instruction):
        if instruction in binaryOperationsMap.keys():
            self.body += f'\t# Binary expression\n'
            self.body += f'\t{binaryOperationsMap[instruction]} {self.expressionResultReg1}, [{self.stackPointer} -2], [{self.stackPointer} -1]\n'
            self.body += f'\tSET [{self.stackPointer} - 2], {self.expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(self.stackPointer)}\n\n'
        elif instruction == '<=':
            self.body += f'\t# Binary expression <=\n'
            self.body += f'\tLTI {self.expressionResultReg1}, [{self.stackPointer} -2], [{self.stackPointer} -1]\n'
            self.body += f'\tEQI {self.expressionResultReg2}, [{self.stackPointer} -2], [{self.stackPointer} -1]\n'
            self.body += f'\tOR {self.expressionResultReg1}, {self.expressionResultReg1}, {self.expressionResultReg2}\n'
            self.body += f'\tSET [{self.stackPointer} - 2], {self.expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(self.stackPointer)}\n\n'
        elif instruction == '>=':
            self.body += f'\t# Binary expression >=\n'
            self.body += f'\tGTI {self.expressionResultReg1}, [{self.stackPointer} -2], [{self.stackPointer} -1]\n'
            self.body += f'\tEQI {self.expressionResultReg2}, [{self.stackPointer} -2], [{self.stackPointer} -1]\n'
            self.body += f'\tOR {self.expressionResultReg1}, {self.expressionResultReg1}, {self.expressionResultReg2}\n'
            self.body += f'\tSET [{self.stackPointer} - 2], {self.expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(self.stackPointer)}\n\n'
        elif instruction == '!=':
            self.body += f'\t# Binary expression !=\n'
            self.body += f'\tEQI {self.expressionResultReg1}, [{self.stackPointer} -2], [{self.stackPointer} -1]\n'
            self.body += f'\tNOT {self.expressionResultReg1}, {self.expressionResultReg1}\n'
            self.body += f'\tSET [{self.stackPointer} - 2], {self.expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(self.stackPointer)}\n\n'

    def notExpression(self):
        self.body += f'\t# Not expression\n'
        self.body += f'\tNOT {self.expressionResultReg1}, [{self.stackPointer} -1]\n'
        self.body += f'\tSET [{self.stackPointer} -1], {self.expressionResultReg1}\n\n'

    def unaryMinus(self):
        self.body += f'\t# Not expression\n'
        self.body += f'\tSUBI {self.expressionResultReg1}, 0, [{self.stackPointer} -1]\n'
        self.body += f'\tSET [{self.stackPointer} -1], {self.expressionResultReg1}\n\n'

    def startIf(self, line, column):
        self.body += f'\t# Start of IF\n'
        self.body += f'\t{decrementRegister(self.stackPointer)}\n'
        self.body += f'\tJUMPNZ IF{line}:{column}, [{self.stackPointer}]\n'
        self.body += f'\tJUMP IF{line}:{column}__end\n'
        self.body += f'\tLABEL IF{line}:{column}\n\n'

    def endIf(self, line, column):
        self.body += f'\t# End of IF part\n'
        self.body += f'\tJUMP ELSE{line}:{column}__end\n'
        self.body += f'\tLABEL IF{line}:{column}__end\n\n'

    def endElse(self, line, column):
        self.body += f'\t# End of ELSE part\n'
        self.body += f'\tLABEL ELSE{line}:{column}__end\n'

    def startWhile(self, line, column):
        self.body += f'\t# Start WHILE\n'
        self.body += f'\tLABEL WHILE{line}:{column}\n'

    def evaluateWhile(self, line, column):
        self.body += f'\t# Evaluate WHILE expression\n'
        self.body += f'\t{decrementRegister(self.stackPointer)}\n'
        self.body += f'\tJUMPZ WHILE{line}:{column}__end, [{self.stackPointer}]\n'


    def endWhile(self, line, column):
        self.body += f'\t# End WHILE\n'
        self.body += f'\tJUMP WHILE{line}:{column}\n'
        self.body += f'\tLABEL WHILE{line}:{column}__end\n'

    def __str__(self):
        return '\n'.join([self.label, self.header, self.body, self.returnCall])


class CodeGenerator:

    def __init__(self):
        self.header = '''#! /bin/vypint
# VYPcode: 1.0
# Generated by: xkozar02
'''
        self.functionDefinitions = {}
    
    def generateCode(self):
        print(self.header)
        print('ALIAS FP $0')
        print("JUMP main\n")
        print(printIntFunction)
        print(printStringFunction)
        for functionKey in self.functionDefinitions:
            print(str(self.functionDefinitions[functionKey].codeGenerator) + '\n')
        print("LABEL __END")

    def generateFunctionHeader(self, function: FunctionSymbol, functionParameters):
        self.functionDefinitions[function.id] = function
        functionLabel = function.id
        if function.ownerClass != "":
            functionLabel = f'{function.ownerClass}:{functionLabel}'
        function.codeGenerator = FunctionCodeGenerator(functionLabel, functionParameters.copy())

    def defineVariable(self, variableName, function):
        function.codeGenerator.defineVariable(variableName)

    def generateLiteralExpression(self, function, value, literalType):
        if literalType == 'int':
            function.codeGenerator.intLiteralExpression(value)
        else:
            function.codeGenerator.stringLiteralExpression(value)
        # TODO string

    def assignValueToVariable(self, function, variableName):
        function.codeGenerator.assignValueToVariable(variableName)

    def callFunction(self, function, functionToCall):
        function.codeGenerator.callFunction(functionToCall)

    def returnFromFunction(self, function):
        function.codeGenerator.returnCallCode()

    def restoreStackPointer(self, function):
        function.codeGenerator.restoreStackPointer()

    def generateReturnValue(self, function):
        function.codeGenerator.generateReturnValue()

    def generateVariableExpression(self, function, variable):
        function.codeGenerator.generateVariableExpression(variable)

    def generateBinaryExpression(self, function, instruction):
        function.codeGenerator.generateBinaryExpression(instruction)

    def generateNotExpression(self, function):
        function.codeGenerator.notExpression()

    def generateUnaryMinusExpression(self, function):
        function.codeGenerator.unaryMinus()

    def generateIfStart(self, function, line, column):
        function.codeGenerator.startIf(line, column)

    def generateIfEnd(self, function, line, column):
        function.codeGenerator.endIf(line, column)

    def generateElseEnd(self, function, line, column):
        function.codeGenerator.endElse(line, column)

    def generateWhileStart(self, function, line, column):
        function.codeGenerator.startWhile(line, column)

    def generateWhileEnd(self, function, line, column):
        function.codeGenerator.endWhile(line, column)

    def generateEvaluateWhile(self, function, line, column):
        function.codeGenerator.evaluateWhile(line, column)




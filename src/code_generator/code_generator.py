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
LABEL print
	WRITEI [$SP - 2]
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
        self.body += f'\t#Literal expression {value}\n'
        self.body += f'\tSET [{self.stackPointer}], {value}\n'
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
        pass
        print(self.header)
        print('ALIAS FP $0')
        print("JUMP main\n")
        print(printIntFunction)
        for functionKey in self.functionDefinitions:
            print(str(self.functionDefinitions[functionKey]) + '\n')
        print("LABEL __END")

    def generateFunctionHeader(self, functionName, functionParameters):
        self.functionDefinitions[functionName] = FunctionCodeGenerator(functionName, functionParameters.copy())

    def defineVariable(self, variableName, functionName):
        self.functionDefinitions[functionName].defineVariable(variableName)

    def generateLiteralExpression(self, functionName, value, literalType):
        if literalType == 'int':
            self.functionDefinitions[functionName].intLiteralExpression(value)
        else:
            pass
        # TODO string

    def assignValueToVariable(self, functionName, variableName):
        self.functionDefinitions[functionName].assignValueToVariable(variableName)

    def callFunction(self, currentFunctionName, functionToCall):
        self.functionDefinitions[currentFunctionName].callFunction(functionToCall)

    def returnFromFunction(self, functionName):
        self.functionDefinitions[functionName].returnCallCode()

    def restoreStackPointer(self, functionName):
        self.functionDefinitions[functionName].restoreStackPointer()

    def generateReturnValue(self, functionName):
        self.functionDefinitions[functionName].generateReturnValue()

    def generateVariableExpression(self, functionName, variable):
        self.functionDefinitions[functionName].generateVariableExpression(variable)

    def generateBinaryExpression(self, functionName, instruction):
        self.functionDefinitions[functionName].generateBinaryExpression(instruction)

    def generateNotExpression(self, functionName):
        self.functionDefinitions[functionName].notExpression()


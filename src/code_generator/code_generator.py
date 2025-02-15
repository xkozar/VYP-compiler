'''
    project: VYPlanguage compiler
    authros: Tomáš Kožár, xkozar02
             Maroš Holko, xholko01
'''
from symbol_table.function_symbol import FunctionSymbol
from symbol_table.class_symbol import ClassSymbol



def incrementRegister(register):
    return f"ADDI {register}, {register}, 1"

def decrementRegister(register):
    return f"SUBI {register}, {register}, 1"



binaryOperationsIntMap = {
    '*': 'MUL',
    '/': 'DIV',
    '+': 'ADD',
    '-': 'SUB',
    '<': 'LT',
    '>': 'GT',
    '==': 'EQ',
    '&&': 'AND',
    '||': 'OR'
}

singleNameOperations = ['||', '&&']

stackPointer = '$SP'
functionPointer = '$FP'
programCounter = '$PC'
expressionResultReg1 = '$4'
expressionResultReg2 = '$5'
chunkPointer = '$6'
miscRegister = '$7'

concatenationFunction = f'''
LABEL concat
    GETSIZE {expressionResultReg1}, [$SP - 3] # Left string
    GETSIZE {expressionResultReg2}, [$SP - 2] # Right string
    COPY {chunkPointer}, [$SP - 3]
    ADDI $1, {expressionResultReg1}, {expressionResultReg2} # Total length
    RESIZE {chunkPointer}, $1
    SET $2, 0

    LABEL concat_start
    LTI $1, $2, {expressionResultReg2}
    JUMPZ concat_end, $1

    GETWORD $1, [$SP-2], $2
    ADDI {miscRegister}, $2, {expressionResultReg1}
    SETWORD {chunkPointer}, {miscRegister}, $1

    ADDI $2, $2, 1
    JUMP concat_start
    LABEL concat_end

    SUBI {stackPointer}, {stackPointer}, 3
    SET [{stackPointer}], {chunkPointer}
    {incrementRegister(stackPointer)}
    RETURN [{stackPointer} + 2]

'''

subStrFunction = f'''
LABEL subStr
    GETSIZE {miscRegister}, [$SP - 4] # Original string size

    GTI {expressionResultReg1}, [$SP - 3], {miscRegister}
    LTI {expressionResultReg2}, [$SP - 3], 0
    OR {expressionResultReg1}, {expressionResultReg1}, {expressionResultReg2}
    JUMPZ __subStrStart, {expressionResultReg1}
    CREATE {chunkPointer}, 1
    SETWORD {chunkPointer}, 0, ""
    GETWORD {chunkPointer}, {chunkPointer}, 0
    JUMP substr_end

    LABEL __subStrStart
    CREATE {chunkPointer}, [$SP - 2] # Chunk with size
    SET {expressionResultReg1}, [$SP - 3] # BEGIN INDEX
    SET $2, 0 #COUNTER
    ADDI $1, {expressionResultReg1}, [$SP - 2]
    LTI $1, $1, {miscRegister}
    JUMPNZ substr_start, $1
    SUBI $1, {miscRegister}, {expressionResultReg1}
    
    RESIZE {chunkPointer}, $1 
    
    LABEL substr_start
    LTI $1, {expressionResultReg1}, {miscRegister}
    JUMPZ substr_end, $1

    LTI $1, $2, [$SP - 2]
    JUMPZ substr_end, $1

    GETWORD $1, [$SP-4], {expressionResultReg1}
    SETWORD {chunkPointer}, $2, $1

    ADDI $2, $2, 1
    ADDI {expressionResultReg1}, {expressionResultReg1}, 1
    JUMP substr_start
    LABEL substr_end

    SUBI {stackPointer}, {stackPointer}, 4
    SET [{stackPointer}], {chunkPointer}
    {incrementRegister(stackPointer)}
    RETURN [{stackPointer} + 3]

'''

toStringFunction = f'''
LABEL Object:toString
    INT2STRING {miscRegister}, [{stackPointer} - 2] 
	SUBI {stackPointer}, {stackPointer}, 1
    SET [{stackPointer} - 1], {miscRegister}
	RETURN [{stackPointer} + 1]

'''

getClassFunction = f'''
LABEL Object:getClass
	GETWORD {miscRegister}, [{stackPointer} - 2], 0
	SUBI {stackPointer}, {stackPointer}, 1
    SET [{stackPointer} - 1], {miscRegister}
	RETURN [{stackPointer} + 1]

'''

getLengthFunction = f'''
LABEL length
	GETSIZE {miscRegister}, [{stackPointer} - 2]
	SUBI {stackPointer}, {stackPointer}, 1
    SET [{stackPointer} - 1], {miscRegister}
	RETURN [{stackPointer} + 1]

'''

readIntFunction = f'''
LABEL readInt
    READI {miscRegister}
    SET [{stackPointer} - 1], {miscRegister}
	RETURN [$SP]

'''

readStringFunction = f'''
LABEL readString
    READS {miscRegister}
    SET [{stackPointer} - 1], {miscRegister}
	RETURN [$SP]

'''

class FunctionCodeGenerator:

    def __init__(self, name, parameters, vmt):
        self.name = name
        self.label = f"LABEL {name}"
        self.header = f'''\t#Function start
\t{incrementRegister(stackPointer)}
\tSET {functionPointer}, {stackPointer}
'''
        self.body = ""
        self.returnCall = ""
        self.parametersList = parameters
        self.variablesList = []
        self.vmt = vmt

    def getVariableOffset(self, variable):
        if variable == 'this':
            value = -3 - len(self.parametersList)
            return f'{value}'
            #value = 
        if variable in self.variablesList:
            value = self.variablesList.index(variable)
            return f'+ {value}'
        else:
            value = - 3 - (len(self.parametersList) - 1 - self.parametersList.index(variable))
            return f'{value}'

    def defineVariable(self, variableName, dataType):
        self.variablesList.append(variableName)
        self.body += f'\t#Create variable {variableName}\n'
        if dataType == 'string':
            self.body += f'\tCREATE {chunkPointer}, 1\n'
            self.body += f'\tSETWORD {chunkPointer}, 0, ""\n'
            self.body += f'\tGETWORD {chunkPointer}, {chunkPointer}, 0\n'
            self.body += f'\tSET [{functionPointer}{self.getVariableOffset(variableName)}], {chunkPointer}\n'
        else:
            self.body += f'\tSET [{functionPointer}{self.getVariableOffset(variableName)}], 0\n'

    def intLiteralExpression(self, value):
        self.body += f'\t#Int literal expression {value}\n'
        self.body += f'\tSET [{stackPointer}], {value}\n'
        self.body += f'\t{incrementRegister(stackPointer)}\n\n'

    def stringLiteralExpression(self, value):
        self.body += f'\t#String literal expression {value}\n'
        self.body += f'\tCREATE {chunkPointer}, 1\n'
        self.body += f'\tSETWORD {chunkPointer}, 0, {value}\n'
        self.body += f'\tGETWORD {chunkPointer}, {chunkPointer}, 0\n'
        self.body += f'\tSET [{stackPointer}], {chunkPointer}\n'
        self.body += f'\t{incrementRegister(stackPointer)}\n\n'

    def assignValueToVariable(self, variable):
        self.body += f'\t# Variable assignment {variable}\n'
        self.body += f'\t{decrementRegister(stackPointer)}\n'        
        self.body += f'\tSET [{functionPointer}{self.getVariableOffset(variable)}], [{stackPointer}]\n\n'

    def assignValueToField(self, classSymbol, fieldName):
        self.body += f'\t# Field assignment \'{fieldName}\'\n'
        self.body += f'\tSUBI {stackPointer}, {stackPointer}, 2\n'  
        index = list(classSymbol.fieldTable.symbols.keys()).index(fieldName)
        self.body += f'\tSETWORD [{stackPointer}], {3 + index}, [{stackPointer} + 1]\n\n'

    def fieldExpression(self, classSymbol, fieldName, toDecrease):
        self.body += f'\t# Field expression \'{fieldName}\'\n'
        index = list(classSymbol.fieldTable.symbols.keys()).index(fieldName)
        self.body += f'\tGETWORD {miscRegister}, [{stackPointer} - 1], {3 + index}\n'
        self.body += f'\tSET [{stackPointer}-1], {miscRegister}\n\n'


    def decreaseStackPointer(self, count):
        self.body += f'\t# Decrease $SP by {count}\n'
        self.body += f'\tSUBI {stackPointer}, {stackPointer}, {count}\n\n'


    def callFunction(self, functionName):
        self.body += f'\t# Calling function {functionName}\n'
        self.body += f'\tSET [{stackPointer}], {functionPointer}\n'
        self.body += f'\t{incrementRegister(stackPointer)}\n'
        self.body += f'\tCALL [{stackPointer}], {functionName}\n\n'

    def callMethod(self, className, method, useSuper):
        index = self.vmt.getMethodOffset(className, method.id)
        parametersLength = len(method.callExpressions)
        vmtIndex = 2 if useSuper else 1
        self.body += f'\t# Calling method {method.id}\n'
        self.body += f'\tGETWORD {miscRegister}, [{stackPointer}-{1+parametersLength}], {vmtIndex}\n'
        self.body += f'\tGETWORD {miscRegister}, {miscRegister}, {index}\n'
        self.body += f'\tSET [{stackPointer}], {functionPointer}\n'
        self.body += f'\t{incrementRegister(stackPointer)}\n'
        self.body += f'\tCALL [{stackPointer}], {miscRegister}\n\n'

    def restoreStackPointer(self):
        self.body += f'\t# Restore stack pointer\n'
        self.body += f'\tADDI {stackPointer}, {functionPointer}, {len(self.variablesList)}\n\n'

    def returnCallCode(self):
        if self.name == 'main':
            self.returnCall += f'\tJUMP __END\n'


    def generateReturnValue(self, setReturnValue):
        self.body += f'\t# Return value\n'
        if self.name == 'main':
            self.body += f'\tJUMP __END\n'
        #self.body += f'\tSET [{functionPointer}], [{functionPointer} - 1]\n'
        self.body += f'\tSET $2, [{functionPointer} - 1]\n'
        self.body += f'\tSET $3, [{functionPointer} - 2]\n'
        self.body += f'\t{decrementRegister(stackPointer)}\n'
        methodOffset = 1 if ':' in self.name and setReturnValue else 0
        if setReturnValue:
            self.body += f'\tSET [{functionPointer} - {2 + len(self.parametersList) + methodOffset}], [{stackPointer}]\n'
        self.body += f'\tSUBI {stackPointer}, {functionPointer}, {1 + len(self.parametersList) + methodOffset}\n'
        if not setReturnValue:
            self.body += f'\t{decrementRegister(stackPointer)}\n'
        
        self.body += f'\tSET {functionPointer}, $3\n'
        self.body += f"\tRETURN $2\n"

    def generateVariableExpression(self, variable):
        self.body += f'\t# Variable expression \'{variable}\'\n'
        self.body += f'\tSET [{stackPointer}], [{functionPointer}{self.getVariableOffset(variable)}]\n'
        self.body += f'\t{incrementRegister(stackPointer)}\n\n'
    
    def generateSelfExpression(self):
        self.body += f'\t# Self expression \'{variable}\'\n'
        self.body += f'\tSET [{stackPointer}], [{functionPointer}{self.getVariableOffset(variable)}]\n'
        self.body += f'\t{incrementRegister(stackPointer)}\n\n'

    def generateBinaryExpression(self, instruction, dataType):
        if dataType == 'string':
            postFix = 'S'
        else:
            postFix = 'I'
        if instruction in binaryOperationsIntMap.keys():
            self.body += f'\t# Binary expression\n'
            if instruction in singleNameOperations:
                self.body += f'\t{binaryOperationsIntMap[instruction]} {expressionResultReg1}, [{stackPointer} -2], [{stackPointer} -1]\n'
            else:
                self.body += f'\t{binaryOperationsIntMap[instruction]}{postFix} {expressionResultReg1}, [{stackPointer} -2], [{stackPointer} -1]\n'
            self.body += f'\tSET [{stackPointer} - 2], {expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(stackPointer)}\n\n'
        elif instruction == '<=':
            self.body += f'\t# Binary expression <=\n'
            self.body += f'\tLT{postFix} {expressionResultReg1}, [{stackPointer} -2], [{stackPointer} -1]\n'
            self.body += f'\tEQ{postFix} {expressionResultReg2}, [{stackPointer} -2], [{stackPointer} -1]\n'
            self.body += f'\tOR {expressionResultReg1}, {expressionResultReg1}, {expressionResultReg2}\n'
            self.body += f'\tSET [{stackPointer} - 2], {expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(stackPointer)}\n\n'
        elif instruction == '>=':
            self.body += f'\t# Binary expression >=\n'
            self.body += f'\tGT{postFix} {expressionResultReg1}, [{stackPointer} -2], [{stackPointer} -1]\n'
            self.body += f'\tEQ{postFix} {expressionResultReg2}, [{stackPointer} -2], [{stackPointer} -1]\n'
            self.body += f'\tOR {expressionResultReg1}, {expressionResultReg1}, {expressionResultReg2}\n'
            self.body += f'\tSET [{stackPointer} - 2], {expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(stackPointer)}\n\n'
        elif instruction == '!=':
            self.body += f'\t# Binary expression !=\n'
            self.body += f'\tEQ{postFix} {expressionResultReg1}, [{stackPointer} -2], [{stackPointer} -1]\n'
            self.body += f'\tNOT {expressionResultReg1}, {expressionResultReg1}\n'
            self.body += f'\tSET [{stackPointer} - 2], {expressionResultReg1}\n'
            self.body += f'\t{decrementRegister(stackPointer)}\n\n'

    def notExpression(self):
        self.body += f'\t# Not expression\n'
        self.body += f'\tNOT {expressionResultReg1}, [{stackPointer} -1]\n'
        self.body += f'\tSET [{stackPointer} -1], {expressionResultReg1}\n\n'

    def unaryMinus(self):
        self.body += f'\t# Not expression\n'
        self.body += f'\tSUBI {expressionResultReg1}, 0, [{stackPointer} -1]\n'
        self.body += f'\tSET [{stackPointer} -1], {expressionResultReg1}\n\n'

    def startIf(self, line, column):
        self.body += f'\t# Start of IF\n'
        self.body += f'\t{decrementRegister(stackPointer)}\n'
        self.body += f'\tJUMPNZ IF{line}:{column}, [{stackPointer}]\n'
        self.body += f'\tJUMP IF{line}:{column}__end\n'
        self.body += f'\tLABEL IF{line}:{column}\n\n'

    def endIf(self, line, column):
        self.body += f'\t# End of IF part\n'
        self.body += f'\tJUMP ELSE{line}:{column}__end\n'
        self.body += f'\tLABEL IF{line}:{column}__end\n\n'

    def endElse(self, line, column):
        self.body += f'\t# End of ELSE part\n'
        self.body += f'\tLABEL ELSE{line}:{column}__end\n\n'

    def startWhile(self, line, column):
        self.body += f'\t# Start WHILE\n'
        self.body += f'\tLABEL WHILE{line}:{column}\n\n'

    def evaluateWhile(self, line, column):
        self.body += f'\t# Evaluate WHILE expression\n'
        self.body += f'\t{decrementRegister(stackPointer)}\n'
        self.body += f'\tJUMPZ WHILE{line}:{column}__end, [{stackPointer}]\n\n'

    def endWhile(self, line, column):
        self.body += f'\t# End WHILE\n'
        self.body += f'\tJUMP WHILE{line}:{column}\n'
        self.body += f'\tLABEL WHILE{line}:{column}__end\n\n'

    def intToStringCast(self):
        self.body += f'\t# INT to STRING conversion\n'
        self.body += f'\tINT2STRING {miscRegister}, [{stackPointer}-1]\n\n'
        self.body += f'\tSET [{stackPointer}-1], {miscRegister}\n\n'

    def generateInstance(self, classSymbol: ClassSymbol):
        vmtOffset = self.vmt.getClassVmtOffset(classSymbol.id)
        self.body += f'\t# Creating new instance of object {classSymbol.id}\n'
        self.body += f'\tCREATE {chunkPointer}, {classSymbol.fieldTable.getLength() + 3}\n'
        self.body += f'\tSETWORD {chunkPointer}, 0, "{classSymbol.id}"\n'
        self.body += f'\tSETWORD {chunkPointer}, 1, [{vmtOffset}]\n'
        if classSymbol.id != 'Object':
            parentVmtOffset = self.vmt.getClassVmtOffset(classSymbol.parent.id)
            self.body += f'\tSETWORD {chunkPointer}, 2, [{parentVmtOffset}]\n'
        for index, field in enumerate(classSymbol.fieldTable.symbols.values()):
            if field.dataType == 'string':
                self.body += f'\tSETWORD {chunkPointer}, {3 + index}, ""\n'
            else:
                self.body += f'\tSETWORD {chunkPointer}, {3 + index}, 0\n'
        self.body += f'\tSET [{stackPointer}], {chunkPointer}\n'
        self.body += f'\t{incrementRegister(stackPointer)}\n\n'

    def generatePrint(self, parameters):
        self.body += f'\t# Print variables\n'
        for index, parameter in enumerate(parameters[::-1]):
            if parameter.dataType == 'string':
                self.body += f'\tWRITES [$SP{- len(parameters) + index}]\n'
            else:
                self.body += f'\tWRITEI [$SP{- len(parameters) + index}]\n'


    def __str__(self):
        return '\n'.join([self.label, self.header, self.body, self.returnCall])

class VirtualMethodTableGenerator:
    
    def __init__(self):
        self.body = ''
        self.classes = []
        self.methodsTable = {}

    def getMethodOffset(self, className, methodName):
        return self.methodsTable[className].index(methodName)

    def generateVirtualMethodTable(self, className, methods):
        if self.methodsTable.get(className) is None:
            self.methodsTable[className] = []
        self.classes.append(className)
        self.body += f'# VMT of class {className}\n'
        self.body += f'CREATE {chunkPointer}, {len(list(methods.keys()))}\n'
        self.body += f'SET [{stackPointer}], {chunkPointer}\n'
        self.body += f'{incrementRegister(stackPointer)}\n\n'
        for index, methodName in enumerate(list(methods.keys())):
            self.methodsTable[className].append(methodName)
            self.body += f'SETWORD {chunkPointer}, {index}, "{methods[methodName].ownerClass}:{methodName}"\n'
            
    def getClassVmtOffset(self, className):
        return self.classes.index(className)

    def generateCode(self):
        print(self.body)


class CodeGenerator:

    def __init__(self):
        self.header = '''#! /bin/vypint
# VYPcode: 1.0
# Generated by: xkozar02
'''
        self.functionDefinitions = {}
        self.VMTGenerator = VirtualMethodTableGenerator()
    
    def generateEmbeddedFunctions(self):
        print(toStringFunction)
        print(getClassFunction)
        print(concatenationFunction)
        print(getLengthFunction)
        print(readIntFunction)
        print(readStringFunction)
        print(subStrFunction)
        

    def generateCode(self):
        print(self.header)
        print('ALIAS FP $0')
        self.VMTGenerator.generateCode()
        print("JUMP main\n")
        self.generateEmbeddedFunctions()
        for functionKey in self.functionDefinitions:
            print(str(self.functionDefinitions[functionKey].codeGenerator) + '\n')
        print("LABEL __END")

    def generateFunctionHeader(self, function: FunctionSymbol, functionParameters):
        self.functionDefinitions[f'{function.ownerClass}:{function.id}'] = function
        functionLabel = function.id
        if function.ownerClass != "":
            functionLabel = f'{function.ownerClass}:{functionLabel}'
        function.codeGenerator = FunctionCodeGenerator(functionLabel, functionParameters.copy(), self.VMTGenerator)

    def defineVariable(self, variableName, function, dataType):
        function.codeGenerator.defineVariable(variableName, dataType)

    def generateLiteralExpression(self, function, value, literalType):
        if literalType == 'int':
            function.codeGenerator.intLiteralExpression(value)
        else:
            function.codeGenerator.stringLiteralExpression(value)

    def assignValueToVariable(self, function, variableName):
        function.codeGenerator.assignValueToVariable(variableName)

    def assignValueToField(self, function, classSymbol, variableName):
        function.codeGenerator.assignValueToField(classSymbol, variableName)

    def generateFieldExpression(self, function, classSymbol, variableName, toDecrease):
        function.codeGenerator.fieldExpression(classSymbol, variableName, toDecrease)

    def callFunction(self, function, functionToCall):
        function.codeGenerator.callFunction(functionToCall)

    def callMethod(self, function, className, method, useSuper=False):
        function.codeGenerator.callMethod(className, method, useSuper)

    def returnFromFunction(self, function):
        function.codeGenerator.returnCallCode()

    def restoreStackPointer(self, function):
        function.codeGenerator.restoreStackPointer()

    def generateReturnValue(self, function, setReturnValue):
        function.codeGenerator.generateReturnValue(setReturnValue)

    def generateVariableExpression(self, function, variable):
        function.codeGenerator.generateVariableExpression(variable)

    def generateBinaryExpression(self, function, instruction, dataType):
        function.codeGenerator.generateBinaryExpression(instruction, dataType)

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

    def generateIntToStringCast(self, function):
        function.codeGenerator.intToStringCast()

    def generateVirtualMethodTable(self, className, methods):
        self.VMTGenerator.generateVirtualMethodTable(className, methods)

    def generateInstance(self, function, classSymbol):
        function.codeGenerator.generateInstance(classSymbol)

    def decreaseStackPointer(self, function, count):
        function.codeGenerator.decreaseStackPointer(count)

    def generatePrint(self, function, parameters):
        function.codeGenerator.generatePrint(parameters)
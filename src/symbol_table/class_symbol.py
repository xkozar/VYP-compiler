'''
    project: VYPlanguage compiler
    authros: Tomáš Kožár, xkozar02
'''

from symbol_table import GeneralSymbol, SymbolType, PartialSymbolTable, PartialClassSymbolTable
from symbol_table.class_partial_symbol_table import ClassPartialSymbolTable
from compiler.custom_exceptions import SemanticGeneralError


class ClassSymbol(GeneralSymbol):

    # This constructor is only for special behaviour of Object class
    def __init__(self, identifier, parent, parentClosure=ClassPartialSymbolTable()):
        super().__init__(identifier, SymbolType.CLASS, identifier)
        self.parent = parent
        self.methodTable = PartialClassSymbolTable()
        self.fieldTable = parent.fieldTable.copy()
    
    def getParent(self):
        return self.parent

    def getMethod(self, key):
        return self.methodTable.getSymbol(key) or self.parent.getMethod(key)

    def getField(self, key):
        return self.fieldTable.getSymbol(key) or self.parent.getField(key)

    def defineField(self, variableSymbol: GeneralSymbol):
        if self.getField(variableSymbol.id):
            raise SemanticGeneralError(f"Redefinition of field \'{variableSymbol.id}\' in class \'{self.id}\'")
        self.fieldTable.addSymbol(variableSymbol.id, variableSymbol)

    def defineMethod(self, symbol):
        pass

    # Get all methods that were directly defined in this class
    def getAllClassDefinedMethods(self):
        return self.methodTable.getAllCurrentSymbols()

    def getMethodFromParents(self, key):
        return self.getParent().getMethod(key)

    def getAllAvailableMethods(self):
        if self.id == 'Object':
            return self.methodTable.getAllCurrentSymbolsAsDict()
        allMethods = self.parent.getAllAvailableMethods()
        currentMethods = self.methodTable.getAllCurrentSymbolsAsDict()
        for method in list(currentMethods.keys()):
            allMethods[method] = currentMethods[method]
        return allMethods




    def __eq__(self, other):
        if not isinstance(other, ClassSymbol):
            return False
        if isinstance(self.dataType, str):
            if self.dataType == other.dataType:
                return True
        elif self.dataType.id == other.dataType.id:
            return True
        return self.__eq__(other.getParent())
        



class StubParentSymbol:

    def __init__(self):
        self.fieldTable = PartialClassSymbolTable()

    def getMethod(self, key):
        return None

    def getField(self, key):
        return None

    def getParent(self):
        return None

class PartialSymbolTable:

    def __init__(self, parentClosure):
        self.symbols = {}
        self.__parentClosure = parentClosure

    def getSymbol(self, key: str):
        return self.symbols.get(key) or self.__parentClosure.getSymbol(key)

    def isSymbolDefined(self, key):
        if self.symbols.get(key):
            return True
        else:
            return self.__parentClosure.getSymbol(key)

    def setSymbol(self, key, symbol):
        self.symbols.update({key: symbol})

    def getParentClosure(self):
        return self.__parentClosure.getClosure()

    def getClosure(self):
        return self

    def containsKey(self, key):
        return key in self.symbols

    def __str__(self):
        return f'{{ \n {self.__parentClosure.__str__()} \n\t {self.symbols.keys()} \n }}'
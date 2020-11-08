class PartialSymbolTable:

    def __init__(self, parentClosure):
        self.symbols = {}
        self.parentClosure = parentClosure

    def getSymbol(self, key: str):
        return self.symbols.get(key) or self.parentClosure.getSymbol(key)

    def setSymbol(self, key, symbol):
        self.symbols.update({key: symbol})

    def containsKey(self, key):
        return key in self.symbols

# print(x.get('c') or "Oopsie")
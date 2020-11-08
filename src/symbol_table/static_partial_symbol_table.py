class StaticPartialSymbolTable:

    def getSymbom(self, key):
        raise SemanticGeneralError(f'No symbol with key "{key}" defined.')
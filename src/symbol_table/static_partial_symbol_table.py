from compiler import CompilerInternalError, SemanticGeneralError


class StaticPartialSymbolTable:

    def getParentClosure(self):
        raise CompilerInternalError("There is no more closures to remove.")

    def getClosure(self):
        raise CompilerInternalError("There is no more closures to remove.")
    
    def getSymbol(self, key):
        raise SemanticGeneralError(f'No symbol with key "{key}" defined.')

    def __str__(self):
        return ''

# from ..compiler.custom_exceptions import SemanticGeneralError, CompilerInternalError
import compiler

class StaticPartialSymbolTable:

    def removeClosure(self):
        raise CompilerInternalError("There is no more closures to remove.")
    
    def getSymbol(self, key):
        raise SemanticGeneralError(f'No symbol with key "{key}" defined.')
from antlr_generated.VYPListener import VYPListener
from symbol_table import *

class CustomParseTreeListener(VYPListener):
    
    def __init__(self): 
        self.symbolTable = SymbolTable()
        self.globalDefinitionTable = SymbolTable()

    def enterProgram(self, ctx):
        pass

    # Exit a parse tree produced by VYPParser#program.
    def exitProgram(self, ctx):
        pass

    # Enter a parse tree produced by VYPParser#function_definition.
    def enterFunction_definition(self, ctx):
        pass

    # Exit a parse tree produced by VYPParser#function_definition.
    def exitFunction_definition(self, ctx):
        pass

    # Enter a parse tree produced by VYPParser#function_header.
    def enterFunction_header(self, ctx):
        print("function ID", ctx.ID())
        pass

    # Exit a parse tree produced by VYPParser#function_header.
    def exitFunction_header(self, ctx):
        pass

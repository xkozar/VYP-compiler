# Generated from VYP.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VYPParser import VYPParser
else:
    from VYPParser import VYPParser

# This class defines a complete listener for a parse tree produced by VYPParser.
class VYPListener(ParseTreeListener):

    # Enter a parse tree produced by VYPParser#program.
    def enterProgram(self, ctx:VYPParser.ProgramContext):
        pass

    # Exit a parse tree produced by VYPParser#program.
    def exitProgram(self, ctx:VYPParser.ProgramContext):
        pass


    # Enter a parse tree produced by VYPParser#hello.
    def enterHello(self, ctx:VYPParser.HelloContext):
        pass

    # Exit a parse tree produced by VYPParser#hello.
    def exitHello(self, ctx:VYPParser.HelloContext):
        pass



del VYPParser
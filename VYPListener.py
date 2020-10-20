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


    # Enter a parse tree produced by VYPParser#function.
    def enterFunction(self, ctx:VYPParser.FunctionContext):
        pass

    # Exit a parse tree produced by VYPParser#function.
    def exitFunction(self, ctx:VYPParser.FunctionContext):
        pass


    # Enter a parse tree produced by VYPParser#function_header.
    def enterFunction_header(self, ctx:VYPParser.Function_headerContext):
        pass

    # Exit a parse tree produced by VYPParser#function_header.
    def exitFunction_header(self, ctx:VYPParser.Function_headerContext):
        pass


    # Enter a parse tree produced by VYPParser#function_body.
    def enterFunction_body(self, ctx:VYPParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by VYPParser#function_body.
    def exitFunction_body(self, ctx:VYPParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by VYPParser#statement.
    def enterStatement(self, ctx:VYPParser.StatementContext):
        pass

    # Exit a parse tree produced by VYPParser#statement.
    def exitStatement(self, ctx:VYPParser.StatementContext):
        pass


    # Enter a parse tree produced by VYPParser#variable_type.
    def enterVariable_type(self, ctx:VYPParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by VYPParser#variable_type.
    def exitVariable_type(self, ctx:VYPParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by VYPParser#parameter_list.
    def enterParameter_list(self, ctx:VYPParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by VYPParser#parameter_list.
    def exitParameter_list(self, ctx:VYPParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by VYPParser#next_parameter.
    def enterNext_parameter(self, ctx:VYPParser.Next_parameterContext):
        pass

    # Exit a parse tree produced by VYPParser#next_parameter.
    def exitNext_parameter(self, ctx:VYPParser.Next_parameterContext):
        pass



del VYPParser
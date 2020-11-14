# Generated from ../../VYP.g4 by ANTLR 4.8
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


    # Enter a parse tree produced by VYPParser#statement.
    def enterStatement(self, ctx:VYPParser.StatementContext):
        pass

    # Exit a parse tree produced by VYPParser#statement.
    def exitStatement(self, ctx:VYPParser.StatementContext):
        pass


    # Enter a parse tree produced by VYPParser#function_definition.
    def enterFunction_definition(self, ctx:VYPParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by VYPParser#function_definition.
    def exitFunction_definition(self, ctx:VYPParser.Function_definitionContext):
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


    # Enter a parse tree produced by VYPParser#class_definition.
    def enterClass_definition(self, ctx:VYPParser.Class_definitionContext):
        pass

    # Exit a parse tree produced by VYPParser#class_definition.
    def exitClass_definition(self, ctx:VYPParser.Class_definitionContext):
        pass


    # Enter a parse tree produced by VYPParser#class_header.
    def enterClass_header(self, ctx:VYPParser.Class_headerContext):
        pass

    # Exit a parse tree produced by VYPParser#class_header.
    def exitClass_header(self, ctx:VYPParser.Class_headerContext):
        pass


    # Enter a parse tree produced by VYPParser#class_body.
    def enterClass_body(self, ctx:VYPParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by VYPParser#class_body.
    def exitClass_body(self, ctx:VYPParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by VYPParser#class_members.
    def enterClass_members(self, ctx:VYPParser.Class_membersContext):
        pass

    # Exit a parse tree produced by VYPParser#class_members.
    def exitClass_members(self, ctx:VYPParser.Class_membersContext):
        pass


    # Enter a parse tree produced by VYPParser#variable_definition.
    def enterVariable_definition(self, ctx:VYPParser.Variable_definitionContext):
        pass

    # Exit a parse tree produced by VYPParser#variable_definition.
    def exitVariable_definition(self, ctx:VYPParser.Variable_definitionContext):
        pass


    # Enter a parse tree produced by VYPParser#multiple_variable_definition.
    def enterMultiple_variable_definition(self, ctx:VYPParser.Multiple_variable_definitionContext):
        pass

    # Exit a parse tree produced by VYPParser#multiple_variable_definition.
    def exitMultiple_variable_definition(self, ctx:VYPParser.Multiple_variable_definitionContext):
        pass


    # Enter a parse tree produced by VYPParser#variable_assignment.
    def enterVariable_assignment(self, ctx:VYPParser.Variable_assignmentContext):
        pass

    # Exit a parse tree produced by VYPParser#variable_assignment.
    def exitVariable_assignment(self, ctx:VYPParser.Variable_assignmentContext):
        pass


    # Enter a parse tree produced by VYPParser#if_else_block.
    def enterIf_else_block(self, ctx:VYPParser.If_else_blockContext):
        pass

    # Exit a parse tree produced by VYPParser#if_else_block.
    def exitIf_else_block(self, ctx:VYPParser.If_else_blockContext):
        pass


    # Enter a parse tree produced by VYPParser#if_part.
    def enterIf_part(self, ctx:VYPParser.If_partContext):
        pass

    # Exit a parse tree produced by VYPParser#if_part.
    def exitIf_part(self, ctx:VYPParser.If_partContext):
        pass


    # Enter a parse tree produced by VYPParser#else_part.
    def enterElse_part(self, ctx:VYPParser.Else_partContext):
        pass

    # Exit a parse tree produced by VYPParser#else_part.
    def exitElse_part(self, ctx:VYPParser.Else_partContext):
        pass


    # Enter a parse tree produced by VYPParser#while_block.
    def enterWhile_block(self, ctx:VYPParser.While_blockContext):
        pass

    # Exit a parse tree produced by VYPParser#while_block.
    def exitWhile_block(self, ctx:VYPParser.While_blockContext):
        pass


    # Enter a parse tree produced by VYPParser#expression.
    def enterExpression(self, ctx:VYPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by VYPParser#expression.
    def exitExpression(self, ctx:VYPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by VYPParser#literal_value.
    def enterLiteral_value(self, ctx:VYPParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by VYPParser#literal_value.
    def exitLiteral_value(self, ctx:VYPParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by VYPParser#instance_creation.
    def enterInstance_creation(self, ctx:VYPParser.Instance_creationContext):
        pass

    # Exit a parse tree produced by VYPParser#instance_creation.
    def exitInstance_creation(self, ctx:VYPParser.Instance_creationContext):
        pass


    # Enter a parse tree produced by VYPParser#instance_variable.
    def enterInstance_variable(self, ctx:VYPParser.Instance_variableContext):
        pass

    # Exit a parse tree produced by VYPParser#instance_variable.
    def exitInstance_variable(self, ctx:VYPParser.Instance_variableContext):
        pass


    # Enter a parse tree produced by VYPParser#instance_function_call.
    def enterInstance_function_call(self, ctx:VYPParser.Instance_function_callContext):
        pass

    # Exit a parse tree produced by VYPParser#instance_function_call.
    def exitInstance_function_call(self, ctx:VYPParser.Instance_function_callContext):
        pass


    # Enter a parse tree produced by VYPParser#nested_object.
    def enterNested_object(self, ctx:VYPParser.Nested_objectContext):
        pass

    # Exit a parse tree produced by VYPParser#nested_object.
    def exitNested_object(self, ctx:VYPParser.Nested_objectContext):
        pass


    # Enter a parse tree produced by VYPParser#function_call.
    def enterFunction_call(self, ctx:VYPParser.Function_callContext):
        pass

    # Exit a parse tree produced by VYPParser#function_call.
    def exitFunction_call(self, ctx:VYPParser.Function_callContext):
        pass


    # Enter a parse tree produced by VYPParser#expression_list.
    def enterExpression_list(self, ctx:VYPParser.Expression_listContext):
        pass

    # Exit a parse tree produced by VYPParser#expression_list.
    def exitExpression_list(self, ctx:VYPParser.Expression_listContext):
        pass


    # Enter a parse tree produced by VYPParser#next_expression.
    def enterNext_expression(self, ctx:VYPParser.Next_expressionContext):
        pass

    # Exit a parse tree produced by VYPParser#next_expression.
    def exitNext_expression(self, ctx:VYPParser.Next_expressionContext):
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


    # Enter a parse tree produced by VYPParser#function_parameter_definition.
    def enterFunction_parameter_definition(self, ctx:VYPParser.Function_parameter_definitionContext):
        pass

    # Exit a parse tree produced by VYPParser#function_parameter_definition.
    def exitFunction_parameter_definition(self, ctx:VYPParser.Function_parameter_definitionContext):
        pass


    # Enter a parse tree produced by VYPParser#function_parameters.
    def enterFunction_parameters(self, ctx:VYPParser.Function_parametersContext):
        pass

    # Exit a parse tree produced by VYPParser#function_parameters.
    def exitFunction_parameters(self, ctx:VYPParser.Function_parametersContext):
        pass


    # Enter a parse tree produced by VYPParser#next_parameter.
    def enterNext_parameter(self, ctx:VYPParser.Next_parameterContext):
        pass

    # Exit a parse tree produced by VYPParser#next_parameter.
    def exitNext_parameter(self, ctx:VYPParser.Next_parameterContext):
        pass



del VYPParser
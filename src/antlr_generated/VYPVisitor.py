# Generated from ../../VYP.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VYPParser import VYPParser
else:
    from VYPParser import VYPParser

# This class defines a complete generic visitor for a parse tree produced by VYPParser.

class VYPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VYPParser#program.
    def visitProgram(self, ctx:VYPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#statement.
    def visitStatement(self, ctx:VYPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#function_definition.
    def visitFunction_definition(self, ctx:VYPParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#function_header.
    def visitFunction_header(self, ctx:VYPParser.Function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#function_body.
    def visitFunction_body(self, ctx:VYPParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#class_definition.
    def visitClass_definition(self, ctx:VYPParser.Class_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#class_header.
    def visitClass_header(self, ctx:VYPParser.Class_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#class_body.
    def visitClass_body(self, ctx:VYPParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#class_members.
    def visitClass_members(self, ctx:VYPParser.Class_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#variable_definition.
    def visitVariable_definition(self, ctx:VYPParser.Variable_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#multiple_variable_definition.
    def visitMultiple_variable_definition(self, ctx:VYPParser.Multiple_variable_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#variable_assignment.
    def visitVariable_assignment(self, ctx:VYPParser.Variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#code_block.
    def visitCode_block(self, ctx:VYPParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#if_else_block.
    def visitIf_else_block(self, ctx:VYPParser.If_else_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#if_part.
    def visitIf_part(self, ctx:VYPParser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#else_part.
    def visitElse_part(self, ctx:VYPParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#while_block.
    def visitWhile_block(self, ctx:VYPParser.While_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#equality_expression.
    def visitEquality_expression(self, ctx:VYPParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#muldiv_expression.
    def visitMuldiv_expression(self, ctx:VYPParser.Muldiv_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#method_expression.
    def visitMethod_expression(self, ctx:VYPParser.Method_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#function_expression.
    def visitFunction_expression(self, ctx:VYPParser.Function_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#comparison_expression.
    def visitComparison_expression(self, ctx:VYPParser.Comparison_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#or_expression.
    def visitOr_expression(self, ctx:VYPParser.Or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#variable_expression.
    def visitVariable_expression(self, ctx:VYPParser.Variable_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#and_expression. 
    def visitAnd_expression(self, ctx:VYPParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#bracket_expression.
    def visitBracket_expression(self, ctx:VYPParser.Bracket_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#negation_expression.
    def visitNegation_expression(self, ctx:VYPParser.Negation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#plusminus_expression.
    def visitPlusminus_expression(self, ctx:VYPParser.Plusminus_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#new_expression.
    def visitNew_expression(self, ctx:VYPParser.New_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#literal_expression.
    def visitLiteral_expression(self, ctx:VYPParser.Literal_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#field_expression.
    def visitField_expression(self, ctx:VYPParser.Field_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#literal_value.
    def visitLiteral_value(self, ctx:VYPParser.Literal_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#instance_creation.
    def visitInstance_creation(self, ctx:VYPParser.Instance_creationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#instance_variable.
    def visitInstance_variable(self, ctx:VYPParser.Instance_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#instance_function_call.
    def visitInstance_function_call(self, ctx:VYPParser.Instance_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#nested_object.
    def visitNested_object(self, ctx:VYPParser.Nested_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#function_call.
    def visitFunction_call(self, ctx:VYPParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#expression_list.
    def visitExpression_list(self, ctx:VYPParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#next_expression.
    def visitNext_expression(self, ctx:VYPParser.Next_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#variable_type.
    def visitVariable_type(self, ctx:VYPParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#parameter_list.
    def visitParameter_list(self, ctx:VYPParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#function_parameter_definition.
    def visitFunction_parameter_definition(self, ctx:VYPParser.Function_parameter_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#function_parameters.
    def visitFunction_parameters(self, ctx:VYPParser.Function_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VYPParser#next_parameter.
    def visitNext_parameter(self, ctx:VYPParser.Next_parameterContext):
        return self.visitChildren(ctx)



del VYPParser
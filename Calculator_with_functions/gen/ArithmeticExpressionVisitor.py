# Generated from /home/asa/Code/Midterm_compiler/Simple-Calculator/grammar/ArithmeticExpression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticExpressionParser import ArithmeticExpressionParser
else:
    from ArithmeticExpressionParser import ArithmeticExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticExpressionParser.

class ArithmeticExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticExpressionParser#start.
    def visitStart(self, ctx:ArithmeticExpressionParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#function_definitions.
    def visitFunction_definitions(self, ctx:ArithmeticExpressionParser.Function_definitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#function_definition.
    def visitFunction_definition(self, ctx:ArithmeticExpressionParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#parameter_list.
    def visitParameter_list(self, ctx:ArithmeticExpressionParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#parameter.
    def visitParameter(self, ctx:ArithmeticExpressionParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#type.
    def visitType(self, ctx:ArithmeticExpressionParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#assigns.
    def visitAssigns(self, ctx:ArithmeticExpressionParser.AssignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#assign.
    def visitAssign(self, ctx:ArithmeticExpressionParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#return_statement.
    def visitReturn_statement(self, ctx:ArithmeticExpressionParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#id.
    def visitId(self, ctx:ArithmeticExpressionParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#expr.
    def visitExpr(self, ctx:ArithmeticExpressionParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#term.
    def visitTerm(self, ctx:ArithmeticExpressionParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_numeric.
    def visitFactor_is_numeric(self, ctx:ArithmeticExpressionParser.Factor_is_numericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_expression.
    def visitFactor_is_expression(self, ctx:ArithmeticExpressionParser.Factor_is_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_id.
    def visitFactor_is_id(self, ctx:ArithmeticExpressionParser.Factor_is_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_string.
    def visitFactor_is_string(self, ctx:ArithmeticExpressionParser.Factor_is_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#function_call.
    def visitFunction_call(self, ctx:ArithmeticExpressionParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#argument_list.
    def visitArgument_list(self, ctx:ArithmeticExpressionParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#sign.
    def visitSign(self, ctx:ArithmeticExpressionParser.SignContext):
        return self.visitChildren(ctx)



del ArithmeticExpressionParser
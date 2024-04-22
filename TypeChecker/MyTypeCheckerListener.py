# Generated from /home/asa/Code/Compiler/TypeChecker/TypeChecker.g4 by ANTLR 4.13.1
from gen.TypeCheckerListener import TypeCheckerListener
from gen.TypeCheckerParser import TypeCheckerParser

# This class defines a complete listener for a parse tree produced by TypeCheckerParser.
class MyTypeCheckerListener(TypeCheckerListener):

    def exitStart(self, ctx:TypeCheckerParser.StartContext):
        print(ctx.getChild(0).getText(), ' is ', ctx.getChild(0).value)
        print(ctx.getChild(0).rule_type)

    # Exit a parse tree produced by TypeCheckerParser#expr3.
    def exitExpr3(self, ctx:TypeCheckerParser.Expr3Context):
        ctx.value = ctx.getChild(0).value
        ctx.rule_type = ctx.getChild(0).rule_type


    # Exit a parse tree produced by TypeCheckerParser#expr2.
    def exitExpr2(self, ctx:TypeCheckerParser.Expr2Context):
        left_child_type = ctx.getChild(0).rule_type
        right_child_type = ctx.getChild(2).rule_type
        if left_child_type == "String" or right_child_type == "String":
            ctx.rule_type = "Error"
            ctx.value = ""
        elif left_child_type in ["Integer" ,"Float"]:
            if left_child_type == "Integer" and right_child_type == "Integer":
                ctx.rule_type = "Integer"
                ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
            else:
                ctx.rule_type = "Float"
                ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
        else:
            ctx.rule_type = "Float"
            ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
    # Exit a parse tree produced by TypeCheckerParser#expr1.
    def exitExpr1(self, ctx:TypeCheckerParser.Expr1Context):
        left_child_type = ctx.getChild(0).rule_type
        right_child_type = ctx.getChild(2).rule_type
        if left_child_type == "String":
            if right_child_type in ["Integer", "Float"]:
                ctx.rule_type = "String"
                ctx.value = ctx.getChild(0).value + str(ctx.getChild(2).value)
        elif left_child_type in ["Integer" ,"Float"]:
            if left_child_type == "Integer" and right_child_type == "Integer" :
                ctx.rule_type = "Integer"
                ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
            else:
                match right_child_type:
                    case "Integer" | "Float":
                        ctx.rule_type = "Float"
                        ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
                    case "String":
                        ctx.rule_type = "Error"
                        ctx.value = ""
        else:
            ctx.rule_type = "Float"
            ctx.value = ctx.getChild(0).value + ctx.getChild(2).value


    # Exit a parse tree produced by TypeCheckerParser#term2.
    def exitTerm2(self, ctx:TypeCheckerParser.Term2Context):
        left_child_type = ctx.getChild(0).rule_type
        right_child_type = ctx.getChild(2).rule_type
        if left_child_type == "String" or right_child_type == "String":
            ctx.value = ""
            ctx.rule_type = "Error"
        else:
            ctx.rule_type = "Float"
            ctx.value = ctx.getChild(0).value / ctx.getChild(2).value


    # Exit a parse tree produced by TypeCheckerParser#term3.
    def exitTerm3(self, ctx:TypeCheckerParser.Term3Context):
        ctx.value = ctx.getChild(0).value
        ctx.rule_type = ctx.getChild(0).rule_type

    # Exit a parse tree produced by TypeCheckerParser#term1.
    def exitTerm1(self, ctx:TypeCheckerParser.Term1Context):
        left_child_type = ctx.getChild(0).rule_type
        right_child_type = ctx.getChild(2).rule_type
        if left_child_type == "String" or right_child_type == "String":
            ctx.value = ""
            ctx.rule_type = "Error"
        else:
            if left_child_type == "Integer" and right_child_type == "Integer":
                ctx.rule_type = "Integer"
            else:
                ctx.rule_type = "Float"
            ctx.value = ctx.getChild(0).value * ctx.getChild(2).value


# Exit a parse tree produced by TypeCheckerParser#factString.
    def exitFactString(self, ctx:TypeCheckerParser.FactStringContext):
        ctx.rule_type = "String"
        ctx.value = ctx.getText()
    # Exit a parse tree produced by TypeCheckerParser#factInteger.
    def exitFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        ctx.rule_type = "Integer"
        ctx.value = int(ctx.getText())
    # Exit a parse tree produced by TypeCheckerParser#factFloat.
    def exitFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        ctx.rule_type = "Float"
        ctx.value = float(ctx.getText())


    # Exit a parse tree produced by TypeCheckerParser#factExpr.
    def exitFactExpr(self, ctx:TypeCheckerParser.FactExprContext):
        ctx.value = ctx.getChild(1).value
        ctx.rule_type = ctx.getChild(1).rule_type


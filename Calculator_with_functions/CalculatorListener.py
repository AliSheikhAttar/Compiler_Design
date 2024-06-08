from default_codes.ast import AST
from default_codes.make_ast_subtree import make_ast_subtree
from gen.ArithmeticExpressionListener import ArithmeticExpressionListener
from gen.ArithmeticExpressionParser import ArithmeticExpressionParser

class CalculatorListener(ArithmeticExpressionListener):
    def __init__(self, rule_names):
        self.overridden_rules = [
            'factor_is_numeric', 'factor_is_expression', 'factor_is_id', 'factor_is_string',
            'function_call', 'parameter_list', 'argument_list', 'function_definition', 'return_statement'
        ]
        self.binary_operator_list = ['term', 'expr', 'assign']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
                make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
            else:
                make_ast_subtree(self.ast, ctx, rule_name)

    def exitFactor_is_numeric(self, ctx: ArithmeticExpressionParser.Factor_is_numericContext):
        make_ast_subtree(self.ast, ctx, ctx.getText(), True)

    def exitFactor_is_expression(self, ctx: ArithmeticExpressionParser.Factor_is_expressionContext):
        make_ast_subtree(self.ast, ctx, 'expression')

    def exitFactor_is_id(self, ctx: ArithmeticExpressionParser.Factor_is_idContext):
        make_ast_subtree(self.ast, ctx, 'id')

    def exitFactor_is_string(self, ctx: ArithmeticExpressionParser.Factor_is_stringContext):
        make_ast_subtree(self.ast, ctx, 'string')

    def exitFunction_call(self, ctx: ArithmeticExpressionParser.Function_callContext):
        make_ast_subtree(self.ast, ctx, 'function_call')
        print("exit_Function_call", ctx.getText())

    def exitParameter_list(self, ctx: ArithmeticExpressionParser.Parameter_listContext):
        make_ast_subtree(self.ast, ctx, 'parameter_list')

    def exitArgument_list(self, ctx: ArithmeticExpressionParser.Argument_listContext):
        make_ast_subtree(self.ast, ctx, 'argument_list')

    def exitFunction_definition(self, ctx: ArithmeticExpressionParser.Function_definitionContext):
        make_ast_subtree(self.ast, ctx, 'function_definition')
        # idPntr = self.ast.make_node(self.ast, ctx, 'xx')
        # assPntr = self.ast.make_node(self.ast, ctx, 'function_definition')
        # ctx.value_attr = assPntr
        # self.ast.root = assPntr

    def exitReturn_statement(self, ctx: ArithmeticExpressionParser.Return_statementContext):
        make_ast_subtree(self.ast, ctx, 'return_statement')

    def exitAssign(self, ctx: ArithmeticExpressionParser.AssignContext):
        make_ast_subtree(self.ast, ctx, 'assign')

import queue
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from gen.AssignmentStatementListener import AssignmentStatementListener
from gen.AssignmentStatementParser import AssignmentStatementParser

class ASTListener(AssignmentStatementListener):
    def __init__(self):
        self.ast = AST()               # Data structure for holding the abstract syntax tree
        self.q = queue.Queue()         # Use to print and visualize InClassPresentation
        self.g = nx.DiGraph()          # Use to visualize InClassPresentation
        self.max_x = 0
        self.symbolTable ={}
    # -------------------------------------------------------
    def draw_tree(self, node, x, y):
        if node is None:
             return
        # Draw the node
        if x < self.max_x:
            x = self.max_x
        plt.plot(x, y, 'o', markersize=15, color='cyan')
        plt.text(x, y, str(node.value), ha='center', va='center')
        print("x = ", x, "max_x ", self.max_x," y = ", y, " nd: ", node.value)
        if node.brother is not None:
            print("brother of ", node.value, " is", node.brother.value)
        if node.child is not None:
            print("child of ", node.value, " is", node.child.value)

        # Draw the vertical line to the first child
        if node.child is not None:
            plt.plot([x, x], [y - 0.1, y - 1], 'k-', linewidth=2, color = 'red')
            self.draw_tree(node.child, x, y - 1)

        # Draw the horizontal line to the first brother
        if node.brother is not None:
            plt.plot([x + 0.1, self.max_x +  1], [y, y], 'k-', linewidth=2, color = 'red')
            print("----x is :", x, "self.max_x ", self.max_x )
            self.max_x += 1
            self.draw_tree(node.brother, x + 1, y)
    def transform_binary_tree(self, root):
        if root is None:
            return None

        tree=ttk.Treeview()
        nodes={}

        def traverse(node, parent, iid=None):
            if node is None:
                return

            node_id=len(nodes)
            nodes[node_id]=node

            if parent is None:
                iid=tree.insert('', 'end', text=str(node.value))
            else:
                iid=tree.insert(parent, 'end', text=str(node.value))

            traverse(node.child, iid)
            traverse(node.brother, parent)

        traverse(root, None)
        return tree
    def display_treeview(self, tree):
        tree.pack()
        tk.mainloop()

    # Make a subtree for a given parsa tree node, tree node.
    def make_AST_subtree(self, tree_node, opertor):
        first_child = None
        brother = None
        no_children = tree_node.getChildCount()
        for i in range(0, no_children):
            next_child = tree_node.getChild(i)
            if(hasattr(next_child, 'value_attr')):
                print("i = ", i, "count = ", no_children, next_child.value_attr.value)
                if first_child == None:
                    first_child = next_child.value_attr
                if brother != None:
                    brother.value_attr.brother = next_child.value_attr
                brother = next_child
        sub_tree_pntr = self.ast.make_node(value=opertor, child=first_child, brother=None)
        tree_node.value_attr = sub_tree_pntr
        self.ast.root = sub_tree_pntr
        # print(self.ast.root)

    # -------------------------------------------------------

    def exitStart(self, ctx: AssignmentStatementParser.StartContext):
        #self.print_tree(node=self.ast.root, level=1)
        # Draw the tree
        print("*********************************************************")
        print(self.symbolTable)
        self.draw_tree(node=self.ast.root, x = 0, y = 0)
        tree = self.transform_binary_tree(self.ast.root)
        #self.display_treeview(tree)
        
        # Show the plot
        #plt.axis('off')
        print("Bye")
        # Save the plot to a file
        plt.savefig('tree.png')
        print('tree.png')
        plt.show()

    def exitStatement(self, ctx: AssignmentStatementParser.StatementContext):
        ctx.value_attr = ctx.getChild(0).value_attr

    def exitCompoundst(self, ctx:AssignmentStatementParser.CompoundstContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "block")
        # ctx.type_attr = ctx.statement().type_attr

    def exitIfst(self, ctx: AssignmentStatementParser.IfstContext):
        self.make_AST_subtree(tree_node=ctx, opertor = "if")

    def exitForst(self, ctx:AssignmentStatementParser.ForstContext):
        self.make_AST_subtree(tree_node=ctx, opertor="for")

    def exitWhilest(self, ctx:AssignmentStatementParser.WhilestContext):
        self.make_AST_subtree(tree_node=ctx, opertor="while")

    def exitCond(self, ctx:AssignmentStatementParser.CondContext):
        self.make_AST_subtree(tree_node=ctx, opertor= ctx.RELOP().getText())

        # TypeCkecking
        if ctx.expr(0).type_attr != ctx.expr(1).type_attr:
            print("incompatible type attributes in condition")
    def exitCase(self, ctx:AssignmentStatementParser.CasestContext):
        self.make_AST_subtree(tree_node=ctx,opertor='Case')

    def exitVariable_declaration(self, ctx:AssignmentStatementParser.Variable_declarationContext):
        IDchilds = ctx.getChildCount()-2 # we minused 2 because of the last two tokens which are {type} and ":"
        # add variables and their types to the dictionary
        for i in range(0,IDchilds,2):
            self.symbolTable[ctx.getChild(i).getText()] = ctx.type_().getText()

    def exitAssign(self, ctx: AssignmentStatementParser.AssignContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=ctx.expr().value_attr)
        assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        ctx.value_attr = assPntr
        self.ast.root = assPntr

        # type checking
        if ctx.expr().type_attr != self.symbolTable[ctx.ID().getText()]:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(f'{ctx.ID().getText()}   {self.symbolTable[ctx.ID().getText()]} ')
            print(ctx.expr().type_attr)
            print("uncompatible types")
        else:
            print(f'{ctx.ID().getText()}   {self.symbolTable[ctx.ID().getText()]} ')
            print(ctx.expr().type_attr)
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("compatible types")

    def arithTypeChecking(self,ctx):
        if ctx.getChild(0).type_attr == "string" or ctx.getChild(2).type_attr == "string":
            print("Type error: No arith operation for strings!")
        elif ctx.getChild(0).type_attr == "float" or ctx.getChild(2).type_attr == "float":
            ctx.type_attr = "float"
        else:
            ctx.type_attr = "int"

    def exitExpr_term_plus(self, ctx: AssignmentStatementParser.Expr_term_plusContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "+")
        self.arithTypeChecking(ctx)
    def exitExpr_term_minus(self, ctx: AssignmentStatementParser.Expr_term_plusContext):
        self.make_AST_subtree(tree_node= ctx, opertor = "-")
        self.arithTypeChecking(ctx)

    def exitTerm4(self, ctx: AssignmentStatementParser.Term4Context):
        ctx.value_attr = ctx.term().value_attr
        ctx.type_attr = ctx.term().type_attr

    def exitTerm_fact_mutiply(self, ctx: AssignmentStatementParser.Term_fact_mutiplyContext):
        self.make_AST_subtree(tree_node= ctx, opertor = "*")
        self.arithTypeChecking(ctx)
    def exitTerm_fact_divide(self, ctx: AssignmentStatementParser.Term_fact_divideContext):
        self.make_AST_subtree(tree_node= ctx, opertor = "/")
        self.arithTypeChecking(ctx)
    def exitFactor3(self, ctx: AssignmentStatementParser.Factor3Context):
        ctx.value_attr = ctx.factor().value_attr
        ctx.type_attr = ctx.factor().type_attr

    def exitFact_expr(self, ctx: AssignmentStatementParser.Fact_exprContext):
        ctx.value_attr = ctx.expr().value_attr
        ctx.type_attr = ctx.getChild(1).type_attr

    def exitFact_id(self, ctx: AssignmentStatementParser.Fact_idContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=None)
        ctx.value_attr = idPntr
        ctx.type_attr = self.symbolTable[ctx.ID().getText()]

    def exitFact_number(self, ctx: AssignmentStatementParser.Fact_numberContext):
        ctx.value_attr = ctx.number().value_attr
        ctx.type_attr = ctx.number().type_attr

    def exitNumber_float(self, ctx: AssignmentStatementParser.Number_floatContext):
        numberPntr = self.ast.make_node(value=ctx.FLOAT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr
        ctx.type_attr = 'float'

    def exitNumber_int(self, ctx: AssignmentStatementParser.Number_intContext):
        numberPntr = self.ast.make_node(value=ctx.INT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr
        ctx.type_attr = 'int'
    # Exit a parse tree produced by AssignmentStatementParser#trnbody.
    def exitTrnbody(self, ctx:AssignmentStatementParser.TrnbodyContext):
        # condptr = self.ast.make_node(value=ctx.getChild(0))
        self.make_AST_subtree(ctx,':')
        print("ext trnbody")
        print(self.ast.root)

    # Exit a parse tree produced by AssignmentStatementParser#simpletrn.
    def exitSimpletrn(self, ctx:AssignmentStatementParser.SimpletrnContext):
        self.make_AST_subtree(ctx,'?')
        print("ext simpletrn")
        print(self.ast.root)

    # Enter a parse tree produced by AssignmentStatementParser#compoundtrn.
    def exitCompoundtrn(self, ctx:AssignmentStatementParser.CompoundtrnContext):
        # idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=ctx.simpletrn().value_attr)
        # assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        # ctx.value_attr = assPntr
        # self.ast.root = assPntr
        self.make_AST_subtree(ctx,":=")
        print("ext compuntdtrn")
        print(self.ast.root)

class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother

class AST:
    def __init__(self):
        self.root = None
        self.current = None

    def make_node(self, value, child, brother):
        tree_node = TreeNode(value, child, brother)
        self.current = tree_node
        return tree_node

    def add_child(self, node, new_child):
        if node.child is None:
            node.child = new_child
        else:
            self.current = node.child
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_child
        self.current = new_child

    def add_brother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
        else:
            self.current = node.brother
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_brother
        self.current = new_brother



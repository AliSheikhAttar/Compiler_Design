from antlr4 import *
from gen.AssignmentStatementParser import AssignmentStatementParser
from gen.AssignmentStatementLexer import  AssignmentStatementLexer
from Code.CustomASTListener import ASTListener
import argparse
import queue
import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    print('Input language_apps:\n{0}'.format(stream))
    print('Result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = AssignmentStatementLexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = AssignmentStatementParser(token_stream)
    # Step 5: Create parse tree
    parse_tree = parser.start()
    # Step 6: Create an instance of AssignmentStListener
    ast_generator = ASTListener()

    # Step 7(a): Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_generator)
    print("\n Finished")

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input6.txt')
    args = argparser.parse_args()
    main(args)

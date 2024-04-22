from antlr4 import *
from MyTypeCheckerListener import MyTypeCheckerListener
from gen.TypeCheckerLexer import TypeCheckerLexer
from gen.TypeCheckerParser import TypeCheckerParser

input_expression = input("Enter an arithmetic expression: ")
lexer = TypeCheckerLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = TypeCheckerParser(token_stream)
parse_tree = parser.start()
listener = MyTypeCheckerListener()
walker = ParseTreeWalker()
walker.walk(listener, parse_tree)

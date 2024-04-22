from antlr4 import *
from MySTGrammarListener import MySTGrammarListener
from gen.STGrammarLexer import STGrammarLexer
from gen.STGrammarParser import STGrammarParser



input_expression = input("Enter an arithmetic expression: ")
lexer = STGrammarLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = STGrammarParser(token_stream)
parse_tree = parser.start()
listener = MySTGrammarListener()
walker = ParseTreeWalker()
walker.walk(listener, parse_tree)

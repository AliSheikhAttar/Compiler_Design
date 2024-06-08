# Generated from /home/asa/Code/Midterm_compiler/Simple-Calculator/grammar/ArithmeticExpression.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,170,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,3,0,34,8,0,1,0,1,0,1,0,1,1,1,1,4,1,41,8,
        1,11,1,12,1,42,1,1,5,1,46,8,1,10,1,12,1,49,9,1,1,1,5,1,52,8,1,10,
        1,12,1,55,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,3,3,80,8,3,1,4,
        1,4,1,4,1,5,1,5,1,6,1,6,1,6,5,6,90,8,6,10,6,12,6,93,9,6,1,6,5,6,
        96,8,6,10,6,12,6,99,9,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,10,
        1,10,1,10,3,10,113,8,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,121,8,
        10,10,10,12,10,124,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,5,11,135,8,11,10,11,12,11,138,9,11,1,12,3,12,141,8,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,150,8,12,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,5,14,160,8,14,10,14,12,14,163,9,14,1,14,3,14,
        166,8,14,1,15,1,15,1,15,0,2,20,22,16,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,0,2,2,0,1,1,5,6,1,0,9,10,172,0,33,1,0,0,0,2,38,1,
        0,0,0,4,56,1,0,0,0,6,79,1,0,0,0,8,81,1,0,0,0,10,84,1,0,0,0,12,86,
        1,0,0,0,14,100,1,0,0,0,16,104,1,0,0,0,18,107,1,0,0,0,20,112,1,0,
        0,0,22,125,1,0,0,0,24,149,1,0,0,0,26,151,1,0,0,0,28,165,1,0,0,0,
        30,167,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,33,34,1,0,0,0,34,35,1,
        0,0,0,35,36,3,12,6,0,36,37,5,0,0,1,37,1,1,0,0,0,38,47,3,4,2,0,39,
        41,5,18,0,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,
        0,0,43,44,1,0,0,0,44,46,3,4,2,0,45,40,1,0,0,0,46,49,1,0,0,0,47,45,
        1,0,0,0,47,48,1,0,0,0,48,53,1,0,0,0,49,47,1,0,0,0,50,52,5,18,0,0,
        51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,3,1,0,
        0,0,55,53,1,0,0,0,56,57,5,1,0,0,57,58,5,19,0,0,58,59,5,13,0,0,59,
        60,3,6,3,0,60,61,5,14,0,0,61,62,5,18,0,0,62,63,5,2,0,0,63,64,5,18,
        0,0,64,65,3,12,6,0,65,66,5,18,0,0,66,67,3,16,8,0,67,68,5,18,0,0,
        68,69,5,3,0,0,69,5,1,0,0,0,70,75,3,8,4,0,71,72,5,4,0,0,72,74,3,8,
        4,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,80,
        1,0,0,0,77,75,1,0,0,0,78,80,1,0,0,0,79,70,1,0,0,0,79,78,1,0,0,0,
        80,7,1,0,0,0,81,82,3,10,5,0,82,83,5,19,0,0,83,9,1,0,0,0,84,85,7,
        0,0,0,85,11,1,0,0,0,86,91,3,14,7,0,87,88,5,18,0,0,88,90,3,14,7,0,
        89,87,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,97,1,
        0,0,0,93,91,1,0,0,0,94,96,5,18,0,0,95,94,1,0,0,0,96,99,1,0,0,0,97,
        95,1,0,0,0,97,98,1,0,0,0,98,13,1,0,0,0,99,97,1,0,0,0,100,101,3,18,
        9,0,101,102,5,7,0,0,102,103,3,20,10,0,103,15,1,0,0,0,104,105,5,8,
        0,0,105,106,3,20,10,0,106,17,1,0,0,0,107,108,5,19,0,0,108,19,1,0,
        0,0,109,110,6,10,-1,0,110,113,3,22,11,0,111,113,3,26,13,0,112,109,
        1,0,0,0,112,111,1,0,0,0,113,122,1,0,0,0,114,115,10,4,0,0,115,116,
        5,9,0,0,116,121,3,20,10,5,117,118,10,3,0,0,118,119,5,10,0,0,119,
        121,3,20,10,4,120,114,1,0,0,0,120,117,1,0,0,0,121,124,1,0,0,0,122,
        120,1,0,0,0,122,123,1,0,0,0,123,21,1,0,0,0,124,122,1,0,0,0,125,126,
        6,11,-1,0,126,127,3,24,12,0,127,136,1,0,0,0,128,129,10,3,0,0,129,
        130,5,11,0,0,130,135,3,22,11,4,131,132,10,2,0,0,132,133,5,12,0,0,
        133,135,3,22,11,3,134,128,1,0,0,0,134,131,1,0,0,0,135,138,1,0,0,
        0,136,134,1,0,0,0,136,137,1,0,0,0,137,23,1,0,0,0,138,136,1,0,0,0,
        139,141,3,30,15,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,
        0,142,150,5,15,0,0,143,144,5,13,0,0,144,145,3,20,10,0,145,146,5,
        14,0,0,146,150,1,0,0,0,147,150,5,19,0,0,148,150,5,16,0,0,149,140,
        1,0,0,0,149,143,1,0,0,0,149,147,1,0,0,0,149,148,1,0,0,0,150,25,1,
        0,0,0,151,152,5,19,0,0,152,153,5,13,0,0,153,154,3,28,14,0,154,155,
        5,14,0,0,155,27,1,0,0,0,156,161,3,20,10,0,157,158,5,4,0,0,158,160,
        3,20,10,0,159,157,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,166,1,0,0,0,163,161,1,0,0,0,164,166,1,0,0,0,165,156,
        1,0,0,0,165,164,1,0,0,0,166,29,1,0,0,0,167,168,7,1,0,0,168,31,1,
        0,0,0,17,33,42,47,53,75,79,91,97,112,120,122,134,136,140,149,161,
        165
    ]

class ArithmeticExpressionParser ( Parser ):

    grammarFileName = "ArithmeticExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'string'", "'begin'", "'end'", "','", 
                     "'int'", "'float'", "'='", "'return'", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ADD", "SUB", "MUL", "DIV", "LPAREN", 
                      "RPAREN", "NUMERICALVALUE", "STRING", "WS", "NEWLINE", 
                      "ID" ]

    RULE_start = 0
    RULE_function_definitions = 1
    RULE_function_definition = 2
    RULE_parameter_list = 3
    RULE_parameter = 4
    RULE_type = 5
    RULE_assigns = 6
    RULE_assign = 7
    RULE_return_statement = 8
    RULE_id = 9
    RULE_expr = 10
    RULE_term = 11
    RULE_factor = 12
    RULE_function_call = 13
    RULE_argument_list = 14
    RULE_sign = 15

    ruleNames =  [ "start", "function_definitions", "function_definition", 
                   "parameter_list", "parameter", "type", "assigns", "assign", 
                   "return_statement", "id", "expr", "term", "factor", "function_call", 
                   "argument_list", "sign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ADD=9
    SUB=10
    MUL=11
    DIV=12
    LPAREN=13
    RPAREN=14
    NUMERICALVALUE=15
    STRING=16
    WS=17
    NEWLINE=18
    ID=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigns(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.AssignsContext,0)


        def EOF(self):
            return self.getToken(ArithmeticExpressionParser.EOF, 0)

        def function_definitions(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.Function_definitionsContext,0)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ArithmeticExpressionParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 32
                self.function_definitions()


            self.state = 35
            self.assigns()
            self.state = 36
            self.match(ArithmeticExpressionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.Function_definitionContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.Function_definitionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticExpressionParser.NEWLINE)
            else:
                return self.getToken(ArithmeticExpressionParser.NEWLINE, i)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_function_definitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definitions" ):
                listener.enterFunction_definitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definitions" ):
                listener.exitFunction_definitions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definitions" ):
                return visitor.visitFunction_definitions(self)
            else:
                return visitor.visitChildren(self)




    def function_definitions(self):

        localctx = ArithmeticExpressionParser.Function_definitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_definitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.function_definition()
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 39
                        self.match(ArithmeticExpressionParser.NEWLINE)
                        self.state = 42 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==18):
                            break

                    self.state = 44
                    self.function_definition() 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 50
                self.match(ArithmeticExpressionParser.NEWLINE)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticExpressionParser.LPAREN, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.Parameter_listContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticExpressionParser.RPAREN, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticExpressionParser.NEWLINE)
            else:
                return self.getToken(ArithmeticExpressionParser.NEWLINE, i)

        def assigns(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.AssignsContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition" ):
                listener.enterFunction_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition" ):
                listener.exitFunction_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = ArithmeticExpressionParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ArithmeticExpressionParser.T__0)
            self.state = 57
            self.match(ArithmeticExpressionParser.ID)
            self.state = 58
            self.match(ArithmeticExpressionParser.LPAREN)
            self.state = 59
            self.parameter_list()
            self.state = 60
            self.match(ArithmeticExpressionParser.RPAREN)
            self.state = 61
            self.match(ArithmeticExpressionParser.NEWLINE)
            self.state = 62
            self.match(ArithmeticExpressionParser.T__1)
            self.state = 63
            self.match(ArithmeticExpressionParser.NEWLINE)
            self.state = 64
            self.assigns()
            self.state = 65
            self.match(ArithmeticExpressionParser.NEWLINE)
            self.state = 66
            self.return_statement()
            self.state = 67
            self.match(ArithmeticExpressionParser.NEWLINE)
            self.state = 68
            self.match(ArithmeticExpressionParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.ParameterContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.ParameterContext,i)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ArithmeticExpressionParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.parameter()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 71
                    self.match(ArithmeticExpressionParser.T__3)
                    self.state = 72
                    self.parameter()
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.TypeContext,0)


        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ArithmeticExpressionParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.type_()
            self.state = 82
            self.match(ArithmeticExpressionParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ArithmeticExpressionParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 98) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.AssignContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.AssignContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticExpressionParser.NEWLINE)
            else:
                return self.getToken(ArithmeticExpressionParser.NEWLINE, i)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_assigns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigns" ):
                listener.enterAssigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigns" ):
                listener.exitAssigns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigns" ):
                return visitor.visitAssigns(self)
            else:
                return visitor.visitChildren(self)




    def assigns(self):

        localctx = ArithmeticExpressionParser.AssignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assigns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.assign()
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87
                    self.match(ArithmeticExpressionParser.NEWLINE)
                    self.state = 88
                    self.assign() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.match(ArithmeticExpressionParser.NEWLINE) 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.IdContext,0)


        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ArithmeticExpressionParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.id_()
            self.state = 101
            self.match(ArithmeticExpressionParser.T__6)
            self.state = 102
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ArithmeticExpressionParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ArithmeticExpressionParser.T__7)
            self.state = 105
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = ArithmeticExpressionParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ArithmeticExpressionParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.TermContext,0)


        def function_call(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.Function_callContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,i)


        def ADD(self):
            return self.getToken(ArithmeticExpressionParser.ADD, 0)

        def SUB(self):
            return self.getToken(ArithmeticExpressionParser.SUB, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExpressionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 110
                self.term(0)
                pass

            elif la_ == 2:
                self.state = 111
                self.function_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 120
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExpressionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 114
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 115
                        self.match(ArithmeticExpressionParser.ADD)
                        self.state = 116
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExpressionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 117
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 118
                        self.match(ArithmeticExpressionParser.SUB)
                        self.state = 119
                        self.expr(4)
                        pass

             
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.FactorContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.TermContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.TermContext,i)


        def MUL(self):
            return self.getToken(ArithmeticExpressionParser.MUL, 0)

        def DIV(self):
            return self.getToken(ArithmeticExpressionParser.DIV, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExpressionParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExpressionParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 128
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 129
                        self.match(ArithmeticExpressionParser.MUL)
                        self.state = 130
                        self.term(4)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExpressionParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 131
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 132
                        self.match(ArithmeticExpressionParser.DIV)
                        self.state = 133
                        self.term(3)
                        pass

             
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Factor_is_stringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExpressionParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ArithmeticExpressionParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_string" ):
                listener.enterFactor_is_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_string" ):
                listener.exitFactor_is_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_string" ):
                return visitor.visitFactor_is_string(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_expressionContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExpressionParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ArithmeticExpressionParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ArithmeticExpressionParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_expression" ):
                listener.enterFactor_is_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_expression" ):
                listener.exitFactor_is_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_expression" ):
                return visitor.visitFactor_is_expression(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_idContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExpressionParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_id" ):
                listener.enterFactor_is_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_id" ):
                listener.exitFactor_is_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_id" ):
                return visitor.visitFactor_is_id(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_numericContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExpressionParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERICALVALUE(self):
            return self.getToken(ArithmeticExpressionParser.NUMERICALVALUE, 0)
        def sign(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.SignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_numeric" ):
                listener.enterFactor_is_numeric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_numeric" ):
                listener.exitFactor_is_numeric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_numeric" ):
                return visitor.visitFactor_is_numeric(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = ArithmeticExpressionParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 15]:
                localctx = ArithmeticExpressionParser.Factor_is_numericContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9 or _la==10:
                    self.state = 139
                    self.sign()


                self.state = 142
                self.match(ArithmeticExpressionParser.NUMERICALVALUE)
                pass
            elif token in [13]:
                localctx = ArithmeticExpressionParser.Factor_is_expressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(ArithmeticExpressionParser.LPAREN)
                self.state = 144
                self.expr(0)
                self.state = 145
                self.match(ArithmeticExpressionParser.RPAREN)
                pass
            elif token in [19]:
                localctx = ArithmeticExpressionParser.Factor_is_idContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(ArithmeticExpressionParser.ID)
                pass
            elif token in [16]:
                localctx = ArithmeticExpressionParser.Factor_is_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.match(ArithmeticExpressionParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticExpressionParser.LPAREN, 0)

        def argument_list(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.Argument_listContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticExpressionParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ArithmeticExpressionParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ArithmeticExpressionParser.ID)
            self.state = 152
            self.match(ArithmeticExpressionParser.LPAREN)
            self.state = 153
            self.argument_list()
            self.state = 154
            self.match(ArithmeticExpressionParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,i)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_list" ):
                listener.enterArgument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_list" ):
                listener.exitArgument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = ArithmeticExpressionParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 13, 15, 16, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.expr(0)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 157
                    self.match(ArithmeticExpressionParser.T__3)
                    self.state = 158
                    self.expr(0)
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ArithmeticExpressionParser.ADD, 0)

        def SUB(self):
            return self.getToken(ArithmeticExpressionParser.SUB, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = ArithmeticExpressionParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        self._predicates[11] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





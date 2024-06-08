# Generated from F:/Term7/Compiler/13. AST-builder/13. AST-builder/AssignmentStatement.g4 by ANTLR 4.13.1
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
        4,1,39,285,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,5,0,47,8,0,10,0,12,0,50,9,0,1,0,1,0,1,1,1,
        1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,5,1,63,8,1,10,1,12,1,66,9,
        1,1,1,4,1,69,8,1,11,1,12,1,70,1,1,1,1,1,2,1,2,5,2,77,8,2,10,2,12,
        2,80,9,2,1,2,1,2,5,2,84,8,2,10,2,12,2,87,9,2,4,2,89,8,2,11,2,12,
        2,90,1,3,1,3,1,3,5,3,96,8,3,10,3,12,3,99,9,3,1,3,1,3,1,3,1,4,1,4,
        1,5,1,5,5,5,108,8,5,10,5,12,5,111,9,5,1,5,1,5,4,5,115,8,5,11,5,12,
        5,116,4,5,119,8,5,11,5,12,5,120,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,132,8,6,1,7,1,7,1,7,1,7,5,7,138,8,7,10,7,12,7,141,9,7,1,
        7,1,7,5,7,145,8,7,10,7,12,7,148,9,7,1,7,1,7,5,7,152,8,7,10,7,12,
        7,155,9,7,1,7,3,7,158,8,7,1,8,1,8,1,8,1,8,5,8,164,8,8,10,8,12,8,
        167,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,177,8,9,10,9,12,9,180,
        9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,
        11,194,8,11,10,11,12,11,197,9,11,1,11,1,11,1,11,3,11,202,8,11,1,
        11,4,11,205,8,11,11,11,12,11,206,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,1,14,1,14,3,14,219,8,14,1,14,1,14,1,14,3,14,224,8,14,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,247,8,17,10,17,12,17,250,
        9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,261,8,18,
        10,18,12,18,264,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        274,8,19,1,20,1,20,3,20,278,8,20,1,21,1,21,1,21,3,21,283,8,21,1,
        21,0,2,34,36,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,0,1,1,0,5,7,302,0,44,1,0,0,0,2,53,1,0,0,0,4,74,1,0,0,
        0,6,92,1,0,0,0,8,103,1,0,0,0,10,105,1,0,0,0,12,131,1,0,0,0,14,133,
        1,0,0,0,16,159,1,0,0,0,18,170,1,0,0,0,20,183,1,0,0,0,22,204,1,0,
        0,0,24,208,1,0,0,0,26,212,1,0,0,0,28,218,1,0,0,0,30,225,1,0,0,0,
        32,230,1,0,0,0,34,234,1,0,0,0,36,251,1,0,0,0,38,273,1,0,0,0,40,277,
        1,0,0,0,42,282,1,0,0,0,44,48,3,2,1,0,45,47,5,37,0,0,46,45,1,0,0,
        0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,
        1,0,0,0,51,52,5,0,0,1,52,1,1,0,0,0,53,54,5,1,0,0,54,58,5,31,0,0,
        55,57,5,37,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,
        0,0,0,59,64,1,0,0,0,60,58,1,0,0,0,61,63,3,4,2,0,62,61,1,0,0,0,63,
        66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,
        0,67,69,5,37,0,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,72,1,0,0,0,72,73,3,10,5,0,73,3,1,0,0,0,74,78,5,2,0,0,
        75,77,5,37,0,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,
        0,0,0,79,88,1,0,0,0,80,78,1,0,0,0,81,85,3,6,3,0,82,84,5,37,0,0,83,
        82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,89,1,0,0,
        0,87,85,1,0,0,0,88,81,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,
        1,0,0,0,91,5,1,0,0,0,92,97,5,31,0,0,93,94,5,3,0,0,94,96,5,31,0,0,
        95,93,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,
        0,0,0,99,97,1,0,0,0,100,101,5,4,0,0,101,102,3,8,4,0,102,7,1,0,0,
        0,103,104,7,0,0,0,104,9,1,0,0,0,105,109,5,8,0,0,106,108,5,37,0,0,
        107,106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,
        110,118,1,0,0,0,111,109,1,0,0,0,112,114,3,12,6,0,113,115,5,37,0,
        0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,
        0,117,119,1,0,0,0,118,112,1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,
        0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,5,9,0,0,123,11,1,0,0,0,
        124,132,3,14,7,0,125,132,3,32,16,0,126,132,3,10,5,0,127,132,3,18,
        9,0,128,132,3,16,8,0,129,132,3,20,10,0,130,132,3,30,15,0,131,124,
        1,0,0,0,131,125,1,0,0,0,131,126,1,0,0,0,131,127,1,0,0,0,131,128,
        1,0,0,0,131,129,1,0,0,0,131,130,1,0,0,0,132,13,1,0,0,0,133,134,5,
        10,0,0,134,135,3,24,12,0,135,139,5,11,0,0,136,138,5,37,0,0,137,136,
        1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,
        1,0,0,0,141,139,1,0,0,0,142,146,3,12,6,0,143,145,5,37,0,0,144,143,
        1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,157,
        1,0,0,0,148,146,1,0,0,0,149,153,5,12,0,0,150,152,5,37,0,0,151,150,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,156,
        1,0,0,0,155,153,1,0,0,0,156,158,3,12,6,0,157,149,1,0,0,0,157,158,
        1,0,0,0,158,15,1,0,0,0,159,160,5,13,0,0,160,161,3,24,12,0,161,165,
        5,14,0,0,162,164,5,37,0,0,163,162,1,0,0,0,164,167,1,0,0,0,165,163,
        1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,165,1,0,0,0,168,169,
        3,12,6,0,169,17,1,0,0,0,170,171,5,15,0,0,171,172,3,32,16,0,172,173,
        5,16,0,0,173,174,3,40,20,0,174,178,5,14,0,0,175,177,5,37,0,0,176,
        175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        181,1,0,0,0,180,178,1,0,0,0,181,182,3,10,5,0,182,19,1,0,0,0,183,
        184,5,17,0,0,184,185,5,31,0,0,185,186,5,18,0,0,186,187,5,37,0,0,
        187,188,3,22,11,0,188,189,5,9,0,0,189,21,1,0,0,0,190,195,5,31,0,
        0,191,192,5,3,0,0,192,194,5,31,0,0,193,191,1,0,0,0,194,197,1,0,0,
        0,195,193,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,195,1,0,0,
        0,198,201,5,4,0,0,199,202,3,36,18,0,200,202,5,30,0,0,201,199,1,0,
        0,0,201,200,1,0,0,0,202,203,1,0,0,0,203,205,5,37,0,0,204,190,1,0,
        0,0,205,206,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,23,1,0,0,
        0,208,209,3,34,17,0,209,210,5,38,0,0,210,211,3,34,17,0,211,25,1,
        0,0,0,212,213,3,24,12,0,213,214,5,19,0,0,214,215,3,28,14,0,215,27,
        1,0,0,0,216,219,3,34,17,0,217,219,3,26,13,0,218,216,1,0,0,0,218,
        217,1,0,0,0,219,220,1,0,0,0,220,223,5,4,0,0,221,224,3,26,13,0,222,
        224,3,34,17,0,223,221,1,0,0,0,223,222,1,0,0,0,224,29,1,0,0,0,225,
        226,5,31,0,0,226,227,5,20,0,0,227,228,3,26,13,0,228,229,5,21,0,0,
        229,31,1,0,0,0,230,231,5,31,0,0,231,232,5,20,0,0,232,233,3,34,17,
        0,233,33,1,0,0,0,234,235,6,17,-1,0,235,236,3,36,18,0,236,248,1,0,
        0,0,237,238,10,4,0,0,238,239,5,22,0,0,239,247,3,36,18,0,240,241,
        10,3,0,0,241,242,5,23,0,0,242,247,3,36,18,0,243,244,10,2,0,0,244,
        245,5,38,0,0,245,247,3,36,18,0,246,237,1,0,0,0,246,240,1,0,0,0,246,
        243,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,
        35,1,0,0,0,250,248,1,0,0,0,251,252,6,18,-1,0,252,253,3,38,19,0,253,
        262,1,0,0,0,254,255,10,3,0,0,255,256,5,24,0,0,256,261,3,38,19,0,
        257,258,10,2,0,0,258,259,5,25,0,0,259,261,3,38,19,0,260,254,1,0,
        0,0,260,257,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,
        0,0,263,37,1,0,0,0,264,262,1,0,0,0,265,266,5,26,0,0,266,267,3,34,
        17,0,267,268,5,27,0,0,268,274,1,0,0,0,269,274,5,31,0,0,270,274,3,
        40,20,0,271,274,5,30,0,0,272,274,3,42,21,0,273,265,1,0,0,0,273,269,
        1,0,0,0,273,270,1,0,0,0,273,271,1,0,0,0,273,272,1,0,0,0,274,39,1,
        0,0,0,275,278,5,29,0,0,276,278,5,28,0,0,277,275,1,0,0,0,277,276,
        1,0,0,0,278,41,1,0,0,0,279,283,5,33,0,0,280,283,5,34,0,0,281,283,
        5,35,0,0,282,279,1,0,0,0,282,280,1,0,0,0,282,281,1,0,0,0,283,43,
        1,0,0,0,30,48,58,64,70,78,85,90,97,109,116,120,131,139,146,153,157,
        165,178,195,201,206,218,223,246,248,260,262,273,277,282
    ]

class AssignmentStatementParser ( Parser ):

    grammarFileName = "AssignmentStatement.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'var'", "','", "':'", "'float'", 
                     "'int'", "'string'", "'begin'", "'end'", "'if'", "'then'", 
                     "'else'", "'while'", "'do'", "'for'", "'to'", "'Case'", 
                     "'of'", "'?'", "':='", "';'", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "String", "ID", "ARRAY_TYPE", "INT_ARRAY", 
                      "FLOAT_ARRAY", "STRING_ARRAY", "WS", "NEWLINE", "RELOP", 
                      "LINE_COMMENT" ]

    RULE_start = 0
    RULE_prog = 1
    RULE_declaration = 2
    RULE_variable_declaration = 3
    RULE_type = 4
    RULE_compoundst = 5
    RULE_statement = 6
    RULE_ifst = 7
    RULE_whilest = 8
    RULE_forst = 9
    RULE_casest = 10
    RULE_casebody = 11
    RULE_cond = 12
    RULE_simpletrn = 13
    RULE_trnbody = 14
    RULE_compoundtrn = 15
    RULE_assign = 16
    RULE_expr = 17
    RULE_term = 18
    RULE_factor = 19
    RULE_number = 20
    RULE_array = 21

    ruleNames =  [ "start", "prog", "declaration", "variable_declaration", 
                   "type", "compoundst", "statement", "ifst", "whilest", 
                   "forst", "casest", "casebody", "cond", "simpletrn", "trnbody", 
                   "compoundtrn", "assign", "expr", "term", "factor", "number", 
                   "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    INT=28
    FLOAT=29
    String=30
    ID=31
    ARRAY_TYPE=32
    INT_ARRAY=33
    FLOAT_ARRAY=34
    STRING_ARRAY=35
    WS=36
    NEWLINE=37
    RELOP=38
    LINE_COMMENT=39

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
            self.value_attr = str()
            self.type_attr = str()

        def prog(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ProgContext,0)


        def EOF(self):
            return self.getToken(AssignmentStatementParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_start

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

        localctx = AssignmentStatementParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.prog()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 45
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(AssignmentStatementParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def compoundst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CompoundstContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.DeclarationContext,i)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = AssignmentStatementParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(AssignmentStatementParser.T__0)
            self.state = 54
            self.match(AssignmentStatementParser.ID)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55
                    self.match(AssignmentStatementParser.NEWLINE) 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 61
                self.declaration()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==37):
                    break

            self.state = 72
            self.compoundst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.Variable_declarationContext,i)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = AssignmentStatementParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(AssignmentStatementParser.T__1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 75
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.variable_declaration()
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 82
                        self.match(AssignmentStatementParser.NEWLINE) 
                    self.state = 87
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.ID)
            else:
                return self.getToken(AssignmentStatementParser.ID, i)

        def type_(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TypeContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = AssignmentStatementParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(AssignmentStatementParser.ID)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 93
                self.match(AssignmentStatementParser.T__2)
                self.state = 94
                self.match(AssignmentStatementParser.ID)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(AssignmentStatementParser.T__3)
            self.state = 101
            self.type_()
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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_type

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

        localctx = AssignmentStatementParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
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


    class CompoundstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,i)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_compoundst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundst" ):
                listener.enterCompoundst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundst" ):
                listener.exitCompoundst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundst" ):
                return visitor.visitCompoundst(self)
            else:
                return visitor.visitChildren(self)




    def compoundst(self):

        localctx = AssignmentStatementParser.CompoundstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_compoundst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(AssignmentStatementParser.T__7)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 106
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.statement()
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 113
                    self.match(AssignmentStatementParser.NEWLINE)
                    self.state = 116 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==37):
                        break

                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147656960) != 0)):
                    break

            self.state = 122
            self.match(AssignmentStatementParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ifst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.IfstContext,0)


        def assign(self):
            return self.getTypedRuleContext(AssignmentStatementParser.AssignContext,0)


        def compoundst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CompoundstContext,0)


        def forst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ForstContext,0)


        def whilest(self):
            return self.getTypedRuleContext(AssignmentStatementParser.WhilestContext,0)


        def casest(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CasestContext,0)


        def compoundtrn(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CompoundtrnContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AssignmentStatementParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.ifst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.compoundst()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.forst()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.whilest()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.casest()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.compoundtrn()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def cond(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CondContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_ifst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfst" ):
                listener.enterIfst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfst" ):
                listener.exitIfst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfst" ):
                return visitor.visitIfst(self)
            else:
                return visitor.visitChildren(self)




    def ifst(self):

        localctx = AssignmentStatementParser.IfstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(AssignmentStatementParser.T__9)
            self.state = 134
            self.cond()
            self.state = 135
            self.match(AssignmentStatementParser.T__10)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 136
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.statement()
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.match(AssignmentStatementParser.NEWLINE) 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 149
                self.match(AssignmentStatementParser.T__11)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 150
                    self.match(AssignmentStatementParser.NEWLINE)
                    self.state = 155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 156
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def cond(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CondContext,0)


        def statement(self):
            return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_whilest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilest" ):
                listener.enterWhilest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilest" ):
                listener.exitWhilest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilest" ):
                return visitor.visitWhilest(self)
            else:
                return visitor.visitChildren(self)




    def whilest(self):

        localctx = AssignmentStatementParser.WhilestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whilest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(AssignmentStatementParser.T__12)
            self.state = 160
            self.cond()
            self.state = 161
            self.match(AssignmentStatementParser.T__13)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 162
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def assign(self):
            return self.getTypedRuleContext(AssignmentStatementParser.AssignContext,0)


        def number(self):
            return self.getTypedRuleContext(AssignmentStatementParser.NumberContext,0)


        def compoundst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CompoundstContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_forst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForst" ):
                listener.enterForst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForst" ):
                listener.exitForst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForst" ):
                return visitor.visitForst(self)
            else:
                return visitor.visitChildren(self)




    def forst(self):

        localctx = AssignmentStatementParser.ForstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(AssignmentStatementParser.T__14)
            self.state = 171
            self.assign()
            self.state = 172
            self.match(AssignmentStatementParser.T__15)
            self.state = 173
            self.number()
            self.state = 174
            self.match(AssignmentStatementParser.T__13)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 175
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self.compoundst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(AssignmentStatementParser.NEWLINE, 0)

        def casebody(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CasebodyContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_casest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasest" ):
                listener.enterCasest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasest" ):
                listener.exitCasest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCasest" ):
                return visitor.visitCasest(self)
            else:
                return visitor.visitChildren(self)




    def casest(self):

        localctx = AssignmentStatementParser.CasestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_casest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(AssignmentStatementParser.T__16)
            self.state = 184
            self.match(AssignmentStatementParser.ID)
            self.state = 185
            self.match(AssignmentStatementParser.T__17)
            self.state = 186
            self.match(AssignmentStatementParser.NEWLINE)
            self.state = 187
            self.casebody()
            self.state = 188
            self.match(AssignmentStatementParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasebodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.ID)
            else:
                return self.getToken(AssignmentStatementParser.ID, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.TermContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.TermContext,i)


        def String(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.String)
            else:
                return self.getToken(AssignmentStatementParser.String, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_casebody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasebody" ):
                listener.enterCasebody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasebody" ):
                listener.exitCasebody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCasebody" ):
                return visitor.visitCasebody(self)
            else:
                return visitor.visitChildren(self)




    def casebody(self):

        localctx = AssignmentStatementParser.CasebodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_casebody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 190
                self.match(AssignmentStatementParser.ID)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 191
                    self.match(AssignmentStatementParser.T__2)
                    self.state = 192
                    self.match(AssignmentStatementParser.ID)
                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 198
                self.match(AssignmentStatementParser.T__3)
                self.state = 201
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.term(0)
                    pass

                elif la_ == 2:
                    self.state = 200
                    self.match(AssignmentStatementParser.String)
                    pass


                self.state = 203
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 206 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.ExprContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,i)


        def RELOP(self):
            return self.getToken(AssignmentStatementParser.RELOP, 0)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = AssignmentStatementParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr(0)
            self.state = 209
            self.match(AssignmentStatementParser.RELOP)
            self.state = 210
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpletrnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def cond(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CondContext,0)


        def trnbody(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TrnbodyContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_simpletrn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpletrn" ):
                listener.enterSimpletrn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpletrn" ):
                listener.exitSimpletrn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpletrn" ):
                return visitor.visitSimpletrn(self)
            else:
                return visitor.visitChildren(self)




    def simpletrn(self):

        localctx = AssignmentStatementParser.SimpletrnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_simpletrn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.cond()
            self.state = 213
            self.match(AssignmentStatementParser.T__18)
            self.state = 214
            self.trnbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrnbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.ExprContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,i)


        def simpletrn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.SimpletrnContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.SimpletrnContext,i)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_trnbody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrnbody" ):
                listener.enterTrnbody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrnbody" ):
                listener.exitTrnbody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrnbody" ):
                return visitor.visitTrnbody(self)
            else:
                return visitor.visitChildren(self)




    def trnbody(self):

        localctx = AssignmentStatementParser.TrnbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_trnbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 216
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 217
                self.simpletrn()
                pass


            self.state = 220
            self.match(AssignmentStatementParser.T__3)
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 221
                self.simpletrn()
                pass

            elif la_ == 2:
                self.state = 222
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundtrnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def simpletrn(self):
            return self.getTypedRuleContext(AssignmentStatementParser.SimpletrnContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_compoundtrn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundtrn" ):
                listener.enterCompoundtrn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundtrn" ):
                listener.exitCompoundtrn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundtrn" ):
                return visitor.visitCompoundtrn(self)
            else:
                return visitor.visitChildren(self)




    def compoundtrn(self):

        localctx = AssignmentStatementParser.CompoundtrnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compoundtrn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(AssignmentStatementParser.ID)
            self.state = 226
            self.match(AssignmentStatementParser.T__19)
            self.state = 227
            self.simpletrn()
            self.state = 228
            self.match(AssignmentStatementParser.T__20)
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
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_assign

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

        localctx = AssignmentStatementParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(AssignmentStatementParser.ID)
            self.state = 231
            self.match(AssignmentStatementParser.T__19)
            self.state = 232
            self.expr(0)
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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr


    class Expr_term_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_minus" ):
                listener.enterExpr_term_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_minus" ):
                listener.exitExpr_term_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_minus" ):
                return visitor.visitExpr_term_minus(self)
            else:
                return visitor.visitChildren(self)


    class Expr_term_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_plus" ):
                listener.enterExpr_term_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_plus" ):
                listener.exitExpr_term_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_plus" ):
                return visitor.visitExpr_term_plus(self)
            else:
                return visitor.visitChildren(self)


    class Term4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm4" ):
                listener.enterTerm4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm4" ):
                listener.exitTerm4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm4" ):
                return visitor.visitTerm4(self)
            else:
                return visitor.visitChildren(self)


    class Expr_term_relopContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)

        def RELOP(self):
            return self.getToken(AssignmentStatementParser.RELOP, 0)
        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_relop" ):
                listener.enterExpr_term_relop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_relop" ):
                listener.exitExpr_term_relop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_relop" ):
                return visitor.visitExpr_term_relop(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatementParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AssignmentStatementParser.Term4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 235
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 246
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatementParser.Expr_term_plusContext(self, AssignmentStatementParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 237
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 238
                        self.match(AssignmentStatementParser.T__21)
                        self.state = 239
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatementParser.Expr_term_minusContext(self, AssignmentStatementParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 240
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 241
                        self.match(AssignmentStatementParser.T__22)
                        self.state = 242
                        self.term(0)
                        pass

                    elif la_ == 3:
                        localctx = AssignmentStatementParser.Expr_term_relopContext(self, AssignmentStatementParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 243
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 244
                        self.match(AssignmentStatementParser.RELOP)
                        self.state = 245
                        self.term(0)
                        pass

             
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr


    class Term_fact_divideContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatementParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_fact_divide" ):
                listener.enterTerm_fact_divide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_fact_divide" ):
                listener.exitTerm_fact_divide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_fact_divide" ):
                return visitor.visitTerm_fact_divide(self)
            else:
                return visitor.visitChildren(self)


    class Term_fact_mutiplyContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatementParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_fact_mutiply" ):
                listener.enterTerm_fact_mutiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_fact_mutiply" ):
                listener.exitTerm_fact_mutiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_fact_mutiply" ):
                return visitor.visitTerm_fact_mutiply(self)
            else:
                return visitor.visitChildren(self)


    class Factor3Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatementParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor3" ):
                listener.enterFactor3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor3" ):
                listener.exitFactor3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor3" ):
                return visitor.visitFactor3(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatementParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AssignmentStatementParser.Factor3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 252
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 260
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatementParser.Term_fact_mutiplyContext(self, AssignmentStatementParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 254
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 255
                        self.match(AssignmentStatementParser.T__23)
                        self.state = 256
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatementParser.Term_fact_divideContext(self, AssignmentStatementParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 257
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 258
                        self.match(AssignmentStatementParser.T__24)
                        self.state = 259
                        self.factor()
                        pass

             
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Fact_exprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_expr" ):
                listener.enterFact_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_expr" ):
                listener.exitFact_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_expr" ):
                return visitor.visitFact_expr(self)
            else:
                return visitor.visitChildren(self)


    class Fact_stringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def String(self):
            return self.getToken(AssignmentStatementParser.String, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_string" ):
                listener.enterFact_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_string" ):
                listener.exitFact_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_string" ):
                return visitor.visitFact_string(self)
            else:
                return visitor.visitChildren(self)


    class Fact_idContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_id" ):
                listener.enterFact_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_id" ):
                listener.exitFact_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_id" ):
                return visitor.visitFact_id(self)
            else:
                return visitor.visitChildren(self)


    class Fact_numberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(AssignmentStatementParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_number" ):
                listener.enterFact_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_number" ):
                listener.exitFact_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_number" ):
                return visitor.visitFact_number(self)
            else:
                return visitor.visitChildren(self)


    class Fact_arrayContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_array" ):
                listener.enterFact_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_array" ):
                listener.exitFact_array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_array" ):
                return visitor.visitFact_array(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = AssignmentStatementParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = AssignmentStatementParser.Fact_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(AssignmentStatementParser.T__25)
                self.state = 266
                self.expr(0)
                self.state = 267
                self.match(AssignmentStatementParser.T__26)
                pass
            elif token in [31]:
                localctx = AssignmentStatementParser.Fact_idContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(AssignmentStatementParser.ID)
                pass
            elif token in [28, 29]:
                localctx = AssignmentStatementParser.Fact_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.number()
                pass
            elif token in [30]:
                localctx = AssignmentStatementParser.Fact_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.match(AssignmentStatementParser.String)
                pass
            elif token in [33, 34, 35]:
                localctx = AssignmentStatementParser.Fact_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 272
                self.array()
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Number_floatContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AssignmentStatementParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_float" ):
                listener.enterNumber_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_float" ):
                listener.exitNumber_float(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_float" ):
                return visitor.visitNumber_float(self)
            else:
                return visitor.visitChildren(self)


    class Number_intContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AssignmentStatementParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_int" ):
                listener.enterNumber_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_int" ):
                listener.exitNumber_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_int" ):
                return visitor.visitNumber_int(self)
            else:
                return visitor.visitChildren(self)



    def number(self):

        localctx = AssignmentStatementParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_number)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = AssignmentStatementParser.Number_floatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(AssignmentStatementParser.FLOAT)
                pass
            elif token in [28]:
                localctx = AssignmentStatementParser.Number_intContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(AssignmentStatementParser.INT)
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Array_floatContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_ARRAY(self):
            return self.getToken(AssignmentStatementParser.FLOAT_ARRAY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_float" ):
                listener.enterArray_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_float" ):
                listener.exitArray_float(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_float" ):
                return visitor.visitArray_float(self)
            else:
                return visitor.visitChildren(self)


    class Array_stringContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_ARRAY(self):
            return self.getToken(AssignmentStatementParser.STRING_ARRAY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_string" ):
                listener.enterArray_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_string" ):
                listener.exitArray_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_string" ):
                return visitor.visitArray_string(self)
            else:
                return visitor.visitChildren(self)


    class Array_intContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_ARRAY(self):
            return self.getToken(AssignmentStatementParser.INT_ARRAY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_int" ):
                listener.enterArray_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_int" ):
                listener.exitArray_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_int" ):
                return visitor.visitArray_int(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = AssignmentStatementParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = AssignmentStatementParser.Array_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(AssignmentStatementParser.INT_ARRAY)
                pass
            elif token in [34]:
                localctx = AssignmentStatementParser.Array_floatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(AssignmentStatementParser.FLOAT_ARRAY)
                pass
            elif token in [35]:
                localctx = AssignmentStatementParser.Array_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(AssignmentStatementParser.STRING_ARRAY)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr_sempred
        self._predicates[18] = self.term_sempred
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
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         





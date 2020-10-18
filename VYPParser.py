# Generated from VYP.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\22\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\20\2\t\3\2\2\2\4")
        buf.write("\16\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13\3\2\2\2\t\7\3")
        buf.write("\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2\2\2\f\r\7\2\2")
        buf.write("\3\r\3\3\2\2\2\16\17\7\3\2\2\17\20\7\20\2\2\20\5\3\2\2")
        buf.write("\2\3\t")
        return buf.getvalue()


class VYPParser ( Parser ):

    grammarFileName = "VYP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello world'", "'class'", "'else'", 
                     "'if'", "'int'", "'new'", "'return'", "'string'", "'super'", 
                     "'this'", "'void'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CLASS", "ELSE", "IF", "INT", 
                      "NEW", "RETURN", "STRING", "SUPER", "THIS", "VOID", 
                      "WHILE", "INTEGER_LITERAL", "ID", "WS" ]

    RULE_program = 0
    RULE_hello = 1

    ruleNames =  [ "program", "hello" ]

    EOF = Token.EOF
    T__0=1
    CLASS=2
    ELSE=3
    IF=4
    INT=5
    NEW=6
    RETURN=7
    STRING=8
    SUPER=9
    THIS=10
    VOID=11
    WHILE=12
    INTEGER_LITERAL=13
    ID=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VYPParser.EOF, 0)

        def hello(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VYPParser.HelloContext)
            else:
                return self.getTypedRuleContext(VYPParser.HelloContext,i)


        def getRuleIndex(self):
            return VYPParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = VYPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VYPParser.T__0:
                self.state = 4
                self.hello()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(VYPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelloContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VYPParser.ID, 0)

        def getRuleIndex(self):
            return VYPParser.RULE_hello

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHello" ):
                listener.enterHello(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHello" ):
                listener.exitHello(self)




    def hello(self):

        localctx = VYPParser.HelloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hello)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(VYPParser.T__0)
            self.state = 13
            self.match(VYPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\b\4\2\t\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\6\2\4\3\2\2\2")
        buf.write("\4\5\7\3\2\2\5\6\7\4\2\2\6\3\3\2\2\2\2")
        return buf.getvalue()


class VYPParser ( Parser ):

    grammarFileName = "VYP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello world'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_test = 0

    ruleNames =  [ "test" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VYPParser.ID, 0)

        def getRuleIndex(self):
            return VYPParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)




    def test(self):

        localctx = VYPParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_test)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(VYPParser.T__0)
            self.state = 3
            self.match(VYPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






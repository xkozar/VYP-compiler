# Generated from VYP.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("!\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\27\n\3\r\3\16\3\30\3")
        buf.write("\4\6\4\34\n\4\r\4\16\4\35\3\4\3\4\2\2\5\3\3\5\4\7\5\3")
        buf.write("\2\4\3\2c|\5\2\13\f\17\17\"\"\2\"\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\3\t\3\2\2\2\5\26\3\2\2\2\7\33\3\2\2\2")
        buf.write("\t\n\7j\2\2\n\13\7g\2\2\13\f\7n\2\2\f\r\7n\2\2\r\16\7")
        buf.write("q\2\2\16\17\7\"\2\2\17\20\7y\2\2\20\21\7q\2\2\21\22\7")
        buf.write("t\2\2\22\23\7n\2\2\23\24\7f\2\2\24\4\3\2\2\2\25\27\t\2")
        buf.write("\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\6\3\2\2\2\32\34\t\3\2\2\33\32\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37")
        buf.write(" \b\4\2\2 \b\3\2\2\2\5\2\30\35\3\b\2\2")
        return buf.getvalue()


class VYPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hello world'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "T__0", "ID", "WS" ]

    grammarFileName = "VYP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



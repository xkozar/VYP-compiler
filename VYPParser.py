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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\7\5&\n\5\f")
        buf.write("\5\16\5)\13\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\7\b\66\n\b\f\b\16\b9\13\b\5\b;\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\3\5\2\f\f\17\17\22\22")
        buf.write("\2<\2\25\3\2\2\2\4\32\3\2\2\2\6\35\3\2\2\2\b#\3\2\2\2")
        buf.write("\n,\3\2\2\2\f/\3\2\2\2\16:\3\2\2\2\20<\3\2\2\2\22\24\5")
        buf.write("\4\3\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26")
        buf.write("\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3\31")
        buf.write("\3\3\2\2\2\32\33\5\6\4\2\33\34\5\b\5\2\34\5\3\2\2\2\35")
        buf.write("\36\5\f\7\2\36\37\7\25\2\2\37 \7\3\2\2 !\5\16\b\2!\"\7")
        buf.write("\4\2\2\"\7\3\2\2\2#\'\7\5\2\2$&\5\n\6\2%$\3\2\2\2&)\3")
        buf.write("\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2\2*+\7")
        buf.write("\6\2\2+\t\3\2\2\2,-\7\25\2\2-.\7\7\2\2.\13\3\2\2\2/\60")
        buf.write("\t\2\2\2\60\r\3\2\2\2\61;\7\22\2\2\62\63\5\f\7\2\63\67")
        buf.write("\7\25\2\2\64\66\5\20\t\2\65\64\3\2\2\2\669\3\2\2\2\67")
        buf.write("\65\3\2\2\2\678\3\2\2\28;\3\2\2\29\67\3\2\2\2:\61\3\2")
        buf.write("\2\2:\62\3\2\2\2;\17\3\2\2\2<=\7\b\2\2=>\5\f\7\2>?\7\25")
        buf.write("\2\2?\21\3\2\2\2\6\25\'\67:")
        return buf.getvalue()


class VYPParser ( Parser ):

    grammarFileName = "VYP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "','", 
                     "'class'", "'else'", "'if'", "'int'", "'new'", "'return'", 
                     "'string'", "'super'", "'this'", "'void'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CLASS", "ELSE", 
                      "IF", "INT", "NEW", "RETURN", "STRING", "SUPER", "THIS", 
                      "VOID", "WHILE", "INTEGER_LITERAL", "ID", "STRING_LITERAL", 
                      "WHITE_SPACE", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_function_header = 2
    RULE_function_body = 3
    RULE_statement = 4
    RULE_variable_type = 5
    RULE_parameter_list = 6
    RULE_next_parameter = 7

    ruleNames =  [ "program", "function", "function_header", "function_body", 
                   "statement", "variable_type", "parameter_list", "next_parameter" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    CLASS=7
    ELSE=8
    IF=9
    INT=10
    NEW=11
    RETURN=12
    STRING=13
    SUPER=14
    THIS=15
    VOID=16
    WHILE=17
    INTEGER_LITERAL=18
    ID=19
    STRING_LITERAL=20
    WHITE_SPACE=21
    LINE_COMMENT=22
    BLOCK_COMMENT=23

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

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VYPParser.FunctionContext)
            else:
                return self.getTypedRuleContext(VYPParser.FunctionContext,i)


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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VYPParser.INT) | (1 << VYPParser.STRING) | (1 << VYPParser.VOID))) != 0):
                self.state = 16
                self.function()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(VYPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_header(self):
            return self.getTypedRuleContext(VYPParser.Function_headerContext,0)


        def function_body(self):
            return self.getTypedRuleContext(VYPParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return VYPParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = VYPParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.function_header()
            self.state = 25
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_type(self):
            return self.getTypedRuleContext(VYPParser.Variable_typeContext,0)


        def ID(self):
            return self.getToken(VYPParser.ID, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(VYPParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return VYPParser.RULE_function_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_header" ):
                listener.enterFunction_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_header" ):
                listener.exitFunction_header(self)




    def function_header(self):

        localctx = VYPParser.Function_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.variable_type()
            self.state = 28
            self.match(VYPParser.ID)
            self.state = 29
            self.match(VYPParser.T__0)
            self.state = 30
            self.parameter_list()
            self.state = 31
            self.match(VYPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VYPParser.StatementContext)
            else:
                return self.getTypedRuleContext(VYPParser.StatementContext,i)


        def getRuleIndex(self):
            return VYPParser.RULE_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_body" ):
                listener.enterFunction_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_body" ):
                listener.exitFunction_body(self)




    def function_body(self):

        localctx = VYPParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(VYPParser.T__2)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VYPParser.ID:
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(VYPParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VYPParser.ID, 0)

        def getRuleIndex(self):
            return VYPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = VYPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(VYPParser.ID)
            self.state = 43
            self.match(VYPParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(VYPParser.INT, 0)

        def STRING(self):
            return self.getToken(VYPParser.STRING, 0)

        def VOID(self):
            return self.getToken(VYPParser.VOID, 0)

        def getRuleIndex(self):
            return VYPParser.RULE_variable_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_type" ):
                listener.enterVariable_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_type" ):
                listener.exitVariable_type(self)




    def variable_type(self):

        localctx = VYPParser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VYPParser.INT) | (1 << VYPParser.STRING) | (1 << VYPParser.VOID))) != 0)):
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


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(VYPParser.VOID, 0)

        def variable_type(self):
            return self.getTypedRuleContext(VYPParser.Variable_typeContext,0)


        def ID(self):
            return self.getToken(VYPParser.ID, 0)

        def next_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VYPParser.Next_parameterContext)
            else:
                return self.getTypedRuleContext(VYPParser.Next_parameterContext,i)


        def getRuleIndex(self):
            return VYPParser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)




    def parameter_list(self):

        localctx = VYPParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(VYPParser.VOID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.variable_type()
                self.state = 49
                self.match(VYPParser.ID)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VYPParser.T__5:
                    self.state = 50
                    self.next_parameter()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_type(self):
            return self.getTypedRuleContext(VYPParser.Variable_typeContext,0)


        def ID(self):
            return self.getToken(VYPParser.ID, 0)

        def getRuleIndex(self):
            return VYPParser.RULE_next_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext_parameter" ):
                listener.enterNext_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext_parameter" ):
                listener.exitNext_parameter(self)




    def next_parameter(self):

        localctx = VYPParser.Next_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_next_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(VYPParser.T__5)
            self.state = 59
            self.variable_type()
            self.state = 60
            self.match(VYPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






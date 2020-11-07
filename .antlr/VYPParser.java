// Generated from c:\Users\kozar\Programming\VYPa\VYP-compiler\VYP.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VYPParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, CLASS=15, ELSE=16, IF=17, 
		INT=18, NEW=19, RETURN=20, STRING=21, SUPER=22, THIS=23, VOID=24, WHILE=25, 
		LE=26, LEQ=27, GT=28, GTQ=29, LOGICAL_EQUAL=30, LOGICAL_NEQUAL=31, LOGICAL_AND=32, 
		LOGICAL_OR=33, INTEGER_LITERAL=34, ID=35, STRING_LITERAL=36, WHITE_SPACE=37, 
		LINE_COMMENT=38, BLOCK_COMMENT=39;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_function_definition = 2, RULE_function_header = 3, 
		RULE_function_body = 4, RULE_class_definition = 5, RULE_class_header = 6, 
		RULE_class_body = 7, RULE_class_members = 8, RULE_variable_definition = 9, 
		RULE_multiple_variable_definition = 10, RULE_variable_assignment = 11, 
		RULE_if_else_block = 12, RULE_if_part = 13, RULE_else_part = 14, RULE_while_block = 15, 
		RULE_expression = 16, RULE_literal_value = 17, RULE_instance_creation = 18, 
		RULE_instance_variable = 19, RULE_instance_function_call = 20, RULE_nested_object = 21, 
		RULE_function_call = 22, RULE_expression_list = 23, RULE_next_expression = 24, 
		RULE_variable_type = 25, RULE_parameter_list = 26, RULE_next_parameter = 27;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "function_definition", "function_header", "function_body", 
			"class_definition", "class_header", "class_body", "class_members", "variable_definition", 
			"multiple_variable_definition", "variable_assignment", "if_else_block", 
			"if_part", "else_part", "while_block", "expression", "literal_value", 
			"instance_creation", "instance_variable", "instance_function_call", "nested_object", 
			"function_call", "expression_list", "next_expression", "variable_type", 
			"parameter_list", "next_parameter"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "':'", "';'", "','", "'='", "'!'", 
			"'*'", "'/'", "'+'", "'-'", "'.'", "'class'", "'else'", "'if'", "'int'", 
			"'new'", "'return'", "'string'", "'super'", "'this'", "'void'", "'while'", 
			"'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'&&'", "'||'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "CLASS", "ELSE", "IF", "INT", "NEW", "RETURN", "STRING", 
			"SUPER", "THIS", "VOID", "WHILE", "LE", "LEQ", "GT", "GTQ", "LOGICAL_EQUAL", 
			"LOGICAL_NEQUAL", "LOGICAL_AND", "LOGICAL_OR", "INTEGER_LITERAL", "ID", 
			"STRING_LITERAL", "WHITE_SPACE", "LINE_COMMENT", "BLOCK_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "VYP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public VYPParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(VYPParser.EOF, 0); }
		public List<Function_definitionContext> function_definition() {
			return getRuleContexts(Function_definitionContext.class);
		}
		public Function_definitionContext function_definition(int i) {
			return getRuleContext(Function_definitionContext.class,i);
		}
		public List<Class_definitionContext> class_definition() {
			return getRuleContexts(Class_definitionContext.class);
		}
		public Class_definitionContext class_definition(int i) {
			return getRuleContext(Class_definitionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CLASS) | (1L << INT) | (1L << STRING) | (1L << VOID))) != 0)) {
				{
				setState(58);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
				case STRING:
				case VOID:
					{
					setState(56);
					function_definition();
					}
					break;
				case CLASS:
					{
					setState(57);
					class_definition();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(63);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public If_else_blockContext if_else_block() {
			return getRuleContext(If_else_blockContext.class,0);
		}
		public While_blockContext while_block() {
			return getRuleContext(While_blockContext.class,0);
		}
		public Variable_definitionContext variable_definition() {
			return getRuleContext(Variable_definitionContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(69);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				if_else_block();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(66);
				while_block();
				}
				break;
			case INT:
			case STRING:
			case VOID:
				enterOuterAlt(_localctx, 3);
				{
				setState(67);
				variable_definition();
				}
				break;
			case T__0:
			case T__8:
			case NEW:
			case THIS:
			case INTEGER_LITERAL:
			case ID:
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(68);
				expression(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_definitionContext extends ParserRuleContext {
		public Function_headerContext function_header() {
			return getRuleContext(Function_headerContext.class,0);
		}
		public Function_bodyContext function_body() {
			return getRuleContext(Function_bodyContext.class,0);
		}
		public Function_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_definition; }
	}

	public final Function_definitionContext function_definition() throws RecognitionException {
		Function_definitionContext _localctx = new Function_definitionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			function_header();
			setState(72);
			function_body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_headerContext extends ParserRuleContext {
		public Variable_typeContext variable_type() {
			return getRuleContext(Variable_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Parameter_listContext parameter_list() {
			return getRuleContext(Parameter_listContext.class,0);
		}
		public Function_headerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_header; }
	}

	public final Function_headerContext function_header() throws RecognitionException {
		Function_headerContext _localctx = new Function_headerContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_function_header);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			variable_type();
			setState(75);
			match(ID);
			setState(76);
			match(T__0);
			setState(77);
			parameter_list();
			setState(78);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_bodyContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Function_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_body; }
	}

	public final Function_bodyContext function_body() throws RecognitionException {
		Function_bodyContext _localctx = new Function_bodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_function_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(T__2);
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << IF) | (1L << INT) | (1L << NEW) | (1L << STRING) | (1L << THIS) | (1L << VOID) | (1L << WHILE) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				{
				setState(81);
				statement();
				}
				}
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(87);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_definitionContext extends ParserRuleContext {
		public Class_headerContext class_header() {
			return getRuleContext(Class_headerContext.class,0);
		}
		public Class_bodyContext class_body() {
			return getRuleContext(Class_bodyContext.class,0);
		}
		public Class_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_definition; }
	}

	public final Class_definitionContext class_definition() throws RecognitionException {
		Class_definitionContext _localctx = new Class_definitionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_class_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			class_header();
			setState(90);
			class_body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_headerContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(VYPParser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(VYPParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(VYPParser.ID, i);
		}
		public Class_headerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_header; }
	}

	public final Class_headerContext class_header() throws RecognitionException {
		Class_headerContext _localctx = new Class_headerContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_class_header);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(CLASS);
			setState(93);
			match(ID);
			setState(94);
			match(T__4);
			setState(95);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_bodyContext extends ParserRuleContext {
		public List<Class_membersContext> class_members() {
			return getRuleContexts(Class_membersContext.class);
		}
		public Class_membersContext class_members(int i) {
			return getRuleContext(Class_membersContext.class,i);
		}
		public Class_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_body; }
	}

	public final Class_bodyContext class_body() throws RecognitionException {
		Class_bodyContext _localctx = new Class_bodyContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_class_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(T__2);
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << STRING) | (1L << VOID))) != 0)) {
				{
				{
				setState(98);
				class_members();
				}
				}
				setState(103);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(104);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_membersContext extends ParserRuleContext {
		public Variable_definitionContext variable_definition() {
			return getRuleContext(Variable_definitionContext.class,0);
		}
		public Function_definitionContext function_definition() {
			return getRuleContext(Function_definitionContext.class,0);
		}
		public Class_membersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_members; }
	}

	public final Class_membersContext class_members() throws RecognitionException {
		Class_membersContext _localctx = new Class_membersContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_class_members);
		try {
			setState(108);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				variable_definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(107);
				function_definition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_definitionContext extends ParserRuleContext {
		public Variable_typeContext variable_type() {
			return getRuleContext(Variable_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public List<Multiple_variable_definitionContext> multiple_variable_definition() {
			return getRuleContexts(Multiple_variable_definitionContext.class);
		}
		public Multiple_variable_definitionContext multiple_variable_definition(int i) {
			return getRuleContext(Multiple_variable_definitionContext.class,i);
		}
		public Variable_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_definition; }
	}

	public final Variable_definitionContext variable_definition() throws RecognitionException {
		Variable_definitionContext _localctx = new Variable_definitionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_variable_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			variable_type();
			setState(111);
			match(ID);
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(112);
				multiple_variable_definition();
				}
				}
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(118);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Multiple_variable_definitionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Multiple_variable_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiple_variable_definition; }
	}

	public final Multiple_variable_definitionContext multiple_variable_definition() throws RecognitionException {
		Multiple_variable_definitionContext _localctx = new Multiple_variable_definitionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_multiple_variable_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(T__6);
			setState(121);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_assignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Variable_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_assignment; }
	}

	public final Variable_assignmentContext variable_assignment() throws RecognitionException {
		Variable_assignmentContext _localctx = new Variable_assignmentContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_variable_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(ID);
			setState(124);
			match(T__7);
			setState(125);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_else_blockContext extends ParserRuleContext {
		public If_partContext if_part() {
			return getRuleContext(If_partContext.class,0);
		}
		public Else_partContext else_part() {
			return getRuleContext(Else_partContext.class,0);
		}
		public If_else_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_else_block; }
	}

	public final If_else_blockContext if_else_block() throws RecognitionException {
		If_else_blockContext _localctx = new If_else_blockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_if_else_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			if_part();
			setState(128);
			else_part();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_partContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(VYPParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public If_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_part; }
	}

	public final If_partContext if_part() throws RecognitionException {
		If_partContext _localctx = new If_partContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_if_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			match(IF);
			setState(131);
			match(T__0);
			setState(132);
			expression(0);
			setState(133);
			match(T__1);
			setState(134);
			match(T__2);
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << IF) | (1L << INT) | (1L << NEW) | (1L << STRING) | (1L << THIS) | (1L << VOID) | (1L << WHILE) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				{
				setState(135);
				statement();
				}
				}
				setState(140);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(141);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_partContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(VYPParser.ELSE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Else_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_part; }
	}

	public final Else_partContext else_part() throws RecognitionException {
		Else_partContext _localctx = new Else_partContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_else_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(ELSE);
			setState(144);
			match(T__0);
			setState(145);
			expression(0);
			setState(146);
			match(T__1);
			setState(147);
			match(T__2);
			setState(151);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << IF) | (1L << INT) | (1L << NEW) | (1L << STRING) | (1L << THIS) | (1L << VOID) | (1L << WHILE) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				{
				setState(148);
				statement();
				}
				}
				setState(153);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(154);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_blockContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(VYPParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public While_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_block; }
	}

	public final While_blockContext while_block() throws RecognitionException {
		While_blockContext _localctx = new While_blockContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_while_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(WHILE);
			setState(157);
			match(T__0);
			setState(158);
			expression(0);
			setState(159);
			match(T__1);
			setState(160);
			match(T__2);
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << IF) | (1L << INT) | (1L << NEW) | (1L << STRING) | (1L << THIS) | (1L << VOID) | (1L << WHILE) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				{
				setState(161);
				statement();
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(167);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Literal_valueContext literal_value() {
			return getRuleContext(Literal_valueContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Instance_creationContext instance_creation() {
			return getRuleContext(Instance_creationContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Instance_function_callContext instance_function_call() {
			return getRuleContext(Instance_function_callContext.class,0);
		}
		public Instance_variableContext instance_variable() {
			return getRuleContext(Instance_variableContext.class,0);
		}
		public TerminalNode LE() { return getToken(VYPParser.LE, 0); }
		public TerminalNode LEQ() { return getToken(VYPParser.LEQ, 0); }
		public TerminalNode GT() { return getToken(VYPParser.GT, 0); }
		public TerminalNode GTQ() { return getToken(VYPParser.GTQ, 0); }
		public TerminalNode LOGICAL_EQUAL() { return getToken(VYPParser.LOGICAL_EQUAL, 0); }
		public TerminalNode LOGICAL_NEQUAL() { return getToken(VYPParser.LOGICAL_NEQUAL, 0); }
		public TerminalNode LOGICAL_AND() { return getToken(VYPParser.LOGICAL_AND, 0); }
		public TerminalNode LOGICAL_OR() { return getToken(VYPParser.LOGICAL_OR, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(170);
				match(ID);
				}
				break;
			case 2:
				{
				setState(171);
				literal_value();
				}
				break;
			case 3:
				{
				setState(172);
				function_call();
				}
				break;
			case 4:
				{
				setState(173);
				instance_creation();
				}
				break;
			case 5:
				{
				setState(174);
				match(T__0);
				setState(175);
				expression(0);
				setState(176);
				match(T__1);
				}
				break;
			case 6:
				{
				setState(178);
				instance_function_call();
				}
				break;
			case 7:
				{
				setState(179);
				instance_variable();
				}
				break;
			case 8:
				{
				setState(180);
				match(T__8);
				setState(181);
				expression(7);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(204);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(202);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(184);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(185);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(186);
						expression(7);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(187);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(188);
						_la = _input.LA(1);
						if ( !(_la==T__11 || _la==T__12) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(189);
						expression(6);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(190);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(191);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LE) | (1L << LEQ) | (1L << GT) | (1L << GTQ))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(192);
						expression(5);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(193);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(194);
						_la = _input.LA(1);
						if ( !(_la==LOGICAL_EQUAL || _la==LOGICAL_NEQUAL) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(195);
						expression(4);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(196);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(197);
						match(LOGICAL_AND);
						setState(198);
						expression(3);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(199);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(200);
						match(LOGICAL_OR);
						setState(201);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(206);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Literal_valueContext extends ParserRuleContext {
		public TerminalNode INTEGER_LITERAL() { return getToken(VYPParser.INTEGER_LITERAL, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(VYPParser.STRING_LITERAL, 0); }
		public Literal_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_value; }
	}

	public final Literal_valueContext literal_value() throws RecognitionException {
		Literal_valueContext _localctx = new Literal_valueContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_literal_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			_la = _input.LA(1);
			if ( !(_la==INTEGER_LITERAL || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Instance_creationContext extends ParserRuleContext {
		public TerminalNode NEW() { return getToken(VYPParser.NEW, 0); }
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public Instance_creationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance_creation; }
	}

	public final Instance_creationContext instance_creation() throws RecognitionException {
		Instance_creationContext _localctx = new Instance_creationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_instance_creation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(NEW);
			setState(210);
			match(ID);
			setState(211);
			match(T__0);
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << NEW) | (1L << THIS) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				setState(212);
				expression_list();
				}
			}

			setState(215);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Instance_variableContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(VYPParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(VYPParser.ID, i);
		}
		public TerminalNode THIS() { return getToken(VYPParser.THIS, 0); }
		public List<Nested_objectContext> nested_object() {
			return getRuleContexts(Nested_objectContext.class);
		}
		public Nested_objectContext nested_object(int i) {
			return getRuleContext(Nested_objectContext.class,i);
		}
		public Instance_variableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance_variable; }
	}

	public final Instance_variableContext instance_variable() throws RecognitionException {
		Instance_variableContext _localctx = new Instance_variableContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_instance_variable);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			_la = _input.LA(1);
			if ( !(_la==THIS || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(221);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(218);
					nested_object();
					}
					} 
				}
				setState(223);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			setState(224);
			match(T__13);
			setState(225);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Instance_function_callContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(VYPParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(VYPParser.ID, i);
		}
		public TerminalNode THIS() { return getToken(VYPParser.THIS, 0); }
		public List<Nested_objectContext> nested_object() {
			return getRuleContexts(Nested_objectContext.class);
		}
		public Nested_objectContext nested_object(int i) {
			return getRuleContext(Nested_objectContext.class,i);
		}
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public Instance_function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance_function_call; }
	}

	public final Instance_function_callContext instance_function_call() throws RecognitionException {
		Instance_function_callContext _localctx = new Instance_function_callContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_instance_function_call);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			_la = _input.LA(1);
			if ( !(_la==THIS || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(231);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(228);
					nested_object();
					}
					} 
				}
				setState(233);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			setState(234);
			match(T__13);
			setState(235);
			match(ID);
			setState(236);
			match(T__0);
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << NEW) | (1L << THIS) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				setState(237);
				expression_list();
				}
			}

			setState(240);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Nested_objectContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Nested_objectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nested_object; }
	}

	public final Nested_objectContext nested_object() throws RecognitionException {
		Nested_objectContext _localctx = new Nested_objectContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_nested_object);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(T__13);
			setState(243);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			match(ID);
			setState(246);
			match(T__0);
			setState(248);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << NEW) | (1L << THIS) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				setState(247);
				expression_list();
				}
			}

			setState(250);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_listContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<Next_expressionContext> next_expression() {
			return getRuleContexts(Next_expressionContext.class);
		}
		public Next_expressionContext next_expression(int i) {
			return getRuleContext(Next_expressionContext.class,i);
		}
		public Expression_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_list; }
	}

	public final Expression_listContext expression_list() throws RecognitionException {
		Expression_listContext _localctx = new Expression_listContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_expression_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			expression(0);
			setState(256);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(253);
				next_expression();
				}
				}
				setState(258);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Next_expressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Next_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_next_expression; }
	}

	public final Next_expressionContext next_expression() throws RecognitionException {
		Next_expressionContext _localctx = new Next_expressionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_next_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			match(T__6);
			setState(260);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(VYPParser.INT, 0); }
		public TerminalNode STRING() { return getToken(VYPParser.STRING, 0); }
		public TerminalNode VOID() { return getToken(VYPParser.VOID, 0); }
		public Variable_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_type; }
	}

	public final Variable_typeContext variable_type() throws RecognitionException {
		Variable_typeContext _localctx = new Variable_typeContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_variable_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << STRING) | (1L << VOID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameter_listContext extends ParserRuleContext {
		public TerminalNode VOID() { return getToken(VYPParser.VOID, 0); }
		public Variable_typeContext variable_type() {
			return getRuleContext(Variable_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public List<Next_parameterContext> next_parameter() {
			return getRuleContexts(Next_parameterContext.class);
		}
		public Next_parameterContext next_parameter(int i) {
			return getRuleContext(Next_parameterContext.class,i);
		}
		public Parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_list; }
	}

	public final Parameter_listContext parameter_list() throws RecognitionException {
		Parameter_listContext _localctx = new Parameter_listContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_parameter_list);
		int _la;
		try {
			setState(273);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(264);
				match(VOID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(265);
				variable_type();
				setState(266);
				match(ID);
				setState(270);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__6) {
					{
					{
					setState(267);
					next_parameter();
					}
					}
					setState(272);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Next_parameterContext extends ParserRuleContext {
		public Variable_typeContext variable_type() {
			return getRuleContext(Variable_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Next_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_next_parameter; }
	}

	public final Next_parameterContext next_parameter() throws RecognitionException {
		Next_parameterContext _localctx = new Next_parameterContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_next_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			match(T__6);
			setState(276);
			variable_type();
			setState(277);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 16:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)\u011a\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2\7\2=\n\2\f\2\16\2@\13"+
		"\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3H\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\6\3\6\7\6U\n\6\f\6\16\6X\13\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b"+
		"\3\b\3\t\3\t\7\tf\n\t\f\t\16\ti\13\t\3\t\3\t\3\n\3\n\5\no\n\n\3\13\3\13"+
		"\3\13\7\13t\n\13\f\13\16\13w\13\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3"+
		"\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u008b\n\17\f\17\16"+
		"\17\u008e\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0098\n\20"+
		"\f\20\16\20\u009b\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00a5"+
		"\n\21\f\21\16\21\u00a8\13\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00b9\n\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\7\22\u00cd\n\22\f\22\16\22\u00d0\13\22\3\23\3\23\3\24\3\24\3\24\3\24"+
		"\5\24\u00d8\n\24\3\24\3\24\3\25\3\25\7\25\u00de\n\25\f\25\16\25\u00e1"+
		"\13\25\3\25\3\25\3\25\3\26\3\26\7\26\u00e8\n\26\f\26\16\26\u00eb\13\26"+
		"\3\26\3\26\3\26\3\26\5\26\u00f1\n\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30"+
		"\3\30\5\30\u00fb\n\30\3\30\3\30\3\31\3\31\7\31\u0101\n\31\f\31\16\31\u0104"+
		"\13\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u010f\n\34\f"+
		"\34\16\34\u0112\13\34\5\34\u0114\n\34\3\35\3\35\3\35\3\35\3\35\2\3\"\36"+
		"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668\2\t\3\2"+
		"\f\r\3\2\16\17\3\2\34\37\3\2 !\4\2$$&&\4\2\31\31%%\5\2\24\24\27\27\32"+
		"\32\2\u011e\2>\3\2\2\2\4G\3\2\2\2\6I\3\2\2\2\bL\3\2\2\2\nR\3\2\2\2\f["+
		"\3\2\2\2\16^\3\2\2\2\20c\3\2\2\2\22n\3\2\2\2\24p\3\2\2\2\26z\3\2\2\2\30"+
		"}\3\2\2\2\32\u0081\3\2\2\2\34\u0084\3\2\2\2\36\u0091\3\2\2\2 \u009e\3"+
		"\2\2\2\"\u00b8\3\2\2\2$\u00d1\3\2\2\2&\u00d3\3\2\2\2(\u00db\3\2\2\2*\u00e5"+
		"\3\2\2\2,\u00f4\3\2\2\2.\u00f7\3\2\2\2\60\u00fe\3\2\2\2\62\u0105\3\2\2"+
		"\2\64\u0108\3\2\2\2\66\u0113\3\2\2\28\u0115\3\2\2\2:=\5\6\4\2;=\5\f\7"+
		"\2<:\3\2\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2"+
		"\2AB\7\2\2\3B\3\3\2\2\2CH\5\32\16\2DH\5 \21\2EH\5\24\13\2FH\5\"\22\2G"+
		"C\3\2\2\2GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2H\5\3\2\2\2IJ\5\b\5\2JK\5\n\6\2"+
		"K\7\3\2\2\2LM\5\64\33\2MN\7%\2\2NO\7\3\2\2OP\5\66\34\2PQ\7\4\2\2Q\t\3"+
		"\2\2\2RV\7\5\2\2SU\5\4\3\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WY\3"+
		"\2\2\2XV\3\2\2\2YZ\7\6\2\2Z\13\3\2\2\2[\\\5\16\b\2\\]\5\20\t\2]\r\3\2"+
		"\2\2^_\7\21\2\2_`\7%\2\2`a\7\7\2\2ab\7%\2\2b\17\3\2\2\2cg\7\5\2\2df\5"+
		"\22\n\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hj\3\2\2\2ig\3\2\2\2jk"+
		"\7\6\2\2k\21\3\2\2\2lo\5\24\13\2mo\5\6\4\2nl\3\2\2\2nm\3\2\2\2o\23\3\2"+
		"\2\2pq\5\64\33\2qu\7%\2\2rt\5\26\f\2sr\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3"+
		"\2\2\2vx\3\2\2\2wu\3\2\2\2xy\7\b\2\2y\25\3\2\2\2z{\7\t\2\2{|\7%\2\2|\27"+
		"\3\2\2\2}~\7%\2\2~\177\7\n\2\2\177\u0080\5\"\22\2\u0080\31\3\2\2\2\u0081"+
		"\u0082\5\34\17\2\u0082\u0083\5\36\20\2\u0083\33\3\2\2\2\u0084\u0085\7"+
		"\23\2\2\u0085\u0086\7\3\2\2\u0086\u0087\5\"\22\2\u0087\u0088\7\4\2\2\u0088"+
		"\u008c\7\5\2\2\u0089\u008b\5\4\3\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2"+
		"\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e"+
		"\u008c\3\2\2\2\u008f\u0090\7\6\2\2\u0090\35\3\2\2\2\u0091\u0092\7\22\2"+
		"\2\u0092\u0093\7\3\2\2\u0093\u0094\5\"\22\2\u0094\u0095\7\4\2\2\u0095"+
		"\u0099\7\5\2\2\u0096\u0098\5\4\3\2\u0097\u0096\3\2\2\2\u0098\u009b\3\2"+
		"\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b"+
		"\u0099\3\2\2\2\u009c\u009d\7\6\2\2\u009d\37\3\2\2\2\u009e\u009f\7\33\2"+
		"\2\u009f\u00a0\7\3\2\2\u00a0\u00a1\5\"\22\2\u00a1\u00a2\7\4\2\2\u00a2"+
		"\u00a6\7\5\2\2\u00a3\u00a5\5\4\3\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2"+
		"\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8"+
		"\u00a6\3\2\2\2\u00a9\u00aa\7\6\2\2\u00aa!\3\2\2\2\u00ab\u00ac\b\22\1\2"+
		"\u00ac\u00b9\7%\2\2\u00ad\u00b9\5$\23\2\u00ae\u00b9\5.\30\2\u00af\u00b9"+
		"\5&\24\2\u00b0\u00b1\7\3\2\2\u00b1\u00b2\5\"\22\2\u00b2\u00b3\7\4\2\2"+
		"\u00b3\u00b9\3\2\2\2\u00b4\u00b9\5*\26\2\u00b5\u00b9\5(\25\2\u00b6\u00b7"+
		"\7\13\2\2\u00b7\u00b9\5\"\22\t\u00b8\u00ab\3\2\2\2\u00b8\u00ad\3\2\2\2"+
		"\u00b8\u00ae\3\2\2\2\u00b8\u00af\3\2\2\2\u00b8\u00b0\3\2\2\2\u00b8\u00b4"+
		"\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ce\3\2\2\2\u00ba"+
		"\u00bb\f\b\2\2\u00bb\u00bc\t\2\2\2\u00bc\u00cd\5\"\22\t\u00bd\u00be\f"+
		"\7\2\2\u00be\u00bf\t\3\2\2\u00bf\u00cd\5\"\22\b\u00c0\u00c1\f\6\2\2\u00c1"+
		"\u00c2\t\4\2\2\u00c2\u00cd\5\"\22\7\u00c3\u00c4\f\5\2\2\u00c4\u00c5\t"+
		"\5\2\2\u00c5\u00cd\5\"\22\6\u00c6\u00c7\f\4\2\2\u00c7\u00c8\7\"\2\2\u00c8"+
		"\u00cd\5\"\22\5\u00c9\u00ca\f\3\2\2\u00ca\u00cb\7#\2\2\u00cb\u00cd\5\""+
		"\22\4\u00cc\u00ba\3\2\2\2\u00cc\u00bd\3\2\2\2\u00cc\u00c0\3\2\2\2\u00cc"+
		"\u00c3\3\2\2\2\u00cc\u00c6\3\2\2\2\u00cc\u00c9\3\2\2\2\u00cd\u00d0\3\2"+
		"\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf#\3\2\2\2\u00d0\u00ce"+
		"\3\2\2\2\u00d1\u00d2\t\6\2\2\u00d2%\3\2\2\2\u00d3\u00d4\7\25\2\2\u00d4"+
		"\u00d5\7%\2\2\u00d5\u00d7\7\3\2\2\u00d6\u00d8\5\60\31\2\u00d7\u00d6\3"+
		"\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\7\4\2\2\u00da"+
		"\'\3\2\2\2\u00db\u00df\t\7\2\2\u00dc\u00de\5,\27\2\u00dd\u00dc\3\2\2\2"+
		"\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2"+
		"\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\7\20\2\2\u00e3\u00e4\7%\2\2\u00e4"+
		")\3\2\2\2\u00e5\u00e9\t\7\2\2\u00e6\u00e8\5,\27\2\u00e7\u00e6\3\2\2\2"+
		"\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec"+
		"\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\7\20\2\2\u00ed\u00ee\7%\2\2\u00ee"+
		"\u00f0\7\3\2\2\u00ef\u00f1\5\60\31\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3"+
		"\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7\4\2\2\u00f3+\3\2\2\2\u00f4\u00f5"+
		"\7\20\2\2\u00f5\u00f6\7%\2\2\u00f6-\3\2\2\2\u00f7\u00f8\7%\2\2\u00f8\u00fa"+
		"\7\3\2\2\u00f9\u00fb\5\60\31\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3\2\2\2"+
		"\u00fb\u00fc\3\2\2\2\u00fc\u00fd\7\4\2\2\u00fd/\3\2\2\2\u00fe\u0102\5"+
		"\"\22\2\u00ff\u0101\5\62\32\2\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2\2"+
		"\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\61\3\2\2\2\u0104\u0102"+
		"\3\2\2\2\u0105\u0106\7\t\2\2\u0106\u0107\5\"\22\2\u0107\63\3\2\2\2\u0108"+
		"\u0109\t\b\2\2\u0109\65\3\2\2\2\u010a\u0114\7\32\2\2\u010b\u010c\5\64"+
		"\33\2\u010c\u0110\7%\2\2\u010d\u010f\58\35\2\u010e\u010d\3\2\2\2\u010f"+
		"\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0114\3\2"+
		"\2\2\u0112\u0110\3\2\2\2\u0113\u010a\3\2\2\2\u0113\u010b\3\2\2\2\u0114"+
		"\67\3\2\2\2\u0115\u0116\7\t\2\2\u0116\u0117\5\64\33\2\u0117\u0118\7%\2"+
		"\2\u01189\3\2\2\2\27<>GVgnu\u008c\u0099\u00a6\u00b8\u00cc\u00ce\u00d7"+
		"\u00df\u00e9\u00f0\u00fa\u0102\u0110\u0113";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
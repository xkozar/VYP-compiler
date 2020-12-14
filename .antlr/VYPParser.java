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
		RULE_class_body = 7, RULE_class_members = 8, RULE_field_definition = 9, 
		RULE_multiple_field_definition = 10, RULE_variable_definition = 11, RULE_multiple_variable_definition = 12, 
		RULE_variable_assignment = 13, RULE_instance_assignment = 14, RULE_return_statement = 15, 
		RULE_code_block = 16, RULE_if_else_block = 17, RULE_if_part = 18, RULE_else_part = 19, 
		RULE_while_block = 20, RULE_expression = 21, RULE_literal_value = 22, 
		RULE_instance_expression = 23, RULE_instance_creation = 24, RULE_nested_object = 25, 
		RULE_next_final = 26, RULE_final_field_expression = 27, RULE_final_method_expression = 28, 
		RULE_function_call = 29, RULE_expression_list = 30, RULE_next_expression = 31, 
		RULE_variable_type = 32, RULE_parameter_list = 33, RULE_function_parameter_definition = 34, 
		RULE_function_parameters = 35, RULE_next_parameter = 36;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "function_definition", "function_header", "function_body", 
			"class_definition", "class_header", "class_body", "class_members", "field_definition", 
			"multiple_field_definition", "variable_definition", "multiple_variable_definition", 
			"variable_assignment", "instance_assignment", "return_statement", "code_block", 
			"if_else_block", "if_part", "else_part", "while_block", "expression", 
			"literal_value", "instance_expression", "instance_creation", "nested_object", 
			"next_final", "final_field_expression", "final_method_expression", "function_call", 
			"expression_list", "next_expression", "variable_type", "parameter_list", 
			"function_parameter_definition", "function_parameters", "next_parameter"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'('", "')'", "'{'", "'}'", "':'", "','", "'='", "'!'", 
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
			setState(76); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(76);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
				case STRING:
				case VOID:
				case ID:
					{
					setState(74);
					function_definition();
					}
					break;
				case CLASS:
					{
					setState(75);
					class_definition();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(78); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CLASS) | (1L << INT) | (1L << STRING) | (1L << VOID) | (1L << ID))) != 0) );
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
		public Variable_assignmentContext variable_assignment() {
			return getRuleContext(Variable_assignmentContext.class,0);
		}
		public Instance_assignmentContext instance_assignment() {
			return getRuleContext(Instance_assignmentContext.class,0);
		}
		public Variable_definitionContext variable_definition() {
			return getRuleContext(Variable_definitionContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
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
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(80);
				if_else_block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(81);
				while_block();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(82);
				variable_assignment();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(83);
				instance_assignment();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(84);
				variable_definition();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(85);
				return_statement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(86);
				expression(0);
				setState(87);
				match(T__0);
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
			setState(91);
			function_header();
			setState(92);
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
			setState(94);
			variable_type();
			setState(95);
			match(ID);
			setState(96);
			match(T__1);
			setState(97);
			parameter_list();
			setState(98);
			match(T__2);
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
			setState(100);
			match(T__3);
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__8) | (1L << IF) | (1L << INT) | (1L << NEW) | (1L << RETURN) | (1L << STRING) | (1L << SUPER) | (1L << THIS) | (1L << VOID) | (1L << WHILE) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				{
				setState(101);
				statement();
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(107);
			match(T__4);
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
			setState(109);
			class_header();
			setState(110);
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
		public Token class_id;
		public Token parent_id;
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
			setState(112);
			match(CLASS);
			setState(113);
			((Class_headerContext)_localctx).class_id = match(ID);
			setState(114);
			match(T__5);
			setState(115);
			((Class_headerContext)_localctx).parent_id = match(ID);
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
			setState(117);
			match(T__3);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << STRING) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				{
				setState(118);
				class_members();
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(124);
			match(T__4);
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
		public Class_membersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_members; }
	 
		public Class_membersContext() { }
		public void copyFrom(Class_membersContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Class_field_definitionContext extends Class_membersContext {
		public Field_definitionContext field_definition() {
			return getRuleContext(Field_definitionContext.class,0);
		}
		public Class_field_definitionContext(Class_membersContext ctx) { copyFrom(ctx); }
	}
	public static class Method_definitionContext extends Class_membersContext {
		public Function_definitionContext function_definition() {
			return getRuleContext(Function_definitionContext.class,0);
		}
		public Method_definitionContext(Class_membersContext ctx) { copyFrom(ctx); }
	}

	public final Class_membersContext class_members() throws RecognitionException {
		Class_membersContext _localctx = new Class_membersContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_class_members);
		try {
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				_localctx = new Class_field_definitionContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				field_definition();
				}
				break;
			case 2:
				_localctx = new Method_definitionContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
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

	public static class Field_definitionContext extends ParserRuleContext {
		public Variable_typeContext variable_type() {
			return getRuleContext(Variable_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public List<Multiple_field_definitionContext> multiple_field_definition() {
			return getRuleContexts(Multiple_field_definitionContext.class);
		}
		public Multiple_field_definitionContext multiple_field_definition(int i) {
			return getRuleContext(Multiple_field_definitionContext.class,i);
		}
		public Field_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_definition; }
	}

	public final Field_definitionContext field_definition() throws RecognitionException {
		Field_definitionContext _localctx = new Field_definitionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_field_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			variable_type();
			setState(131);
			match(ID);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(132);
				multiple_field_definition();
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(138);
			match(T__0);
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

	public static class Multiple_field_definitionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Multiple_field_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiple_field_definition; }
	}

	public final Multiple_field_definitionContext multiple_field_definition() throws RecognitionException {
		Multiple_field_definitionContext _localctx = new Multiple_field_definitionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_multiple_field_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			match(T__6);
			setState(141);
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
		enterRule(_localctx, 22, RULE_variable_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			variable_type();
			setState(144);
			match(ID);
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(145);
				multiple_variable_definition();
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(151);
			match(T__0);
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
		enterRule(_localctx, 24, RULE_multiple_variable_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(T__6);
			setState(154);
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
		enterRule(_localctx, 26, RULE_variable_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(ID);
			setState(157);
			match(T__7);
			setState(158);
			expression(0);
			setState(159);
			match(T__0);
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

	public static class Instance_assignmentContext extends ParserRuleContext {
		public Instance_expressionContext instance_expression() {
			return getRuleContext(Instance_expressionContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Instance_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance_assignment; }
	}

	public final Instance_assignmentContext instance_assignment() throws RecognitionException {
		Instance_assignmentContext _localctx = new Instance_assignmentContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_instance_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			instance_expression();
			setState(162);
			match(T__7);
			setState(163);
			expression(0);
			setState(164);
			match(T__0);
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

	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(VYPParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(RETURN);
			setState(167);
			expression(0);
			setState(168);
			match(T__0);
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

	public static class Code_blockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Code_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_code_block; }
	}

	public final Code_blockContext code_block() throws RecognitionException {
		Code_blockContext _localctx = new Code_blockContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_code_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(T__3);
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__8) | (1L << IF) | (1L << INT) | (1L << NEW) | (1L << RETURN) | (1L << STRING) | (1L << SUPER) | (1L << THIS) | (1L << VOID) | (1L << WHILE) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				{
				setState(171);
				statement();
				}
				}
				setState(176);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(177);
			match(T__4);
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
		enterRule(_localctx, 34, RULE_if_else_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			if_part();
			setState(180);
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
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public If_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_part; }
	}

	public final If_partContext if_part() throws RecognitionException {
		If_partContext _localctx = new If_partContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_if_part);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(IF);
			setState(183);
			match(T__1);
			setState(184);
			expression(0);
			setState(185);
			match(T__2);
			setState(186);
			code_block();
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
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public Else_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_part; }
	}

	public final Else_partContext else_part() throws RecognitionException {
		Else_partContext _localctx = new Else_partContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_else_part);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			match(ELSE);
			setState(189);
			code_block();
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
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public While_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_block; }
	}

	public final While_blockContext while_block() throws RecognitionException {
		While_blockContext _localctx = new While_blockContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_while_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(WHILE);
			setState(192);
			match(T__1);
			setState(193);
			expression(0);
			setState(194);
			match(T__2);
			setState(195);
			code_block();
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
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Equality_expressionContext extends ExpressionContext {
		public Token operator;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LOGICAL_EQUAL() { return getToken(VYPParser.LOGICAL_EQUAL, 0); }
		public TerminalNode LOGICAL_NEQUAL() { return getToken(VYPParser.LOGICAL_NEQUAL, 0); }
		public Equality_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Muldiv_expressionContext extends ExpressionContext {
		public Token operator;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Muldiv_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Function_expressionContext extends ExpressionContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Function_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Instance_expression_valueContext extends ExpressionContext {
		public Instance_expressionContext instance_expression() {
			return getRuleContext(Instance_expressionContext.class,0);
		}
		public Instance_expression_valueContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Comparison_expressionContext extends ExpressionContext {
		public Token operator;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LE() { return getToken(VYPParser.LE, 0); }
		public TerminalNode LEQ() { return getToken(VYPParser.LEQ, 0); }
		public TerminalNode GT() { return getToken(VYPParser.GT, 0); }
		public TerminalNode GTQ() { return getToken(VYPParser.GTQ, 0); }
		public Comparison_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class CastExpressionContext extends ExpressionContext {
		public Token cast;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode INT() { return getToken(VYPParser.INT, 0); }
		public TerminalNode STRING() { return getToken(VYPParser.STRING, 0); }
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public CastExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Or_expressionContext extends ExpressionContext {
		public Token operator;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LOGICAL_OR() { return getToken(VYPParser.LOGICAL_OR, 0); }
		public Or_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Variable_expressionContext extends ExpressionContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Variable_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class And_expressionContext extends ExpressionContext {
		public Token operator;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LOGICAL_AND() { return getToken(VYPParser.LOGICAL_AND, 0); }
		public And_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Bracket_expressionContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Bracket_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Negation_expressionContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Negation_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Plusminus_expressionContext extends ExpressionContext {
		public Token operator;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Plusminus_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class New_expressionContext extends ExpressionContext {
		public Instance_creationContext instance_creation() {
			return getRuleContext(Instance_creationContext.class,0);
		}
		public New_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Literal_expressionContext extends ExpressionContext {
		public Literal_valueContext literal_value() {
			return getRuleContext(Literal_valueContext.class,0);
		}
		public Literal_expressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				_localctx = new CastExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(198);
				match(T__1);
				setState(199);
				((CastExpressionContext)_localctx).cast = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << STRING) | (1L << ID))) != 0)) ) {
					((CastExpressionContext)_localctx).cast = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(200);
				match(T__2);
				setState(201);
				expression(14);
				}
				break;
			case 2:
				{
				_localctx = new Bracket_expressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(202);
				match(T__1);
				setState(203);
				expression(0);
				setState(204);
				match(T__2);
				}
				break;
			case 3:
				{
				_localctx = new Negation_expressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(206);
				match(T__8);
				setState(207);
				expression(12);
				}
				break;
			case 4:
				{
				_localctx = new Instance_expression_valueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(208);
				instance_expression();
				}
				break;
			case 5:
				{
				_localctx = new New_expressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(209);
				instance_creation();
				}
				break;
			case 6:
				{
				_localctx = new Function_expressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(210);
				function_call();
				}
				break;
			case 7:
				{
				_localctx = new Literal_expressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(211);
				literal_value();
				}
				break;
			case 8:
				{
				_localctx = new Variable_expressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(212);
				match(ID);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(235);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(233);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new Muldiv_expressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(215);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(216);
						((Muldiv_expressionContext)_localctx).operator = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
							((Muldiv_expressionContext)_localctx).operator = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(217);
						expression(12);
						}
						break;
					case 2:
						{
						_localctx = new Plusminus_expressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(218);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(219);
						((Plusminus_expressionContext)_localctx).operator = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__11 || _la==T__12) ) {
							((Plusminus_expressionContext)_localctx).operator = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(220);
						expression(11);
						}
						break;
					case 3:
						{
						_localctx = new Comparison_expressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(221);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(222);
						((Comparison_expressionContext)_localctx).operator = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LE) | (1L << LEQ) | (1L << GT) | (1L << GTQ))) != 0)) ) {
							((Comparison_expressionContext)_localctx).operator = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(223);
						expression(10);
						}
						break;
					case 4:
						{
						_localctx = new Equality_expressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(224);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(225);
						((Equality_expressionContext)_localctx).operator = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==LOGICAL_EQUAL || _la==LOGICAL_NEQUAL) ) {
							((Equality_expressionContext)_localctx).operator = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(226);
						expression(9);
						}
						break;
					case 5:
						{
						_localctx = new And_expressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(227);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(228);
						((And_expressionContext)_localctx).operator = match(LOGICAL_AND);
						setState(229);
						expression(8);
						}
						break;
					case 6:
						{
						_localctx = new Or_expressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(230);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(231);
						((Or_expressionContext)_localctx).operator = match(LOGICAL_OR);
						setState(232);
						expression(7);
						}
						break;
					}
					} 
				}
				setState(237);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
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
		enterRule(_localctx, 44, RULE_literal_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
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

	public static class Instance_expressionContext extends ParserRuleContext {
		public Token reference;
		public Nested_objectContext nested_object() {
			return getRuleContext(Nested_objectContext.class,0);
		}
		public TerminalNode SUPER() { return getToken(VYPParser.SUPER, 0); }
		public TerminalNode THIS() { return getToken(VYPParser.THIS, 0); }
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Instance_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance_expression; }
	}

	public final Instance_expressionContext instance_expression() throws RecognitionException {
		Instance_expressionContext _localctx = new Instance_expressionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_instance_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			((Instance_expressionContext)_localctx).reference = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SUPER) | (1L << THIS) | (1L << ID))) != 0)) ) {
				((Instance_expressionContext)_localctx).reference = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(241);
			nested_object();
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
		public Instance_creationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance_creation; }
	}

	public final Instance_creationContext instance_creation() throws RecognitionException {
		Instance_creationContext _localctx = new Instance_creationContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_instance_creation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(NEW);
			setState(244);
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

	public static class Nested_objectContext extends ParserRuleContext {
		public Final_field_expressionContext final_field_expression() {
			return getRuleContext(Final_field_expressionContext.class,0);
		}
		public Final_method_expressionContext final_method_expression() {
			return getRuleContext(Final_method_expressionContext.class,0);
		}
		public List<Next_finalContext> next_final() {
			return getRuleContexts(Next_finalContext.class);
		}
		public Next_finalContext next_final(int i) {
			return getRuleContext(Next_finalContext.class,i);
		}
		public Nested_objectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nested_object; }
	}

	public final Nested_objectContext nested_object() throws RecognitionException {
		Nested_objectContext _localctx = new Nested_objectContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_nested_object);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(246);
				final_field_expression();
				}
				break;
			case 2:
				{
				setState(247);
				final_method_expression();
				}
				break;
			}
			setState(253);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(250);
					next_final();
					}
					} 
				}
				setState(255);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
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

	public static class Next_finalContext extends ParserRuleContext {
		public Final_field_expressionContext final_field_expression() {
			return getRuleContext(Final_field_expressionContext.class,0);
		}
		public Final_method_expressionContext final_method_expression() {
			return getRuleContext(Final_method_expressionContext.class,0);
		}
		public Next_finalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_next_final; }
	}

	public final Next_finalContext next_final() throws RecognitionException {
		Next_finalContext _localctx = new Next_finalContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_next_final);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(256);
				final_field_expression();
				}
				break;
			case 2:
				{
				setState(257);
				final_method_expression();
				}
				break;
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

	public static class Final_field_expressionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Final_field_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_final_field_expression; }
	}

	public final Final_field_expressionContext final_field_expression() throws RecognitionException {
		Final_field_expressionContext _localctx = new Final_field_expressionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_final_field_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(T__13);
			setState(261);
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

	public static class Final_method_expressionContext extends ParserRuleContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Final_method_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_final_method_expression; }
	}

	public final Final_method_expressionContext final_method_expression() throws RecognitionException {
		Final_method_expressionContext _localctx = new Final_method_expressionContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_final_method_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			match(T__13);
			setState(264);
			function_call();
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
		enterRule(_localctx, 58, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
			match(ID);
			setState(267);
			match(T__1);
			setState(269);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__8) | (1L << NEW) | (1L << SUPER) | (1L << THIS) | (1L << INTEGER_LITERAL) | (1L << ID) | (1L << STRING_LITERAL))) != 0)) {
				{
				setState(268);
				expression_list();
				}
			}

			setState(271);
			match(T__2);
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
		enterRule(_localctx, 60, RULE_expression_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			expression(0);
			setState(277);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(274);
				next_expression();
				}
				}
				setState(279);
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
		enterRule(_localctx, 62, RULE_next_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			match(T__6);
			setState(281);
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
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Variable_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_type; }
	}

	public final Variable_typeContext variable_type() throws RecognitionException {
		Variable_typeContext _localctx = new Variable_typeContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_variable_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << STRING) | (1L << VOID) | (1L << ID))) != 0)) ) {
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
		public Function_parametersContext function_parameters() {
			return getRuleContext(Function_parametersContext.class,0);
		}
		public Parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_list; }
	}

	public final Parameter_listContext parameter_list() throws RecognitionException {
		Parameter_listContext _localctx = new Parameter_listContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_parameter_list);
		try {
			setState(287);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(285);
				match(VOID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(286);
				function_parameters();
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

	public static class Function_parameter_definitionContext extends ParserRuleContext {
		public Variable_typeContext variable_type() {
			return getRuleContext(Variable_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(VYPParser.ID, 0); }
		public Function_parameter_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_parameter_definition; }
	}

	public final Function_parameter_definitionContext function_parameter_definition() throws RecognitionException {
		Function_parameter_definitionContext _localctx = new Function_parameter_definitionContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_function_parameter_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			variable_type();
			setState(290);
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

	public static class Function_parametersContext extends ParserRuleContext {
		public Function_parameter_definitionContext function_parameter_definition() {
			return getRuleContext(Function_parameter_definitionContext.class,0);
		}
		public List<Next_parameterContext> next_parameter() {
			return getRuleContexts(Next_parameterContext.class);
		}
		public Next_parameterContext next_parameter(int i) {
			return getRuleContext(Next_parameterContext.class,i);
		}
		public Function_parametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_parameters; }
	}

	public final Function_parametersContext function_parameters() throws RecognitionException {
		Function_parametersContext _localctx = new Function_parametersContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_function_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			function_parameter_definition();
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(293);
				next_parameter();
				}
				}
				setState(298);
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

	public static class Next_parameterContext extends ParserRuleContext {
		public Function_parameter_definitionContext function_parameter_definition() {
			return getRuleContext(Function_parameter_definitionContext.class,0);
		}
		public Next_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_next_parameter; }
	}

	public final Next_parameterContext next_parameter() throws RecognitionException {
		Next_parameterContext _localctx = new Next_parameterContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_next_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
			match(T__6);
			setState(300);
			function_parameter_definition();
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
		case 21:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 11);
		case 1:
			return precpred(_ctx, 10);
		case 2:
			return precpred(_ctx, 9);
		case 3:
			return precpred(_ctx, 8);
		case 4:
			return precpred(_ctx, 7);
		case 5:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)\u0131\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\3\2\3\2\6\2O\n\2\r\2\16\2P\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\\\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\6\3\6\7\6i\n\6\f\6\16\6l\13\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3"+
		"\b\3\b\3\t\3\t\7\tz\n\t\f\t\16\t}\13\t\3\t\3\t\3\n\3\n\5\n\u0083\n\n\3"+
		"\13\3\13\3\13\7\13\u0088\n\13\f\13\16\13\u008b\13\13\3\13\3\13\3\f\3\f"+
		"\3\f\3\r\3\r\3\r\7\r\u0095\n\r\f\r\16\r\u0098\13\r\3\r\3\r\3\16\3\16\3"+
		"\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3"+
		"\21\3\22\3\22\7\22\u00af\n\22\f\22\16\22\u00b2\13\22\3\22\3\22\3\23\3"+
		"\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3"+
		"\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3"+
		"\27\3\27\3\27\3\27\3\27\5\27\u00d8\n\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00ec"+
		"\n\27\f\27\16\27\u00ef\13\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3"+
		"\33\3\33\5\33\u00fb\n\33\3\33\7\33\u00fe\n\33\f\33\16\33\u0101\13\33\3"+
		"\34\3\34\5\34\u0105\n\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37"+
		"\5\37\u0110\n\37\3\37\3\37\3 \3 \7 \u0116\n \f \16 \u0119\13 \3!\3!\3"+
		"!\3\"\3\"\3#\3#\5#\u0122\n#\3$\3$\3$\3%\3%\7%\u0129\n%\f%\16%\u012c\13"+
		"%\3&\3&\3&\3&\2\3,\'\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60"+
		"\62\64\668:<>@BDFHJ\2\n\5\2\24\24\27\27%%\3\2\f\r\3\2\16\17\3\2\34\37"+
		"\3\2 !\4\2$$&&\4\2\30\31%%\6\2\24\24\27\27\32\32%%\2\u012d\2N\3\2\2\2"+
		"\4[\3\2\2\2\6]\3\2\2\2\b`\3\2\2\2\nf\3\2\2\2\fo\3\2\2\2\16r\3\2\2\2\20"+
		"w\3\2\2\2\22\u0082\3\2\2\2\24\u0084\3\2\2\2\26\u008e\3\2\2\2\30\u0091"+
		"\3\2\2\2\32\u009b\3\2\2\2\34\u009e\3\2\2\2\36\u00a3\3\2\2\2 \u00a8\3\2"+
		"\2\2\"\u00ac\3\2\2\2$\u00b5\3\2\2\2&\u00b8\3\2\2\2(\u00be\3\2\2\2*\u00c1"+
		"\3\2\2\2,\u00d7\3\2\2\2.\u00f0\3\2\2\2\60\u00f2\3\2\2\2\62\u00f5\3\2\2"+
		"\2\64\u00fa\3\2\2\2\66\u0104\3\2\2\28\u0106\3\2\2\2:\u0109\3\2\2\2<\u010c"+
		"\3\2\2\2>\u0113\3\2\2\2@\u011a\3\2\2\2B\u011d\3\2\2\2D\u0121\3\2\2\2F"+
		"\u0123\3\2\2\2H\u0126\3\2\2\2J\u012d\3\2\2\2LO\5\6\4\2MO\5\f\7\2NL\3\2"+
		"\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\3\3\2\2\2R\\\5$\23\2S\\"+
		"\5*\26\2T\\\5\34\17\2U\\\5\36\20\2V\\\5\30\r\2W\\\5 \21\2XY\5,\27\2YZ"+
		"\7\3\2\2Z\\\3\2\2\2[R\3\2\2\2[S\3\2\2\2[T\3\2\2\2[U\3\2\2\2[V\3\2\2\2"+
		"[W\3\2\2\2[X\3\2\2\2\\\5\3\2\2\2]^\5\b\5\2^_\5\n\6\2_\7\3\2\2\2`a\5B\""+
		"\2ab\7%\2\2bc\7\4\2\2cd\5D#\2de\7\5\2\2e\t\3\2\2\2fj\7\6\2\2gi\5\4\3\2"+
		"hg\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2km\3\2\2\2lj\3\2\2\2mn\7\7\2\2"+
		"n\13\3\2\2\2op\5\16\b\2pq\5\20\t\2q\r\3\2\2\2rs\7\21\2\2st\7%\2\2tu\7"+
		"\b\2\2uv\7%\2\2v\17\3\2\2\2w{\7\6\2\2xz\5\22\n\2yx\3\2\2\2z}\3\2\2\2{"+
		"y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\7\2\2\177\21\3\2\2\2\u0080"+
		"\u0083\5\24\13\2\u0081\u0083\5\6\4\2\u0082\u0080\3\2\2\2\u0082\u0081\3"+
		"\2\2\2\u0083\23\3\2\2\2\u0084\u0085\5B\"\2\u0085\u0089\7%\2\2\u0086\u0088"+
		"\5\26\f\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2"+
		"\u0089\u008a\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d"+
		"\7\3\2\2\u008d\25\3\2\2\2\u008e\u008f\7\t\2\2\u008f\u0090\7%\2\2\u0090"+
		"\27\3\2\2\2\u0091\u0092\5B\"\2\u0092\u0096\7%\2\2\u0093\u0095\5\32\16"+
		"\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097"+
		"\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\7\3\2\2\u009a"+
		"\31\3\2\2\2\u009b\u009c\7\t\2\2\u009c\u009d\7%\2\2\u009d\33\3\2\2\2\u009e"+
		"\u009f\7%\2\2\u009f\u00a0\7\n\2\2\u00a0\u00a1\5,\27\2\u00a1\u00a2\7\3"+
		"\2\2\u00a2\35\3\2\2\2\u00a3\u00a4\5\60\31\2\u00a4\u00a5\7\n\2\2\u00a5"+
		"\u00a6\5,\27\2\u00a6\u00a7\7\3\2\2\u00a7\37\3\2\2\2\u00a8\u00a9\7\26\2"+
		"\2\u00a9\u00aa\5,\27\2\u00aa\u00ab\7\3\2\2\u00ab!\3\2\2\2\u00ac\u00b0"+
		"\7\6\2\2\u00ad\u00af\5\4\3\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0"+
		"\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3\2"+
		"\2\2\u00b3\u00b4\7\7\2\2\u00b4#\3\2\2\2\u00b5\u00b6\5&\24\2\u00b6\u00b7"+
		"\5(\25\2\u00b7%\3\2\2\2\u00b8\u00b9\7\23\2\2\u00b9\u00ba\7\4\2\2\u00ba"+
		"\u00bb\5,\27\2\u00bb\u00bc\7\5\2\2\u00bc\u00bd\5\"\22\2\u00bd\'\3\2\2"+
		"\2\u00be\u00bf\7\22\2\2\u00bf\u00c0\5\"\22\2\u00c0)\3\2\2\2\u00c1\u00c2"+
		"\7\33\2\2\u00c2\u00c3\7\4\2\2\u00c3\u00c4\5,\27\2\u00c4\u00c5\7\5\2\2"+
		"\u00c5\u00c6\5\"\22\2\u00c6+\3\2\2\2\u00c7\u00c8\b\27\1\2\u00c8\u00c9"+
		"\7\4\2\2\u00c9\u00ca\t\2\2\2\u00ca\u00cb\7\5\2\2\u00cb\u00d8\5,\27\20"+
		"\u00cc\u00cd\7\4\2\2\u00cd\u00ce\5,\27\2\u00ce\u00cf\7\5\2\2\u00cf\u00d8"+
		"\3\2\2\2\u00d0\u00d1\7\13\2\2\u00d1\u00d8\5,\27\16\u00d2\u00d8\5\60\31"+
		"\2\u00d3\u00d8\5\62\32\2\u00d4\u00d8\5<\37\2\u00d5\u00d8\5.\30\2\u00d6"+
		"\u00d8\7%\2\2\u00d7\u00c7\3\2\2\2\u00d7\u00cc\3\2\2\2\u00d7\u00d0\3\2"+
		"\2\2\u00d7\u00d2\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d7"+
		"\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00ed\3\2\2\2\u00d9\u00da\f\r"+
		"\2\2\u00da\u00db\t\3\2\2\u00db\u00ec\5,\27\16\u00dc\u00dd\f\f\2\2\u00dd"+
		"\u00de\t\4\2\2\u00de\u00ec\5,\27\r\u00df\u00e0\f\13\2\2\u00e0\u00e1\t"+
		"\5\2\2\u00e1\u00ec\5,\27\f\u00e2\u00e3\f\n\2\2\u00e3\u00e4\t\6\2\2\u00e4"+
		"\u00ec\5,\27\13\u00e5\u00e6\f\t\2\2\u00e6\u00e7\7\"\2\2\u00e7\u00ec\5"+
		",\27\n\u00e8\u00e9\f\b\2\2\u00e9\u00ea\7#\2\2\u00ea\u00ec\5,\27\t\u00eb"+
		"\u00d9\3\2\2\2\u00eb\u00dc\3\2\2\2\u00eb\u00df\3\2\2\2\u00eb\u00e2\3\2"+
		"\2\2\u00eb\u00e5\3\2\2\2\u00eb\u00e8\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed"+
		"\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee-\3\2\2\2\u00ef\u00ed\3\2\2\2"+
		"\u00f0\u00f1\t\7\2\2\u00f1/\3\2\2\2\u00f2\u00f3\t\b\2\2\u00f3\u00f4\5"+
		"\64\33\2\u00f4\61\3\2\2\2\u00f5\u00f6\7\25\2\2\u00f6\u00f7\7%\2\2\u00f7"+
		"\63\3\2\2\2\u00f8\u00fb\58\35\2\u00f9\u00fb\5:\36\2\u00fa\u00f8\3\2\2"+
		"\2\u00fa\u00f9\3\2\2\2\u00fb\u00ff\3\2\2\2\u00fc\u00fe\5\66\34\2\u00fd"+
		"\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2"+
		"\2\2\u0100\65\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0105\58\35\2\u0103\u0105"+
		"\5:\36\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105\67\3\2\2\2\u0106"+
		"\u0107\7\20\2\2\u0107\u0108\7%\2\2\u01089\3\2\2\2\u0109\u010a\7\20\2\2"+
		"\u010a\u010b\5<\37\2\u010b;\3\2\2\2\u010c\u010d\7%\2\2\u010d\u010f\7\4"+
		"\2\2\u010e\u0110\5> \2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111"+
		"\3\2\2\2\u0111\u0112\7\5\2\2\u0112=\3\2\2\2\u0113\u0117\5,\27\2\u0114"+
		"\u0116\5@!\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2"+
		"\2\u0117\u0118\3\2\2\2\u0118?\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b"+
		"\7\t\2\2\u011b\u011c\5,\27\2\u011cA\3\2\2\2\u011d\u011e\t\t\2\2\u011e"+
		"C\3\2\2\2\u011f\u0122\7\32\2\2\u0120\u0122\5H%\2\u0121\u011f\3\2\2\2\u0121"+
		"\u0120\3\2\2\2\u0122E\3\2\2\2\u0123\u0124\5B\"\2\u0124\u0125\7%\2\2\u0125"+
		"G\3\2\2\2\u0126\u012a\5F$\2\u0127\u0129\5J&\2\u0128\u0127\3\2\2\2\u0129"+
		"\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012bI\3\2\2\2"+
		"\u012c\u012a\3\2\2\2\u012d\u012e\7\t\2\2\u012e\u012f\5F$\2\u012fK\3\2"+
		"\2\2\25NP[j{\u0082\u0089\u0096\u00b0\u00d7\u00eb\u00ed\u00fa\u00ff\u0104"+
		"\u010f\u0117\u0121\u012a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
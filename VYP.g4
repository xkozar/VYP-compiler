/* 
    use this command to generate grammar with antlr
        java org.antlr.v4.Tool -Dlanguage=Python3 VYP.g4
    use this command for lexer testing
        java org.antlr.v4.runtime.misc.TestRig VYP r -tokens
*/

grammar VYP;

// program: hello* EOF;
// hello: 'hello world' ID;

program: function* EOF;

function: function_header function_body;

function_header: variable_type ID '(' parameter_list ')';

function_body: '{' statement* '}';

statement: ID ';';

variable_type: INT | STRING | VOID;
parameter_list
    :   VOID
    |   variable_type ID next_parameter*;

next_parameter: ',' variable_type ID;

CLASS: 'class';
ELSE: 'else';
IF: 'if';
INT: 'int';
NEW: 'new';
RETURN: 'return';
STRING: 'string';
SUPER: 'super';
THIS: 'this';
VOID: 'void';
WHILE: 'while';

INTEGER_LITERAL: [1-9] DIGIT*;
ID: (CILETTER | UNDERSCORE)(CILETTER | UNDERSCORE | DIGIT)*;
STRING_LITERAL: '"' STRING_CHARACTER* '"';

/* Lexemes to ignore */
WHITE_SPACE: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' .*? '\r' ? '\n' -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

fragment CILETTER: [a-zA-Z]; // Case In-sensitive letter
fragment UNDERSCORE: [_];
fragment DIGIT: [0-9];
fragment OCTAL_DIGIT: [0-7];
fragment HEXADECIMAL_DIGIT: [0-9A-Fa-f];
fragment PRINTABLE_CHARACTER: [ !#-~];
fragment STRING_CHARACTER: (PRINTABLE_CHARACTER | ESCAPE_SEQUENCE);

fragment ESCAPE_SEQUENCE
    :   SIMPLE_ESCAPE_SEQUENCE
    |   UTF8_ESCAPE_SEQUENCE;
    // |   OCTAL_ESCAPE_SEQUENCE
    // |   HEXA_ESCAPE_SEQUENCE;

fragment SIMPLE_ESCAPE_SEQUENCE: BACKSLASH [nt\\"?];
fragment UTF8_ESCAPE_SEQUENCE: BACKSLASH HEXADECIMAL_DIGIT HEXADECIMAL_DIGIT HEXADECIMAL_DIGIT HEXADECIMAL_DIGIT HEXADECIMAL_DIGIT HEXADECIMAL_DIGIT;

fragment BACKSLASH: '\\';

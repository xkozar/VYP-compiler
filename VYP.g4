/* 
    use this command to generate grammar with antlr
        java org.antlr.v4.Tool -Dlanguage=Python3 VYP.g4
    use this command for lexer testing
        java org.antlr.v4.runtime.misc.TestRig VYP r -tokens
*/

grammar VYP;

program: hello* EOF;

hello: 'hello world' ID;

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

INTEGER_LITERAL: [1-9][0-9]*;
// TODO STRING_LITERAL: 
ID: (CILETTER | UNDERSCORE)(CILETTER | UNDERSCORE | DIGIT)*;
WS: [ \t\r\n]+ -> skip;

fragment CILETTER: [a-zA-Z]; // Case In-sensitive letter
fragment UNDERSCORE: [_];
fragment DIGIT: [0-9];
fragment OCTAL_DIGIT: [0-7]; 

// List of possible escape sequences taken from https://en.wikipedia.org/wiki/Escape_sequences_in_C

fragment ESCAPE_SEQUENCE
    :   SIMPLE_ESCAPE_SEQUENCE
    |   OCTAL_ECAPE_SEQUENCE;

fragment SIMPLE_ESCAPE_SEQUENCE: BACKSLASH [abefnrtv\\'"?];
fragment OCTAL_ECAPE_SEQUENCE
    :   BACKSLASH OCTAL_DIGIT
    |   BACKSLASH OCTAL_DIGIT OCTAL_DIGIT
    |   BACKSLASH OCTAL_DIGIT OCTAL_DIGIT OCTAL_DIGIT;

fragment BACKSLASH: '\\';

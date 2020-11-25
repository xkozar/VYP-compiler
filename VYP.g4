/* 
    use this command to generate grammar with antlr
        java org.antlr.v4.Tool -Dlanguage=Python3 VYP.g4
    use this command for lexer testing
        java org.antlr.v4.runtime.misc.TestRig VYP r -tokens
*/

grammar VYP;

program: (function_definition | class_definition)+;

//TODO return statement

statement
    :   if_else_block
    |   while_block
    |   variable_assignment
    |   variable_definition
    |   expression ';'
    ;

function_definition: function_header function_body;
function_header: variable_type ID '(' parameter_list ')';
function_body: '{' statement* '}';

class_definition: class_header class_body;
class_header: CLASS ID ':' ID;
class_body: '{' class_members* '}';
class_members
    :   variable_definition
    |   function_definition;

// Might be extended with visibility modificators
variable_definition: variable_type ID multiple_variable_definition* ';';
multiple_variable_definition: ',' ID;
variable_assignment: ID '=' expression ';';

code_block: '{' statement* '}';
if_else_block: if_part else_part;
if_part: IF '(' expression ')' code_block;
else_part: ELSE code_block;
while_block: WHILE '(' expression ')' code_block;

expression
    :   '(' expression ')'  #bracket_expression
    |   '!' expression      #negation_expression
    |   expression operator=('*' | '/') expression #muldiv_expression
    |   expression operator=('+' | '-') expression #plusminus_expression
    |   expression operator=(LE | LEQ | GT | GTQ) expression #comparison_expression
    |   expression operator=(LOGICAL_EQUAL | LOGICAL_NEQUAL) expression #equality_expression
    |   expression operator=LOGICAL_AND expression #and_expression
    |   expression operator=LOGICAL_OR expression #or_expression
    |   instance_function_call #method_expression
    |   instance_variable   #field_expression
    |   instance_creation   #new_expression
    |   function_call       #function_expression
    |   literal_value       #literal_expression
    |   ID                  #variable_expression;

literal_value
    :   INTEGER_LITERAL
    |   STRING_LITERAL;

instance_creation: NEW ID '(' expression_list? ')';
instance_variable: (THIS | ID) nested_object* '.' ID;
instance_function_call: (THIS | ID) nested_object* '.' ID '(' expression_list? ')';
nested_object: '.' ID;

function_call: ID '(' expression_list? ')';

expression_list: expression next_expression*;

next_expression
    :   ',' expression next_expression?;


variable_type: INT | STRING | VOID | ID;
parameter_list
    :   VOID
    |   function_parameters;

function_parameter_definition: variable_type ID;
function_parameters: function_parameter_definition next_parameter*;
next_parameter: ',' function_parameter_definition;

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

LE: '<';
LEQ: '<=';
GT: '>';
GTQ: '>=';

LOGICAL_EQUAL: '==';
LOGICAL_NEQUAL: '!=';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';

INTEGER_LITERAL: ('-'? [1-9] DIGIT* | '0');
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

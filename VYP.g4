/* 
    use this command to generate grammar with antlr
        java org.antlr.v4.Tool -Dlanguage=Python3 VYP.g4
*/

grammar VYP;

test: 'hello world' ID;
ID: [a-z]+;
WS: [ \t\r\n]+ -> skip;
